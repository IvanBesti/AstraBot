# Setup Mistral AI untuk AstraBot

## Cara Mendapatkan API Key Mistral

### 1. Daftar di Mistral AI
1. Kunjungi https://console.mistral.ai/
2. Klik "Sign Up" dan buat akun
3. Verifikasi email Anda

### 2. Dapatkan API Key
1. Login ke console Mistral
2. Klik "API Keys" di sidebar
3. Klik "Create API Key"
4. Beri nama untuk API key (misal: "AstraBot")
5. Copy API key yang dihasilkan

### 3. Setup di AstraBot
1. Buka file `app/chatbot.py`
2. Cari baris: `MISTRAL_API_KEY = "YOUR_MISTRAL_API_KEY_HERE"`
3. Ganti dengan API key Anda:
   ```python
   MISTRAL_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   ```

### 4. Jalankan Aplikasi
```bash
cd app
streamlit run main.py --server.port 8501
```

## Model yang Tersedia

AstraBot menggunakan model `mistral-small-latest` yang:
- ✅ Gratis untuk penggunaan dasar
- ✅ Cepat dan responsif
- ✅ Mendukung function calling
- ✅ Bisa berbahasa Indonesia

## Troubleshooting

### Error 401 Unauthorized
- Pastikan API key sudah benar
- Pastikan API key belum expired
- Cek apakah akun sudah terverifikasi

### Error 404 Model Not Found
- Model `mistral-small-latest` sudah benar
- Pastikan koneksi internet stabil

### Fallback ke Demo Mode
Jika ada error, AstraBot akan otomatis fallback ke demo mode yang tetap berfungsi dengan baik.

## Biaya

- **Mistral Small**: Gratis untuk penggunaan dasar
- **Mistral Medium**: Berbayar per token
- **Mistral Large**: Berbayar per token

Untuk demo dan testing, Mistral Small sudah cukup! 