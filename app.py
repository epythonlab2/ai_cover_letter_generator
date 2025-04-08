from flask import Flask, render_template, request, send_file
from xhtml2pdf import pisa
import io
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Loads the .env file to get the API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set the API key from the .env file

app = Flask(__name__)  # Initializes the Flask app

generated_letter = ""  # Variable to store the generated cover letter

@app.route('/', methods=['GET', 'POST'])
def index():
    global generated_letter  # Access the global variable to store the letter
    if request.method == 'POST':  # If the form is submitted
        job_title = request.form['job_title']
        job_description = request.form['job_description']
        experience = request.form['experience']
        skills = request.form['skills']

        # Construct the prompt for GPT
        prompt = f"""
        Write a professional cover letter for a job titled '{job_title}'.
        The applicant has {experience} years of experience and the following skills: {skills}.
        Job Description: {job_description}
        """

        # Call OpenAI's GPT-4 model using ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            store=True,  # gpt-4o-mini" if available in your account
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,  # Limit the output length
            temperature=0.7   # Optional: Controls creativity of the response
        )

        # Extract the generated cover letter from the response
        generated_letter = response["choices"][0]["message"]["content"].strip()

        # Send the result to the frontend to display it
        return render_template('index.html', cover_letter=generated_letter)


    return render_template('index.html', cover_letter=None)

# Download PDF Route - Converts the cover letter to a PDF
@app.route('/download_pdf')
def download_pdf():
    global generated_letter  # Use the generated letter
    html = render_template("pdf_template.html", cover_letter=generated_letter)  # Prepare HTML for PDF
    result = io.BytesIO()  # Create an in-memory file to store the PDF
    pisa.CreatePDF(io.StringIO(html), dest=result)  # Convert HTML to PDF
    result.seek(0)  # Go to the beginning of the file
    return send_file(result, download_name="cover_letter.pdf", as_attachment=True)  # Send the PDF to the user



if __name__ == "__main__":
    app.run(debug=True)
