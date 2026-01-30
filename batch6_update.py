import sys
sys.stdout.reconfigure(encoding='utf-8')

# Summary data from batch 6
new_salesforce = ["Thermo Fisher", "Progressive", "ADM", "Dow", "Delta Air Lines", "Allstate", "Abbott", "Honeywell", "3M"]
new_servicenow = ["Thermo Fisher", "ADM", "Dow", "Delta Air Lines", "Allstate", "Broadcom", "Honeywell", "3M"]
new_jira = ["Allstate", "Broadcom", "Honeywell"]
new_confluence = ["Broadcom"]
new_slack = ["Delta Air Lines"]
new_gmail = ["Broadcom"]
new_box = ["Broadcom"]

print(f"New Target App Counts from Batch 6 (10 companies):")
print(f"  Salesforce: +{len(new_salesforce)}")
print(f"  ServiceNow: +{len(new_servicenow)}")
print(f"  Jira: +{len(new_jira)}")
print(f"  Confluence: +{len(new_confluence)}")
print(f"  Slack: +{len(new_slack)}")
print(f"  Gmail/Google Drive: +{len(new_gmail)}")
print(f"  Box: +{len(new_box)}")

# Read existing markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update statistics
content = content.replace(
    '**Salesforce**: 71 companies',
    f'**Salesforce**: {71 + len(new_salesforce)} companies'
)
content = content.replace(
    '**ServiceNow**: 67 companies',
    f'**ServiceNow**: {67 + len(new_servicenow)} companies'
)
content = content.replace(
    '**Jira**: 35 companies',
    f'**Jira**: {35 + len(new_jira)} companies'
)
content = content.replace(
    '**Confluence**: 31 companies',
    f'**Confluence**: {31 + len(new_confluence)} companies'
)
content = content.replace(
    '**Slack**: 24 companies',
    f'**Slack**: {24 + len(new_slack)} companies'
)

# Update total count
content = content.replace(
    'Summary Statistics (Updated: 111 Companies)',
    'Summary Statistics (Updated: 121 Companies)'
)
content = content.replace(
    '**Total Companies Analyzed**: 111 companies',
    '**Total Companies Analyzed**: 121 companies'
)
content = content.replace(
    '**Fortune 100 Expansion**: 77 additional companies',
    '**Fortune 100 Expansion**: 87 additional companies'
)

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nStatistics updated in markdown file!")
print(f"New totals:")
print(f"  Total companies: 121")
print(f"  Salesforce: {71 + len(new_salesforce)}")
print(f"  ServiceNow: {67 + len(new_servicenow)}")
print(f"  Jira: {35 + len(new_jira)}")
print(f"  Confluence: {31 + len(new_confluence)}")
print(f"  Slack: {24 + len(new_slack)}")
