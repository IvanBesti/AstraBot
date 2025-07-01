# 🎯 AstraBot Demo Examples

Berikut adalah contoh-contoh interaksi dengan AstraBot untuk mendemonstrasikan fitur-fiturnya:

## 📋 Demo 0: Template Pertanyaan (CARA TERMUDAH!)

**Cara Pakai**: Klik tombol template → Pesan langsung terkirim → AstraBot langsung merespon!

### Template 1: 🔧 Buat Tiket Masalah
**[Klik tombol "🔧 Buat Tiket Masalah"]**
```
User: Saya ingin membuat tiket untuk masalah printer yang tidak berfungsi
Bot: Tiket berhasil dibuat dengan ID TCK20241201123456. Tim IT akan menghubungi Anda dalam 24 jam.
```

### Template 2: 👤 Buat Akun Karyawan
**[Klik tombol "👤 Buat Akun Karyawan"]**
```
User: Buatkan akun untuk karyawan baru bernama Andi dari departemen Marketing
Bot: Akun untuk Andi berhasil dibuat! Username: andi, Password: Astra2024!
```

### Template 3: 📊 Download Laporan
**[Klik tombol "📊 Download Laporan"]**
```
User: Saya ingin download laporan absensi bulan Juni
Bot: Berikut adalah file yang tersedia untuk download:
- laporan_absensi.csv (1.2 KB)
Silakan klik tombol Download untuk mengunduh file.
```

### Template 4: 📋 Cek Status Tiket
**[Klik tombol "📋 Cek Status Tiket"]**
```
User: Cek status tiket saya yang terakhir
Bot: Tiket TCK20241201123456 tidak ditemukan. Silakan buat tiket baru untuk mendapatkan bantuan.
```

---

## 🎫 Demo 1: Membuat Tiket (Manual)

**User:** Saya tidak bisa login ke portal HRIS

**Bot:** Baik, saya akan membuatkan tiket untuk masalah login portal HRIS. Mohon tunggu sebentar...
Tiket berhasil dibuat dengan ID TCK20241201123456. Tim IT akan menghubungi Anda dalam 24 jam.

---

**User:** Email saya tidak bisa dibuka, selalu error

**Bot:** Baik, saya akan membuatkan tiket untuk masalah email yang tidak bisa dibuka. Mohon tunggu sebentar...
Tiket berhasil dibuat dengan ID TCK20241201123457. Tim IT akan menghubungi Anda dalam 24 jam.

---

**User:** Printer di lantai 3 tidak berfungsi

**Bot:** Baik, saya akan membuatkan tiket untuk masalah printer di lantai 3. Mohon tunggu sebentar...
Tiket berhasil dibuat dengan ID TCK20241201123458. Tim IT akan menghubungi Anda dalam 24 jam.

## 👤 Demo 2: Membuat Akun (Manual)

**User:** Buatkan akun untuk karyawan baru bernama Andi Setiawan

**Bot:** Baik, saya akan membuatkan akun untuk Andi Setiawan. Mohon tunggu sebentar...
Akun untuk Andi Setiawan berhasil dibuat! Username: andi.setiawan, Password: Astra2024!

---

**User:** Tolong buat akun untuk Dinda Wijaya

**Bot:** Baik, saya akan membuatkan akun untuk Dinda Wijaya. Mohon tunggu sebentar...
Akun untuk Dinda Wijaya berhasil dibuat! Username: dinda.wijaya, Password: Astra2024!

---

**User:** Karyawan baru Eko Santoso perlu akun

**Bot:** Baik, saya akan membuatkan akun untuk Eko Santoso. Mohon tunggu sebentar...
Akun untuk Eko Santoso berhasil dibuat! Username: eko.santoso, Password: Astra2024!

## 📁 Demo 3: Download Data (Manual)

**User:** Saya ingin unduh laporan absensi Juni

**Bot:** Berikut adalah file yang tersedia untuk download:
- laporan_absensi.csv (1.2 KB)

Silakan klik tombol Download untuk mengunduh file.

---

**User:** Ada laporan gaji bulan ini?

**Bot:** Berikut adalah file yang tersedia untuk download:
- laporan_absensi.csv (1.2 KB)

Saat ini hanya tersedia laporan absensi Juni. Untuk laporan gaji, silakan hubungi HR.

---

**User:** Download semua laporan yang ada

**Bot:** Berikut adalah file yang tersedia untuk download:
- laporan_absensi.csv (1.2 KB)

Anda dapat mengunduh file yang tersedia melalui sidebar aplikasi.

## 📊 Demo 4: Cek Status Tiket (Manual)

**User:** Cek status tiket TCK20241201123456

**Bot:** Status tiket TCK20241201123456: open. Deskripsi: Saya tidak bisa login ke portal HRIS

---

**User:** Bagaimana status tiket saya?

**Bot:** Untuk mengecek status tiket, saya memerlukan ID tiket yang spesifik. Silakan berikan ID tiket yang ingin Anda cek.

