import fitz  # PyMuPDF
import spacy
from typing import Dict

# Cargar modelo de spaCy en español
nlp = spacy.load("es_core_news_sm")

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extrae texto completo desde un archivo PDF usando PyMuPDF.
    """
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def analyze_cv_text(text: str) -> Dict[str, str]:
    """
    Analiza el texto del CV para extraer experiencia, educación y habilidades
    usando heurísticas simples y spaCy.
    """
    doc = nlp(text.lower())

    analysis = {
        "skills": "",
        "experience": "",
        "education": "",
        "analysis_summary": "",
        "analysis_result": ""
    }

    for sent in doc.sents:
        s = sent.text.strip()
        if "experiencia" in s:
            analysis["experience"] += s + " "
        elif "educación" in s or "formación" in s:
            analysis["education"] += s + " "
        elif any(palabra in s for palabra in ["habilidades", "skills", "tecnologías", "herramientas"]):
            analysis["skills"] += s + " "

    analysis["analysis_summary"] = "Análisis automático generado por IA."
    analysis["analysis_result"] = "Análisis completado exitosamente."

    return analysis
