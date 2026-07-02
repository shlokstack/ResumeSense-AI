# 🎓 ResumeSense AI

An AI-powered Resume Analyzer that evaluates resumes for ATS compatibility, extracts and categorizes skills, identifies missing skills, and provides personalized recommendations to improve employability.

---

## 🚀 Features

* 📄 Upload resumes in PDF format
* 🤖 AI-powered resume analysis using Groq LLM
* 📊 ATS Score calculation (out of 100)
* 📈 Visual ATS score with a progress bar
* 💻 Automatic skill extraction and categorization
* 🔍 Missing skill identification
* ✅ Resume strengths analysis
* ⚠️ Weakness detection
* 💡 Personalized resume improvement suggestions
* 🎯 Career guidance based on the uploaded resume

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### AI & LLM

* LangChain
* Groq API
* Llama 3.3 70B Versatile

### Backend

* Python

### Libraries

* pypdf
* python-dotenv
* Regular Expressions (`re`)

---

## 📂 Project Structure

```text
ResumeSense-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── .env                # Not included in GitHub
├── assets/             # Images and icons (optional)
└── __pycache__/        # Ignored
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/shlokstack/ResumeSense-AI.git
```

Move into the project directory:

```bash
cd ResumeSense-AI
```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows (PowerShell)

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📋 How It Works

1. Upload your resume in PDF format.
2. Resume text is extracted using **pypdf**.
3. The extracted content is sent to the **Groq Llama 3.3 70B** model through **LangChain**.
4. The AI analyzes the resume and generates:

   * ATS Score
   * Strengths
   * Categorized Skills
   * Missing Skills
   * Weaknesses
   * Personalized Suggestions
5. ResumeSense AI displays the ATS score with a visual progress bar and detailed analysis.

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```
assets/
├── home.png
├── upload.png
└── analysis.png
```

Then display them using:

```markdown
![Home](assets/home.png)

![Analysis](assets/analysis.png)
```

---

## 🔮 Future Enhancements

* Job Description (JD) matching
* Resume-to-job compatibility score
* Downloadable PDF report
* Resume keyword highlighting
* AI-powered resume rewriting
* Support for DOCX resumes
* Interactive analytics dashboard
* Multiple resume comparison

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Shlok Shah**

Computer Science Undergraduate | AI & GenAI Enthusiast

GitHub: https://github.com/shlokstack

---

⭐ If you found this project useful, consider giving it a star on GitHub!
