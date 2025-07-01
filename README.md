# 🤖 AstraBot - LLM-based Internal Helpdesk Chatbot

AstraBot adalah chatbot internal yang dirancang untuk membantu karyawan dengan masalah teknis, pembuatan akun, dan pengunduhan data. Dibangun dengan LangChain, Streamlit, dan mendukung berbagai LLM provider (OpenRouter, Mistral, Groq).

## 🎯 Fitur Utama

- **🎫 Pembuatan Tiket Otomatis**: Membuat tiket support untuk masalah teknis
- **👤 Pembuatan Akun**: Membuat akun untuk karyawan baru melalui API
- **📁 Download Data**: Mengunduh laporan dan file dari sistem
- **📊 Manajemen Tiket**: Melihat dan mengelola tiket yang dibuat
- **💬 Chat Interface**: Interface chat yang modern dan responsif
- **📋 Template Pertanyaan**: Tombol template untuk pertanyaan umum
- **🌏 Bahasa Indonesia**: Respon dalam bahasa Indonesia
- **🤖 Multi-LLM Support**: Mendukung OpenRouter, Mistral, Groq, dan demo mode

## 🏗️ Arsitektur

```
AstraBot/
├── app/                   
│   ├── main.py               # Streamlit interface
│   ├── chatbot.py            # Core logic (LangChain)
│   ├── utils.py              # Helper functions
│   └── prompts.yaml          # Prompt templates
├── data/
│   └── tickets.db            # SQLite database
├── mock_api/
│   └── user_api.py           # Mock API for user creation
├── downloads/
│   └── laporan_absensi.csv   # Sample files
├── requirements.txt
└── README.md
```

## 🚀 Instalasi

### 1. Clone Repository
```bash
git clone <repository-url>
cd AstraBot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables (Recommended)
```bash
# Copy template file
cp config.env .env

# Edit .env file dan masukkan API keys Anda
# Lihat SETUP_ENV.md untuk panduan lengkap
```

**Atau set environment variables manual:**
```bash
# Untuk OpenRouter
export OPENROUTER_API_KEY="your-openrouter-api-key"

# Untuk Mistral
export MISTRAL_API_KEY="your-mistral-api-key"

# Untuk Groq
export GROQ_API_KEY="your-groq-api-key"
```

### 4. Initialize Database
Database akan otomatis dibuat saat pertama kali menjalankan aplikasi.

## 🏃‍♂️ Menjalankan Aplikasi

### 1. Start Mock API (Optional)
```bash
cd mock_api
python3 user_api.py
```
Mock API akan berjalan di `http://localhost:8001`

### 2. Start Streamlit App
```bash
cd app
streamlit run main.py --server.port 8501
```
Aplikasi akan berjalan di `http://localhost:8501`

## 💬 Cara Penggunaan

### Template Pertanyaan Cepat
AstraBot menyediakan 4 template pertanyaan yang bisa langsung diklik:

1. **🔧 Buat Tiket Masalah**: "Saya ingin membuat tiket untuk masalah printer yang tidak berfungsi"
2. **👤 Buat Akun Karyawan**: "Buatkan akun untuk karyawan baru bernama Andi dari departemen Marketing"
3. **📊 Download Laporan**: "Saya ingin download laporan absensi bulan Juni"
4. **📋 Cek Status Tiket**: "Cek status tiket saya yang terakhir"

### Contoh Interaksi

#### 1. Membuat Tiket
```
User: Saya tidak bisa login ke portal HRIS
Bot: Baik, saya akan membuatkan tiket untuk masalah login portal HRIS. Mohon tunggu sebentar...
[Proses: simpan data ke DB]
Bot: Tiket berhasil dibuat dengan ID TCK20241201123456. Tim IT akan menghubungi Anda dalam 24 jam.
```

#### 2. Membuat Akun
```
User: Buatkan akun untuk karyawan baru bernama Andi
Bot: Baik, saya akan membuatkan akun untuk Andi. Mohon tunggu sebentar...
[Proses: kirim POST ke API]
Bot: Akun untuk Andi berhasil dibuat! Username: andi, Password: Astra2024!
```

#### 3. Download Data
```
User: Saya ingin unduh laporan absensi Juni
Bot: Berikut adalah file yang tersedia untuk download:
- laporan_absensi.csv (1.2 KB)
Silakan klik tombol Download untuk mengunduh file.
```

## 🛠️ Komponen Teknis

