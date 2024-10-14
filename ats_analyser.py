import spacy
import streamlit as st
import fitz  # PyMuPDF

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to extract keywords from text
def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return keywords

# Function to compare resume and job description
def compare_resume(resume_text, job_desc_text):
    resume_keywords = extract_keywords(resume_text)
    job_desc_keywords = extract_keywords(job_desc_text)
    common_keywords = set(resume_keywords) & set(job_desc_keywords)
    keyword_score = len(common_keywords) / len(set(job_desc_keywords)) * 100

    # Placeholder for other aspects
    experience_score = 80  
    skills_score = 70      
    education_score = 90  
    structure_score = 85   
    language_score = 75    

    # Calculate overall score
    overall_score = (keyword_score + experience_score + skills_score + 
                     education_score + structure_score + language_score) / 6

    return overall_score, common_keywords, keyword_score, experience_score, skills_score, education_score, structure_score, language_score

# Streamlit UI
st.title("Smart ATS Resume Analyzer")
resume_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")
job_desc_text = st.text_area("Paste the Job Description here")

if st.button("Analyze"):
    if resume_file and job_desc_text:
        resume_text = extract_text_from_pdf(resume_file)
        overall_score, common_keywords, keyword_score, experience_score, skills_score, education_score, structure_score, language_score = compare_resume(resume_text, job_desc_text)
        st.write(f"Overall Match Score: {overall_score:.2f}%")
        st.write(f"Keyword Match Score: {keyword_score:.2f}%")
        st.write(f"Experience Relevance Score: {experience_score:.2f}%")
        st.write(f"Skills Match Score: {skills_score:.2f}%")
        st.write(f"Education Match Score: {education_score:.2f}%")
        st.write(f"Resume Structure Score: {structure_score:.2f}%")
        st.write(f"Language and Grammar Score: {language_score:.2f}%")
        st.write("Common Keywords:", ", ".join(common_keywords))
    else:
        st.write("Please upload a Resume and provide the Job Description.")
