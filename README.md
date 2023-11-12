# TTS Telegram Bot

TTS Telegram Bot is a Telegram bot that converts text messages into speech using text-to-speech (TTS) technology. Users
can send text messages to the bot, and it will generate audio files in response.

## Features

- **Text to Speech Conversion:** Converts text messages to speech.
- **Character Limit:** Supports messages up to 350 characters.
- **Rate Limiting:** Limits the number of messages a user can send within 5 minutes.
- **Summary Message:** Provides a summary message with the length of the message and creation time of the audio file.

## Requirements

- **Python 3.x**
- **Pyrogram:** A Python wrapper for the Telegram API. [Pyrogram Documentation](https://docs.pyrogram.org/)
- **gTTS (Google Text-to-Speech):** A Python library and CLI tool to interface with Google Translate's text-to-speech
  API. [gTTS PyPI Page](https://pypi.org/project/gTTS/)

## Setup Instructions

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/nhman-python/tts-telegram-bot.git
   ```

2. **Navigate to the Project Directory:**
   ```sh
   cd tts-telegram-bot
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Bot:**
   ```sh
   python3 app.py
   ```

## Usage

1. **Start a Chat:**
   Start a chat with the bot on Telegram.

2. **Send Text Message:**
   Send a text message within the character limit (350 characters) to the bot.

3. **Receive Audio File:**
   Wait for the bot to generate and send an audio file in response to your message.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.