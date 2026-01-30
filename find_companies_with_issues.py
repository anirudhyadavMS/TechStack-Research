import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Scanning for companies with 'NOT Confirmed' apps...\n")

# Read markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Split into company sections
sections = re.split(r'^## (\d+)\. (.+)$', content, flags=re.MULTILINE)

companies_with_issues = []

# Process sections (sections come as: ['before', '1', 'COMPANY_NAME', 'content', '2', 'COMPANY_NAME', 'content', ...])
for i in range(1, len(sections), 3):
    if i+2 > len(sections):
        break

    company_num = sections[i]
    company_name = sections[i+1]
    company_content = sections[i+2] if i+2 < len(sections) else ""

    # Only check detailed entries (likely companies 1-65)
    if len(company_content) < 200:  # Skip simple entries
        continue

    # Look for NOT Confirmed patterns
    not_confirmed_patterns = [
        'NOT Confirmed',
        'NOT CONFIRMED',
        'NOT FOR',
        'No evidence found',
        'No evidence of',
        '❌ NOT',
        '✗ NOT',
        '- No specific evidence'
    ]

    issues_found = []
    for pattern in not_confirmed_patterns:
        if pattern in company_content:
            # Extract context
            matches = re.finditer(re.escape(pattern), company_content, re.IGNORECASE)
            for match in matches:
                start = max(0, match.start() - 100)
                end = min(len(company_content), match.end() + 150)
                context = company_content[start:end].strip()
                # Clean up
                context = re.sub(r'\n+', ' ', context)
                context = context[:200] + '...' if len(context) > 200 else context
                issues_found.append(context)

    if issues_found:
        companies_with_issues.append({
            'num': company_num,
            'name': company_name,
            'issues': issues_found[:3]  # Limit to 3 examples per company
        })

print(f"Found {len(companies_with_issues)} companies with 'NOT Confirmed' or similar issues:\n")
print("="*80)

for company in companies_with_issues:
    print(f"\n## {company['num']}. {company['name']}")
    print("-" * 80)
    for idx, issue in enumerate(company['issues'], 1):
        print(f"  {idx}. ...{issue}")
    print()

print("="*80)
print(f"\nTotal: {len(companies_with_issues)} companies need review")
