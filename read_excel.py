import sys
import os

# Try multiple methods to read the Excel file
file_path = r"C:\Users\anirudhyadav\Downloads\VIP Customer Key Metrics Overview.xlsx"

# Method 1: Try with win32com (COM automation)
try:
    import win32com.client as win32
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = False
    wb = excel.Workbooks.Open(file_path)
    ws = wb.Worksheets(1)

    # Get used range
    used_range = ws.UsedRange
    rows = used_range.Rows.Count
    cols = used_range.Columns.Count

    print(f"Successfully opened file with {rows} rows and {cols} columns")
    print("\nFirst row (headers):")
    headers = []
    for col in range(1, min(cols + 1, 20)):  # First 20 columns
        val = ws.Cells(1, col).Value
        if val:
            headers.append(str(val))
            print(f"  Column {col}: {val}")

    print("\n\nFirst 10 data rows:")
    for row in range(2, min(12, rows + 1)):
        row_data = []
        for col in range(1, min(cols + 1, 10)):
            val = ws.Cells(row, col).Value
            row_data.append(str(val) if val else "")
        print(f"Row {row}: {' | '.join(row_data)}")

    wb.Close(SaveChanges=False)
    excel.Quit()

except Exception as e:
    print(f"Error with win32com: {e}")
    print("\nTrying alternative method...")

    # Method 2: Try saving to temp file and reading
    try:
        import pandas as pd
        # Try reading with different engines
        df = pd.read_excel(file_path, engine='xlrd')
        print("\nSuccessfully read with xlrd")
        print("Columns:", list(df.columns))
        print("\nFirst 10 rows:")
        print(df.head(10).to_string())
    except Exception as e2:
        print(f"Error with pandas: {e2}")
