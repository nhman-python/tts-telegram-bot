import os
import time
import uuid
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from utility import utility
from utility import db
from utility.logs import logger


app = Client("tts_bot")


@app.on_message(filters.private & filters.command("start"))
async def handle_start(_, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    db.user_logger(user_id)
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("➕ הצטרף לפייתון טיפ ישראל", url="https://t.me/python_tip_israel")]]
    )
    await app.send_message(
        chat_id,
        '🤖 ברוכים הבאים ל- TTS Creator! 🎙️\nשלח לי טקסט, ואני אמיר אותו לדיבור.',
        reply_markup=keyboard
    )


@app.on_message(filters.private & filters.text)
async def send_audio(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    start = time.time()
    if not db.check_message_limit(user_id):
        await app.send_message(chat_id, 'הגעת למגבלת ההודעות שניתן לשלוח ב-5 דקות. נסה שוב מאוחר יותר.')
        return

    if len(message.text) > 350:
        await app.send_chat_action(chat_id, action=enums.ChatAction.TYPING)
        await app.send_message(chat_id, 'אני יכול לקבל רק עד 350 תווים.\nנסה שוב.')
    elif message.text:
        message_reply = await app.send_message(chat_id, 'אנא המתן, יוצר קובץ שמע כעת...')
        logger.info(f'Received text from user {user_id}: {message.text}')

        audio_path: str = await utility.voice_creator(message.text)
        if audio_path and os.path.isfile(audio_path):
            res = open(audio_path, 'rb')
            await app.send_chat_action(chat_id, action=enums.ChatAction.UPLOAD_DOCUMENT)
            if await app.send_audio(chat_id, audio=res, file_name=f'{uuid.uuid4()}.mp3'):
                res_time = time.time() - start
                message_length = len(message.text)
                await app.edit_message_text(chat_id, message_reply.id, utility.create_message(message_length, res_time))
                os.remove(audio_path)
                db.update_message_count(user_id)
                logger.info(f'Audio sent to user {user_id}')
        else:
            await app.edit_message_text(chat_id, message_reply.id,
                                        "טקסט לא מזוהה. בבקשה נסה שוב!")
    else:
        await app.send_message(chat_id, 'נא לשלוח טקסט בלבד!')


if __name__ == '__main__':
    app.run()
