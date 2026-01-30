import sys
sys.stdout.reconfigure(encoding='utf-8')

# BATCH TEMPLATE - Copy and modify for new batches
# Usage: Update company names and previous counts, then run

# ============================================================================
# BATCH CONFIGURATION
# ============================================================================
BATCH_NUMBER = 12
COMPANY_RANGE = "202-211"
COMPANY_COUNT = 10

# Company names in this batch (for reference)
COMPANIES_IN_BATCH = [
    "Company A", "Company B", "Company C", "Company D", "Company E",
    "Company F", "Company G", "Company H", "Company I", "Company J"
]

# ============================================================================
# PREVIOUS COUNTS (Update these from last batch)
# ============================================================================
PREVIOUS_COUNTS = {
    'total': 201,
    'salesforce': 139,
    'servicenow': 131,
    'jira': 60,
    'confluence': 51,
    'slack': 33,
    'gmail': 19,
    'box': 3,
    'gong': 2,
    'fortune_expansion': 167  # total - 34 (original Fortune 100 subset)
}

# ============================================================================
# NEW FINDINGS (Fill in after research completes)
# ============================================================================
new_salesforce = [
    # Add company names that use Salesforce
]

new_servicenow = [
    # Add company names that use ServiceNow
]

new_jira = [
    # Add company names that use Jira
]

new_confluence = [
    # Add company names that use Confluence
]

new_slack = [
    # Add company names that use Slack
]

new_gmail = [
    # Add company names that use Gmail/Google Workspace
]

new_box = [
    # Add company names that use Box
]

new_gong = [
    # Add company names that use Gong
]

# ============================================================================
# PRINT NEW ADDITIONS
# ============================================================================
print(f"\nNew Target App Counts from Batch {BATCH_NUMBER} ({COMPANY_COUNT} companies, ranks {COMPANY_RANGE}):")
print(f"  Salesforce: +{len(new_salesforce)}")
print(f"  ServiceNow: +{len(new_servicenow)}")
print(f"  Jira: +{len(new_jira)}")
print(f"  Confluence: +{len(new_confluence)}")
print(f"  Slack: +{len(new_slack)}")
print(f"  Gmail/Google Drive: +{len(new_gmail)}")
print(f"  Box: +{len(new_box)}")
print(f"  Gong: +{len(new_gong)}")

# ============================================================================
# UPDATE MARKDOWN FILE
# ============================================================================
# Read existing markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update statistics
content = content.replace(
    f"**Salesforce**: {PREVIOUS_COUNTS['salesforce']} companies",
    f"**Salesforce**: {PREVIOUS_COUNTS['salesforce'] + len(new_salesforce)} companies"
)
content = content.replace(
    f"**ServiceNow**: {PREVIOUS_COUNTS['servicenow']} companies",
    f"**ServiceNow**: {PREVIOUS_COUNTS['servicenow'] + len(new_servicenow)} companies"
)
content = content.replace(
    f"**Jira**: {PREVIOUS_COUNTS['jira']} companies",
    f"**Jira**: {PREVIOUS_COUNTS['jira'] + len(new_jira)} companies"
)
content = content.replace(
    f"**Confluence**: {PREVIOUS_COUNTS['confluence']} companies",
    f"**Confluence**: {PREVIOUS_COUNTS['confluence'] + len(new_confluence)} companies"
)
content = content.replace(
    f"**Slack**: {PREVIOUS_COUNTS['slack']} companies",
    f"**Slack**: {PREVIOUS_COUNTS['slack'] + len(new_slack)} companies"
)
content = content.replace(
    f"**Gmail/Google Drive**: {PREVIOUS_COUNTS['gmail']} companies",
    f"**Gmail/Google Drive**: {PREVIOUS_COUNTS['gmail'] + len(new_gmail)} companies"
)
content = content.replace(
    f"**Box**: {PREVIOUS_COUNTS['box']} companies",
    f"**Box**: {PREVIOUS_COUNTS['box'] + len(new_box)} companies"
)
content = content.replace(
    f"**Gong**: {PREVIOUS_COUNTS['gong']} companies",
    f"**Gong**: {PREVIOUS_COUNTS['gong'] + len(new_gong)} companies"
)

# Update total count
new_total = PREVIOUS_COUNTS['total'] + COMPANY_COUNT
new_expansion = PREVIOUS_COUNTS['fortune_expansion'] + COMPANY_COUNT

content = content.replace(
    f"Summary Statistics (Updated: {PREVIOUS_COUNTS['total']} Companies)",
    f"Summary Statistics (Updated: {new_total} Companies)"
)
content = content.replace(
    f"**Total Companies Analyzed**: {PREVIOUS_COUNTS['total']} companies",
    f"**Total Companies Analyzed**: {new_total} companies"
)
content = content.replace(
    f"**Fortune 100 Expansion**: {PREVIOUS_COUNTS['fortune_expansion']} additional companies",
    f"**Fortune 100 Expansion**: {new_expansion} additional companies"
)

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

# ============================================================================
# PRINT RESULTS
# ============================================================================
print("\nStatistics updated in markdown file!")
print(f"\nNew totals:")
print(f"  Total companies: {new_total}")
print(f"  Salesforce: {PREVIOUS_COUNTS['salesforce'] + len(new_salesforce)} ({round((PREVIOUS_COUNTS['salesforce'] + len(new_salesforce))/new_total*100, 1)}%)")
print(f"  ServiceNow: {PREVIOUS_COUNTS['servicenow'] + len(new_servicenow)} ({round((PREVIOUS_COUNTS['servicenow'] + len(new_servicenow))/new_total*100, 1)}%)")
print(f"  Jira: {PREVIOUS_COUNTS['jira'] + len(new_jira)} ({round((PREVIOUS_COUNTS['jira'] + len(new_jira))/new_total*100, 1)}%)")
print(f"  Confluence: {PREVIOUS_COUNTS['confluence'] + len(new_confluence)} ({round((PREVIOUS_COUNTS['confluence'] + len(new_confluence))/new_total*100, 1)}%)")
print(f"  Slack: {PREVIOUS_COUNTS['slack'] + len(new_slack)} ({round((PREVIOUS_COUNTS['slack'] + len(new_slack))/new_total*100, 1)}%)")
print(f"  Gmail/Google Drive: {PREVIOUS_COUNTS['gmail'] + len(new_gmail)} ({round((PREVIOUS_COUNTS['gmail'] + len(new_gmail))/new_total*100, 1)}%)")
print(f"  Box: {PREVIOUS_COUNTS['box'] + len(new_box)}")
print(f"  Gong: {PREVIOUS_COUNTS['gong'] + len(new_gong)}")
