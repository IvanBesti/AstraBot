#!/usr/bin/env python3
"""
AstraBot Setup Script
Script untuk setup awal aplikasi AstraBot
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def print_banner():
    """Print welcome banner"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    🤖 AstraBot Setup                        ║
    ║              Internal Helpdesk Chatbot                      ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 atau lebih tinggi diperlukan")
        print(f"   Versi saat ini: {sys.version}")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} terdeteksi")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Menginstall dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies berhasil diinstall")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Gagal menginstall dependencies: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    print("\n📁 Membuat direktori yang diperlukan...")
    directories = [
        "data",
        "downloads", 
        "logs",
        "mock_api/data"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Direktori {directory} dibuat")

def create_sample_files():
    """Create sample files for demonstration"""
    print("\n📄 Membuat file sample...")
    
    # Create sample CSV file
    import pandas as pd
    
    attendance_data = {
        'Nama': ['Andi', 'Budi', 'Cindy', 'Dinda', 'Eko'],
        'Tanggal': ['2024-06-01', '2024-06-01', '2024-06-01', '2024-06-01', '2024-06-01'],
        'Jam_Masuk': ['08:00', '08:15', '07:55', '08:05', '08:10'],
        'Jam_Keluar': ['17:00', '17:30', '17:15', '17:00', '17:45'],
        'Status': ['Hadir', 'Hadir', 'Hadir', 'Hadir', 'Hadir']
    }
    
    df = pd.DataFrame(attendance_data)
    df.to_csv("downloads/laporan_absensi_juni.csv", index=False)
    print("✅ File sample laporan_absensi_juni.csv dibuat")

def setup_environment():
    """Setup environment variables"""
    print("\n🔧 Setup environment variables...")
    
    # Check if .env exists
    if os.path.exists(".env"):
        print("⚠️  File .env sudah ada")
        overwrite = input("Apakah Anda ingin menimpa? (y/N): ").lower()
        if overwrite != 'y':
            print("⏭️  Melewati setup environment")
            return
    
    # Copy config.env to .env
    if Path("config.env").exists():
        shutil.copy("config.env", ".env")
        print("✅ .env file created from config.env")
        print("📝 Edit .env file to add your API keys")
    else:
        print("❌ config.env not found")

def test_installation():
    """Test if installation is successful"""
    print("\n🧪 Testing instalasi...")
    
    try:
        # Test imports
        import streamlit
        import langchain
        import openai
        import yaml
        import pandas
        print("✅ Semua dependencies berhasil diimport")
        
        # Test database creation
        import sqlite3
        conn = sqlite3.connect("data/tickets.db")
        conn.close()
        print("✅ Database berhasil dibuat")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def print_next_steps():
    """Print next steps for user"""
    print("\n" + "="*60)
    print("🎉 Setup AstraBot selesai!")
    print("="*60)
    print("\n📋 Langkah selanjutnya:")
    print("1. Edit file .env dengan OpenAI API key Anda")
    print("2. Jalankan aplikasi dengan: python run_app.py")
    print("3. Atau jalankan langsung: cd app && streamlit run main.py")
    print("\n🔗 Link aplikasi:")
    print("   - Streamlit App: http://localhost:8501")
    print("   - Mock API: http://localhost:8001")
    print("\n📚 Dokumentasi:")
    print("   - README.md: Panduan lengkap")
    print("   - demo_examples.md: Contoh penggunaan")
    print("\n❓ Bantuan:")
    print("   - Buat issue di repository")
    print("   - Hubungi tim development")
    print("\n" + "="*60)

def main():
    """Main setup function"""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        return
    
    # Install dependencies
    if not install_dependencies():
        return
    
    # Create directories
    create_directories()
    
    # Create sample files
    create_sample_files()
    
    # Setup environment
    setup_environment()
    
    # Test installation
    if not test_installation():
        print("❌ Setup gagal. Silakan cek error di atas.")
        return
    
    # Print next steps
    print_next_steps()

if __name__ == "__main__":
    main() 