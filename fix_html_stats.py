import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read HTML file
with open('company_technology_stack_analysis.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

print("Fixing HTML stats to match actual data...\n")

# Extract the companies JSON array
companies_match = re.search(r'const companies = (\[.*?\]);', html_content, re.DOTALL)
if not companies_match:
    print("ERROR: Could not find companies array")
    sys.exit(1)

companies_json = companies_match.group(1)
companies = json.loads(companies_json)

# Count actual stats
total_companies = len(companies)
salesforce_count = sum(1 for c in companies if 'Salesforce' in c.get('apps', []))
servicenow_count = sum(1 for c in companies if 'ServiceNow' in c.get('apps', []))
jira_count = sum(1 for c in companies if 'Jira' in c.get('apps', []))
slack_count = sum(1 for c in companies if 'Slack' in c.get('apps', []))

print(f"Actual counts from data:")
print(f"  Total companies: {total_companies}")
print(f"  Salesforce: {salesforce_count}")
print(f"  ServiceNow: {servicenow_count}")
print(f"  Jira: {jira_count}")
print(f"  Slack: {slack_count}")

# Update the hardcoded stats in HTML
# Update total companies
html_content = re.sub(
    r'<div class="stat-number">201</div>',
    f'<div class="stat-number">{total_companies}</div>',
    html_content
)

# Update Salesforce count
html_content = re.sub(
    r'<div class="stat-number" id="salesforce-count">139</div>',
    f'<div class="stat-number" id="salesforce-count">{salesforce_count}</div>',
    html_content
)

# Update ServiceNow count
html_content = re.sub(
    r'<div class="stat-number" id="servicenow-count">131</div>',
    f'<div class="stat-number" id="servicenow-count">{servicenow_count}</div>',
    html_content
)

# Update Jira count
html_content = re.sub(
    r'<div class="stat-number" id="jira-count">60</div>',
    f'<div class="stat-number" id="jira-count">{jira_count}</div>',
    html_content
)

# Update Slack count
html_content = re.sub(
    r'<div class="stat-number" id="slack-count">33</div>',
    f'<div class="stat-number" id="slack-count">{slack_count}</div>',
    html_content
)

# Update subtitle
html_content = re.sub(
    r'Comprehensive research of 201 companies - 2026',
    f'Comprehensive research of {total_companies} companies - 2026',
    html_content
)

# Update title
html_content = re.sub(
    r'<title>Company Technology Stack Analysis - 201 Companies',
    f'<title>Company Technology Stack Analysis - {total_companies} Companies',
    html_content
)

# Save updated HTML
with open('company_technology_stack_analysis.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"\n✓ Updated all stat tiles to match actual data")
print(f"✓ HTML file updated successfully!")
