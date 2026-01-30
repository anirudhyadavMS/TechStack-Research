import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

print("Adding Google Drive to Abbvie and Exxon Mobil...\n")

# Update Abbvie - add to Confirmed Enterprise Software section
print("Processing ABBVIE...")
abbvie_pattern = r'(## 36\. ABBVIE.*?### Confirmed Enterprise Software\n)(.*?)(### NOT Confirmed in Research)'
abbvie_match = re.search(abbvie_pattern, content, re.DOTALL)

if abbvie_match:
    header = abbvie_match.group(1)
    confirmed_section = abbvie_match.group(2)
    not_confirmed_header = abbvie_match.group(3)

    # Check if Google Drive already in confirmed section
    if '**Google Drive**' not in confirmed_section:
        # Add Google Drive at the end of confirmed section
        new_confirmed = confirmed_section.rstrip() + '\n\n**Google Drive** - CONFIRMED. Used as part of enterprise collaboration and storage solutions.\n\n'

        # Also remove from NOT Confirmed section
        after_not_confirmed = content[abbvie_match.end():]
        # Remove the Google Drive NOT USED line
        after_not_confirmed = re.sub(r'\*\*Google Drive\*\* - NOT USED.*?\n\n', '', after_not_confirmed, count=1, flags=re.DOTALL)

        # Reconstruct
        new_section = header + new_confirmed + not_confirmed_header + after_not_confirmed
        content = content[:abbvie_match.start()] + new_section
        print("  ✓ Added Google Drive to ABBVIE confirmed section")
    else:
        print("  → Google Drive already in confirmed section")
else:
    print("  ✗ Could not find ABBVIE section")

# Update Exxon Mobil - add to Confirmed Enterprise Applications section
print("\nProcessing EXXON MOBIL...")
exxon_pattern = r'(## 48\. EXXON MOBIL.*?### Additional Confirmed Enterprise Tools\n)(.*?)(### NOT Confirmed)'
exxon_match = re.search(exxon_pattern, content, re.DOTALL)

if exxon_match:
    header = exxon_match.group(1)
    confirmed_section = exxon_match.group(2)
    not_confirmed_header = exxon_match.group(3)

    # Check if Google Drive already in confirmed section
    if '**Google Drive**' not in confirmed_section:
        # Add Google Drive at the end of Additional Confirmed Tools section
        new_confirmed = confirmed_section.rstrip() + '\n-- **Google Drive**: Used for document collaboration and storage\n\n'

        # Also remove from NOT Confirmed section
        after_not_confirmed = content[exxon_match.end():]
        # Remove the Google Drive line from NOT Confirmed
        after_not_confirmed = re.sub(r'-- \*\*Google Drive\*\*:.*?\n', '', after_not_confirmed, count=1)

        # Reconstruct
        new_section = header + new_confirmed + not_confirmed_header + after_not_confirmed
        content = content[:exxon_match.start()] + new_section
        print("  ✓ Added Google Drive to EXXON MOBIL confirmed section")
    else:
        print("  → Google Drive already in confirmed section")
else:
    print("  ✗ Could not find EXXON MOBIL section")

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ Update complete")
print("\nChanges:")
print("  - Abbvie: Added Google Drive to Confirmed Enterprise Software")
print("  - Exxon Mobil: Added Google Drive to Additional Confirmed Enterprise Tools")
