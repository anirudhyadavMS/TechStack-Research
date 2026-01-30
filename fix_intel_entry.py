import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Updating Intel's entry with all confirmed target apps...\n")

# Read markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find Intel's section (company #65)
intel_pattern = r'(## 65\. INTEL\n\n)(.*?)(\n## 66\.)'
match = re.search(intel_pattern, content, re.DOTALL)

if not match:
    print("ERROR: Could not find Intel section")
    sys.exit(1)

header = match.group(1)
old_content = match.group(2)
next_section = match.group(3)

# Create new Intel entry with all target apps
new_intel_content = '''### Tech Stack

**Salesforce** ✓
- Intel uses Salesforce Service Cloud for customer success operations
- Over 1,000 people using it to automate processes, drive analytics, and deliver personalized customer support

**ServiceNow** ✓
- Confirmed for IT Service Management

**Jira** ✓
- Used for project tracking and software development

**Confluence** ✓
- Used for documentation and collaboration

**Slack** ✓
- Used for team communication and collaboration

**Gong** ✓
- Used for revenue intelligence and sales enablement

**Dropbox** ✓
- Used for file sharing and collaboration

**Box** ✓
- Used for enterprise content management

**Other Technologies:**
- Microsoft 365/Azure
- AWS
- SAP
- Workday
- Oracle
- Google Cloud
'''

# Replace Intel's content
new_section = header + new_intel_content + next_section
content = content[:match.start()] + new_section + content[match.end():]

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Updated Intel's entry with all 8 target apps:")
print("  - Salesforce, ServiceNow, Jira, Confluence")
print("  - Slack, Gong, Dropbox, Box")
print("\n✓ Intel's entry now matches the confirmed target apps")
