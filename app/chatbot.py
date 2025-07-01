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

# Get API keys from environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "your_openrouter_api_key_here")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "your_mistral_api_key_here")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your_groq_api_key_here")

class DummyBot:
    def __init__(self):
        self.chat_history = []
    
    def chat(self, message):
        """Demo mode responses"""
        message_lower = message.lower()
        
        if any(word in message_lower for word in ['halo', 'hai', 'hello', 'hi']):
            return "Halo! Saya AstraBot, asisten IT internal. Bagaimana saya bisa membantu Anda hari ini? 😊"
        
        elif any(word in message_lower for word in ['tiket', 'masalah', 'error', 'bug', 'trouble']):
            return "Untuk membuat tiket, silakan berikan detail masalah Anda. Contoh: 'Saya tidak bisa login ke portal HRIS' atau 'Printer di lantai 3 tidak berfungsi'."
        
        elif any(word in message_lower for word in ['akun', 'account', 'user', 'karyawan baru']):
            return "Untuk pembuatan akun, silakan berikan nama dan departemen karyawan baru. Contoh: 'Buatkan akun untuk Dinda dari departemen Marketing'."
        
        elif any(word in message_lower for word in ['download', 'unduh', 'laporan', 'data', 'file']):
            return "Untuk mengunduh data, silakan pilih jenis laporan yang Anda butuhkan. Saya bisa membantu dengan laporan HR, keuangan, atau data teknis."
        
        elif any(word in message_lower for word in ['status', 'cek', 'check', 'tiket saya']):
            return "Untuk mengecek status tiket, silakan berikan nomor tiket Anda atau nama Anda yang terdaftar."
        
        elif any(word in message_lower for word in ['bantuan', 'help', 'tolong', 'apa yang bisa']):
            return """Saya AstraBot, asisten IT internal yang bisa membantu Anda dengan:

🔧 **Membuat Tiket** - Laporkan masalah teknis
👤 **Pembuatan Akun** - Buat akun untuk karyawan baru  
📊 **Download Data** - Unduh laporan dan file
📋 **Cek Status** - Lihat status tiket Anda

Silakan pilih layanan yang Anda butuhkan! 😊"""
        
        else:
            return "Terima kasih atas pesannya! Saya AstraBot, asisten IT internal. Saya bisa membantu dengan pembuatan tiket, akun, download data, dan cek status. Ada yang bisa saya bantu? 😊"
    
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
        """Initialize LLM with error handling and multiple providers"""
        # Try OpenRouter first (recommended)
        if OPENROUTER_API_KEY and OPENROUTER_API_KEY != "your_openrouter_api_key_here":
            try:
                llm_kwargs = {
                    "model": "mistralai/mistral-7b-instruct",
                    "temperature": 0.7,
                    "openai_api_key": OPENROUTER_API_KEY,
                    "openai_api_base": "https://openrouter.ai/api/v1"
                }
                self.llm = ChatOpenAI(**llm_kwargs)
                # Test the LLM connection
                test_response = self.llm.invoke("Hello")
                print("LLM connection successful with OpenRouter")
                self.agent = self._create_agent()
                return
            except Exception as e:
                print(f"Error initializing LLM with OpenRouter: {e}")
        
        # Try Mistral AI directly
        if MISTRAL_API_KEY and MISTRAL_API_KEY != "your_mistral_api_key_here":
            try:
                from langchain_mistralai import ChatMistralAI
                self.llm = ChatMistralAI(
                    model="mistral-small-latest",
                    mistral_api_key=MISTRAL_API_KEY
                )
                test_response = self.llm.invoke("Hello")
                print("LLM connection successful with Mistral")
                self.agent = self._create_agent()
                return
            except Exception as e:
                print(f"Error initializing LLM with Mistral: {e}")
        
        # Try Groq
        if GROQ_API_KEY and GROQ_API_KEY != "your_groq_api_key_here":
            try:
                from langchain_groq import ChatGroq
                self.llm = ChatGroq(
                    model="llama3-8b-8192",
                    groq_api_key=GROQ_API_KEY
                )
                test_response = self.llm.invoke("Hello")
                print("LLM connection successful with Groq")
                self.agent = self._create_agent()
                return
            except Exception as e:
                print(f"Error initializing LLM with Groq: {e}")
        
        # Fallback to demo mode
        print("No valid API keys found. Using demo mode.")
        self.llm = None
        self.agent = None
        self.dummy = DummyBot()

    def _create_tools(self) -> List[Tool]:
        """Create tools for the agent"""
        
        def create_ticket_tool(issue_description: str, user_name: str = "User") -> str:
            """Create a support ticket for user issues"""
            try:
                ticket = utils.create_ticket(user_name, issue_description)
                return f"Tiket berhasil dibuat dengan ID {ticket['ticket_id']}. Tim IT akan menghubungi Anda dalam 24 jam."
            except Exception as e:
                return f"Maaf, terjadi kesalahan saat membuat tiket: {str(e)}"
        
        def create_user_account_tool(full_name: str) -> str:
            """Create user account for new employee"""
            try:
                result = utils.create_user_account(full_name)
                if result.get("success"):
                    return f"Akun untuk {full_name} berhasil dibuat! Username: {result['username']}, Password: {result['password']}"
                else:
                    return f"Maaf, gagal membuat akun untuk {full_name}"
            except Exception as e:
                return f"Maaf, terjadi kesalahan saat membuat akun: {str(e)}"
        
        def get_download_files_tool() -> str:
            """Get available files for download"""
            try:
                files = utils.get_download_files()
                if files:
                    file_list = "\n".join([f"- {f['filename']} ({f['size']} bytes)" for f in files])
                    return f"File yang tersedia untuk download:\n{file_list}"
                else:
                    return "Tidak ada file yang tersedia untuk download saat ini."
            except Exception as e:
                return f"Maaf, terjadi kesalahan saat mengambil daftar file: {str(e)}"
        
        def get_ticket_status_tool(ticket_id: str) -> str:
            """Get status of a specific ticket"""
            try:
                ticket = utils.get_ticket(ticket_id)
                if ticket:
                    return f"Status tiket {ticket_id}: {ticket['status']}. Deskripsi: {ticket['issue_description']}"
                else:
                    return f"Tiket {ticket_id} tidak ditemukan."
            except Exception as e:
                return f"Maaf, terjadi kesalahan saat mencari tiket: {str(e)}"
        
        return [
            Tool(
                name="create_ticket",
                description="Buat tiket support untuk masalah teknis yang dilaporkan user",
                func=create_ticket_tool
            ),
            Tool(
                name="create_user_account",
                description="Buat akun untuk karyawan baru",
                func=create_user_account_tool
            ),
            Tool(
                name="get_download_files",
                description="Dapatkan daftar file yang tersedia untuk download",
                func=get_download_files_tool
            ),
            Tool(
                name="get_ticket_status",
                description="Cek status tiket berdasarkan ID tiket",
                func=get_ticket_status_tool
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
            system_message = """Kamu adalah AstraBot, asisten IT internal yang membantu karyawan dengan masalah teknis.

PENTING: Selalu jawab dalam bahasa Indonesia yang sopan dan profesional.

Jika user hanya menyapa (halo, hai, hi, hello), jawab dengan ramah dalam bahasa Indonesia seperti:
"Halo! Saya AstraBot, asisten IT internal. Bagaimana saya bisa membantu Anda hari ini? 😊"

Untuk semua respons lainnya, gunakan bahasa Indonesia yang sopan dan profesional."""
            
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
                response = "Maaf, sistem chatbot sedang tidak tersedia. Silakan coba lagi nanti."
            
            self.chat_history.append({"user": message, "bot": response})
            return response
        except Exception as e:
            error_msg = f"Maaf, terjadi kesalahan: {str(e)}"
            self.chat_history.append({"user": message, "bot": error_msg})
            return error_msg

    def _chat_only(self, message):
        """Chat-only mode tanpa function calling"""
        try:
            if self.llm:
                response = self.llm.invoke(message)
                return response.content
            else:
                return "Maaf, LLM tidak tersedia."
        except Exception as e:
            return f"Error dalam chat-only mode: {str(e)}"

    def process_message(self, user_message: str, user_name: str = "User") -> str:
        """Process user message - compatibility method"""
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