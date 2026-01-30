import sys
sys.stdout.reconfigure(encoding='utf-8')

# Summary data from batch 4
new_salesforce = ["Tyson Foods", "Dollar General", "Deere & Company", "TIAA", "Liberty Mutual"]
new_servicenow = ["Plains All American", "Tyson Foods", "Dollar General", "CHS Inc.", "Deere & Company", "TIAA", "Exelon", "Liberty Mutual"]
new_jira = ["StoneX Group", "TIAA", "Liberty Mutual"]
new_confluence = ["StoneX Group", "Liberty Mutual"]
new_slack = ["Liberty Mutual"]

print(f"New Target App Counts from Batch 4 (10 companies):")
print(f"  Salesforce: +{len(new_salesforce)}")
print(f"  ServiceNow: +{len(new_servicenow)}")
print(f"  Jira: +{len(new_jira)}")
print(f"  Confluence: +{len(new_confluence)}")
print(f"  Slack: +{len(new_slack)}")

# Read existing markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update statistics
content = content.replace(
    '**Salesforce**: 59 companies',
    f'**Salesforce**: {59 + len(new_salesforce)} companies'
)
content = content.replace(
    '**ServiceNow**: 53 companies',
    f'**ServiceNow**: {53 + len(new_servicenow)} companies'
)
content = content.replace(
    '**Jira**: 26 companies',
    f'**Jira**: {26 + len(new_jira)} companies'
)
content = content.replace(
    '**Confluence**: 23 companies',
    f'**Confluence**: {23 + len(new_confluence)} companies'
)
content = content.replace(
    '**Slack**: 22 companies',
    f'**Slack**: {22 + len(new_slack)} companies'
)

# Update total count
content = content.replace(
    'Summary Statistics (Updated: 91 Companies)',
    'Summary Statistics (Updated: 101 Companies)'
)
content = content.replace(
    '**Total Companies Analyzed**: 91 companies',
    '**Total Companies Analyzed**: 101 companies'
)
content = content.replace(
    '**Fortune 100 Expansion**: 57 additional companies',
    '**Fortune 100 Expansion**: 67 additional companies'
)

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nStatistics updated in markdown file!")
print(f"New totals:")
print(f"  Total companies: 101")
print(f"  Salesforce: {59 + len(new_salesforce)}")
print(f"  ServiceNow: {53 + len(new_servicenow)}")
print(f"  Jira: {26 + len(new_jira)}")
print(f"  Confluence: {23 + len(new_confluence)}")
print(f"  Slack: {22 + len(new_slack)}")
