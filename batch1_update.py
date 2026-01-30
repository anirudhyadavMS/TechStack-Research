import sys
sys.stdout.reconfigure(encoding='utf-8')

# Summary data for quick statistics update
new_salesforce = ["Johnson & Johnson", "Procter & Gamble", "General Electric", "Phillips 66", "Archer Daniels Midland", "American Express", "Walgreens Boots Alliance", "ConocoPhillips"]
new_servicenow = ["Johnson & Johnson", "General Electric", "Marathon Petroleum", "Phillips 66", "Archer Daniels Midland", "Walgreens Boots Alliance", "ConocoPhillips"]
new_jira = ["Phillips 66", "Archer Daniels Midland", "ConocoPhillips"]
new_confluence = ["Phillips 66", "Archer Daniels Midland", "ConocoPhillips"]
new_slack = ["General Electric", "American Express"]
new_box = ["Johnson & Johnson", "Procter & Gamble", "General Electric", "Walgreens Boots Alliance"]

print(f"New Target App Counts from Batch 1 (10 companies):")
print(f"  Salesforce: +{len(new_salesforce)}")
print(f"  ServiceNow: +{len(new_servicenow)}")
print(f"  Jira: +{len(new_jira)}")
print(f"  Confluence: +{len(new_confluence)}")
print(f"  Slack: +{len(new_slack)}")
print(f"  Box: +{len(new_box)}")

# Read existing markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update statistics
content = content.replace(
    '**Salesforce**: 39 companies',
    f'**Salesforce**: {39 + len(new_salesforce)} companies'
)
content = content.replace(
    '**ServiceNow**: 37 companies',
    f'**ServiceNow**: {37 + len(new_servicenow)} companies'
)
content = content.replace(
    '**Jira**: 20 companies',
    f'**Jira**: {20 + len(new_jira)} companies'
)
content = content.replace(
    '**Confluence**: 18 companies',
    f'**Confluence**: {18 + len(new_confluence)} companies'
)
content = content.replace(
    '**Slack**: 20 companies',
    f'**Slack**: {20 + len(new_slack)} companies'
)

# Update total count
content = content.replace(
    'Summary Statistics (Updated: 65 Companies)',
    'Summary Statistics (Updated: 75 Companies)'
)
content = content.replace(
    '**Total Companies Analyzed**: 65 companies',
    '**Total Companies Analyzed**: 75 companies'
)
content = content.replace(
    '**Fortune 100 Expansion**: 31 additional companies',
    '**Fortune 100 Expansion**: 41 additional companies'
)

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nStatistics updated in markdown file!")
print(f"New totals:")
print(f"  Total companies: 75")
print(f"  Salesforce: {39 + len(new_salesforce)}")
print(f"  ServiceNow: {37 + len(new_servicenow)}")
print(f"  Jira: {20 + len(new_jira)}")
print(f"  Slack: {20 + len(new_slack)}")
