# Chatbot untuk Obat Lansia

Ini adalah aplikasi web Flask untuk chatbot yang memberikan informasi tentang obat untuk penyakit pada lansia.

## Fitur

- Memungkinkan pengguna berinteraksi dengan chatbot untuk menanyakan tentang obat untuk penyakit pada lansia.
- Memberikan rekomendasi obat berdasarkan pertanyaan pengguna.
- Antarmuka yang sederhana dan intuitif.

## Instalasi

1. Clone repositori:

    ```bash
    git clone https://github.com/SecretXpawn/webchatbot_AI.git
    ```

2. Buka direktori proyek:

    ```bash
    cd webchatbot_AI
    ```

3. Pasang dependensi:

    ```bash
    pip install -r requirements.txt
    ```

## Penggunaan

1. Mulai aplikasi Flask:

    ```bash
    python run.py
    ```

2. Buka web browser Anda dan buka [http://localhost:5000](http://localhost:5000) untuk mengakses aplikasi.

3. Berinteraksi dengan chatbot dengan mengetik pesan dan menerima respons.

## Konfigurasi

- Anda mungkin perlu mengonfigurasi file `config.py` untuk menentukan detail koneksi database dan kunci API jika diperlukan.

## Struktur File

```
your_flask_app/
│
├── app/
│   ├── __init__.py
│   ├── model.py
│   ├── routes.py
│   ├── templates/
│   │   ├── index.html
│   │   └── chat.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── script.js
│
├── data/
│   └── Medicine_Description.xlsx 
│
├── config.py
├── requirements.txt
└── run.py
```

Pastikan untuk menyesuaikan nama direktori dan file dengan struktur proyek Anda.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan buka sebuah isu atau kirimkan permintaan tarik.

## Lisensi

Tidak ada lisensi yang diberikan untuk proyek ini.

