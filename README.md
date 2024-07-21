ATS Resume Analyser
Description:
ATS Resume Analyser is a Python-based application designed to analyze and rank resumes based on their relevance to a job description. This tool leverages Natural Language Processing (NLP) to extract and compare keywords from resumes and job descriptions, providing a comprehensive score that aids in the recruitment process.

Features:

Extracts text from PDF resumes
Identifies and extracts keywords from resumes and job descriptions
Compares resume keywords with job description keywords
Provides a detailed scoring system based on keyword match, experience, skills, education, structure, and language
Technologies Used:

Python
Streamlit for the web interface
spaCy for Natural Language Processing
PyMuPDF (fitz) for PDF text extraction
Setup and Installation:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/ats-resume-analyser.git
cd ats-resume-analyser
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Download the spaCy model:

bash
Copy code
python -m spacy download en_core_web_sm
Usage:

Run the Streamlit application:

bash
Copy code
streamlit run app.py
Open your web browser and navigate to http://localhost:8501

Upload your resume (PDF format) and paste the job description in the provided text area.

Click the "Analyze" button to get the analysis and scores.
