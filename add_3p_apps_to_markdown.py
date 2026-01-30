import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

# Load 3P apps data
with open('company_3p_apps.json', 'r', encoding='utf-8') as f:
    company_3p_apps = json.load(f)

# Read markdown file
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Company name mappings (Excel name -> Markdown name patterns)
company_mappings = {
    'EY': ['EY', 'ERNST & YOUNG', 'Ernst & Young'],
    'Infosys': ['Infosys', 'INFOSYS'],
    'Koch': ['Koch', 'KOCH INDUSTRIES'],
    'LTI Mindtree': ['LTI', 'LTIMINDTREE', 'LTIMindtree'],
    'Manhattan Associates': ['Manhattan Associates', 'MANHATTAN ASSOCIATES'],
    'MSIT': ['MSIT', 'Microsoft IT'],  # Likely not in our Fortune 500 list
    'Qualcomm': ['Qualcomm', 'QUALCOMM'],
    'Roche': ['Roche', 'ROCHE'],
    'Wells Fargo': ['Wells Fargo', 'WELLS FARGO']
}

# Track updates
updates_made = []
companies_not_found = []

for excel_name, apps in company_3p_apps.items():
    if not apps:
        print(f"Skipping {excel_name} - no apps listed")
        continue

    # Find possible markdown names
    possible_names = company_mappings.get(excel_name, [excel_name])

    company_found = False
    for name_pattern in possible_names:
        # Look for company section (case insensitive)
        # Pattern: ## <number>. <company name>
        pattern = rf'(## \d+\.\s+[^\n]*{re.escape(name_pattern)}[^\n]*\n)'

        matches = list(re.finditer(pattern, content, re.IGNORECASE))

        if matches:
            for match in matches:
                # Get the section start
                section_start = match.end()

                # Find the next section or end of file
                next_section = re.search(r'\n## \d+\.', content[section_start:])
                if next_section:
                    section_end = section_start + next_section.start()
                else:
                    section_end = len(content)

                section_content = content[section_start:section_end]

                # Check if 3P Connectors section already exists
                if '### 3P Connectors' in section_content or '### Third-Party Connectors' in section_content:
                    print(f"✓ {excel_name} already has 3P Connectors section")
                    continue

                # Find where to insert (after first paragraph, before "Key Findings" if it exists)
                insert_point = section_start

                # Try to find a good insertion point
                key_findings_match = re.search(r'\n### Key Findings', section_content)
                if key_findings_match:
                    insert_point = section_start + key_findings_match.start()
                else:
                    # Insert after first paragraph (look for double newline)
                    first_para_end = re.search(r'\n\n', section_content)
                    if first_para_end:
                        insert_point = section_start + first_para_end.end()

                # Create 3P Connectors section
                apps_text = '\n### 3P Connectors (Microsoft Copilot)\n\n'
                apps_text += 'Confirmed connectors in use:\n'
                for app in apps:
                    apps_text += f'- **{app}**\n'
                apps_text += '\n'

                # Insert the section
                content = content[:insert_point] + apps_text + content[insert_point:]

                updates_made.append(f"{excel_name} ({len(apps)} apps)")
                company_found = True
                print(f"✓ Added 3P apps for {excel_name} ({len(apps)} apps)")
                break

            if company_found:
                break

    if not company_found:
        companies_not_found.append(excel_name)
        print(f"✗ Could not find {excel_name} in markdown")

# Save updated markdown
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n" + "=" * 80)
print(f"\nSummary:")
print(f"  Updates made: {len(updates_made)}")
print(f"  Companies not found: {len(companies_not_found)}")

if updates_made:
    print(f"\n  Updated companies:")
    for update in updates_made:
        print(f"    - {update}")

if companies_not_found:
    print(f"\n  Not found in markdown:")
    for company in companies_not_found:
        print(f"    - {company}")

print("\nMarkdown file updated successfully!")
