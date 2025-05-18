## Appendix A - Report Format

### 1. Motivation

I picked this role challenge because I’m deeply interested in scalable backend development and working with structured data. When I saw a project that blends database reverse-engineering, data cleaning, and exploratory analysis, it felt like the perfect playground to apply my Python + SQL skills, sharpen my data intuition, and build something that mimics a real-world product pipeline. As a backend-focused B.Tech student at SRM, this aligned well with my interests in system design, data pipelines, and practical software development.

---

### 2. Introduction about the Task

**Situation:** The challenge involved analyzing a raw SQL database dump and converting it into actionable insights. This is a common scenario in industry, where we’re handed legacy databases or third-party systems and need to make sense of the data for reporting or ML.

**Task:**

- Understand schema relationships from a `.sqlite` database.
- Visualize it using an ER diagram.
- Consolidate normalized table data into a flat, analysis-friendly CSV.
- Perform exploratory data analysis (EDA) on that CSV.

**Approach:**
I followed a modular approach:

1. Used `sqlite3` and custom schema inspection code to derive table relationships.
2. Generated the ER diagram using ERAlchemy.
3. Wrote a Python script to join key tables and output a clean CSV.
4. Ran EDA in a Jupyter Notebook using pandas, matplotlib, seaborn.

**Significance:**
This mirrors real-world workflows in backend/data engineering—starting from raw DBs and ending with insightful dashboards or ML inputs.

---

### 3. Data Extraction, Preprocessing, and Analysis

#### 🔍 Extraction

- Loaded the SQL dump into a SQLite database using a custom script.
- Parsed schema using introspection: `PRAGMA table_info` and `PRAGMA foreign_key_list`.
- Exported relationship structure into a text file.

#### 🔁 Preprocessing

- Joined tables: `Patients`, `Appointments`, `Ultrasound_Results`, `Reports`.
- Merged relevant fields like `Age`, `Gender`, `ReportText`, `VisitReason`, etc.
- Converted datetime columns properly and created derived fields like `PatientAge` and `DaysToReport`.

#### ⚙️ Flowchart

**System-level Flow:**

```
[SQL Dump] → [SQLite DB] → [Schema Analysis] → [ER Diagram] → [Data Join Script] → [Clean CSV] → [Jupyter EDA]
```

#### 💻 Pseudocode of Pipeline

```python
# load_sql_to_db.py
conn = sqlite3.connect("ultrasound_db.sqlite")
execute_schema_from_dump()

# schema_inspector.py
for table in all_tables:
    describe_columns(table)
    find_foreign_keys(table)

# generate_er_diagram.py
subprocess("eralchemy -i sqlite:///ultrasound_db.sqlite -o output/er_diagram.png")

# consolidate_data.py
query = JOIN(Patients, Appointments, Ultrasound_Results, Reports)
pd.DataFrame.from_sql(query).to_csv("output/consolidated.csv")

# exploratory_analysis.ipynb
analyze("output/consolidated.csv")
```

---

### 4. Results

#### 📊 EDA Summary

- Most patients fall in the **30–40 age** group.
- **Gender** distribution is nearly even.
- **Days to Report** typically ranges between 0 to 30 days. A few outliers had delays > 60 days.
- **Top visit reasons**: Routine checkups, dermatology, and neuro-related consultations.
- **Null Analysis**: Most fields were complete, except for a few missing `ReportText` values.
- **Correlation Heatmap**: No strong correlation between numerical fields, but interesting patterns in `DaysToReport` for older patients.

---

### 5. Key Findings

- 🧠 **Older patients** tend to have slightly delayed reports, possibly due to follow-ups.
- 🧾 **VisitReason** is a strong feature for clustering future patient categories.
- 📅 A majority of reports are delivered within a **7–14 day window**, suggesting a performance benchmark for the clinic.
- 🚩 The dataset is **well-structured** but slightly verbose in report text fields, which could be mined using NLP later.

---

### 6. Future Work

If I had more time, I would:

- 🧠 Apply **NLP techniques** (TF-IDF, topic modeling) on `UltrasoundReport` to detect common diagnoses.
- 📉 Run **time-series** or seasonal analysis on appointments to identify peak visit periods.
- 🤖 Build a **classification model** to predict visit reasons based on patient metadata and prior report text.
- 📊 Deploy the CSV + notebook on a Flask app to serve dynamic insights to non-technical users.
- 🛡️ Add **security checks** (e.g., input validation, access controls) if moving to a real data product.

---

### Final Thoughts

This challenge was a crash course in backend data wrangling. It blended schema design thinking, SQL/Python fluency, and data storytelling. Honestly, it felt like working on a startup product's internal data dashboard—and I loved it. Real-world-ready stuff.
