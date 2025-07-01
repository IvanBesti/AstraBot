import os
import re
from typing import Dict, List, Any
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.tools import Tool
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import utils
from langchain.agents import initialize_agent, AgentType
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get OpenRouter API key from environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "your_openrouter_api_key_here")

class DummyBot:
    def __init__(self):
        self.chat_history = []
    
    def chat(self, message):
        """Demo mode responses"""
        message_lower = message.lower()
        
        if any(word in message_lower for word in ['halo', 'hai', 'hello', 'hi']):
            return "Hello! I'm AstraBot, your internal IT assistant. How can I help you today? 😊"
        
        elif any(word in message_lower for word in ['tiket', 'masalah', 'error', 'bug', 'trouble']):
            return "To create a ticket, please provide the details of your issue. Example: 'I can't log in to the HRIS portal' or 'The printer on the 3rd floor is not working.'"
        
        elif any(word in message_lower for word in ['akun', 'account', 'user', 'karyawan baru']):
            return "To create an account, please provide the name and department of the new employee. Example: 'Create an account for Dinda from the Marketing department.'"
        
        elif any(word in message_lower for word in ['download', 'unduh', 'laporan', 'data', 'file']):
            return "To download data, please select the type of report you need. I can help with HR reports, finance, or technical data."
        
        elif any(word in message_lower for word in ['status', 'cek', 'check', 'tiket saya']):
            return "To check ticket status, please provide your ticket number or your registered name."
        
        elif any(word in message_lower for word in ['bantuan', 'help', 'tolong', 'apa yang bisa']):
            return """I'm AstraBot, your internal IT assistant who can help you with:

🔧 **Create Ticket** - Report technical issues
👤 **Create Account** - Create an account for a new employee  
📊 **Download Data** - Download reports and files
📋 **Check Status** - View your ticket status

Please select the service you need! 😊"""
        
        else:
            return "Thank you for your message! I'm AstraBot, your internal IT assistant. I can help with ticket creation, account creation, data download, and status checking. How can I assist you? 😊"
    
    def clear_history(self):
        self.chat_history = []

