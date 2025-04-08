# 📝 AI-Powered Cover Letter Generator

Welcome to the **AI-Powered Cover Letter Generator**, a beginner-friendly web app that helps you create professional cover letters based on job title, description, your experience, and your skills — all powered by OpenAI.

This project is perfect for beginners learning **Python**, **Flask**, and **Tailwind CSS** while also exploring AI automation.

---

## ✨ Features

- ✅ Clean and responsive UI using **Tailwind CSS**
- 🤖 Generates customized cover letters using **OpenAI API**
- 📥 Download your cover letter as a **PDF**
- 🧩 Easy to understand project structure with beginner-level code explanations
- 🔐 Uses `.env` to keep your API keys secure

---

## 🛠 Tech Stack

| Layer         | Technology        |
|---------------|-------------------|
| Frontend      | HTML, Tailwind CSS |
| Backend       | Flask (Python)     |
| AI API        | OpenAI API         |
| PDF Export    | pdfkit + wkhtmltopdf |

---

## 📁 Project Structure

```
cover-letter-generator/
│
├── templates/
│   └── index.html            # Frontend with Tailwind CSS
│
├── static/
│   └── styles.css (optional)  # Add custom styles here
│   └── scripts.js (optional)  # Add custom javascripts here

│
├── app.py                    # Main Flask application
├── .env                      # API Key (not pushed to Git)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

> 💡 Need help creating a virtual environment and setting up the project structure? Check the tutorial link in the description of the video!

---

## 🔐 Prerequisites

Before running this project, make sure you:

1. Have **Python 3.7+** installed.
2. Installed **wkhtmltopdf** on your machine:
   - [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)
3. Have a valid **OpenAI API key**:
   - Sign up at [https://platform.openai.com](https://platform.openai.com)
   - Copy your secret key and save it in a `.env` file:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

---

## ⚙️ Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/epythonlab2/cover_letter_generator.git
cd cover_letter_generator
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate       # On Windows use: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📦 Requirements

```text
Flask
python-dotenv
openai
pdfkit
```

Make sure you’ve also installed `wkhtmltopdf` on your system.

---

## 🖼️ UI Preview

| Input Form                          | Cover Letter Output                  |
|-------------------------------------|--------------------------------------|
| ![Form Screenshot](screenshots/form.png) | ![Output Screenshot](screenshots/output.png) |

*(Add your own screenshots to the `screenshots/` folder)*

---

## 📥 PDF Download

Once the cover letter is generated, click **“Download PDF”** to get a formatted version of your letter, ready to use.

---

## 💡 Future Improvements

- Add user authentication
- Save generated letters in history
- Export to other formats (e.g. DOCX)
- Support for multiple languages

---

## 🤝 Contributing

Pull requests and suggestions are welcome!  
If you’d like to contribute, fork the repo and submit a PR. 😊

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🎓 Tutorial

📽️ Watch the full beginner-friendly tutorial on YouTube:  
👉 [YouTube Video Link](#)

---

## 🧠 Made With

Made with 💙 for learners and job seekers who want to supercharge their applications with AI.
