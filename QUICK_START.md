# 🚀 AstraBot - Quick Start Guide

## ✅ **Status: SEMUA BERHASIL DIINSTALL & BERJALAN!**

AstraBot sudah berhasil diinstall dan berjalan di sistem Anda!

---

## 🌐 **Akses Aplikasi**

### **1. Streamlit App (Main Interface)**
- **URL**: http://localhost:8501
- **Status**: ✅ Berjalan
- **Fitur**: Chat interface utama dengan AstraBot + Template Pertanyaan

### **2. Mock API (Backend)**
- **URL**: http://localhost:8001
- **Status**: ✅ Berjalan
- **Fitur**: Simulasi API untuk pembuatan user

---

## 🎯 **Cara Menggunakan AstraBot**

### **Step 1: Buka Browser**
Buka browser dan kunjungi: **http://localhost:8501**

### **Step 2: Gunakan Template Pertanyaan (REKOMENDASI)**
AstraBot menyediakan 4 tombol template yang bisa langsung diklik:

1. **🔧 Buat Tiket Masalah** - Untuk masalah teknis
2. **👤 Buat Akun Karyawan** - Untuk karyawan baru
3. **📊 Download Laporan** - Untuk unduh data
4. **📋 Cek Status Tiket** - Untuk cek tiket

**Cara pakai**: Klik tombol → Pesan langsung terkirim → AstraBot langsung merespon!

### **Step 3: Chat Manual (Opsional)**
1. Masukkan nama Anda di sidebar (opsional)
2. Ketik pesan di chat input
3. Tekan Enter untuk mengirim

---

## 💬 **Contoh Interaksi**

### **Menggunakan Template (Cepat)**
```
[Klik tombol "🔧 Buat Tiket Masalah"]
AstraBot: Tiket berhasil dibuat dengan ID TCK20241201123456. Tim IT akan menghubungi Anda dalam 24 jam.
```

### **Chat Manual**
```
Anda: Saya tidak bisa login ke portal HRIS
AstraBot: Baik, saya akan membuatkan tiket untuk masalah login portal HRIS. Mohon tunggu sebentar...
Tiket berhasil dibuat dengan ID TCK20241201123456. Tim IT akan menghubungi Anda dalam 24 jam.
```

### **Membuat Akun**
```
Anda: Buatkan akun untuk karyawan baru bernama Andi
AstraBot: Baik, saya akan membuatkan akun untuk Andi. Mohon tunggu sebentar...
Akun untuk Andi berhasil dibuat! Username: andi, Password: Astra2024!
```

### **Download Data**
```
Anda: Saya ingin unduh laporan absensi Juni
AstraBot: Berikut adalah file yang tersedia untuk download:
- laporan_absensi.csv (1.2 KB)
Silakan klik tombol Download untuk mengunduh file.
```

---

## 🛠️ **Fitur Interface**

### **Template Pertanyaan Cepat**
- **🔧 Buat Tiket Masalah**: "Saya ingin membuat tiket untuk masalah printer yang tidak berfungsi"
- **👤 Buat Akun Karyawan**: "Buatkan akun untuk karyawan baru bernama Andi dari departemen Marketing"
- **📊 Download Laporan**: "Saya ingin download laporan absensi bulan Juni"
- **📋 Cek Status Tiket**: "Cek status tiket saya yang terakhir"

### **Sidebar Features**
- ⚙️ **Konfigurasi**: Nama user, bersihkan chat
- 🚀 **Aksi Cepat**: Lihat tiket, lihat file
- ❓ **Bantuan**: Contoh pertanyaan

### **Chat Interface**
- 💬 **Real-time Chat**: Interface modern
- 📱 **Responsive**: Bisa diakses dari mobile
- 🌏 **Bahasa Indonesia**: Semua respon dalam bahasa Indonesia

---

## 🔧 **Troubleshooting**

### **Jika aplikasi tidak bisa diakses:**

#### **1. Cek apakah aplikasi berjalan**
```bash
# Cek Mock API
curl http://localhost:8001/

# Cek Streamlit
curl http://localhost:8501/
```

#### **2. Restart aplikasi**
```bash
# Stop aplikasi (Ctrl+C di terminal)
# Kemudian jalankan ulang:

# Terminal 1 - Mock API
cd mock_api && python3 user_api.py

# Terminal 2 - Streamlit
cd app && streamlit run main.py --server.port 8501
```

#### **3. Jika ada error dependencies**
```bash
# Reinstall dependencies
python3 -m pip install -r requirements.txt --upgrade
```

### **Jika LLM tidak merespon:**
1. **Demo Mode**: AstraBot akan menggunakan demo mode jika API gagal
2. **Cek API Key**: Pastikan API key valid (jika menggunakan)
3. **Cek Internet**: Pastikan koneksi internet stabil

---

## 📊 **Database & Data**

### **Lokasi File**
- **Database**: `data/tickets.db`
- **Sample Files**: `downloads/laporan_absensi.csv`
- **Logs**: `logs/` (jika ada)

### **Cek Data Tiket**
```bash
# Lihat database
sqlite3 data/tickets.db "SELECT * FROM tickets;"
```

---

## 🌟 **Fitur Baru**

### **Template Pertanyaan**
- ✅ Tombol template untuk pertanyaan umum
- ✅ Langsung mengirim pesan tanpa perlu mengetik
- ✅ Mendukung 4 jenis pertanyaan utama

### **Multi-LLM Support**
- ✅ OpenRouter sebagai provider utama
- ✅ Fallback ke provider lain jika gagal
- ✅ Demo mode untuk testing tanpa API key

### **Bahasa Indonesia**
- ✅ Semua respon dalam bahasa Indonesia
- ✅ Template pertanyaan dalam bahasa Indonesia
- ✅ Interface yang user-friendly

---

## 🎉 **Selamat!**

AstraBot sudah siap digunakan! Anda bisa:

- 🎫 **Membuat tiket** untuk masalah teknis (dengan template!)
- 👤 **Membuat akun** untuk karyawan baru (dengan template!)
- 📁 **Download laporan** dan data (dengan template!)
- 💬 **Chat** dengan AI assistant dalam bahasa Indonesia

---

## 📞 **Support**

Jika ada masalah:
1. Cek troubleshooting di atas
2. Lihat `README.md` untuk dokumentasi lengkap
3. Lihat `demo_examples.md` untuk contoh penggunaan
4. Buat issue di repository

---

**AstraBot** - Internal Helpdesk Chatbot | Status: ✅ **READY TO USE!** 

**Fitur Terbaru**: Template Pertanyaan + Bahasa Indonesia + Multi-LLM Support 