## 💬 Demo 5: Pertanyaan Umum

**User:** Apa saja yang bisa kamu bantu?

**Bot:** Saya adalah AstraBot, asisten IT internal yang dapat membantu Anda dengan:

1. **Membuat tiket** untuk masalah teknis (login, email, printer, dll)
2. **Membuat akun** untuk karyawan baru
3. **Mengunduh laporan** dan data dari sistem
4. **Mengecek status tiket** yang sudah dibuat
5. **Memberikan informasi** umum tentang sistem

**Cara Tercepat**: Gunakan tombol template di atas untuk pertanyaan umum!

Silakan beri tahu saya apa yang bisa saya bantu!

---

**User:** Bagaimana cara membuat tiket?

**Bot:** Untuk membuat tiket, Anda bisa:

**Cara Tercepat**: Klik tombol "🔧 Buat Tiket Masalah" di atas!

**Cara Manual**: Beritahu saya masalah yang Anda alami. Contoh:
- "Saya tidak bisa login ke sistem"
- "Printer tidak berfungsi"
- "Email error"
- "Aplikasi crash"

Saya akan otomatis membuat tiket untuk masalah tersebut dan memberikan ID tiket kepada Anda.

---

**User:** Terima kasih atas bantuannya

**Bot:** Sama-sama! Senang bisa membantu Anda. Jika ada masalah lain, jangan ragu untuk bertanya lagi. Tim IT siap membantu Anda kapan saja!

## 🔧 Demo 6: Error Handling

**User:** Cek tiket yang tidak ada

**Bot:** Tiket TCK999999999 tidak ditemukan.

---

**User:** Buat akun tanpa nama

**Bot:** Maaf, saya memerlukan nama lengkap untuk membuat akun. Silakan berikan nama karyawan yang perlu dibuatkan akun.

## 🌟 Demo 7: Multi-LLM Support

**User:** Hai, apa kabar?

**Bot:** Halo! Kabar saya baik, terima kasih sudah bertanya. Saya AstraBot, asisten IT internal yang siap membantu Anda dengan berbagai masalah teknis. Ada yang bisa saya bantu hari ini?

*[Note: Respon ini bisa dari OpenRouter, Mistral, Groq, atau Demo Mode tergantung ketersediaan API]*

## 📱 Fitur Interface

### Template Buttons (Fitur Terbaru):
- **🔧 Buat Tiket Masalah**: Template untuk masalah teknis
- **👤 Buat Akun Karyawan**: Template untuk karyawan baru
- **📊 Download Laporan**: Template untuk unduh data
- **📋 Cek Status Tiket**: Template untuk cek tiket

### Sidebar Features:
- **Nama User**: Personalisasi dengan nama Anda
- **Bersihkan Chat**: Reset percakapan
- **Lihat Tiket**: Tampilkan semua tiket yang dibuat
- **Lihat File**: Tampilkan file yang tersedia untuk download

### Chat Interface:
- **Real-time Chat**: Interface modern dengan timestamp
- **Indonesian Language**: Semua respon dalam bahasa Indonesia
- **Responsive Design**: Bisa diakses dari mobile
- **Auto-refresh**: Otomatis update setelah input

## 🔧 Technical Features

### Multi-LLM Support:
- **OpenRouter** (default): Mendukung berbagai model
- **Mistral AI**: Model bahasa yang powerful
- **Groq**: Kecepatan tinggi
- **Demo Mode**: Fallback tanpa API key

### Database Features:
- Tiket tersimpan di SQLite database
- Data user tersimpan untuk referensi
- File download tersedia di folder downloads/

### API Integration:
- Mock API untuk simulasi pembuatan user
- Fallback mode jika API tidak tersedia
- Error handling yang robust

### Language Support:
- **Indonesian Responses**: Semua respon dalam bahasa Indonesia
- **Indonesian Templates**: Template pertanyaan dalam bahasa Indonesia
- **Indonesian Interface**: UI elements dalam bahasa Indonesia

---

## 🎯 Cara Penggunaan Terbaik

### **Untuk User Baru:**
1. **Gunakan Template Buttons** - Klik tombol sesuai kebutuhan
2. **Lihat Contoh di Sidebar** - Panduan penggunaan
3. **Chat Manual** - Jika ada pertanyaan spesifik

### **Untuk Admin:**
1. **Cek Tiket** - Lihat semua tiket di sidebar
2. **Cek File** - Lihat file yang tersedia
3. **Monitor Chat** - Pantau interaksi user

---

**Note:** Demo ini menggunakan multi-LLM support dengan fallback ke demo mode. Dalam implementasi nyata, Anda bisa:
1. Menggunakan OpenRouter API key (recommended)
2. Menggunakan Mistral AI API key
3. Menggunakan Groq API key
4. Menggunakan demo mode tanpa API key

**Status**: ✅ **READY TO USE** dengan Template Buttons + Indonesian Language + Multi-LLM Support 