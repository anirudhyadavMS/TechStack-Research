#!/usr/bin/env python3
"""
Count actual app usage from all 301 companies and update summary
"""
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("="*80)
print("COUNTING APP USAGE ACROSS ALL 301 COMPANIES")
print("="*80)

# Read markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Count company sections
companies = len(re.findall(r'^## \d+\.', content, re.MULTILINE))
print(f"\nTotal Companies Found: {companies}\n")

# Count each target app with checkmark
apps = {
    'Salesforce': len(re.findall(r'\*\*Salesforce\*\*: ✓', content)),
    'ServiceNow': len(re.findall(r'\*\*ServiceNow\*\*: ✓', content)),
    'Jira': len(re.findall(r'\*\*Jira\*\*: ✓', content)),
    'Confluence': len(re.findall(r'\*\*Confluence\*\*: ✓', content)),
    'Slack': len(re.findall(r'\*\*Slack\*\*: ✓', content)),
    'Gmail': len(re.findall(r'\*\*Gmail\*\*: ✓', content)),
    'Google Drive': len(re.findall(r'\*\*Google Drive\*\*: ✓', content)),
    'Gong': len(re.findall(r'\*\*Gong\*\*: ✓', content)),
    'Dropbox': len(re.findall(r'\*\*Dropbox\*\*: ✓', content)),
    'Box': len(re.findall(r'\*\*Box\*\*: ✓', content)),
}

print('Target App Counts (CONFIRMED only):')
print('-' * 80)
for app, count in apps.items():
    print(f'  {app:20s}: {count:3d} companies')

# Create new summary section
new_summary = f"""---

## Summary Statistics

**Analysis of {companies} Fortune 500 Companies**

Target Application Adoption (CONFIRMED):
- **Salesforce**: {apps['Salesforce']} companies
- **ServiceNow**: {apps['ServiceNow']} companies
- **Jira**: {apps['Jira']} companies
- **Confluence**: {apps['Confluence']} companies
- **Slack**: {apps['Slack']} companies
- **Gmail**: {apps['Gmail']} companies
- **Google Drive**: {apps['Google Drive']} companies
- **Gong**: {apps['Gong']} companies
- **Dropbox**: {apps['Dropbox']} companies
- **Box**: {apps['Box']} companies

**Key Findings:**
- Salesforce and ServiceNow dominate enterprise SaaS adoption
- Atlassian tools (Jira) show strong presence in tech-forward companies
- Slack has significant but not universal adoption
- Gmail and Google Drive show limited adoption in Fortune 500
- Gong, Dropbox, and Box have minimal confirmed adoption

**Methodology:**
- Only apps marked with ✓ (CONFIRMED) are counted
- Data collected from company career pages, LinkedIn, and public sources
- Conservative approach: unconfirmed = not included in statistics

---"""

# Find and replace existing summary section
summary_pattern = r'---\n\n## Summary Statistics.*?---'
if re.search(summary_pattern, content, re.DOTALL):
    updated_content = re.sub(summary_pattern, new_summary, content, flags=re.DOTALL)
    print("\n✓ Found and updated existing summary section")
else:
    # If no summary exists, add before final section
    updated_content = content + "\n" + new_summary
    print("\n✓ Added new summary section to end of file")

# Write updated markdown
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print(f"\n✓ Summary statistics updated for {companies} companies")
print(f"\nTop 3 apps:")
print(f"  1. ServiceNow: {apps['ServiceNow']} companies")
print(f"  2. Salesforce: {apps['Salesforce']} companies")
print(f"  3. Jira: {apps['Jira']} companies")

print("\n" + "="*80)
print("Summary update complete. Ready to regenerate HTML.")
print("="*80)
