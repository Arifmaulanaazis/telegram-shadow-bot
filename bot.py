import telebot
from telebot import types
from PIL import Image
import os

# Token bot Anda
TOKEN = 'TOKENBOTTELEGRAM'
bot = telebot.TeleBot(TOKEN)

# Simpan path gambar sementara
USER_IMAGE_PATH = ''

# Fungsi untuk menambahkan shadow
def add_shadow(image_path, shadow_path, output_path, shadow_height):
    image = Image.open(image_path).convert("RGBA")
    shadow = Image.open(shadow_path).convert("RGBA")
    image_width, image_height = image.size
    original_shadow_width, original_shadow_height = shadow.size

    if shadow_height != original_shadow_height:
        new_shadow_width = int(original_shadow_width * (shadow_height / original_shadow_height))
        shadow = shadow.resize((new_shadow_width, shadow_height), Image.LANCZOS)

    new_image = Image.new("RGBA", (image_width, image_height), (0, 0, 0, 0))
    new_image.paste(image, (0, 0))
    shadow_width, shadow_height = shadow.size

    for x in range(0, image_width, shadow_width):
        new_image.paste(shadow, (x, image_height - shadow_height), shadow)

    # Simpan gambar sebagai PNG
    new_image.save(output_path, format="PNG")

# Mulai bot
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Halo! Kirim gambar yang ingin ditambahkan shadow.")

# Handle gambar yang dikirim sebagai photo (dengan kompresi)
@bot.message_handler(content_types=['photo'])
def handle_image_photo(message):
    global USER_IMAGE_PATH
    photo = message.photo[-1]  # Mengambil foto dengan resolusi tertinggi
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    USER_IMAGE_PATH = f"{file_info.file_id}.jpg"
    with open(USER_IMAGE_PATH, 'wb') as new_file:
        new_file.write(downloaded_file)

    # Meminta user untuk menginput tinggi shadow
    msg = bot.reply_to(message, "Berapa tinggi shadow yang diinginkan? (Masukkan angka)")
    bot.register_next_step_handler(msg, process_shadow_height)

# Handle gambar yang dikirim sebagai document (tanpa kompresi)
@bot.message_handler(content_types=['document'])
def handle_image_document(message):
    global USER_IMAGE_PATH

    # Cek apakah file yang dikirim adalah gambar (berdasarkan extension)
    file_info = bot.get_file(message.document.file_id)
    file_extension = file_info.file_path.split('.')[-1].lower()

    if file_extension in ['jpg', 'jpeg', 'png']:
        downloaded_file = bot.download_file(file_info.file_path)
        USER_IMAGE_PATH = f"{file_info.file_id}.{file_extension}"

        with open(USER_IMAGE_PATH, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Meminta user untuk menginput tinggi shadow
        msg = bot.reply_to(message, "Berapa tinggi shadow yang diinginkan? (Masukkan angka)")
        bot.register_next_step_handler(msg, process_shadow_height)
    else:
        bot.reply_to(message, "File yang dikirim bukan gambar. Harap kirim file dengan format JPG atau PNG.")

# Proses tinggi shadow
def process_shadow_height(message):
    try:
        shadow_height = int(message.text)

        # Path gambar shadow yang harus ada di direktori yang sama
        shadow_path = "shadow.png"
        output_path = f"output_{USER_IMAGE_PATH}"

        # Tambahkan shadow ke gambar
        add_shadow(USER_IMAGE_PATH, shadow_path, output_path, shadow_height)

        # Kirim hasil gambar ke user
        with open(output_path, 'rb') as result_photo:
            bot.send_photo(message.chat.id, result_photo)

        # Hapus file sementara
        os.remove(USER_IMAGE_PATH)
        os.remove(output_path)

    except ValueError:
        bot.reply_to(message, "Input tidak valid. Harap masukkan angka untuk tinggi shadow.")

while True:
    try:
        bot.polling()
    except Exception as e:
        print(e)
        pass
