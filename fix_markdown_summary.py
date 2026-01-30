#!/usr/bin/env python3
"""
Fix markdown summary section with correct counts
"""
import sys
import re
import os

sys.stdout.reconfigure(encoding='utf-8')

print("="*80)
print("FIXING MARKDOWN SUMMARY WITH CORRECT COUNTS")
print("="*80)

base_dir = r'C:\Users\anirudhyadav\Fortune500_TechStack_Research_2026'

# Read markdown
with open(os.path.join(base_dir, 'company_technology_stack_analysis.md'), 'r', encoding='utf-8') as f:
    content = f.read()

# Count company sections
companies = len(re.findall(r'^## \d+\.', content, re.MULTILINE))
print(f"\nTotal Companies Found: {companies}\n")

# Count each target app with checkmark (actual counts from markdown)
# Handle both formats: **App** ✓ and **App**: ✓
apps = {
    'Salesforce': len(re.findall(r'\*\*Salesforce\*\*\s*:?\s*✓', content)),
    'ServiceNow': len(re.findall(r'\*\*ServiceNow\*\*\s*:?\s*✓', content)),
    'Jira': len(re.findall(r'\*\*Jira\*\*\s*:?\s*✓', content)),
    'Confluence': len(re.findall(r'\*\*Confluence\*\*\s*:?\s*✓', content)),
    'Slack': len(re.findall(r'\*\*Slack\*\*\s*:?\s*✓', content)),
    'Gmail': len(re.findall(r'\*\*Gmail\*\*\s*:?\s*✓', content)),
    'Google Drive': len(re.findall(r'\*\*Google Drive\*\*\s*:?\s*✓', content)),
    'Gong': len(re.findall(r'\*\*Gong\*\*\s*:?\s*✓', content)),
    'Dropbox': len(re.findall(r'\*\*Dropbox\*\*\s*:?\s*✓', content)),
    'Box': len(re.findall(r'\*\*Box\*\*\s*:?\s*✓', content)),
}

print('Actual Target App Counts (CONFIRMED):')
print('-' * 80)
for app, count in apps.items():
    print(f'  {app:20s}: {count:3d} companies')

# Create new summary section with correct counts
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
- ServiceNow ({apps['ServiceNow']} companies) and Salesforce ({apps['Salesforce']} companies) dominate enterprise SaaS adoption
- Atlassian tools show strong presence: Jira ({apps['Jira']} companies), Confluence ({apps['Confluence']} companies)
- Slack has moderate adoption ({apps['Slack']} companies) among Fortune 500
- Gmail ({apps['Gmail']} companies) and Google Drive ({apps['Google Drive']} companies) have limited adoption in Fortune 500
- Gong ({apps['Gong']} companies), Dropbox ({apps['Dropbox']} companies), and Box ({apps['Box']} companies) have minimal confirmed adoption

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
    print("\n❌ Could not find summary section to update")
    sys.exit(1)

# Write updated markdown
with open(os.path.join(base_dir, 'company_technology_stack_analysis.md'), 'w', encoding='utf-8') as f:
    f.write(updated_content)

print(f"\n✓ Summary statistics updated for {companies} companies")
print(f"\nTop 3 apps:")
print(f"  1. Salesforce: {apps['Salesforce']} companies")
print(f"  2. ServiceNow: {apps['ServiceNow']} companies")
print(f"  3. Jira: {apps['Jira']} companies")

print("\n" + "="*80)
print("Summary update complete.")
print("="*80)
