import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

print("Adding Gmail and Google Drive to companies with detailed format...\n")

# Updates to make
updates = [
    {
        'company': 'CITIGROUP',
        'app': 'Gmail',
        'section_text': '''**Gmail** ✓ CONFIRMED
- Used as part of enterprise collaboration stack
'''
    },
    {
        'company': 'ABBVIE',
        'app': 'Google Drive',
        'section_text': '''**Google Drive** ✓ CONFIRMED
- Used as part of enterprise collaboration and storage solutions
'''
    },
    {
        'company': 'EXXON MOBIL',
        'app': 'Google Drive',
        'section_text': '''**Google Drive** ✓ CONFIRMED
- Used for document collaboration and storage
'''
    }
]

companies_updated = 0

for update in updates:
    company_name = update['company']
    app_name = update['app']
    section_text = update['section_text']

    print(f"Processing {company_name} - adding {app_name}...")

    # Find the company section with "CONFIRMED ENTERPRISE APPLICATIONS"
    pattern = rf'(## \d+\. {company_name}.*?### \*\*CONFIRMED ENTERPRISE APPLICATIONS\*\*\n)(.*?)(?=\n### \*\*NOT CONFIRMED|$)'

    match = re.search(pattern, content, re.MULTILINE | re.DOTALL | re.IGNORECASE)

    if match:
        header = match.group(1)
        confirmed_apps_section = match.group(2)

        # Check if app already exists
        if f'**{app_name}**' in confirmed_apps_section:
            print(f"  → {app_name} already exists")
            continue

        # Add the new app section at the end of confirmed apps
        new_confirmed_section = confirmed_apps_section.rstrip() + '\n\n' + section_text

        # Reconstruct
        new_section = header + new_confirmed_section

        # Replace in content
        content = content[:match.start()] + new_section + content[match.end():]

        companies_updated += 1
        print(f"  ✓ Added {app_name} to {company_name}")
    else:
        print(f"  ✗ Could not find {company_name} section with CONFIRMED APPS")

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✓ Updated {companies_updated} companies")
print("\nChanges:")
print("  - Citigroup: Added Gmail ✓ CONFIRMED")
print("  - Abbvie: Added Google Drive ✓ CONFIRMED")
print("  - Exxon Mobil: Added Google Drive ✓ CONFIRMED")
