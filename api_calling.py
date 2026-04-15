from google import genai
import os
from dotenv import load_dotenv
from gtts import gTTS
import io
load_dotenv()
api_key=os.environ.get("GEMINI_API")
#initialize a client
client=genai.Client(api_key=api_key)


def notegenerator(images):
    prompt="""Summarize the picture in note formet
      at max 250 words in bangla make sure to add necessary 
      markdown to different section"""
    response=client.models.generate_content(model='gemini-3-flash-preview',
                                            contents=[images,prompt])
    return response.text
def text_to_speech(text):
    speech=gTTS(text,lang='bn',slow=False)
    audio_buffer=io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer
def Quiz_generator(images,difficulty):
    prompt=f"""Generate 5 Quizes based on {difficulty} and make sure 
    to add markdown to differentiate the options and add correct answer too after the quiz """
    response=client.models.generate_content(model='gemini-3-flash-preview',
                                            contents=[images,prompt])
    return response.text




