import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Fixing stat tiles to match actual data...\n")

# Read HTML
with open('company_technology_stack_analysis.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract companies array
match = re.search(r'const companies = (\[.*?\]);', html, re.DOTALL)
companies = json.loads(match.group(1))

# Count actual apps
salesforce = sum(1 for c in companies if 'Salesforce' in c.get('apps', []))
servicenow = sum(1 for c in companies if 'ServiceNow' in c.get('apps', []))
jira = sum(1 for c in companies if 'Jira' in c.get('apps', []))
slack = sum(1 for c in companies if 'Slack' in c.get('apps', []))

print(f"Actual counts from data:")
print(f"  Salesforce: {salesforce}")
print(f"  ServiceNow: {servicenow}")
print(f"  Jira: {jira}")
print(f"  Slack: {slack}")

# Update stat tiles
html = re.sub(
    r'(<div class="stat-number" id="salesforce-count">)\d+(</div>)',
    rf'\g<1>{salesforce}\g<2>',
    html
)
html = re.sub(
    r'(<div class="stat-number" id="servicenow-count">)\d+(</div>)',
    rf'\g<1>{servicenow}\g<2>',
    html
)
html = re.sub(
    r'(<div class="stat-number" id="jira-count">)\d+(</div>)',
    rf'\g<1>{jira}\g<2>',
    html
)
html = re.sub(
    r'(<div class="stat-number" id="slack-count">)\d+(</div>)',
    rf'\g<1>{slack}\g<2>',
    html
)

# Save
with open('company_technology_stack_analysis.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✓ Updated stat tiles to match actual data")
print(f"✓ Tiles now show the same counts as dropdown filters")
