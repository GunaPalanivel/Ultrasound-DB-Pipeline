from consolidate_reports import consolidate_reports

input_csv = 'input/flattened_ultrasound_data.csv'
output_csv = 'output/consolidated_patient_visits.csv'

consolidate_reports(input_csv, output_csv)
