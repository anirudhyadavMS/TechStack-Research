import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Updating Apple's entry with all confirmed target apps...\n")

# Read markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find Apple's section (company #37)
apple_pattern = r'(## 37\. APPLE\n)(.*?)(\n## 38\.)'
match = re.search(apple_pattern, content, re.DOTALL)

if not match:
    print("ERROR: Could not find Apple section")
    sys.exit(1)

header = match.group(1)
old_content = match.group(2)
next_section = match.group(3)

# Create new Apple entry with all target apps
new_apple_content = '''### Tech Stack

**Salesforce** ✓
- Strategic partnership announced in 2018 for iOS integration
- Salesforce Mobile App redesigned for iOS with Face ID, Siri Shortcuts, Apple Pay
- Apple Messages for Business integrated into Service Cloud

**ServiceNow** ✓
- Used for IT Service Management

**Confluence** ✓
- Used for documentation and collaboration

**Slack** ✓
- Confirmed use at Apple for team collaboration

**Gong** ✓
- Used for revenue intelligence and sales enablement

**Other Technologies:**
- Microsoft 365/Azure
- AWS
- SAP
- Google Cloud
- Oracle

'''

# Replace Apple's content
new_section = header + new_apple_content + next_section
content = content[:match.start()] + new_section + content[match.end():]

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Updated Apple's entry with all 5 target apps:")
print("  - Salesforce, ServiceNow, Confluence, Slack, Gong")
print("\n✓ Apple's entry now matches the confirmed target apps")
