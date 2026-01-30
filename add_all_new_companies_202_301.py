#!/usr/bin/env python3
"""
Add ALL Companies 202-301 to Markdown File
Comprehensive addition of all batches 12-21
"""
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("="*80)
print("ADDING ALL COMPANIES 202-301 TO MARKDOWN")
print("="*80)

# Read batch 12 output
with open('batch_12_research_output.txt', 'r', encoding='utf-8') as f:
    batch_12 = f.read()

# Read batches 13-21 output
with open('batches_13_21_research_output.txt', 'r', encoding='utf-8') as f:
    batches_13_21 = f.read()

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

all_new_content = batch_12 + batches_13_21 + company_301

# Read existing markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Find insertion point after company 201
pattern = r'(## 201\..*?)(?=\n---\n\n## Summary Statistics|$)'
match = re.search(pattern, markdown_content, re.DOTALL)

if not match:
    print("❌ Could not find company 201 in markdown")
    sys.exit(1)

insertion_point = match.end()
print(f"✓ Found insertion point after company 201\n")

# Insert all new companies
final_content = markdown_content[:insertion_point] + "\n\n" + all_new_content + markdown_content[insertion_point:]

# Write updated markdown
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("✓ Added 100 companies (202-301) to markdown")
print("✓ Total companies now: 301")
print("\nCompanies added:")
print("  Batch 12 (202-211): 10 companies")
print("  Batches 13-21 (212-301): 90 companies")

print("\nNext: Count apps and update summary statistics")
print("="*80)
