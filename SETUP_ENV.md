# 🔐 AstraBot - Environment Setup Guide

## 📋 Setup Environment Variables

Untuk menjalankan AstraBot dengan aman, Anda perlu mengatur environment variables untuk API keys.

### 🚀 Quick Setup

1. **Copy template file:**
```bash
cp config.env .env
```

2. **Edit file `.env` dan masukkan API keys Anda:**
```bash
# OpenRouter API Key (Recommended)
OPENROUTER_API_KEY=sk-or-v1-your-actual-api-key-here

# Mistral AI API Key (Alternative)
MISTRAL_API_KEY=your-mistral-api-key-here

# Groq API Key (High-speed alternative)
GROQ_API_KEY=your-groq-api-key-here
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Jalankan aplikasi:**
```bash
cd app && streamlit run main.py --server.port 8501
```

---

## 🔑 Getting API Keys

### OpenRouter (Recommended)
1. Kunjungi [OpenRouter.ai](https://openrouter.ai)
2. Daftar akun gratis
3. Dapatkan API key dari dashboard
4. Gratis untuk penggunaan dasar

### Mistral AI
1. Kunjungi [Mistral AI](https://mistral.ai)
2. Daftar akun
3. Dapatkan API key dari console
4. Ada free tier tersedia

### Groq
1. Kunjungi [Groq](https://groq.com)
2. Daftar akun
3. Dapatkan API key dari dashboard
4. Ada free tier tersedia

---

## 🛡️ Security Best Practices

### ✅ Do's:
- ✅ Simpan API keys di file `.env`
- ✅ Tambahkan `.env` ke `.gitignore`
- ✅ Gunakan environment variables di production
- ✅ Rotate API keys secara berkala
- ✅ Monitor penggunaan API

### ❌ Don'ts:
- ❌ Jangan commit API keys ke Git
- ❌ Jangan share API keys di public
- ❌ Jangan hardcode API keys di code
- ❌ Jangan gunakan API keys yang sama untuk multiple projects

---

## 🔧 Environment Variables Reference

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENROUTER_API_KEY` | OpenRouter API key | No* | `your_openrouter_api_key_here` |
| `MISTRAL_API_KEY` | Mistral AI API key | No* | `your_mistral_api_key_here` |
| `GROQ_API_KEY` | Groq API key | No* | `your_groq_api_key_here` |
| `DATABASE_URL` | Database connection string | No | `sqlite:///data/tickets.db` |
| `MOCK_API_URL` | Mock API endpoint | No | `http://localhost:8001` |
| `DEBUG` | Debug mode | No | `false` |
| `STREAMLIT_SERVER_PORT` | Streamlit port | No | `8501` |

*At least one API key is recommended for full functionality. Without API keys, AstraBot will use demo mode.

---

## 🎯 Demo Mode

Jika tidak ada API key yang valid, AstraBot akan menggunakan **Demo Mode**:
- ✅ Semua fitur tetap berfungsi
- ✅ Respon menggunakan dummy bot
- ✅ Perfect untuk testing dan demo
- ✅ Tidak memerlukan API key

---

## 🚀 Production Deployment

### Heroku
```bash
# Set environment variables
heroku config:set OPENROUTER_API_KEY=your-api-key
heroku config:set MISTRAL_API_KEY=your-api-key
heroku config:set GROQ_API_KEY=your-api-key
```

### Docker
```bash
# Build image
docker build -t astrabot .

# Run with environment variables
docker run -e OPENROUTER_API_KEY=your-api-key -p 8501:8501 astrabot
```

### Streamlit Cloud
1. Deploy ke Streamlit Cloud
2. Set environment variables di dashboard
3. Deploy otomatis

---

## 🔍 Troubleshooting

### "No valid API keys found"
- ✅ Pastikan file `.env` ada di root directory
- ✅ Pastikan format API key benar
- ✅ Cek apakah API key masih valid
- ✅ AstraBot akan menggunakan demo mode

### "ModuleNotFoundError: langchain_mistralai"
```bash
pip install langchain-mistralai langchain-groq
```

### "API key error"
- ✅ Cek koneksi internet
- ✅ Cek apakah API key valid
- ✅ Cek apakah ada credit di akun
- ✅ Coba provider lain

---

## 📞 Support

Jika ada masalah dengan setup:
1. Cek troubleshooting di atas
2. Lihat `README.md` untuk dokumentasi lengkap
3. Pastikan semua dependencies terinstall
4. Coba demo mode untuk testing

---

**AstraBot** - Internal Helpdesk Chatbot  
**Status**: ✅ **Ready for Production**  
**Security**: ✅ **Environment Variables Protected** 