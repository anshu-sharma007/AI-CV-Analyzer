# AI CV Analyzer Architecture

```text
+------------------+
|   User Uploads   |
|      Resume      |
+--------+---------+
         |
         v
+------------------+
| Flask Web Server |
+--------+---------+
         |
         v
+------------------+
| PDFPlumber       |
| Text Extraction  |
+--------+---------+
         |
         v
+------------------+
| Skill Matching   |
| Engine           |
+--------+---------+
         |
         +----------------+
         |                |
         v                v
+----------------+   +----------------+
| Profile Score  |   | Missing Skills |
+----------------+   +----------------+
         |                |
         +-------+--------+
                 |
                 v
        +------------------+
        | Recommendations  |
        +------------------+
                 |
                 v
        +------------------+
        | Result Display   |
        +------------------+
```

## Future Architecture

- NLP Engine (spaCy)
- Machine Learning Scoring
- LinkedIn API
- GitHub API
- Power BI Dashboard
- Database Integration