class AstraBot:
    def __init__(self):
        self.api_key = OPENROUTER_API_KEY
        self.model = "mistralai/mistral-7b-instruct"  # Model Mistral via OpenRouter
        self.prompts = utils.load_prompts()
        utils.init_database()
        utils.create_sample_data()
        self.tools = self._create_tools()
        self.agent = None
        self.chat_history = []
        self.dummy = None
        self._init_llm()

    def _init_llm(self):
        """Initialize LLM with OpenRouter only"""
        if not self.api_key or self.api_key == "your_openrouter_api_key_here":
            print("API key OpenRouter belum diset. Menggunakan demo mode.")
            self.llm = None
            self.agent = None
            self.dummy = DummyBot()
            return
        try:
            llm_kwargs = {
                "model": self.model,
                "temperature": 0.7,
                "openai_api_key": self.api_key,
                "openai_api_base": "https://openrouter.ai/api/v1"
            }
            self.llm = ChatOpenAI(**llm_kwargs)
            # Test the LLM connection
            test_response = self.llm.invoke("Hello")
            print("LLM connection successful with OpenRouter")
            self.agent = self._create_agent()
        except Exception as e:
            print(f"Error initializing LLM with OpenRouter: {e}")
            self.llm = None
            self.agent = None
            self.dummy = DummyBot()
            print("Falling back to dummy bot")

    def _create_tools(self) -> List[Tool]:
        """Create tools for the agent"""
        
        def create_ticket_tool(issue_description: str, user_name: str = "User") -> str:
            """Create a support ticket for user issues"""
            try:
                ticket = utils.create_ticket(user_name, issue_description)
                return f"Ticket successfully created with ID {ticket['ticket_id']}. The IT team will contact you within 24 hours."
            except Exception as e:
                return f"Sorry, an error occurred: {str(e)}"
        
        def create_user_account_tool(full_name: str) -> str:
            """Create user account for new employee"""
            try:
                result = utils.create_user_account(full_name)
                if result.get("success"):
                    return f"Account for {full_name} has been successfully created! Username: {result['username']}, Password: {result['password']}"
                else:
                    return f"Sorry, failed to create account for {full_name}"
            except Exception as e:
                return f"Sorry, an error occurred: {str(e)}"
        
        def get_download_files_tool() -> str:
            """Get available files for download"""
            try:
                files = utils.get_download_files()
                if files:
                    file_list = "\n".join([f"- {f['filename']} ({f['size']} bytes)" for f in files])
                    return f"Available files for download:\n{file_list}"
                else:
                    return "No files are currently available for download."
            except Exception as e:
                return f"Sorry, an error occurred: {str(e)}"
        
        def get_ticket_status_tool(ticket_id: str) -> str:
            """Get status of a specific ticket"""
            try:
                # Extract only the pure ticket ID (e.g. TCK20250701174707) from the input
                match = re.search(r'TCK\d{14}', ticket_id)
                ticket_id_clean = match.group(0) if match else ticket_id.strip(' ",()')
                ticket = utils.get_ticket(ticket_id_clean)
                if ticket:
                    return f"Ticket status {ticket_id_clean}: {ticket['status']}. Description: {ticket['issue_description']}"
                else:
                    return f"Ticket {ticket_id_clean} not found."
            except Exception as e:
                return f"Sorry, an error occurred: {str(e)}"
        
        def get_latest_ticket_id_for_user_tool(user_name: str = None) -> str:
            """Get the latest ticket ID for a user. If user_name is missing or a placeholder, use self.user_name."""
            try:
                # Use the chatbot's user_name if input is missing or a placeholder
                if not user_name or 'current user' in user_name or 'user_name' in user_name:
                    user_name = getattr(self, 'current_user_name', 'User')
                ticket_id = utils.get_latest_ticket_id_for_user(user_name)
                if ticket_id:
                    return f"The latest ticket ID for user '{user_name}' is {ticket_id}."
                else:
                    return f"No tickets found for user '{user_name}'."
            except Exception as e:
                return f"Sorry, an error occurred: {str(e)}"
        
        return [
            Tool(
                name="create_ticket",
                description="Create a support ticket for technical issues reported by the user",
                func=create_ticket_tool
            ),
            Tool(
                name="create_user_account",
                description="Create an account for a new employee",
                func=create_user_account_tool
            ),
            Tool(
                name="get_download_files",
                description="Get a list of files available for download",
                func=get_download_files_tool
            ),
            Tool(
                name="get_ticket_status",
                description="Check ticket status by ticket ID",
                func=get_ticket_status_tool
            ),
            Tool(
                name="get_latest_ticket_id_for_user",
                description="Get the latest ticket ID for a given user name",
                func=get_latest_ticket_id_for_user_tool
            )
        ]

    def _create_agent(self):
        """Create LangChain agent with tools"""
        try:
            # Coba buat agent dengan tools
            prompt = PromptTemplate(
                input_variables=["input", "agent_scratchpad"],
                template=self.prompts["agent_template"]
            )
            
            # Tambahkan system message untuk bahasa Indonesia
            system_message = """You are AstraBot, an internal IT assistant who helps employees with technical issues.\n\nIMPORTANT: Always respond in polite and professional English.\n\nIf the user just greets (hello, hi), respond politely in English such as:\n'Hello! I'm AstraBot, your internal IT assistant. How can I help you today? 😊'\n\nFor all other responses, use polite and professional English."""
            
            agent = initialize_agent(
                tools=self.tools,
                llm=self.llm,
                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                verbose=True,
                handle_parsing_errors=True,
                max_iterations=3
            )
            return agent
        except Exception as e:
            print(f"Error creating agent with tools: {e}")
            # Fallback ke mode chat-only tanpa tools
            return None

    def chat(self, message):
        """Chat with the bot"""
        try:
            if self.agent and self.llm:
                # Gunakan agent dengan tools
                response = self.agent.run(message)
            elif self.llm:
                # Fallback ke chat-only mode
                response = self._chat_only(message)
            elif self.dummy:
                # Fallback ke dummy bot
                response = self.dummy.chat(message)
            else:
                response = "Sorry, the chatbot system is currently unavailable. Please try again later."
            
            self.chat_history.append({"user": message, "bot": response})
            return response
        except Exception as e:
            error_msg = f"Sorry, an error occurred: {str(e)}"
            self.chat_history.append({"user": message, "bot": error_msg})
            return error_msg

    def _chat_only(self, message):
        """Chat-only mode tanpa function calling"""
        try:
            if self.llm:
                response = self.llm.invoke(message)
                return response.content
            else:
                return "Sorry, the LLM is not available."
        except Exception as e:
            return f"Sorry, an error occurred: {str(e)}"

    def process_message(self, user_message: str, user_name: str = "User") -> str:
        """Process user message - compatibility method"""
        # Store the user_name for use in tools
        self.current_user_name = user_name
        return self.chat(user_message)

    def get_chat_history(self) -> List[Dict]:
        """Get formatted chat history"""
        history = []
        for i in range(0, len(self.chat_history), 2):
            if i + 1 < len(self.chat_history):
                history.append({
                    "user": self.chat_history[i].content,
                    "bot": self.chat_history[i + 1].content
                })
        return history

    def clear_history(self):
        """Clear chat history"""
        self.chat_history = []

    def classify_intent(self, message: str) -> str:
        """Classify user intent"""
        message_lower = message.lower()
        
        # Ticket creation keywords
        ticket_keywords = [
            "tidak bisa", "error", "masalah", "bug", "rusak", "gagal",
            "login", "password", "email", "sistem", "aplikasi", "website",
            "tiket", "support", "bantuan", "tolong"
        ]
        
        # User creation keywords
        user_keywords = [
            "buat akun", "buatkan akun", "karyawan baru", "user baru",
            "daftar", "register", "akun baru"
        ]
        
        # Download keywords
        download_keywords = [
            "download", "unduh", "laporan", "data", "file", "excel",
            "csv", "pdf", "report", "absensi", "gaji"
        ]
        
        # Check for ticket intent
        if any(keyword in message_lower for keyword in ticket_keywords):
            return "create_ticket"
        
        # Check for user creation intent
        if any(keyword in message_lower for keyword in user_keywords):
            return "create_user"
        
        # Check for download intent
        if any(keyword in message_lower for keyword in download_keywords):
            return "download_data"
        
        return "general_help" 