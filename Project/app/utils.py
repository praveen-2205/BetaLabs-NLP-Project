import PyPDF2 
import re

def extract_text_from_pdf(file_path):

    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_name(text):

    name_pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
    match = re.search(name_pattern, text)
    return match.group(0) if match else "Name not found"

def extract_email(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    match = re.search(email_pattern, text)
    return match.group(0) if match else "email not found"

def extract_phone(text):

    phone_pattern = r'(\+?\d{1,3}[-.\s]?)?(?:\(\d{1,4}\)|\d{1,4})[-.\s]?\d{1,4}[-.\s]?\d{1,9}'  
    match = re.search(phone_pattern, text)
    return match.group(0) if match else "phone number not found"


#please check this . i think it will not work properly.
def extract_education(text):

    education_keywords = ["Bachelors", "Masters", "PhD", "degree", "University", "College", "school", "education", "qualification", "institute","course",
    "academy", "diploma", "certification", "certified", "certificates", "training", "studies", "study", "learning", "learned","AI","ML"]

    education_info = []
    for keyword in education_keywords:
        if keyword.lower() in text.lower():
            education_info.append(keyword)
    return education_info if education_info else "Education details not found"
