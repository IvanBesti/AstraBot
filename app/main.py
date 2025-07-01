import streamlit as st
import os
import sys
from datetime import datetime
import pandas as pd

# Add app directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chatbot import AstraBot
import utils

# Page configuration
st.set_page_config(
    page_title="AstraBot - Internal Helpdesk",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling with dark mode support
st.markdown("""
<style>
    /* Dark mode detection and variables */
    @media (prefers-color-scheme: dark) {
        :root {
            --bg-color: #0e1117;
            --text-color: #fafafa;
            --card-bg: #262730;
            --border-color: #464646;
            --primary-color: #4CAF50;
            --secondary-color: #2196F3;
            --accent-color: #9C27B0;
            --muted-color: #888;
        }
    }
    
    @media (prefers-color-scheme: light) {
        :root {
            --bg-color: #ffffff;
            --text-color: #31333f;
            --card-bg: #f8f9fa;
            --border-color: #e0e0e0;
            --primary-color: #28a745;
            --secondary-color: #1f77b4;
            --accent-color: #9c27b0;
            --muted-color: #666;
        }
    }
    
    /* Streamlit dark mode override */
    .stApp[data-testid="stAppViewContainer"] {
        background-color: var(--bg-color) !important;
        color: var(--text-color) !important;
    }
    
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: var(--secondary-color);
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
    }
    
    .user-message {
        background-color: rgba(33, 150, 243, 0.1);
        border-left: 4px solid var(--secondary-color);
    }
    
    .bot-message {
        background-color: rgba(156, 39, 176, 0.1);
        border-left: 4px solid var(--accent-color);
    }
    
    .message-time {
        font-size: 0.8rem;
        color: var(--muted-color);
        margin-top: 0.5rem;
    }
    
    .sidebar-header {
        font-size: 1.2rem;
        font-weight: bold;
        color: var(--secondary-color);
        margin-bottom: 1rem;
    }
    
    .ticket-card {
        background-color: var(--card-bg);
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
        border-left: 4px solid var(--primary-color);
        border: 1px solid var(--border-color);
        color: var(--text-color);
    }
    
    .file-card {
        background-color: var(--card-bg);
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
        border: 1px solid var(--border-color);
        color: var(--text-color);
    }
    
    .download-link {
        color: var(--secondary-color);
        text-decoration: none;
    }
    
    .download-link:hover {
        text-decoration: underline;
    }
    
    /* Button styling for dark mode */
    .stButton > button {
        background-color: var(--secondary-color);
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: var(--accent-color);
        transform: translateY(-2px);
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        background-color: var(--card-bg);
        color: var(--text-color);
        border: 1px solid var(--border-color);
    }
    
    /* Chat input styling */
    .stChatInput > div > div > textarea {
        background-color: var(--card-bg);
        color: var(--text-color);
        border: 1px solid var(--border-color);
    }
    
    /* Info box styling */
    .stAlert {
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
        color: var(--text-color);
    }
    
    /* Error box styling */
    .stAlert[data-baseweb="notification"] {
        background-color: rgba(244, 67, 54, 0.1);
        border: 1px solid #f44336;
        color: var(--text-color);
    }
    
    /* Navigation buttons styling */
    .navigation-buttons {
        margin-bottom: 1rem;
        padding: 1rem;
        background-color: var(--card-bg);
        border-radius: 0.5rem;
        border: 1px solid var(--border-color);
    }
    
    /* File card improvements */
    .file-card {
        background-color: var(--card-bg);
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
        border: 1px solid var(--border-color);
        color: var(--text-color);
        transition: all 0.3s ease;
    }
    
    .file-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    /* Download button styling */
    .stDownloadButton > button {
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }
    
    .stDownloadButton > button:hover {
        background-color: var(--accent-color);
        transform: translateY(-2px);
    }
    
    /* Spinner styling for dark mode */
    .stSpinner > div {
        color: var(--secondary-color);
    }
    
    /* Divider styling */
    hr {
        border-color: var(--border-color);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if 'chatbot' not in st.session_state:
        try:
            st.session_state.chatbot = AstraBot()
        except Exception as e:
            st.session_state.chatbot = None
            st.session_state.init_error = str(e)
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'user_name' not in st.session_state:
        st.session_state.user_name = "User"

def display_chat_message(message, is_user=True):
    """Display a chat message with proper styling"""
    if is_user:
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>👤 Anda:</strong><br>
            {message['content']}
            <div class="message-time">{message['timestamp']}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message bot-message">
            <strong>🤖 AstraBot:</strong><br>
            {message['content']}
            <div class="message-time">{message['timestamp']}</div>
        </div>
        """, unsafe_allow_html=True)

def main():
    """Main application function"""
    
    # Initialize session state
    initialize_session_state()
    
    # Sidebar
    with st.sidebar:
        st.markdown('<div class="sidebar-header">⚙️ Konfigurasi</div>', unsafe_allow_html=True)
        
        # User name input
        user_name = st.text_input(
            "Nama Anda",
            value=st.session_state.user_name,
            key="user_name",
            help="Masukkan nama Anda untuk personalisasi"
        )
        
        if user_name != st.session_state.user_name:
            st.session_state.user_name = user_name
        
        st.divider()
        
        # Quick actions
        st.markdown('<div class="sidebar-header">🚀 Aksi Cepat</div>', unsafe_allow_html=True)
        
        if st.button("🗑️ Bersihkan Chat"):
            st.session_state.messages = []
            if st.session_state.chatbot:
                st.session_state.chatbot.clear_history()
            st.rerun()
        
        if st.button("📊 Lihat Tiket"):
            st.session_state.show_tickets = True
        
        if st.button("📁 Lihat File"):
            st.session_state.show_files = True
        
        st.divider()
        
        # Help section
        st.markdown('<div class="sidebar-header">❓ Bantuan</div>', unsafe_allow_html=True)
        st.markdown("""
        **Contoh pertanyaan:**
        - "Saya tidak bisa login ke portal HRIS"
        - "Buatkan akun untuk karyawan baru bernama Andi"
        - "Saya ingin unduh laporan absensi Juni"
        - "Cek status tiket TCK1234567890"
        """)
    
    # Main content
    st.markdown('<h1 class="main-header">🤖 AstraBot - Internal Helpdesk</h1>', unsafe_allow_html=True)
    
    # Check if chatbot is initialized
    if not st.session_state.chatbot:
        st.error("Chatbot gagal diinisialisasi. Silakan hubungi admin.\n" + st.session_state.get('init_error', ''))
        return
    
    # Display tickets if requested
    if st.session_state.get('show_tickets', False):
        st.subheader("📊 Daftar Tiket")
        
        # Navigation buttons
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("🏠 Kembali ke Chat"):
                st.session_state.show_tickets = False
                st.session_state.show_files = False
                st.rerun()
        with col2:
            if st.button("📁 Lihat File"):
                st.session_state.show_tickets = False
                st.session_state.show_files = True
                st.rerun()
        with col3:
            st.write("")  # Empty column for spacing
        
        st.divider()
        
        tickets = utils.get_all_tickets()
        
        if tickets:
            for ticket in tickets:
                st.markdown(f"""
                <div class="ticket-card">
                    <strong>ID: {ticket['ticket_id']}</strong><br>
                    <strong>Status:</strong> {ticket['status']}<br>
                    <strong>User:</strong> {ticket['user_name']}<br>
                    <strong>Deskripsi:</strong> {ticket['issue_description']}<br>
                    <strong>Dibuat:</strong> {ticket['created_at']}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Belum ada tiket yang dibuat.")
        
        return
    
    # Display files if requested
    if st.session_state.get('show_files', False):
        st.subheader("📁 File yang Tersedia")
        
        # Navigation buttons
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("🏠 Kembali ke Chat"):
                st.session_state.show_tickets = False
                st.session_state.show_files = False
                st.rerun()
        with col2:
            if st.button("📊 Lihat Tiket"):
                st.session_state.show_tickets = True
                st.session_state.show_files = False
                st.rerun()
        with col3:
            st.write("")  # Empty column for spacing
        
        st.divider()
        
        files = utils.get_download_files()
        
        if files:
            for file in files:
                st.markdown(f"""
                <div class="file-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <strong>📄 {file['filename']}</strong><br>
                            <small>Size: {file['size']} bytes</small>
                        </div>
                        <div>
                """, unsafe_allow_html=True)
                
                with open(file['path'], 'rb') as f:
                    st.download_button(
                        label="📥 Download",
                        data=f.read(),
                        file_name=file['filename'],
                        mime="application/octet-stream"
                    )
                
                st.markdown("</div></div></div>", unsafe_allow_html=True)
        else:
            st.info("Tidak ada file yang tersedia untuk download.")
        
        return
    
    # Chat interface
    st.markdown("### 💬 Chat dengan AstraBot")
    
    # Template pertanyaan untuk memudahkan user
    st.markdown("**📋 Template Pertanyaan Cepat:**")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔧 Buat Tiket Masalah"):
            user_input = "Saya ingin membuat tiket untuk masalah printer yang tidak berfungsi"
            # Add user message to history
            user_message = {
                'content': user_input,
                'is_user': True,
                'timestamp': datetime.now().strftime("%H:%M:%S")
            }
            st.session_state.messages.append(user_message)
            
            # Process with chatbot
            with st.spinner("AstraBot sedang memproses..."):
                try:
                    # Use chat method for both AstraBot and DummyBot
                    if hasattr(st.session_state.chatbot, 'process_message'):
                        bot_response = st.session_state.chatbot.process_message(
                            user_input, 
                            st.session_state.user_name
                        )
                    else:
                        # Fallback for DummyBot
                        bot_response = st.session_state.chatbot.chat(user_input)
                    
                    # Add bot response to history
                    bot_message = {
                        'content': bot_response,
                        'is_user': False,
                        'timestamp': datetime.now().strftime("%H:%M:%S")
                    }
                    st.session_state.messages.append(bot_message)
                    
                except Exception as e:
                    error_message = {
                        'content': f"Maaf, terjadi kesalahan: {str(e)}",
                        'is_user': False,
                        'timestamp': datetime.now().strftime("%H:%M:%S")
                    }
                    st.session_state.messages.append(error_message)
            st.rerun()
        
        if st.button("👤 Buat Akun Karyawan"):
            user_input = "Buatkan akun untuk karyawan baru bernama Andi dari departemen Marketing"
            # Add user message to history
            user_message = {
                'content': user_input,
                'is_user': True,
                'timestamp': datetime.now().strftime("%H:%M:%S")
            }
            st.session_state.messages.append(user_message)
            
            # Process with chatbot
            with st.spinner("AstraBot sedang memproses..."):
                try:
                    # Use chat method for both AstraBot and DummyBot
                    if hasattr(st.session_state.chatbot, 'process_message'):
                        bot_response = st.session_state.chatbot.process_message(
                            user_input, 
                            st.session_state.user_name
                        )
                    else:
                        # Fallback for DummyBot
                        bot_response = st.session_state.chatbot.chat(user_input)
                    
                    # Add bot response to history
                    bot_message = {
                        'content': bot_response,
                        'is_user': False,
                        'timestamp': datetime.now().strftime("%H:%M:%S")
                    }
                    st.session_state.messages.append(bot_message)
                    
                except Exception as e:
                    error_message = {
                        'content': f"Maaf, terjadi kesalahan: {str(e)}",
                        'is_user': False,
                        'timestamp': datetime.now().strftime("%H:%M:%S")
                    }
                    st.session_state.messages.append(error_message)
            st.rerun()
    
    with col2:
        if st.button("📊 Download Laporan"):
            user_input = "Saya ingin download laporan absensi bulan Juni"
            # Add user message to history
            user_message = {
                'content': user_input,
                'is_user': True,
                'timestamp': datetime.now().strftime("%H:%M:%S")
            }
            st.session_state.messages.append(user_message)
            
            # Process with chatbot
            with st.spinner("AstraBot sedang memproses..."):
                try:
                    # Use chat method for both AstraBot and DummyBot
                    if hasattr(st.session_state.chatbot, 'process_message'):
                        bot_response = st.session_state.chatbot.process_message(
                            user_input, 
                            st.session_state.user_name
                        )
                    else:
                        # Fallback for DummyBot
                        bot_response = st.session_state.chatbot.chat(user_input)
                    
                    # Add bot response to history
                    bot_message = {
                        'content': bot_response,
                        'is_user': False,
                        'timestamp': datetime.now().strftime("%H:%M:%S")
                    }
                    st.session_state.messages.append(bot_message)
                    
                except Exception as e:
                    error_message = {
                        'content': f"Maaf, terjadi kesalahan: {str(e)}",
                        'is_user': False,
                        'timestamp': datetime.now().strftime("%H:%M:%S")
                    }
                    st.session_state.messages.append(error_message)
            st.rerun()
        
        if st.button("📋 Cek Status Tiket"):
            user_input = "Cek status tiket saya yang terakhir"
            # Add user message to history
            user_message = {
                'content': user_input,
                'is_user': True,
                'timestamp': datetime.now().strftime("%H:%M:%S")
            }
            st.session_state.messages.append(user_message)
            
            # Process with chatbot
            with st.spinner("AstraBot sedang memproses..."):
                try:
                    # Use chat method for both AstraBot and DummyBot
                    if hasattr(st.session_state.chatbot, 'process_message'):
                        bot_response = st.session_state.chatbot.process_message(
                            user_input, 
                            st.session_state.user_name
                        )
                    else:
                        # Fallback for DummyBot
                        bot_response = st.session_state.chatbot.chat(user_input)
                    
                    # Add bot response to history
                    bot_message = {
                        'content': bot_response,
                        'is_user': False,
                        'timestamp': datetime.now().strftime("%H:%M:%S")
                    }
                    st.session_state.messages.append(bot_message)
                    
                except Exception as e:
                    error_message = {
                        'content': f"Maaf, terjadi kesalahan: {str(e)}",
                        'is_user': False,
                        'timestamp': datetime.now().strftime("%H:%M:%S")
                    }
                    st.session_state.messages.append(error_message)
            st.rerun()
    
    # Display chat history
    chat_container = st.container()
    
    with chat_container:
        for message in st.session_state.messages:
            display_chat_message(message, message['is_user'])
    
    # Chat input
    with st.container():
        user_input = st.chat_input("Ketik pesan Anda di sini atau gunakan template di atas...")
        
        if user_input:
            # Add user message to history
            user_message = {
                'content': user_input,
                'is_user': True,
                'timestamp': datetime.now().strftime("%H:%M:%S")
            }
            st.session_state.messages.append(user_message)
            
            # Process with chatbot
            with st.spinner("AstraBot sedang memproses..."):
                try:
                    # Use chat method for both AstraBot and DummyBot
                    if hasattr(st.session_state.chatbot, 'process_message'):
                        bot_response = st.session_state.chatbot.process_message(
                            user_input, 
                            st.session_state.user_name
                        )
                    else:
                        # Fallback for DummyBot
                        bot_response = st.session_state.chatbot.chat(user_input)
                    
                    # Add bot response to history
                    bot_message = {
                        'content': bot_response,
                        'is_user': False,
                        'timestamp': datetime.now().strftime("%H:%M:%S")
                    }
                    st.session_state.messages.append(bot_message)
                    
                except Exception as e:
                    error_message = {
                        'content': f"Maaf, terjadi kesalahan: {str(e)}",
                        'is_user': False,
                        'timestamp': datetime.now().strftime("%H:%M:%S")
                    }
                    st.session_state.messages.append(error_message)
            
            # Rerun to display new messages
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown(
        "**AstraBot** - Internal Helpdesk Chatbot | "
        "Powered by OpenRouter & Mistral | "
        "Built with Streamlit & LangChain"
    )

if __name__ == "__main__":
    main() 