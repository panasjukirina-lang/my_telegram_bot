import telebot
# Імпортуємо типи даних для створення кнопок
from telebot import types

TOKEN = '8822010460:AAHGe1nhV7ZE4xeGu2chz1m6Qy9EpeOHbME'
bot = telebot.TeleBot(TOKEN)

# Спрямуємо боту посилання на ваш документ (замініть на своє)
GOOGLE_DRIVE_URL = 'https://docs.google.com/document/d/1uf-ly3J3H7u1UXPXNfhXV145sqyN9_AcXdVwTUAJnhQ/edit?usp=sharing'

# Реагуємо на команду /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Створюємо звичайну клавіатуру, яка з'явиться внизу екрана
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_schedule = types.KeyboardButton("Показати розклад 📅")
    markup.add(btn_schedule)
    
    bot.send_message(
        message.chat.id, 
        "Привіт! Натисніть на кнопку нижче, щоб отримати доступ до розкладу.", 
        reply_markup=markup
    )

# Обробляємо натискання на звичайну кнопку "Показати rozklad"
@bot.message_handler(func=lambda message: message.text == "Показати розклад 📅")
def show_schedule(message):
    # Створюємо інлайн-клавіатуру (кнопку під повідомленням)
    inline_markup = types.InlineKeyboardMarkup()
    
    # Створюємо кнопку-посилання. Параметр url вказує, куди перенаправити користувача
    url_button = types.InlineKeyboardButton(text="Відкрити розклад на Google Диску 🔗", url=GOOGLE_DRIVE_URL)
    
    # Додаємо кнопку в розмітку
    inline_markup.add(url_button)
    
    # Надсилаємо повідомлення разом із цією кнопкою
    bot.send_message(
        message.chat.id, 
        "Натисніть на кнопку нижче, щоб перейти до документа з розкладом:", 
        reply_markup=inline_markup
    )

if __name__ == '__main__':
    print("Бот запущений і чекає на команду...")
    bot.infinity_polling()
