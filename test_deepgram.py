from utils import qa_deepgram


texts = [
    "mmm, I understand your concern, but let me suggest you something",
    "uhmmm, I understand your concern, but let me suggest you something", 
    "aha, you are right, well, let's take a look",
    "well, hmm, let me think for a moment"
]

voices = ["asteria", "orion"]

if __name__ == "__main__":
    for voice in voices:
        for text in texts:
            qa_deepgram(text, voice, to_save=True)