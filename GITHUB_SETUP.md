# 🚀 AstraBot - GitHub Setup Guide

## 📋 Persiapan untuk Push ke GitHub

AstraBot sudah dikonfigurasi dengan aman untuk deployment ke GitHub. Berikut adalah langkah-langkah yang perlu dilakukan:

### ✅ Yang Sudah Dikonfigurasi

1. **Environment Variables** - API keys disimpan di `.env` (tidak di-commit)
2. **Gitignore** - File sensitif sudah di-exclude
3. **Template Files** - `config.env` sebagai template
4. **Security** - Tidak ada hardcoded API keys

### 🔐 File Keamanan

| File | Status | Keterangan |
|------|--------|------------|
| `.env` | ✅ **SAFE** | Berisi API keys asli (tidak di-commit) |
| `config.env` | ✅ **SAFE** | Template tanpa API keys asli |
| `.gitignore` | ✅ **SAFE** | Mengexclude file sensitif |
| `app/chatbot.py` | ✅ **SAFE** | Menggunakan environment variables |

---

## 🚀 Langkah Push ke GitHub

### 1. Inisialisasi Git Repository
```bash
# Jika belum ada git repository
git init

# Add semua file (kecuali yang di .gitignore)
git add .

# Commit pertama
git commit -m "Initial commit: AstraBot Internal Helpdesk Chatbot"
```

### 2. Buat Repository di GitHub
1. Buka [GitHub.com](https://github.com)
2. Klik "New repository"
3. Beri nama: `AstraBot` atau `internal-helpdesk-chatbot`
4. **JANGAN** centang "Add a README file" (karena sudah ada)
5. Klik "Create repository"

### 3. Push ke GitHub
```bash
# Tambahkan remote origin
git remote add origin https://github.com/USERNAME/REPOSITORY_NAME.git

# Push ke main branch
git branch -M main
git push -u origin main
```

---

## 🔍 Verifikasi Keamanan

### Cek File yang Akan Di-commit
```bash
# Lihat file yang akan di-commit
git status

# Pastikan .env TIDAK ada di daftar
# Pastikan config.env ADA di daftar
```

### Cek Isi Repository
```bash
# Lihat file yang sudah di-track
git ls-files

# Pastikan tidak ada file sensitif
grep -r "sk-" .  # Cari API keys
grep -r "your_api_key" .  # Cari placeholder
```

---

## 📚 Dokumentasi untuk Contributors

### Setup untuk Developer Baru
```bash
# Clone repository
git clone https://github.com/USERNAME/REPOSITORY_NAME.git
cd REPOSITORY_NAME

# Setup environment
cp config.env .env
# Edit .env dengan API keys

# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
cd app && streamlit run main.py
```

### Environment Variables yang Diperlukan
```bash
# Wajib (pilih salah satu)
OPENROUTER_API_KEY=sk-or-v1-your-key-here
MISTRAL_API_KEY=your-mistral-key-here
GROQ_API_KEY=your-groq-key-here

# Opsional
DATABASE_URL=sqlite:///data/tickets.db
MOCK_API_URL=http://localhost:8001
DEBUG=false
```

---

## 🛡️ Security Checklist

### ✅ Pre-Push Checklist
- [ ] `.env` file TIDAK di-commit
- [ ] `config.env` ADA di-commit (template)
- [ ] Tidak ada hardcoded API keys di code
- [ ] `.gitignore` sudah benar
- [ ] Dependencies sudah di-update
- [ ] Dokumentasi sudah lengkap

### ✅ Post-Push Verification
- [ ] Repository di GitHub tidak berisi API keys
- [ ] Semua file template ada
- [ ] README.md bisa diakses
- [ ] Setup instructions jelas

---

## 🎯 Demo Mode

Jika repository di-clone tanpa API keys:
- ✅ AstraBot akan menggunakan **Demo Mode**
- ✅ Semua fitur tetap berfungsi
- ✅ Perfect untuk testing dan demo
- ✅ Tidak memerlukan setup tambahan

---

## 📞 Support & Maintenance

### Update Dependencies
```bash
# Update requirements.txt
pip freeze > requirements.txt

# Commit perubahan
git add requirements.txt
git commit -m "Update dependencies"
git push
```

### Environment Variables Update
```bash
# Update config.env template
# Commit perubahan
git add config.env
git commit -m "Update environment variables template"
git push
```

---

## 🔗 Links Penting

- **Repository**: `https://github.com/USERNAME/REPOSITORY_NAME`
- **Live Demo**: `https://astrabot-demo.streamlit.app` (jika di-deploy)
- **Documentation**: `README.md`
- **Setup Guide**: `SETUP_ENV.md`

---

**Status**: ✅ **Ready for GitHub**  
**Security**: ✅ **Environment Variables Protected**  
**Demo Mode**: ✅ **Available without API keys** 