import sys
sys.stdout.reconfigure(encoding='utf-8')

# Summary data from batch 5
new_salesforce = ["Morgan Stanley", "U.S. Bancorp", "Pfizer", "General Motors", "United Airlines", "PNC Financial", "American Airlines"]
new_servicenow = ["U.S. Bancorp", "Pfizer", "General Motors", "United Airlines", "PNC Financial", "American Airlines"]
new_jira = ["U.S. Bancorp", "Pfizer", "General Motors", "United Airlines", "PNC Financial", "Capital One"]
new_confluence = ["U.S. Bancorp", "Pfizer", "General Motors", "United Airlines", "PNC Financial", "Capital One"]
new_slack = ["Capital One"]
new_box = ["Morgan Stanley"]

print(f"New Target App Counts from Batch 5 (10 companies):")
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
    '**Salesforce**: 64 companies',
    f'**Salesforce**: {64 + len(new_salesforce)} companies'
)
content = content.replace(
    '**ServiceNow**: 61 companies',
    f'**ServiceNow**: {61 + len(new_servicenow)} companies'
)
content = content.replace(
    '**Jira**: 29 companies',
    f'**Jira**: {29 + len(new_jira)} companies'
)
content = content.replace(
    '**Confluence**: 25 companies',
    f'**Confluence**: {25 + len(new_confluence)} companies'
)
content = content.replace(
    '**Slack**: 23 companies',
    f'**Slack**: {23 + len(new_slack)} companies'
)

# Update total count
content = content.replace(
    'Summary Statistics (Updated: 101 Companies)',
    'Summary Statistics (Updated: 111 Companies)'
)
content = content.replace(
    '**Total Companies Analyzed**: 101 companies',
    '**Total Companies Analyzed**: 111 companies'
)
content = content.replace(
    '**Fortune 100 Expansion**: 67 additional companies',
    '**Fortune 100 Expansion**: 77 additional companies'
)

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nStatistics updated in markdown file!")
print(f"New totals:")
print(f"  Total companies: 111")
print(f"  Salesforce: {64 + len(new_salesforce)}")
print(f"  ServiceNow: {61 + len(new_servicenow)}")
print(f"  Jira: {29 + len(new_jira)}")
print(f"  Confluence: {25 + len(new_confluence)}")
print(f"  Slack: {23 + len(new_slack)}")
