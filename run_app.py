#!/usr/bin/env python3
"""
AstraBot - Internal Helpdesk Chatbot
Runner script untuk menjalankan aplikasi
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import streamlit
        import langchain
        import openai
        import yaml
        import pandas
        print("✅ Semua dependencies terinstall")
        return True
    except ImportError as e:
        print(f"❌ Dependency missing: {e}")
        print("Jalankan: pip install -r requirements.txt")
        return False

def check_api_key():
    """Check if OpenAI API key is set"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("⚠️  OPENAI_API_KEY tidak ditemukan di environment variables")
        print("Silakan set environment variable atau masukkan di aplikasi")
        return False
    print("✅ OpenAI API key ditemukan")
    return True

def start_mock_api():
    """Start the mock API server"""
    print("🚀 Menjalankan Mock API server...")
    try:
        # Start mock API in background
        api_process = subprocess.Popen([
            sys.executable, "mock_api/user_api.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait a bit for server to start
        time.sleep(3)
        
        print("✅ Mock API server berjalan di http://localhost:8001")
        return api_process
    except Exception as e:
        print(f"❌ Gagal menjalankan Mock API: {e}")
        return None

def start_streamlit_app():
    """Start the Streamlit application"""
    print("🚀 Menjalankan AstraBot Streamlit app...")
    try:
        # Change to app directory
        os.chdir("app")
        
        # Start Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "main.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n👋 AstraBot dihentikan")
    except Exception as e:
        print(f"❌ Gagal menjalankan Streamlit app: {e}")

def main():
    """Main function"""
    print("🤖 AstraBot - Internal Helpdesk Chatbot")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Check API key
    check_api_key()
    
    print("\n📋 Opsi menjalankan aplikasi:")
    print("1. Jalankan hanya Streamlit app")
    print("2. Jalankan Mock API + Streamlit app")
    print("3. Jalankan Mock API saja")
    
    choice = input("\nPilih opsi (1-3): ").strip()
    
    if choice == "1":
        print("\n🎯 Menjalankan Streamlit app saja...")
        start_streamlit_app()
        
    elif choice == "2":
        print("\n🎯 Menjalankan Mock API + Streamlit app...")
        api_process = start_mock_api()
        if api_process:
            try:
                start_streamlit_app()
            finally:
                # Cleanup
                api_process.terminate()
                print("🛑 Mock API server dihentikan")
                
    elif choice == "3":
        print("\n🎯 Menjalankan Mock API saja...")
        api_process = start_mock_api()
        if api_process:
            try:
                print("Mock API berjalan. Tekan Ctrl+C untuk menghentikan...")
                api_process.wait()
            except KeyboardInterrupt:
                api_process.terminate()
                print("\n🛑 Mock API server dihentikan")
                
    else:
        print("❌ Pilihan tidak valid")

if __name__ == "__main__":
    main() 