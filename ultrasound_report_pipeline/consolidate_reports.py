import pandas as pd
from pathlib import Path

def consolidate_reports(csv_path: str, output_path: str):
    df = pd.read_csv(csv_path)

    group_cols = ['PatientID', 'FullName', 'Gender', 'DateOfBirth', 'AppointmentDate',
                  'VisitReason', 'UltrasoundImage', 'UltrasoundReport']
    grouped = df.groupby(group_cols, dropna=False)

    consolidated_rows = []
    for group_keys, group_df in grouped:
        report_list = group_df[['ReportText', 'ReportDate']].dropna().to_dict(orient='records')
        row = dict(zip(group_cols, group_keys))
        row['Reports'] = report_list
        consolidated_rows.append(row)

    output_df = pd.DataFrame(consolidated_rows)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    output_df.to_csv(output_path, index=False)
    output_df.to_json(output_path.replace('.csv', '.json'), orient='records', indent=2)

    print(f"[✓] Consolidated reports saved to: {output_path}")