### LLM & AI
- **OpenRouter**: Mendukung berbagai model (Mistral, Llama, GPT)
- **Mistral AI**: Model bahasa alternatif
- **Groq**: LLM provider berkecepatan tinggi
- **LangChain**: Framework untuk orchestration
- **Function Calling**: Untuk eksekusi tools
- **Demo Mode**: Fallback ketika API tidak tersedia

### Backend
- **SQLite**: Database untuk tiket
- **FastAPI**: Mock API untuk user creation
- **Pandas**: Manipulasi data

### Frontend
- **Streamlit**: Web interface
- **Custom CSS**: Styling modern
- **Real-time Chat**: Interface chat responsif
- **Template Buttons**: Tombol pertanyaan cepat

## 📊 Database Schema

### Tickets Table
```sql
CREATE TABLE tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id TEXT UNIQUE NOT NULL,
    user_name TEXT,
    issue_description TEXT,
    status TEXT DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    full_name TEXT,
    email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🔧 Konfigurasi

### Environment Variables
- `OPENROUTER_API_KEY`: API key OpenRouter (recommended)
- `MISTRAL_API_KEY`: API key Mistral AI
- `GROQ_API_KEY`: API key Groq

### LLM Provider Priority
1. **OpenRouter** (default) - Mendukung berbagai model
2. **Mistral AI** - Model bahasa yang powerful
3. **Groq** - Kecepatan tinggi
4. **Demo Mode** - Fallback tanpa API key

### Customization
- Edit `app/prompts.yaml` untuk mengubah prompt
- Modifikasi `app/utils.py` untuk menambah fungsi
- Update `mock_api/user_api.py` untuk simulasi API yang berbeda

## 📁 File Structure

### Core Files
- `app/main.py`: Streamlit interface utama dengan template buttons
- `app/chatbot.py`: Logic chatbot dengan multi-LLM support
- `app/utils.py`: Helper functions dan database operations
- `app/prompts.yaml`: Template prompt untuk berbagai fungsi

### Data & API
- `data/tickets.db`: SQLite database
- `mock_api/user_api.py`: Mock API server
- `downloads/`: Folder untuk file yang bisa diunduh

## 🧪 Testing

### Manual Testing
1. Buka aplikasi di browser (`http://localhost:8501`)
2. Test template pertanyaan dengan mengklik tombol
3. Test berbagai skenario:
   - Membuat tiket
   - Membuat akun
   - Download file
   - Cek status tiket
4. Test fallback ke demo mode

### API Testing
```bash
# Test mock API
curl -X POST http://localhost:8001/create_user \
  -H "Content-Type: application/json" \
  -d '{"full_name": "Test User"}'
```

## 🔒 Security Considerations

- API keys disimpan di environment variables
- Database menggunakan SQLite dengan proper escaping
- Input validation pada semua endpoints
- Error handling yang comprehensive
- Fallback ke demo mode untuk testing

## 🚀 Deployment

### Local Development
```bash
cd app
streamlit run main.py --server.port 8501
```

### Production
- Deploy ke Streamlit Cloud
- Setup environment variables
- Configure database (PostgreSQL recommended)
- Setup proper API endpoints

## 🌟 Fitur Baru

### Template Pertanyaan
- Tombol template untuk pertanyaan umum
- Langsung mengirim pesan tanpa perlu mengetik
- Mendukung 4 jenis pertanyaan utama

### Multi-LLM Support
- OpenRouter sebagai provider utama
- Fallback ke provider lain jika gagal
- Demo mode untuk testing tanpa API key

### Bahasa Indonesia
- Semua respon dalam bahasa Indonesia
- Template pertanyaan dalam bahasa Indonesia
- Interface yang user-friendly

## 🤝 Contributing

1. Fork repository
2. Buat feature branch
3. Commit changes
4. Push ke branch
5. Buat Pull Request

## 📝 License

MIT License - lihat file LICENSE untuk detail.

## 🆘 Troubleshooting

### Common Issues

1. **ModuleNotFoundError: langchain_community**
   ```bash
   pip install langchain-community
   ```

2. **API Key Error**
   - Pastikan API key sudah benar
   - Cek provider yang digunakan
   - Gunakan demo mode untuk testing

3. **Port Already in Use**
   ```bash
   streamlit run main.py --server.port 8502
   ```

### Demo Mode
Jika semua API gagal, AstraBot akan menggunakan demo mode yang memberikan respon dummy untuk testing.

---

**AstraBot** - Internal Helpdesk Chatbot | Built with ❤️ using OpenAI GPT & LangChain 