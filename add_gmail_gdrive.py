import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

print("Adding Gmail and Google Drive to specific companies...\n")

# Updates to make
updates = {
    'CITIGROUP': {'app': 'Gmail', 'note': 'Uses Gmail'},
    'ABBVIE': {'app': 'Google Drive', 'note': 'Uses Google Drive'},
    'EXXON MOBIL': {'app': 'Google Drive', 'note': 'Uses Google Drive'}
}

companies_updated = 0

for company_name, update_info in updates.items():
    app_name = update_info['app']

    print(f"Processing {company_name} - adding {app_name}...")

    # Find company section
    if company_name == 'EXXON MOBIL':
        pattern = r'(## \d+\. EXXON MOBIL.*?\*\*Tech Stack:\*\*\n)(.*?)(?=\n\n|\n---|\n###|^## \d+\.)'
    else:
        pattern = rf'(## \d+\. {company_name}.*?\*\*Tech Stack:\*\*\n)(.*?)(?=\n\n|\n---|\n###|^## \d+\.)'

    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

    if match:
        header = match.group(1)
        tech_stack_content = match.group(2)

        # Check if app already exists in tech stack
        if f'**{app_name}**' in tech_stack_content:
            print(f"  → {app_name} already exists in tech stack")
            continue

        # Add the app with checkmark at the beginning of tech stack
        lines = tech_stack_content.split('\n')

        # Find first bullet point
        first_bullet_idx = 0
        for i, line in enumerate(lines):
            if line.strip().startswith('-'):
                first_bullet_idx = i
                break

        # Insert the new app after the first bullet
        new_line = f"- **{app_name}** ✓"
        lines.insert(first_bullet_idx + 1, new_line)

        # Reconstruct
        new_tech_stack = '\n'.join(lines)
        new_section = header + new_tech_stack

        # Replace in content
        content = content[:match.start()] + new_section + content[match.end():]

        companies_updated += 1
        print(f"  ✓ Added {app_name} to {company_name}")
    else:
        print(f"  ✗ Could not find {company_name} section")

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✓ Updated {companies_updated} companies")
print("\nChanges:")
print("  - Citigroup: Added Gmail ✓")
print("  - Abbvie: Added Google Drive ✓")
print("  - Exxon Mobil: Added Google Drive ✓")
