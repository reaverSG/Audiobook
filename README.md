Project Title: PDF to Audiobook Converter in Python

Description:
This Python script aims to convert PDF files into audiobooks using text-to-speech (TTS) technology. The script leverages pdfplumber for PDF text extraction and gTTS for generating audio files. Please note that the current implementation may encounter issues and requires improvements for robust functionality.

Features:

Converts PDF documents into spoken audio (MP3 format).
Utilizes pdfplumber for PDF text extraction.
Uses gTTS (Google Text-to-Speech) for audio synthesis.
Handles multiple pages in a PDF document.
Current Issues:

Inconsistent text extraction from PDF pages.
Potential interruptions in audio generation.
Dependency on uninterrupted internet access for gTTS usage.
Steps to Use:

Ensure Python environment is set up with necessary libraries (pdfplumber, gTTS).
Define the pdf_path variable to point to the PDF file you wish to convert.
Run the script. It extracts text from each page of the PDF with a slight delay (time.sleep(0.5)) to manage processing.
If text extraction is successful (checked with if full_text.strip() == ""), it proceeds to convert the extracted text into an audiobook.
The audiobook is saved as audiobook.mp3 in the script's directory.
Upon completion, a message confirms that the audiobook has been saved.
Contributing:
Contributions are welcome to improve text extraction reliability, handle edge cases, and enhance overall script stability. Please follow the project's guidelines and contribute responsibly.

License:
This project is licensed under the MIT License. See the LICENSE file for details.

