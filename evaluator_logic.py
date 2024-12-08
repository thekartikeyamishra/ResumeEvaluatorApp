import spacy
import pypdf

from textblob import TextBlob
import os

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        reader = pypdf.PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_key_skills(text):
    doc = nlp(text)
    skills = []
    for ent in doc.ents:
        if ent.label_ == "ORG" or ent.label_ == "PRODUCT":
            skills.append(ent.text)
    return set(skills)

def calculate_ats_score(resume_text, job_desc_text):
    resume_skills = extract_key_skills(resume_text)
    job_desc_text = extract_key_skills(job_desc_text)
    matched_skills = resume_skills.intersection(job_desc_text)
    ats_score = (len(matched_skills)/len(job_desc_text))*100
    return  ats_score, matched_skills