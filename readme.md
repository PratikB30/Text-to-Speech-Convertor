# Text-to-Speech Converter

This web application allows users to upload various document formats (images, Word documents, PDFs) and get them converted into downloadable audio files.

## Functionality Overview
The application leverages Optical Character Recognition (OCR) technology to extract text from uploaded files. This extracted text is then processed by a text-to-speech engine, which converts it into an audio format (typically MP3). Users can then download the generated audio file for playback.

## Key Technologies:

- Flask: Provides the web application framework.
- Tesseract: Enables Optical Character Recognition (OCR) for text extraction.
- Text-to-Speech Engine (gTTS or pyttsx3): Converts extracted text to speech.

---
  
### How It Works
- Users visit the web interface and upload a document file.
- The application utilizes OCR to extract text from the uploaded file, handling various formats like images (PNG, JPG, JPEG), Word documents (DOCX, DOC), and PDFs.
- The extracted text is fed into a text-to-speech engine, which synthesizes the text into an audio file.
- Users are presented with the option to download the generated audio file.

---

### Benefits:

- Accessibility: Converts documents into a format suitable for audio listeners.
- Convenience: Simplifies the process of consuming text content through audio.
- Versatility: Supports different document formats for user flexibility.

---

### Project Snapshots

### 1. Home Page: Users upload their document file.
 
  <p align="center">
  <img src="Project Snapshots/home.png" alt="Home Page" width="75%" height="75%"/>
</p>  

---

### 2. Text Conversion: The application displays the extracted text for confirmation.
   
<p align="center">
  <img src="Project Snapshots/covert.png" alt="Conversion" width="75%" height="75%"/>
</p>  

---

### 3. DOCX Conversion (example):  The application handles different document formats like Word documents.
   
  <p align="center">
  <img src="Project Snapshots/docxconv.png" alt="Document Conversion" width="75%" height="75%"/>
</p>  

---

### 4. Download: Audio file is automatically downloaded.
   
  <p align="center">
  <img src="Project Snapshots/download.png" alt="Download" width="75%" height="75%"/>
</p>  

---

### Getting Started
#### Prerequisites:
- Python
- Flask framework
- Tesseract OCR library (instructions: https://sourceforge.net/projects/tesseract-ocr.mirror/)
- Additional libraries for text-to-speech functionality (e.g., gTTS or pyttsx3)
  
### Steps to run:

Clone the repository:

- git clone [Text-to-Speech-Convertor](https://github.com/PratikB30/Text-to-Speech-Convertor.git)
  
  OR
  
-  Download [Text-to-Speech-Convertor.zip](https://github.com/PratikB30/Text-to-Speech-Convertor/archive/refs/heads/main.zip)

  
- Install dependencies:
```bash

pip install -r requirements.txt
```

- Running the Application:
```bash
flask run app.py
```
- Access the Application:

  Open http://127.0.0.1:5000/ in your web browser.

---

### Contributing
- We welcome contributions to this project. Feel free to fork the repository and submit pull requests with your enhancements or bug fixes.   

