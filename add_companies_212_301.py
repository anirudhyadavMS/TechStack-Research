#!/usr/bin/env python3
"""
Add Companies 212-301 to Markdown File
Final consolidation of batches 13-21
"""
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("="*80)
print("ADDING COMPANIES 212-301 TO MARKDOWN")
print("="*80)

# Read research output for companies 212-300
with open('batches_13_21_research_output.txt', 'r', encoding='utf-8') as f:
    research_212_300 = f.read()

# Add company 301
company_301 = """## 301. Targa Resources

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: ✓
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- SAP
- Oracle
- Microsoft 365

**Sources:**
- https://www.targaresources.com/careers
- https://www.linkedin.com/company/targa-resources/

"""

all_new_content = research_212_300 + company_301

# Read existing markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Remove the placeholder note if it exists
markdown_content = re.sub(
    r'\n---\n\n\*\*NOTE:\*\* Batches 13-21.*?Data will be added systematically to maintain quality standards\.\n\n',
    '\n',
    markdown_content,
    flags=re.DOTALL
)

# Find insertion point after company 211
pattern = r'(## 211\..*?---\n\n## Summary Statistics|## 211\..*?)(?=\n## \d+\.|$)'
match = re.search(pattern, markdown_content, re.DOTALL)

if not match:
    print("❌ Could not find company 211 in markdown")
    sys.exit(1)

insertion_point = match.end()
print(f"✓ Found insertion point after company 211\n")

# Insert new companies
final_content = markdown_content[:insertion_point] + "\n" + all_new_content + markdown_content[insertion_point:]

# Write updated markdown
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("✓ Added 90 companies (212-301) to markdown")
print("✓ Total companies now: 301")
print("\nNext steps:")
print("  1. Count actual app usage across all 301 companies")
print("  2. Update summary statistics in markdown")
print("  3. Regenerate HTML dashboard")
print("  4. Validate with validation scripts")

print("="*80)
