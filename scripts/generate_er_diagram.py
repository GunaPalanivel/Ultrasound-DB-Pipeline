import os
import subprocess
from pathlib import Path

DB_PATH = Path("data/ultrasound_db.sqlite")
OUTPUT_PATH = Path("output/er_diagram.png")

def generate_er_diagram(sqlite_path: Path, output_path: Path):
    if not sqlite_path.exists():
        raise FileNotFoundError(f"[ERROR] SQLite DB not found at {sqlite_path}")
    
    print("[INFO] Generating ER diagram using ERAlchemy...")

    try:
        subprocess.run([
            "eralchemy", 
            "-i", f"sqlite:///{sqlite_path}", 
            "-o", str(output_path)
        ], check=True)
        print(f"[SUCCESS] ER diagram saved to: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] ERAlchemy failed with exit code {e.returncode}")
        print(e)
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")

if __name__ == "__main__":
    generate_er_diagram(DB_PATH, OUTPUT_PATH)
