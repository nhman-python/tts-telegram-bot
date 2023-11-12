import re
import uuid
import gtts
import langdetect
from .logs import logger


async def voice_creator(text):
    supported_languages = {'en', 'et', 'tr', 'da', 'fi'}
    language_mapping = {'he': 'iw'}

    try:
        detected_language = langdetect.detect(text)
    except langdetect.LangDetectException:
        detected_language = ''

    if language := language_mapping.get(detected_language, detected_language):
        try:
            tts = gtts.gTTS(text=text, lang=language, slow=False)
            output_file = f'{uuid.uuid4()}.mp3'
            tts.save(output_file)
            return output_file
        except Exception as e:
            logger.error(f"Error generating voice: {e}")
    return False


def remove_emojis_and_smileys(text):
    """
    Remove emojis and smileys from the given text.

    Args:
        text (str): Input text containing emojis and smileys.

    Returns:
        str: Text with emojis and smileys removed.
    """
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F700-\U0001F77F"  # alchemical symbols
                               u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                               u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                               u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                               u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                               u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                               u"\U00002702-\U000027B0"  # Dingbats
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)

    return re.sub(emoji_pattern, '', text).strip()


def create_message(length, res_time):
    """
    Create a response message for the edited message after the file was sent to the user.

    Args:
        length (int): The length of the message.
        res_time (float): The time it took to create the voice and send it back to the user.

    Returns:
        str: Formatted summary message with message length and creation time.
    """
    cool_emoji = "\U0001F60E"
    return f'סיכום {cool_emoji}:\nאורך ההודעה: {length} תווים\nמהירות יצירה: {res_time:.3f} שניות\n'
