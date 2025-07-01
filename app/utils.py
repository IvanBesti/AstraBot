import sqlite3
import os
import json
import requests
from datetime import datetime
import pandas as pd
from typing import Dict, List, Optional

# Database setup
DB_PATH = "data/tickets.db"

def init_database():
    """Initialize SQLite database for tickets"""
    os.makedirs("data", exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id TEXT UNIQUE NOT NULL,
            user_name TEXT,
            issue_description TEXT,
            status TEXT DEFAULT 'open',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            full_name TEXT,
            email TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def create_ticket(user_name: str, issue_description: str) -> Dict:
    """Create a new ticket in the database"""
    ticket_id = f"TCK{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO tickets (ticket_id, user_name, issue_description)
        VALUES (?, ?, ?)
    ''', (ticket_id, user_name, issue_description))
    
    conn.commit()
    conn.close()
    
    return {
        "ticket_id": ticket_id,
        "user_name": user_name,
        "issue_description": issue_description,
        "status": "open",
        "created_at": datetime.now().isoformat()
    }

def get_ticket(ticket_id: str) -> Optional[Dict]:
    """Get ticket by ID"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM tickets WHERE ticket_id = ?', (ticket_id,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return {
            "id": result[0],
            "ticket_id": result[1],
            "user_name": result[2],
            "issue_description": result[3],
            "status": result[4],
            "created_at": result[5],
            "updated_at": result[6]
        }
    return None

def get_all_tickets() -> List[Dict]:
    """Get all tickets"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM tickets ORDER BY created_at DESC')
    results = cursor.fetchall()
    
    conn.close()
    
    tickets = []
    for result in results:
        tickets.append({
            "id": result[0],
            "ticket_id": result[1],
            "user_name": result[2],
            "issue_description": result[3],
            "status": result[4],
            "created_at": result[5],
            "updated_at": result[6]
        })
    
    return tickets

def create_user_account(full_name: str) -> Dict:
    """Create user account via mock API"""
    try:
        # Mock API call to user creation service
        response = requests.post(
            "http://localhost:8001/create_user",
            json={
                "full_name": full_name,
                "email": f"{full_name.lower().replace(' ', '.')}@astra.com",
                "department": "IT"
            },
            timeout=5
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            # Fallback if API is not available
            username = full_name.lower().replace(' ', '.')
            return {
                "success": True,
                "username": username,
                "password": "Astra2024!",
                "email": f"{username}@astra.com",
                "message": "Akun berhasil dibuat"
            }
    except requests.exceptions.RequestException:
        # Fallback if API is not available
        username = full_name.lower().replace(' ', '.')
        return {
            "success": True,
            "username": username,
            "password": "Astra2024!",
            "email": f"{username}@astra.com",
            "message": "Akun berhasil dibuat (offline mode)"
        }

def get_download_files() -> List[Dict]:
    """Get available download files"""
    downloads_dir = "downloads"
    files = []
    
    if os.path.exists(downloads_dir):
        for filename in os.listdir(downloads_dir):
            if filename.endswith(('.csv', '.xlsx', '.pdf')):
                file_path = os.path.join(downloads_dir, filename)
                file_size = os.path.getsize(file_path)
                files.append({
                    "filename": filename,
                    "size": file_size,
                    "path": file_path,
                    "download_url": f"/download/{filename}"
                })
    
    return files

def create_sample_data():
    """Create sample data for demonstration"""
    # Create sample CSV file
    os.makedirs("downloads", exist_ok=True)
    
    # Sample attendance report
    attendance_data = {
        'Nama': ['Andi', 'Budi', 'Cindy', 'Dinda', 'Eko'],
        'Tanggal': ['2024-06-01', '2024-06-01', '2024-06-01', '2024-06-01', '2024-06-01'],
        'Jam_Masuk': ['08:00', '08:15', '07:55', '08:05', '08:10'],
        'Jam_Keluar': ['17:00', '17:30', '17:15', '17:00', '17:45'],
        'Status': ['Hadir', 'Hadir', 'Hadir', 'Hadir', 'Hadir']
    }
    
    df = pd.DataFrame(attendance_data)
    df.to_csv("downloads/laporan_absensi_juni.csv", index=False)
    
    # Create sample user data
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Add some sample users
    sample_users = [
        ('andi.astrabot', 'Andi Setiawan', 'andi@astra.com'),
        ('budi.astrabot', 'Budi Santoso', 'budi@astra.com'),
        ('cindy.astrabot', 'Cindy Wijaya', 'cindy@astra.com')
    ]
    
    for username, full_name, email in sample_users:
        cursor.execute('''
            INSERT OR IGNORE INTO users (username, full_name, email)
            VALUES (?, ?, ?)
        ''', (username, full_name, email))
    
    conn.commit()
    conn.close()

def load_prompts() -> Dict:
    """Load prompts from YAML file"""
    import yaml
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))
    prompts_path = os.path.join(base_dir, "prompts.yaml")
    with open(prompts_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file) 