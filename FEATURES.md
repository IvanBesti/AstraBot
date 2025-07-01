# 🌟 AstraBot - Features Documentation

## 📋 Overview

AstraBot adalah chatbot internal IT helpdesk yang dirancang untuk membantu karyawan dengan masalah teknis, pembuatan akun, dan pengunduhan data. Dibangun dengan teknologi modern dan mendukung berbagai LLM provider.

---

## 🎯 Core Features

### 1. 📋 Template Pertanyaan Cepat
**Status**: ✅ **IMPLEMENTED**

Fitur terbaru yang memungkinkan user mengirim pertanyaan dengan satu klik:

#### Template Buttons:
- **🔧 Buat Tiket Masalah**: "Saya ingin membuat tiket untuk masalah printer yang tidak berfungsi"
- **👤 Buat Akun Karyawan**: "Buatkan akun untuk karyawan baru bernama Andi dari departemen Marketing"
- **📊 Download Laporan**: "Saya ingin download laporan absensi bulan Juni"
- **📋 Cek Status Tiket**: "Cek status tiket saya yang terakhir"

#### Cara Kerja:
1. User klik tombol template
2. Pesan langsung terkirim ke AstraBot
3. AstraBot langsung memproses dan merespon
4. Tidak perlu mengetik manual

#### Keunggulan:
- ✅ User-friendly untuk user baru
- ✅ Mengurangi kesalahan input
- ✅ Akses cepat ke fitur utama
- ✅ Template dalam bahasa Indonesia

---

### 2. 🎫 Pembuatan Tiket Otomatis
**Status**: ✅ **IMPLEMENTED**

Sistem pembuatan tiket support yang otomatis:

#### Fitur:
- ✅ Auto-generate ticket ID (format: TCK + timestamp)
- ✅ Simpan ke database SQLite
- ✅ Informasi lengkap (user, deskripsi, status, timestamp)
- ✅ Interface untuk melihat semua tiket
- ✅ Respon dalam bahasa Indonesia

#### Database Schema:
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

#### Contoh Penggunaan:
```
User: "Saya tidak bisa login ke portal HRIS"
Bot: "Tiket berhasil dibuat dengan ID TCK20241201123456. Tim IT akan menghubungi Anda dalam 24 jam."
```

---

### 3. 👤 Pembuatan Akun Karyawan
**Status**: ✅ **IMPLEMENTED**

Sistem pembuatan akun untuk karyawan baru:

#### Fitur:
- ✅ Mock API dengan FastAPI
- ✅ Auto-generate username dan password
- ✅ Fallback mode jika API tidak tersedia
- ✅ Simpan data user ke database
- ✅ Respon dalam bahasa Indonesia

#### API Endpoints:
- `POST /create_user` - Membuat akun baru
- `GET /` - Health check

#### Contoh Penggunaan:
```
User: "Buatkan akun untuk Andi"
Bot: "Akun untuk Andi berhasil dibuat! Username: andi, Password: Astra2024!"
```

---

### 4. 📁 Download Data
**Status**: ✅ **IMPLEMENTED**

Sistem pengunduhan file dan laporan:

#### Fitur:
- ✅ File management system
- ✅ Sample CSV file untuk demo
- ✅ Interface download dengan Streamlit
- ✅ Support untuk berbagai format file
- ✅ Respon dalam bahasa Indonesia

#### File yang Tersedia:
- `laporan_absensi.csv` - Sample laporan absensi

#### Contoh Penggunaan:
```
User: "Saya ingin unduh laporan absensi Juni"
Bot: "Berikut adalah file yang tersedia untuk download: laporan_absensi.csv"
```

---

### 5. 💬 Chat Interface Modern
**Status**: ✅ **IMPLEMENTED**

Interface chat yang modern dan responsif:

#### Fitur:
- ✅ Modern Streamlit interface dengan custom CSS
- ✅ Real-time chat dengan history
- ✅ Sidebar untuk konfigurasi dan aksi cepat
- ✅ Responsive design (mobile-friendly)
- ✅ Template buttons untuk pertanyaan cepat
- ✅ Timestamp untuk setiap pesan

#### UI Components:
- **Main Chat Area**: Real-time chat interface
- **Sidebar**: Konfigurasi, aksi cepat, bantuan
- **Template Buttons**: Quick question interface
- **File Download Area**: Interface untuk unduh file
- **Ticket Management**: Lihat semua tiket

---

### 6. 🤖 Multi-LLM Support
**Status**: ✅ **IMPLEMENTED**

Sistem yang mendukung berbagai LLM provider:

#### Provider Priority:
1. **OpenRouter** (default) - Mendukung berbagai model
2. **Mistral AI** - Model bahasa yang powerful
3. **Groq** - Kecepatan tinggi
4. **Demo Mode** - Fallback tanpa API key

#### Supported Models:
- **OpenRouter**: `mistralai/mistral-7b-instruct`, `meta-llama/llama-3-70b-instruct`
- **Mistral**: `mistral-small-latest`, `mistral-medium-latest`
- **Groq**: `llama3-8b-8192`, `mixtral-8x7b-32768`

#### Fallback System:
- ✅ Automatic fallback jika API gagal
- ✅ Demo mode untuk testing tanpa API key
- ✅ Error handling yang robust
- ✅ Graceful degradation

---

### 7. 🌏 Bahasa Indonesia
**Status**: ✅ **IMPLEMENTED**

Dukungan penuh untuk bahasa Indonesia:

