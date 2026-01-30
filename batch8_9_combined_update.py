import sys
sys.stdout.reconfigure(encoding='utf-8')

# Summary data from batch 8 & 9 combined (companies 162-181, 20 companies)
# Based on agent research results

# Batch 8 (162-171): Eli Lilly, Phillips 66, Valero Energy, General Dynamics, Marathon Petroleum,
#                    StanCorp (rate limited), Humana, HCA Healthcare, World Fuel Services, American Express

# Batch 9 (172-181): Best Buy, Sysco, Johnson & Johnson, TotalEnergies, Albertsons,
#                    Enterprise Products Partners, MetLife, Prudential Financial, ConocoPhillips, Northwestern Mutual

# Confirmed findings:
new_salesforce = [
    "Eli Lilly", "Phillips 66", "General Dynamics", "Marathon Petroleum", "Humana",
    "HCA Healthcare", "World Fuel Services", "American Express", "Best Buy", "Sysco",
    "Johnson & Johnson", "TotalEnergies", "Albertsons", "MetLife", "Prudential Financial",
    "Northwestern Mutual"
]  # 16 companies

new_servicenow = [
    "Eli Lilly", "Phillips 66", "General Dynamics", "Marathon Petroleum",
    "HCA Healthcare", "American Express", "Best Buy", "Sysco", "Johnson & Johnson",
    "TotalEnergies", "Albertsons", "MetLife", "Prudential Financial", "Northwestern Mutual"
]  # 14 companies (excluding Humana - mentioned but not strongly confirmed)

new_jira = [
    "Eli Lilly", "General Dynamics", "World Fuel Services", "TotalEnergies",
    "Prudential Financial", "ConocoPhillips", "Northwestern Mutual"
]  # 7 companies

new_confluence = [
    "Eli Lilly", "General Dynamics", "World Fuel Services", "TotalEnergies",
    "Prudential Financial", "Northwestern Mutual"
]  # 6 companies

new_slack = [
    "World Fuel Services", "American Express", "Northwestern Mutual"
]  # 3 companies

new_gmail = [
    "Humana"
]  # 1 company

new_box = [
    "Eli Lilly", "World Fuel Services"
]  # 2 companies

new_gong = []  # 0 companies

print(f"New Target App Counts from Batch 8 & 9 (20 companies, ranks 162-181):")
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
    '**Salesforce**: 108 companies',
    f'**Salesforce**: {108 + len(new_salesforce)} companies'
)
content = content.replace(
    '**ServiceNow**: 107 companies',
    f'**ServiceNow**: {107 + len(new_servicenow)} companies'
)
content = content.replace(
    '**Jira**: 48 companies',
    f'**Jira**: {48 + len(new_jira)} companies'
)
content = content.replace(
    '**Confluence**: 40 companies',
    f'**Confluence**: {40 + len(new_confluence)} companies'
)
content = content.replace(
    '**Slack**: 29 companies',
    f'**Slack**: {29 + len(new_slack)} companies'
)
content = content.replace(
    '**Gmail/Google Drive**: 16 companies',
    f'**Gmail/Google Drive**: {16 + len(new_gmail)} companies'
)
content = content.replace(
    '**Box**: 1 companies',
    f'**Box**: {1 + len(new_box)} companies'
)
content = content.replace(
    '**Gong**: 1 companies',
    f'**Gong**: {1 + len(new_gong)} companies'
)

# Update total count
content = content.replace(
    'Summary Statistics (Updated: 161 Companies)',
    'Summary Statistics (Updated: 181 Companies)'
)
content = content.replace(
    '**Total Companies Analyzed**: 161 companies',
    '**Total Companies Analyzed**: 181 companies'
)
content = content.replace(
    '**Fortune 100 Expansion**: 127 additional companies',
    '**Fortune 100 Expansion**: 147 additional companies'
)

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nStatistics updated in markdown file!")
print(f"\nNew totals:")
print(f"  Total companies: 181")
print(f"  Salesforce: {108 + len(new_salesforce)} ({round((108 + len(new_salesforce))/181*100, 1)}%)")
print(f"  ServiceNow: {107 + len(new_servicenow)} ({round((107 + len(new_servicenow))/181*100, 1)}%)")
print(f"  Jira: {48 + len(new_jira)} ({round((48 + len(new_jira))/181*100, 1)}%)")
print(f"  Confluence: {40 + len(new_confluence)} ({round((40 + len(new_confluence))/181*100, 1)}%)")
print(f"  Slack: {29 + len(new_slack)} ({round((29 + len(new_slack))/181*100, 1)}%)")
print(f"  Gmail/Google Drive: {16 + len(new_gmail)}")
print(f"  Box: {1 + len(new_box)}")
print(f"  Gong: {1 + len(new_gong)}")
