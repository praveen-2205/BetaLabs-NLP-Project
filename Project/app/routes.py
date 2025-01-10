from flask import Blueprint, render_template, request
import os
from werkzeug.utils import secure_filename
from .utils import extract_text_from_pdf, extract_name, extract_email, extract_phone, extract_education

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file uploaded!", 400 # file not uploaded returning bad request page with 400 status code.
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join('app/uploads', filename)
            file.save(filepath)

            # extracting details for document uploaded...
            text = extract_text_from_pdf(filepath)
            name = extract_name(text)
            email = extract_email(text)
            phone = extract_phone(text)
            education = extract_education(text)

            return render_template('home.html', name=name, email=email, phone=phone, education=education)

    return render_template('home.html', name=None)
