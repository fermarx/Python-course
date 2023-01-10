import pyttsx3
import pdfplumber as pp

engine = pyttsx3.init()
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0")

all_data = ""
with pp.open("Violeta (Isabel Allende) (z-lib.org).pdf") as book:
    for page_no, page in enumerate(book.pages, start = 1):
        data = page.extract_text()
        all_data += data

engine.save_to_file(all_data, "audio_book.mp3")
engine.runAndWait()
engine.stop()