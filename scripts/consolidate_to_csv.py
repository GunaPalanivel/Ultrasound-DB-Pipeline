import sqlite3
import pandas as pd
from pathlib import Path

# --- CONFIG ---
DB_PATH = Path("data/ultrasound_db.sqlite")
CSV_OUTPUT_PATH = Path("output/consolidated.csv")


def consolidate_ultrasound_data(db_path: Path, output_csv_path: Path):
    """
    Consolidates patient, appointment, ultrasound, and report data into a flat CSV for analysis.

    Arguments:
    - db_path (Path): Path to the SQLite database.
    - output_csv_path (Path): Target CSV output location.
    """
    if not db_path.exists():
        raise FileNotFoundError(f"Database not found at {db_path}")

    with sqlite3.connect(db_path) as conn:
        query = """
        SELECT
            p.PatientID,
            p.FirstName || ' ' || p.LastName AS FullName,
            p.Gender,
            p.DateOfBirth,
            a.AppointmentDate,
            a.Reason AS VisitReason,
            u.Image AS UltrasoundImage,
            u.Report AS UltrasoundReport,
            r.ReportText,
            r.ReportDate
        FROM Patients p
        JOIN Appointments a ON p.PatientID = a.PatientID
        LEFT JOIN Ultrasound_Results u ON a.AppointmentID = u.AppointmentID
        LEFT JOIN Reports r ON a.AppointmentID = r.AppointmentID
        ORDER BY p.PatientID, a.AppointmentDate;
        """

        try:
            df = pd.read_sql_query(query, conn)
        except Exception as e:
            raise RuntimeError(f"Error running SQL query: {e}")

    # Create output directory if it doesn't exist
    output_csv_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        df.to_csv(output_csv_path, index=False)
        print(f"[SUCCESS] CSV written to: {output_csv_path.resolve()}")
    except Exception as e:
        raise IOError(f"Failed to write CSV: {e}")


if __name__ == "__main__":
    consolidate_ultrasound_data(DB_PATH, CSV_OUTPUT_PATH)