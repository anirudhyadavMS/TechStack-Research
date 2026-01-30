import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

print("Updating companies with 3P connector changes...\n")

# Define company updates
updates = {
    'Qualcomm': {
        'remove_3p': True,
        'add_target_apps': ['Azure DevOps Work Items', 'ServiceNow']
    },
    'EY': {
        'remove_3p': True,
        'add_target_apps': ['Aha', 'Azure DevOps Work Items', 'Azure SQL']
    },
    'Koch': {
        'remove_3p': True,
        'add_target_apps': ['FileShare', 'GitHub', 'ServiceNow']
    },
    'LTIMindtree': {
        'remove_3p': True,
        'add_target_apps': []
    },
    'Wells Fargo': {
        'remove_3p': True,
        'add_target_apps': []
    }
}

# Process each company
for company_name, actions in updates.items():
    print(f"Processing {company_name}...")

    # Find the company section (case insensitive, flexible matching)
    if company_name == 'EY':
        pattern = r'(## \d+\.\s+EY\s*(?:\(ERNST & YOUNG\))?)(.*?)(?=\n## \d+\.|$)'
    elif company_name == 'Koch':
        pattern = r'(## \d+\.\s+KOCHIND\.COM\s*(?:\(KOCH INDUSTRIES\))?)(.*?)(?=\n## \d+\.|$)'
    elif company_name == 'LTIMindtree':
        pattern = r'(## \d+\.\s+LTIMINDTREE)(.*?)(?=\n## \d+\.|$)'
    elif company_name == 'Wells Fargo':
        pattern = r'(## \d+\.\s+WELLS FARGO)(.*?)(?=\n## \d+\.|$)'
    else:
        pattern = rf'(## \d+\.\s+{re.escape(company_name.upper())})(.*?)(?=\n## \d+\.|$)'

    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

    if not match:
        print(f"  ✗ Could not find {company_name} section")
        continue

    section_start = match.start()
    section_header = match.group(1)
    section_content = match.group(2)

    # Remove 3P Connectors section if requested
    if actions['remove_3p']:
        # Find and remove the 3P Connectors section
        connector_pattern = r'\n### 3P Connectors \(Microsoft Copilot\)\n\nConfirmed connectors in use:\n(?:- \*\*[^*]+\*\*\n)+\n'
        if re.search(connector_pattern, section_content):
            section_content = re.sub(connector_pattern, '\n', section_content)
            print(f"  ✓ Removed 3P Connectors section")
        else:
            print(f"  ⚠ No 3P Connectors section found")

    # Add target apps if requested
    if actions['add_target_apps']:
        # Find the Target Apps Found section
        target_apps_match = re.search(r'(\*\*Target Apps Found:\*\*\n)', section_content)

        if target_apps_match:
            # Find where to insert (after "Target Apps Found:" line)
            insert_pos = target_apps_match.end()

            # Build the apps text
            apps_text = ""
            for app in actions['add_target_apps']:
                apps_text += f"- **{app}** ✓\n"

            # Insert the apps
            section_content = section_content[:insert_pos] + apps_text + section_content[insert_pos:]
            print(f"  ✓ Added {len(actions['add_target_apps'])} target apps: {', '.join(actions['add_target_apps'])}")
        else:
            print(f"  ⚠ Could not find Target Apps Found section")

    # Replace the section in content
    new_section = section_header + section_content
    content = content[:section_start] + new_section + content[match.end():]

# Save updated markdown
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ Markdown file updated successfully!")
print("\nSummary:")
print("  - Qualcomm: Removed 3P, Added Azure DevOps Work Items, ServiceNow")
print("  - EY: Removed 3P, Added Aha, Azure DevOps Work Items, Azure SQL")
print("  - Koch: Removed 3P, Added FileShare, GitHub, ServiceNow")
print("  - LTIMindtree: Removed 3P")
print("  - Wells Fargo: Removed 3P")
