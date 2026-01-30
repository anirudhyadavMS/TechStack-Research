import sys
sys.stdout.reconfigure(encoding='utf-8')

# Summary data from batch 3
new_salesforce = ["Fannie Mae", "Freddie Mac", "Energy Transfer", "New York Life", "State Farm"]
new_servicenow = ["Fannie Mae", "Freddie Mac", "State Farm"]
new_jira = ["Fannie Mae", "Freddie Mac"]
new_confluence = ["Fannie Mae", "Freddie Mac"]

print(f"New Target App Counts from Batch 3 (6 companies):")
print(f"  Salesforce: +{len(new_salesforce)}")
print(f"  ServiceNow: +{len(new_servicenow)}")
print(f"  Jira: +{len(new_jira)}")
print(f"  Confluence: +{len(new_confluence)}")

# Read existing markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update statistics
content = content.replace(
    '**Salesforce**: 54 companies',
    f'**Salesforce**: {54 + len(new_salesforce)} companies'
)
content = content.replace(
    '**ServiceNow**: 50 companies',
    f'**ServiceNow**: {50 + len(new_servicenow)} companies'
)
content = content.replace(
    '**Jira**: 24 companies',
    f'**Jira**: {24 + len(new_jira)} companies'
)
content = content.replace(
    '**Confluence**: 21 companies',
    f'**Confluence**: {21 + len(new_confluence)} companies'
)
content = content.replace(
    '**Slack**: 22 companies',
    f'**Slack**: 22 companies'
)

# Update total count
content = content.replace(
    'Summary Statistics (Updated: 85 Companies)',
    'Summary Statistics (Updated: 91 Companies)'
)
content = content.replace(
    '**Total Companies Analyzed**: 85 companies',
    '**Total Companies Analyzed**: 91 companies'
)
content = content.replace(
    '**Fortune 100 Expansion**: 51 additional companies',
    '**Fortune 100 Expansion**: 57 additional companies'
)

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nStatistics updated in markdown file!")
print(f"New totals:")
print(f"  Total companies: 91")
print(f"  Salesforce: {54 + len(new_salesforce)}")
print(f"  ServiceNow: {50 + len(new_servicenow)}")
print(f"  Jira: {24 + len(new_jira)}")
print(f"  Confluence: {21 + len(new_confluence)}")
