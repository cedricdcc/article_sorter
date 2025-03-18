# PDF processing utilities for extracting or generating abstracts

import requests
import fitz  # PyMuPDF for PDF text extraction


def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file.
    :param file_path: The path to the PDF file
    :return: Extracted text or None if extraction fails
    """
    try:
        with fitz.open(file_path) as pdf:
            text = ""
            for page in pdf:
                text += page.get_text()
            return text if text.strip() else None
    except Exception as e:
        print(f"Error extracting text from PDF {file_path}: {e}")
        return None


def generate_abstract_from_text(text):
    """
    Generates an abstract from the given text using an LLM model.
    :param text: The input text
    :return: Generated abstract
    """
    try:
        response = requests.post(
            "http://ollama:11434/api/generate",  # Example endpoint for Ollama
            json={"prompt": f"Summarize the following text:\n{text}"},
        )
        response.raise_for_status()
        return response.json().get("summary", "Abstract generation failed.")
    except requests.RequestException as e:
        print(f"Error generating abstract: {e}")
        return "Abstract generation failed."
