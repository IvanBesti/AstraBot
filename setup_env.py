#!/usr/bin/env python3
"""
AstraBot Environment Setup Script
Helps users configure environment variables for AstraBot
"""

import os
import sys
from pathlib import Path

def create_env_file():
    """Create .env file from template"""
    config_file = Path("config.env")
    env_file = Path(".env")
    
    if not config_file.exists():
        print("❌ config.env tidak ditemukan!")
        print("Pastikan Anda menjalankan script ini dari root directory AstraBot")
        return False
    
    if env_file.exists():
        response = input("⚠️  File .env sudah ada. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Setup dibatalkan.")
            return False
    
    # Copy config.env to .env
    with open(config_file, 'r') as f:
        content = f.read()
    
    with open(env_file, 'w') as f:
        f.write(content)
    
    print("✅ File .env berhasil dibuat!")
    return True

def check_env_file():
    """Check if .env file exists and has valid content"""
    env_file = Path(".env")
    
    if not env_file.exists():
        print("❌ File .env tidak ditemukan!")
        print("Jalankan: python setup_env.py")
        return False
    
    with open(env_file, 'r') as f:
        content = f.read()
    
    # Check for placeholder values
    placeholders = [
        "your_openrouter_api_key_here",
        "your_mistral_api_key_here", 
        "your_groq_api_key_here"
    ]
    
    found_placeholders = []
    for placeholder in placeholders:
        if placeholder in content:
            found_placeholders.append(placeholder)
    
    if found_placeholders:
        print("⚠️  Beberapa API keys masih menggunakan placeholder:")
        for placeholder in found_placeholders:
            print(f"   - {placeholder}")
        print("\n📝 Silakan edit file .env dan masukkan API keys yang valid")
        print("📖 Lihat SETUP_ENV.md untuk panduan lengkap")
        return False
    
    print("✅ File .env sudah dikonfigurasi dengan benar!")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    os.system("pip install -r requirements.txt")
    print("✅ Dependencies berhasil diinstall!")

def main():
    """Main setup function"""
    print("🤖 AstraBot Environment Setup")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not Path("app").exists() or not Path("config.env").exists():
        print("❌ Pastikan Anda menjalankan script ini dari root directory AstraBot")
        print("   Directory harus berisi folder 'app' dan file 'config.env'")
        return
    
    # Create .env file
    if not create_env_file():
        return
    
    # Check environment configuration
    if not check_env_file():
        print("\n💡 Tips:")
        print("   - AstraBot akan menggunakan demo mode jika tidak ada API key")
        print("   - Demo mode tetap bisa digunakan untuk testing")
        print("   - Lihat SETUP_ENV.md untuk panduan lengkap")
        return
    
    # Install dependencies
    install_dependencies()
    
    print("\n🎉 Setup selesai!")
    print("\n🚀 Untuk menjalankan AstraBot:")
    print("   cd app && streamlit run main.py --server.port 8501")
    print("\n📖 Dokumentasi lengkap: README.md")
    print("🔐 Panduan API keys: SETUP_ENV.md")

if __name__ == "__main__":
    main() 