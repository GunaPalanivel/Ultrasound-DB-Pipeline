# 🩻 Ultrasound Data Pipeline – SQL to Insights

> A backend-driven pipeline that transforms a raw `.sql` dump into a clean CSV, ER diagram, and EDA dashboard — simulating a real-world clinic data product.

---

## 📌 Introduction

This repo showcases a **realistic backend challenge**: reverse-engineering a medical SQL database into actionable insights using Python and SQLite.

As a B.Tech student focused on backend systems and data pipelines, I approached this task like a production engineer — with schema inspection, modular ETL scripts, and clean code practices. The goal? Build something real, robust, and reusable.

---

## ⚙️ Project Setup

### 🧾 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

> **Dependencies**:
>
> - `sqlite3` (standard library)
> - `pandas`
> - `eralchemy` (for ER diagram generation)
> - `matplotlib`, `seaborn` (for EDA – optional)

---

## 🧱 Usage Overview

### 1️⃣ Load `.sql` dump into SQLite

```bash
python scripts/load_sql_to_db.py
```

> Converts `data/ultrasound_db.sql` → `ultrasound_db.sqlite`

### 2️⃣ Inspect Schema (Tables + Foreign Keys)

```bash
python scripts/inspect_schema.py
```

> Outputs a relationship map to `output/schema_relationships.txt`
> Uses `PRAGMA` introspection to extract foreign keys and structure.

### 3️⃣ Generate ER Diagram (Visual)

```bash
python scripts/generate_er_diagram.py
```

> Uses [`eralchemy`](https://github.com/Alexis-benoist/eralchemy) to render an ER diagram to `output/er_diagram.png`

### 4️⃣ Consolidate Data into CSV

```bash
python scripts/consolidate_data.py
```

> Joins normalized tables:
> `Patients`, `Appointments`, `Ultrasound_Results`, `Reports`
> → Produces `output/consolidated.csv` (flat, clean, analysis-ready)

### 5️⃣ Analyze the Data (Optional Notebook)

Explore trends, delays, and demographics:

```bash
jupyter notebook notebooks/exploratory_analysis.ipynb
```

---

## 📊 System Flow (Real-World Inspired)

```text
[SQL Dump]
   ↓
[SQLite DB]
   ↓
[Schema Inspector + ER Diagram]
   ↓
[Join & Flatten via SQL]
   ↓
[CSV Output]
   ↓
[EDA in Notebook]
```

---

## 🧠 Key Concepts Applied

| Topic                    | Real-World Usage                                       |
| ------------------------ | ------------------------------------------------------ |
| **Schema Introspection** | Used `PRAGMA` to analyze unknown DB structure          |
| **ETL Scripting**        | Modular Python scripts with error handling             |
| **SQL Joins**            | Multi-table join to consolidate normalized schema      |
| **Data Cleaning**        | Handled NULLs, joined text fields, date parsing        |
| **Visualization**        | Generated ER diagram + EDA plots                       |
| **Pipeline Design**      | Modeled like a backend ETL pipeline in healthcare apps |

---

## 💡 Tips & Best Practices

- Use **ERAlchemy** to visualize unknown DBs fast.
- Use `PRAGMA table_info` and `foreign_key_list` to reverse-engineer old schemas.
- Design your queries with **LEFT JOINs** to retain incomplete rows (important for real-world clinics).
- Always export a **flat CSV** for downstream ML or dashboard usage.
- Use `Pathlib` instead of hardcoded strings for better cross-platform paths.
- Always wrap DB/file I/O in error-handled `try/except` blocks.

---

## 📂 Project Structure

```
.
├── data/
│   ├── ultrasound_db.sql          # Raw SQL dump
│   └── ultrasound_db.sqlite       # SQLite DB (after running loader)
│
├── scripts/
│   ├── load_sql_to_db.py          # Load SQL into SQLite
│   ├── inspect_schema.py          # Output schema + relationships
│   ├── generate_er_diagram.py     # Render ER diagram with ERAlchemy
│   └── consolidate_data.py        # Run SQL join and output CSV
│
├── output/
│   ├── consolidated.csv           # Flattened final CSV
│   ├── er_diagram.png             # ER diagram
│   └── schema_relationships.txt   # Textual FK + column structure
│
├── notebooks/
│   └── exploratory_analysis.ipynb # Pandas/Seaborn-based insights
│
└── README.md                      # You’re reading it
```

---

## 🧪 Sample Output Preview

| PatientID | FullName  | Gender | DOB        | VisitReason     | ReportDate | DaysToReport |
| --------- | --------- | ------ | ---------- | --------------- | ---------- | ------------ |
| 101       | Raj Kumar | Male   | 1984-07-11 | Routine Checkup | 2024-01-21 | 5            |
| 102       | Priya M.  | Female | 1990-05-18 | Neurology       | 2024-02-10 | 12           |
| ...       | ...       | ...    | ...        | ...             | ...        | ...          |

---

## 🔍 Example Use Case

Imagine this powering a **hospital dashboard** where:

- Admins track report delays by age/gender.
- Data scientists build models to **predict diagnoses**.
- Engineers expose CSV data to a **React + Flask** frontend for insights.

---

## 🚀 Future Enhancements

- 🧠 NLP on `UltrasoundReport` for common conditions.
- 🕒 Time-series trends on appointment volume.
- 🔐 Secure API endpoints to serve CSV slices.
- 📊 Deploy EDA dashboard via Streamlit/Flask.

---

## 🙌 Why This Matters

This project blends real-world backend thinking:
🔄 ETL | 📊 Analytics | 🛠️ Systems Design | 🧠 SQL | 🧹 Data Cleaning

It's the kind of pipeline you'd build at a hospital startup or diagnostics lab to **make sense of raw, messy databases** — and turn them into real product features.

```

```
