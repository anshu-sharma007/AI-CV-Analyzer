# AI CV Analyzer - Project Documentation

## Project Overview

AI CV Analyzer is a web-based application that analyzes resumes and evaluates candidate profiles based on predefined industry-relevant skills.

The system extracts text from uploaded PDF resumes, identifies skills, calculates a profile score, and recommends missing skills.

---

## Working Flow

1. User uploads resume (PDF)
2. System extracts text using PDFPlumber
3. Skills are matched against required skills database
4. Profile score is calculated
5. Missing skills are identified
6. Recommendations are generated

---

## Profile Scoring Logic

Required Skills:

- Python
- Java
- HTML
- CSS
- JavaScript
- React
- Node.js
- MongoDB

Formula:

Profile Score =

(Number of Skills Found / Total Required Skills) × 100

Example:

8 Skills Found out of 8

Score = 100%

---

## Technology Stack

Frontend:
- HTML
- CSS

Backend:
- Python
- Flask

Libraries:
- PDFPlumber

Deployment:
- Render

Version Control:
- GitHub

---

## AI / NLP Approach

Current Version:
- Keyword Matching Based Skill Extraction

Future NLP Enhancement:
- Named Entity Recognition (NER)
- Resume Parsing
- Semantic Skill Matching
- Skill Classification Models

Libraries Proposed:
- spaCy
- NLTK
- Transformers

---

## Recommendation Engine

The recommendation engine identifies missing skills and suggests learning paths.

Example:

Missing Skill:
React

Recommendation:
Complete React Fundamentals Course.

---

## API Integration Plan

Future integrations:

### LinkedIn API
- Profile Verification
- Experience Analysis

### GitHub API
- Repository Analysis
- Coding Activity Score

### Tableau API
- Dashboard Visualization

### Power BI API
- Analytics Reporting

---

## Ethical AI Considerations

The system avoids bias by:

- Not using gender information
- Not using age information
- Not using caste/religion information
- Evaluating only skills

This ensures fair and transparent candidate assessment.

---

## Future Enhancements

- AI Based Resume Ranking
- NLP Resume Understanding
- ATS Compatibility Score
- Job Matching Engine
- LinkedIn Integration
- GitHub Integration
- Dashboard Analytics
