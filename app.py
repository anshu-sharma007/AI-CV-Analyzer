from flask import Flask, render_template, request
import pdfplumber

app = Flask(__name__)

required_skills = [
    "Python",
    "Java",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Node.js",
    "MongoDB"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    found_skills = []

    for skill in required_skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    missing_skills = list(set(required_skills) - set(found_skills))

    score = int((len(found_skills) / len(required_skills)) * 100)

    return render_template(
        'result.html',
        score=score,
        found=found_skills,
        missing=missing_skills
    )

if __name__ == '__main__':
    app.run(debug=True)
    