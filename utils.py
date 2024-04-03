import os
import time
from dotenv import load_dotenv
from collections import  namedtuple
from deepgram import (
    DeepgramClient,
    SpeakOptions,
)

result = namedtuple("result", ["provider", "model", "text", "ttft", "total_time"])

load_dotenv(override=True)  # take environment variables from .env.

# ------ Deepgram ------
deepgram_api_key = os.getenv("DEEPGRAM_API_KEY")
if not deepgram_api_key:
    raise Exception("Please check that you've indicated DEEPGRAM_API_KEY in your .env file")

deepgram = DeepgramClient(api_key=deepgram_api_key)


def qa_deepgram(text: str, voice: str="asteria", model: str="aura", lang: str="en", encoding:str="mp3", to_save: bool=False):
    # https://developers.deepgram.com/docs/text-to-speech#make-the-request-with-the-sdk
    full_model_name = f"{model}-{voice}-{lang}"
    options = SpeakOptions(
        model=full_model_name,
        encoding=encoding, # opus
    )

    fn = f"./generated_samples/deepgram/{text[:10]}_{model}_{voice}_{lang}.{encoding}"

    start = time.time()
    response = deepgram.speak.v("1").save(fn, {"text": text}, options)
    total_time = time.time() - start

    if to_save:
        # deepgram always save the file
        pass 

    return result(
        provider="deepgram",
        model=full_model_name,
        text=text,
        ttft=None,
        total_time=total_time
        )