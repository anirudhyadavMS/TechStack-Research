import sys
sys.stdout.reconfigure(encoding='utf-8')

# Summary data from batch 10 (companies 182-191, 10 companies)
# AIG, Raytheon Technologies, USAA, ADM, Energy Transfer,
# Dollar Tree, Nationwide, PBF Energy, USPS, Publix

# Confirmed findings from agent research:
new_salesforce = [
    "AIG", "USAA", "ADM", "Dollar Tree", "Nationwide", "USPS", "Publix"
]  # 7 companies

new_servicenow = [
    "AIG", "Raytheon Technologies", "USAA", "Dollar Tree", "USPS", "Publix"
]  # 6 companies

new_jira = [
    "Raytheon Technologies", "USAA"
]  # 2 companies

new_confluence = [
    "Raytheon Technologies", "USAA"
]  # 2 companies

new_slack = [
    "PBF Energy"
]  # 1 company

new_gmail = []  # 0 companies

new_box = []  # 0 companies

new_gong = []  # 0 companies

print(f"New Target App Counts from Batch 10 (10 companies, ranks 182-191):")
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
    '**Salesforce**: 124 companies',
    f'**Salesforce**: {124 + len(new_salesforce)} companies'
)
content = content.replace(
    '**ServiceNow**: 121 companies',
    f'**ServiceNow**: {121 + len(new_servicenow)} companies'
)
content = content.replace(
    '**Jira**: 55 companies',
    f'**Jira**: {55 + len(new_jira)} companies'
)
content = content.replace(
    '**Confluence**: 46 companies',
    f'**Confluence**: {46 + len(new_confluence)} companies'
)
content = content.replace(
    '**Slack**: 32 companies',
    f'**Slack**: {32 + len(new_slack)} companies'
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
    'Summary Statistics (Updated: 181 Companies)',
    'Summary Statistics (Updated: 191 Companies)'
)
content = content.replace(
    '**Total Companies Analyzed**: 181 companies',
    '**Total Companies Analyzed**: 191 companies'
)
content = content.replace(
    '**Fortune 100 Expansion**: 147 additional companies',
    '**Fortune 100 Expansion**: 157 additional companies'
)

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nStatistics updated in markdown file!")
print(f"\nNew totals:")
print(f"  Total companies: 191")
print(f"  Salesforce: {124 + len(new_salesforce)} ({round((124 + len(new_salesforce))/191*100, 1)}%)")
print(f"  ServiceNow: {121 + len(new_servicenow)} ({round((121 + len(new_servicenow))/191*100, 1)}%)")
print(f"  Jira: {55 + len(new_jira)} ({round((55 + len(new_jira))/191*100, 1)}%)")
print(f"  Confluence: {46 + len(new_confluence)} ({round((46 + len(new_confluence))/191*100, 1)}%)")
print(f"  Slack: {32 + len(new_slack)} ({round((32 + len(new_slack))/191*100, 1)}%)")
print(f"  Gmail/Google Drive: {17 + len(new_gmail)}")
print(f"  Box: {3 + len(new_box)}")
print(f"  Gong: {1 + len(new_gong)}")
