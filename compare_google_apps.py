import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read scratchpad version (source of truth)
scratchpad_path = r"C:\Users\ANIRUD~1\AppData\Local\Temp\claude\C--Users-anirudhyadav\dc0ceeb2-9b05-4ee7-90c0-0bed22840132\scratchpad\company_technology_stack_analysis.md"

print("Reading scratchpad version (source of truth)...")
with open(scratchpad_path, 'r', encoding='utf-8') as f:
    scratchpad_content = f.read()

# Read current version
print("Reading current version...")
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    current_content = f.read()

# Function to extract companies and their Google apps
def extract_google_apps(content):
    companies = {}

    # Split by company sections
    sections = re.split(r'^## (\d+)\. (.+)$', content, flags=re.MULTILINE)

    for i in range(1, len(sections), 3):
        if i + 2 < len(sections):
            company_num = sections[i]
            company_name = sections[i + 1].strip()
            company_content = sections[i + 2]

            # Look for Gmail, Google Drive, Google Cloud in this section
            # Only in bullet points (- Gmail, - Google Drive, - Google Cloud)
            google_apps = {
                'gmail': bool(re.search(r'^\s*-\s+Gmail\s*$', company_content, re.MULTILINE)),
                'google_drive': bool(re.search(r'^\s*-\s+Google Drive\s*$', company_content, re.MULTILINE)),
                'google_cloud': bool(re.search(r'^\s*-\s+Google Cloud\s*$', company_content, re.MULTILINE))
            }

            if any(google_apps.values()):
                companies[company_name] = google_apps

    return companies

print("\nExtracting Google apps from both versions...")
scratchpad_companies = extract_google_apps(scratchpad_content)
current_companies = extract_google_apps(current_content)

print(f"\nScratchpad: {len(scratchpad_companies)} companies with Google apps")
print(f"Current: {len(current_companies)} companies with Google apps")

# Compare and find differences
differences = []
for company in scratchpad_companies:
    scratchpad_apps = scratchpad_companies[company]
    current_apps = current_companies.get(company, {'gmail': False, 'google_drive': False, 'google_cloud': False})

    if scratchpad_apps != current_apps:
        differences.append({
            'company': company,
            'scratchpad': scratchpad_apps,
            'current': current_apps
        })

print(f"\nFound {len(differences)} companies with differences:")
print("="*80)

for diff in differences:
    print(f"\n{diff['company']}:")
    print(f"  Scratchpad: Gmail={diff['scratchpad']['gmail']}, Google Drive={diff['scratchpad']['google_drive']}, Google Cloud={diff['scratchpad']['google_cloud']}")
    print(f"  Current:    Gmail={diff['current']['gmail']}, Google Drive={diff['current']['google_drive']}, Google Cloud={diff['current']['google_cloud']}")

# Now update current version with scratchpad data
print("\n" + "="*80)
print("Updating current version with scratchpad data...")

# For each company, replace the Google apps section
updated_count = 0

for company in scratchpad_companies:
    scratchpad_apps = scratchpad_companies[company]

    # Find company section in current content
    company_pattern = rf'^(## \d+\. {re.escape(company)}\n.*?\*\*Tech Stack:\*\*\n)(.*?)(?=\n\n|\n---|\n###|^## \d+\.)'

    def replace_google_apps(match):
        global updated_count
        header = match.group(1)
        tech_stack_content = match.group(2)

        # Remove existing Google apps lines
        tech_stack_content = re.sub(r'^\s*-\s+Gmail\s*$\n?', '', tech_stack_content, flags=re.MULTILINE)
        tech_stack_content = re.sub(r'^\s*-\s+Google Drive\s*$\n?', '', tech_stack_content, flags=re.MULTILINE)
        tech_stack_content = re.sub(r'^\s*-\s+Google Cloud\s*$\n?', '', tech_stack_content, flags=re.MULTILINE)

        # Get the lines
        lines = tech_stack_content.split('\n')

        # Find where to insert (after first bullet point)
        insert_index = 0
        for i, line in enumerate(lines):
            if line.strip().startswith('-'):
                insert_index = i + 1
                break

        # Insert scratchpad Google apps
        new_lines = []
        if scratchpad_apps['gmail']:
            new_lines.append('- Gmail')
        if scratchpad_apps['google_drive']:
            new_lines.append('- Google Drive')
        if scratchpad_apps['google_cloud']:
            new_lines.append('- Google Cloud')

        if new_lines:
            lines = lines[:insert_index] + new_lines + lines[insert_index:]
            updated_count += 1

        return header + '\n'.join(lines)

    current_content = re.sub(company_pattern, replace_google_apps, current_content, flags=re.MULTILINE | re.DOTALL)

print(f"Updated {updated_count} company sections")

# Save updated content
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(current_content)

print("\n✓ Current version updated with scratchpad Google apps data!")
