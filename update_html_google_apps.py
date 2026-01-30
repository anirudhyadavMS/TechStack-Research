import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read HTML file
with open('company_technology_stack_analysis.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

print("Updating HTML with Google Cloud changes...\n")

# Extract the companies JSON array from the JavaScript
companies_match = re.search(r'const companies = (\[.*?\]);', html_content, re.DOTALL)
if not companies_match:
    print("ERROR: Could not find companies array in HTML")
    sys.exit(1)

companies_json = companies_match.group(1)
companies = json.loads(companies_json)

print(f"Found {len(companies)} companies in HTML\n")

# Track changes
changes_log = []

# Process each company
for company in companies:
    company_name = company['name']
    changes = []

    # Check if company has Gmail or Google Drive
    has_gmail = 'Gmail' in company.get('other_apps', [])
    has_gdrive = 'Google Drive' in company.get('other_apps', [])
    has_gmail_target = 'Gmail' in company.get('apps', [])
    has_gdrive_target = 'Google Drive' in company.get('apps', [])

    if not (has_gmail or has_gdrive or has_gmail_target or has_gdrive_target):
        continue  # No changes needed

    # CITIGROUP - Special case
    if company_name == 'CITIGROUP':
        # Keep Gmail in target apps
        # Remove Google Drive from other_apps, add Google Cloud
        if 'Google Drive' in company['other_apps']:
            company['other_apps'].remove('Google Drive')
            changes.append("Removed Google Drive from other_apps")
        if 'Gmail' in company['other_apps']:
            company['other_apps'].remove('Gmail')
            changes.append("Removed Gmail from other_apps (already in target)")
        if 'Google Cloud' not in company['other_apps']:
            company['other_apps'].append('Google Cloud')
            changes.append("Added Google Cloud to other_apps")

        # Update tech_stack
        company['tech_stack'] = [item for item in company['tech_stack'] if item['name'] not in ['Google Drive']]
        if not any(item['name'] == 'Google Cloud' for item in company['tech_stack']):
            company['tech_stack'].append({'name': 'Google Cloud', 'is_target': False})

    # ABBVIE - Special case
    elif company_name == 'ABBVIE':
        # Keep Google Drive in target apps
        # Remove Gmail and Google Drive from other_apps, add Google Cloud
        if 'Gmail' in company['other_apps']:
            company['other_apps'].remove('Gmail')
            changes.append("Removed Gmail from other_apps")
        if 'Google Drive' in company['other_apps']:
            company['other_apps'].remove('Google Drive')
            changes.append("Removed Google Drive from other_apps (already in target)")
        if 'Google Cloud' not in company['other_apps']:
            company['other_apps'].append('Google Cloud')
            changes.append("Added Google Cloud to other_apps")

        # Update tech_stack - keep Google Drive as target, add Google Cloud as other
        company['tech_stack'] = [item for item in company['tech_stack'] if item['name'] not in ['Gmail']]
        # Remove duplicate Google Drive from other_apps in tech_stack
        company['tech_stack'] = [item for item in company['tech_stack']
                                if not (item['name'] == 'Google Drive' and not item['is_target'])]
        if not any(item['name'] == 'Google Cloud' for item in company['tech_stack']):
            company['tech_stack'].append({'name': 'Google Cloud', 'is_target': False})

    # EXXON MOBIL - Special case
    elif company_name == 'EXXON MOBIL':
        # Keep Google Drive in target apps
        # Remove Gmail and Google Drive from other_apps, add Google Cloud
        if 'Gmail' in company['other_apps']:
            company['other_apps'].remove('Gmail')
            changes.append("Removed Gmail from other_apps")
        if 'Google Drive' in company['other_apps']:
            company['other_apps'].remove('Google Drive')
            changes.append("Removed Google Drive from other_apps (already in target)")
        if 'Google Cloud' not in company['other_apps']:
            company['other_apps'].append('Google Cloud')
            changes.append("Added Google Cloud to other_apps")

        # Update tech_stack - keep Google Drive as target, add Google Cloud as other
        company['tech_stack'] = [item for item in company['tech_stack'] if item['name'] not in ['Gmail']]
        # Remove duplicate Google Drive from other_apps in tech_stack
        company['tech_stack'] = [item for item in company['tech_stack']
                                if not (item['name'] == 'Google Drive' and not item['is_target'])]
        if not any(item['name'] == 'Google Cloud' for item in company['tech_stack']):
            company['tech_stack'].append({'name': 'Google Cloud', 'is_target': False})

    # ALL OTHER COMPANIES
    else:
        # Remove Gmail and Google Drive from other_apps, add Google Cloud
        if 'Gmail' in company['other_apps']:
            company['other_apps'].remove('Gmail')
            changes.append("Removed Gmail from other_apps")
        if 'Google Drive' in company['other_apps']:
            company['other_apps'].remove('Google Drive')
            changes.append("Removed Google Drive from other_apps")
        if (has_gmail or has_gdrive) and 'Google Cloud' not in company['other_apps']:
            company['other_apps'].append('Google Cloud')
            changes.append("Added Google Cloud to other_apps")

        # Update tech_stack
        company['tech_stack'] = [item for item in company['tech_stack']
                                if item['name'] not in ['Gmail', 'Google Drive']]
        if (has_gmail or has_gdrive) and not any(item['name'] == 'Google Cloud' for item in company['tech_stack']):
            company['tech_stack'].append({'name': 'Google Cloud', 'is_target': False})

    if changes:
        changes_log.append(f"{company_name}: {', '.join(changes)}")

# Convert back to JSON
new_companies_json = json.dumps(companies, ensure_ascii=False)

# Replace in HTML
new_html = html_content.replace(companies_json, new_companies_json)

# Save updated HTML
with open('company_technology_stack_analysis.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"✓ Updated {len(changes_log)} companies\n")
print("Changes made:")
for log in changes_log:
    print(f"  - {log}")

print(f"\n✓ HTML file updated successfully!")