#### Fitur:
- ✅ Semua respon dalam bahasa Indonesia
- ✅ Template pertanyaan dalam bahasa Indonesia
- ✅ Interface yang user-friendly
- ✅ Prompt templates dalam bahasa Indonesia
- ✅ Error messages dalam bahasa Indonesia

#### Contoh Respon:
```
Bot: "Tiket berhasil dibuat dengan ID TCK20241201123456. Tim IT akan menghubungi Anda dalam 24 jam."
Bot: "Akun untuk Andi berhasil dibuat! Username: andi, Password: Astra2024!"
Bot: "Berikut adalah file yang tersedia untuk download: laporan_absensi.csv"
```

---

## 🛠️ Technical Features

### Backend Technologies:
- **LangChain**: AI orchestration framework
- **OpenRouter API**: Multi-model LLM provider
- **Mistral AI**: Alternative LLM provider
- **Groq**: High-speed LLM provider
- **SQLite**: Database untuk tiket dan user
- **FastAPI**: Mock API server
- **Pandas**: Data manipulation

### Frontend Technologies:
- **Streamlit**: Web interface framework
- **Custom CSS**: Modern styling
- **Template Buttons**: Quick question interface
- **Real-time Chat**: Responsive chat interface
- **Indonesian UI**: Localized interface

### Tools & Functions:
- **create_ticket**: Membuat tiket support
- **create_user_account**: Membuat akun karyawan
- **get_download_files**: Mendapatkan daftar file
- **get_ticket_status**: Cek status tiket

---

## 📊 Database Features

### Tables:
1. **tickets** - Menyimpan data tiket support
2. **users** - Menyimpan data user

### Data Management:
- ✅ Auto-increment IDs
- ✅ Timestamp tracking
- ✅ Unique constraints
- ✅ Foreign key relationships (future)

---

## 🔧 Configuration

### Environment Variables:
- `OPENROUTER_API_KEY`: API key OpenRouter (recommended)
- `MISTRAL_API_KEY`: API key Mistral AI
- `GROQ_API_KEY`: API key Groq

### Customization Points:
- `app/prompts.yaml`: Edit prompt templates (Indonesian)
- `app/utils.py`: Add new helper functions
- `app/main.py`: Modify template buttons
- `app/chatbot.py`: Add new LLM providers

---

## 🚀 Deployment Features

### Local Development:
- ✅ Easy setup dengan requirements.txt
- ✅ Mock API untuk testing
- ✅ Demo mode tanpa API key
- ✅ Hot reload dengan Streamlit

### Production Ready:
- ✅ Multi-LLM support dengan fallback
- ✅ Error handling yang robust
- ✅ Database management
- ✅ API integration

---

## 📈 Performance Features

### Speed Optimizations:
- ✅ Template buttons untuk akses cepat
- ✅ LLM provider fallback untuk reliability
- ✅ Database indexing untuk query cepat
- ✅ Caching untuk file operations

### Scalability:
- ✅ Modular architecture
- ✅ Easy to add new LLM providers
- ✅ Easy to add new features
- ✅ Database abstraction layer

---

## 🔒 Security Features

### Data Protection:
- ✅ API keys disimpan di environment variables
- ✅ Database menggunakan proper escaping
- ✅ Input validation pada semua endpoints
- ✅ Error handling yang comprehensive

### Access Control:
- ✅ Mock API untuk testing
- ✅ Demo mode untuk public access
- ✅ Database isolation
- ✅ File access controls

---

## 🎯 User Experience Features

### Ease of Use:
- ✅ Template buttons untuk pertanyaan umum
- ✅ Interface dalam bahasa Indonesia
- ✅ Responsive design untuk mobile
- ✅ Clear error messages

### Accessibility:
- ✅ Keyboard navigation
- ✅ Screen reader friendly
- ✅ High contrast interface
- ✅ Mobile responsive

---

## 🌟 Future Enhancements

### Planned Features:
- 🔄 Email notifications untuk tiket
- 🔄 Real-time chat dengan WebSocket
- 🔄 File upload capabilities
- 🔄 User authentication system
- 🔄 Advanced ticket management
- 🔄 Integration dengan sistem HR
- 🔄 Multi-language support (English, etc.)
- 🔄 Voice input/output

### Technical Improvements:
- 🔄 PostgreSQL database
- 🔄 Redis caching
- 🔄 Docker containerization
- 🔄 CI/CD pipeline
- 🔄 Monitoring dan logging
- 🔄 API rate limiting
- 🔄 Backup dan recovery

---

## 📊 Feature Status Summary

| Feature | Status | Priority | Notes |
|---------|--------|----------|-------|
| Template Pertanyaan | ✅ Complete | High | Fitur terbaru |
| Ticket Creation | ✅ Complete | High | Core feature |
| User Account Creation | ✅ Complete | High | Core feature |
| File Download | ✅ Complete | High | Core feature |
| Chat Interface | ✅ Complete | High | Core feature |
| Multi-LLM Support | ✅ Complete | High | Robust system |
| Indonesian Language | ✅ Complete | High | User-friendly |
| Database Management | ✅ Complete | Medium | SQLite |
| Mock API | ✅ Complete | Medium | Testing |
| Error Handling | ✅ Complete | Medium | Robust |
| Documentation | ✅ Complete | Medium | Comprehensive |

---

**AstraBot** - Internal Helpdesk Chatbot  
**Status**: ✅ **PRODUCTION READY**  
**Latest Features**: Template Questions + Indonesian Language + Multi-LLM Support 