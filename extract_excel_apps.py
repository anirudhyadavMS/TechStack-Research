import sys
import json

file_path = r"C:\Users\anirudhyadav\Downloads\VIP Customer Key Metrics Overview.xlsx"

try:
    import win32com.client as win32
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = False
    wb = excel.Workbooks.Open(file_path)
    ws = wb.Worksheets(1)

    # Get used range
    used_range = ws.UsedRange
    rows = used_range.Rows.Count

    # Extract company -> apps mapping
    company_apps = {}

    # Skip header row, start from row 2
    for row in range(2, rows + 1):
        company_name = ws.Cells(row, 1).Value  # Column A: Tenant Name
        apps_text = ws.Cells(row, 2).Value     # Column B: Connectors (All 3P)

        if company_name:
            company_name = str(company_name).strip()
            if apps_text:
                # Split by comma and clean up
                apps_list = [app.strip() for app in str(apps_text).split(',') if app.strip()]
                company_apps[company_name] = apps_list
            else:
                company_apps[company_name] = []

    wb.Close(SaveChanges=False)
    excel.Quit()

    # Print results
    print(f"Extracted data for {len(company_apps)} companies\n")
    print("=" * 80)

    for company, apps in company_apps.items():
        print(f"\n{company}:")
        if apps:
            print(f"  Apps ({len(apps)}): {', '.join(apps)}")
        else:
            print("  No apps listed")

    print("\n" + "=" * 80)

    # Save to JSON for later use
    output_file = 'company_3p_apps.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(company_apps, f, indent=2, ensure_ascii=False)

    print(f"\nData saved to {output_file}")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
