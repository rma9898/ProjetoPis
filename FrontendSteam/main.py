from bot_instance import bot
import handlers.start
import handlers.promocoes_steam
import handlers.promocoes_steam_callbacks


if __name__ == "__main__":
  print("Bot iniciado...")
  bot.infinity_polling(timeout=10, long_polling_timeout=5)