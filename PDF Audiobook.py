import pdfplumber
from gtts import gTTS
import time

pdf_path="moby-dick.pdf"
pdf=pdfplumber.open(pdf_path)

full_text=""
for page in pdf.pages:
    full_text+=page.extract_text()
    time.sleep(0.5)

pdf.close()

if full_text.strip()==" ":
    raise ValueError("Text cannot be extracted")

tts=gTTS(text=full_text, lang='en')
output_path="audiobook.mp3"
tts.save(output_path)

print("Audiobook has been saved")



