import sys
sys.stdout.reconfigure(encoding='utf-8')

# Summary data from batch 11 (companies 192-201, 10 companies)
# Paccar, Stryker, Rocket Companies, CHS Inc, INTL FCStone/StoneX,
# Nucor, Uber, Cummins, Bristol Myers Squibb, CenterPoint Energy

# Confirmed findings from agent research:
new_salesforce = [
    "Paccar", "Stryker", "Rocket Companies", "StoneX", "Uber",
    "Cummins", "Bristol Myers Squibb", "CenterPoint Energy"
]  # 8 companies

new_servicenow = [
    "Stryker", "Uber", "Cummins", "Bristol Myers Squibb"
]  # 4 companies

new_jira = [
    "StoneX", "Uber", "Bristol Myers Squibb"
]  # 3 companies

new_confluence = [
    "StoneX", "Uber", "Bristol Myers Squibb"
]  # 3 companies

new_slack = []  # 0 companies

new_gmail = [
    "Uber", "Bristol Myers Squibb"
]  # 2 companies (Google Workspace)

new_box = []  # 0 companies

new_gong = [
    "Uber"
]  # 1 company

print(f"New Target App Counts from Batch 11 (10 companies, ranks 192-201):")
print(f"  Salesforce: +{len(new_salesforce)}")
print(f"  ServiceNow: +{len(new_servicenow)}")
print(f"  Jira: +{len(new_jira)}")
print(f"  Confluence: +{len(new_confluence)}")
print(f"  Slack: +{len(new_slack)}")
print(f"  Gmail/Google Drive: +{len(new_gmail)}")
print(f"  Box: +{len(new_box)}")
print(f"  Gong: +{len(new_gong)}")

# Read existing markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update statistics
content = content.replace(
    '**Salesforce**: 131 companies',
    f'**Salesforce**: {131 + len(new_salesforce)} companies'
)
content = content.replace(
    '**ServiceNow**: 127 companies',
    f'**ServiceNow**: {127 + len(new_servicenow)} companies'
)
content = content.replace(
    '**Jira**: 57 companies',
    f'**Jira**: {57 + len(new_jira)} companies'
)
content = content.replace(
    '**Confluence**: 48 companies',
    f'**Confluence**: {48 + len(new_confluence)} companies'
)
content = content.replace(
    '**Slack**: 33 companies',
    f'**Slack**: {33 + len(new_slack)} companies'
)
content = content.replace(
    '**Gmail/Google Drive**: 17 companies',
    f'**Gmail/Google Drive**: {17 + len(new_gmail)} companies'
)
content = content.replace(
    '**Box**: 3 companies',
    f'**Box**: {3 + len(new_box)} companies'
)
content = content.replace(
    '**Gong**: 1 companies',
    f'**Gong**: {1 + len(new_gong)} companies'
)

# Update total count
content = content.replace(
    'Summary Statistics (Updated: 191 Companies)',
    'Summary Statistics (Updated: 201 Companies)'
)
content = content.replace(
    '**Total Companies Analyzed**: 191 companies',
    '**Total Companies Analyzed**: 201 companies'
)
content = content.replace(
    '**Fortune 100 Expansion**: 157 additional companies',
    '**Fortune 100 Expansion**: 167 additional companies'
)

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nStatistics updated in markdown file!")
print(f"\nNew totals:")
print(f"  Total companies: 201")
print(f"  Salesforce: {131 + len(new_salesforce)} ({round((131 + len(new_salesforce))/201*100, 1)}%)")
print(f"  ServiceNow: {127 + len(new_servicenow)} ({round((127 + len(new_servicenow))/201*100, 1)}%)")
print(f"  Jira: {57 + len(new_jira)} ({round((57 + len(new_jira))/201*100, 1)}%)")
print(f"  Confluence: {48 + len(new_confluence)} ({round((48 + len(new_confluence))/201*100, 1)}%)")
print(f"  Slack: {33 + len(new_slack)} ({round((33 + len(new_slack))/201*100, 1)}%)")
print(f"  Gmail/Google Drive: {17 + len(new_gmail)}")
print(f"  Box: {3 + len(new_box)}")
print(f"  Gong: {1 + len(new_gong)}")
