# **Telegram Shadow Bot**
<p align="center">
  <img src="icon.png" alt="Telegram Shadow Bot Icon" width="300" height="300">
</p>

## Deskripsi
Telegram Shadow Bot adalah sebuah bot yang dibuat dengan Python, yang dapat menambahkan bayangan (shadow) pada gambar yang dikirimkan oleh pengguna melalui Telegram. Gambar hasil proses akan dikirim kembali ke pengguna setelah ditambahkan bayangan.

---

## Preinstalasi
Sebelum menjalankan aplikasi ini, pastikan Anda sudah menginstall **Python** atau **Anaconda** di komputer Anda:

- [Download Python](https://www.python.org/downloads/)
- [Download Anaconda](https://www.anaconda.com/products/individual)

---

## Cara Instalasi

1. Clone repository ini ke komputer Anda:

    ```bash
    git clone https://github.com/Arifmaulanaazis/telegram-shadow-bot.git
    cd telegram-shadow-bot
    ```

2. Install semua library yang diperlukan dengan menjalankan perintah berikut:

    ```bash
    pip install -r requirements.txt
    ```

---

## Cara Menjalankan Bot

1. Buka file `bot.py` dan masukkan token bot Telegram Anda di baris:

    ```python
    TOKEN = 'TOKENBOTTELEGRAM'
    ```

2. Setelah itu, jalankan kode dengan perintah:

    ```bash
    python bot.py
    ```

3. Bot akan mulai polling dan siap menerima gambar untuk ditambahkan shadow.

---

## Cara Berkontribusi

Kami menyambut kontribusi dari siapa pun. Jika Anda ingin berkontribusi, ikuti langkah-langkah berikut:

1. Fork repository ini
2. Buat branch baru untuk fitur atau perbaikan yang ingin Anda tambahkan (`git checkout -b feature-branch`)
3. Commit perubahan Anda (`git commit -m 'Add some feature'`)
4. Push branch ke GitHub (`git push origin feature-branch`)
5. Buat pull request dan kami akan melakukan review terhadap perubahan Anda

---

## Lisensi
Aplikasi ini dilisensikan di bawah Lisensi MIT. Silakan lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.