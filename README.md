# AstraBot

AstraBot is an internal IT helpdesk chatbot built with LangChain, Streamlit, and OpenRouter. It can:
- Create support tickets
- Create user accounts
- Provide downloadable files
- Check ticket status

## Features
- Powered by OpenRouter LLM
- Simple Streamlit web interface
- Mock FastAPI backend for user/account actions

## Quick Start
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Set your OpenRouter API key:**
   - Create a `.env` file and add:
     ```
     OPENROUTER_API_KEY=your-openrouter-api-key
     ```
3. **Run the app:**
   ```bash
   cd app
   streamlit run main.py
   ```

## Usage
- Use the chat interface to create tickets, accounts, download files, or check ticket status.
- All responses and UI are in English.

---
For any issues, please contact the maintainer. 