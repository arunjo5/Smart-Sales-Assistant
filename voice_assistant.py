import os
import speech_recognition as sr
import requests
import pyttsx3
import openai
from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import sys

os.environ["OPENAI_API_KEY"] = 'YOUR API KEY'


def getWhisperResponse(audio):
    with open("/home/pi/Downloads/microphone.wav", "wb") as f:
        f.write(audio.get_wav_data())
    file = open("/home/pi/Downloads/microphone.wav", "rb")
    response = openai.Audio.transcribe(model="whisper-1", file=file)
    os.remove("/home/pi/Downloads/microphone.wav")
    return response.text


def voice_bot(microphone: sr.Microphone, recognizer: sr.Recognizer):
    OPENAI_API_KEY = 'YOUR API KEY'
    openai.api_key = OPENAI_API_KEY

    # instatiate speaker and set speaker rate
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    # set gender based voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'english+f4')

    # start a loop for pinput
    while True:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Say something!")
            audio = recognizer.listen(source)

            try:
                # convert audio to text using Google speech API
                whisperresponse: str = getWhisperResponse(audio)

                # check for wake up word
                if "hello" in whisperresponse.lower():
                    # create user
                    engine.say("Hi, Welcome")

    max_input_size = 4096
    num_outputs = 256
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs))

    documents = SimpleDirectoryReader("/home/pi/Documents").load_data()
    index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index.save_to_disk('index.json')
    query_engine = GPTSimpleVectorIndex.load_from_disk('index.json')
    chatgpt_response = query_engine.query(whisperresponse, response_mode="compact")
    engine.say(chatgpt_response)
    engine.runAndWait()

except sr.UnknownValueError:
print("Recognizer unknown error")
except sr.RequestError as e:
print(f"Request Error Speeck Recognizer {e}")

if __name__ == "__main__":
    # create a recognizer
    recoginzer = sr.Recognizer()
    mcrophone = sr.Microphone()
    # start the bot
    voice_bot(mcrophone, recoginzer)