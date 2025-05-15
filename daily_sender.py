from telegram import Bot
from datetime import datetime

BOT_TOKEN = "7020279588:AAER0SU6QqAeqTPQfHfijWNJ5fOeKsVLXrk"
CHAT_ID = 1688425359

def generate_forecast():
    return f"""📅 HAIL Forecast – {datetime.now().strftime('%B %d, %Y')}

1. 🌩️ Nebraska, South Dakota, North Dakota
2. ⛈️ Illinois, Wisconsin, Michigan
3. 🌧️ Ohio, Kentucky, Tennessee

(This is an automated message.)
"""

def main():
    bot = Bot(token=BOT_TOKEN)
    forecast_message = generate_forecast()
    bot.send_message(chat_id=CHAT_ID, text=forecast_message)

if __name__ == "__main__":
    main()
