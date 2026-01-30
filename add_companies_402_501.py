#!/usr/bin/env python3
"""
Add Companies 402-501 to Markdown
"""
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("="*80)
print("ADDING COMPANIES 402-501 TO MARKDOWN")
print("="*80)

import os
base_dir = r'C:\Users\anirudhyadav\Fortune500_TechStack_Research_2026'

print('\nReading full research file...')
with open(os.path.join(base_dir, 'full_research_402_501.txt'), 'r', encoding='utf-8') as f:
    full_research = f.read()

# Extract just the company entries (remove the batch headers and summary)
lines = full_research.split('\n')
company_data = []
capture = False
for line in lines:
    if line.startswith('## '):
        capture = True
    if 'Summary Statistics for Companies 402-501' in line:
        break
    if capture:
        company_data.append(line)

new_companies = '\n'.join(company_data)

print('Reading existing markdown...')
with open(os.path.join(base_dir, 'company_technology_stack_analysis.md'), 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Find company 401
pattern = r'(## 401\..*?)(?=\n---\n\n## Summary Statistics|$)'
match = re.search(pattern, markdown_content, re.DOTALL)

if not match:
    print('ERROR: Could not find company 401')
    sys.exit(1)
else:
    insertion_point = match.end()
    print(f'✓ Found insertion point after company 401 at position {insertion_point}')

    # Insert new companies
    final_content = markdown_content[:insertion_point] + '\n\n' + new_companies + '\n' + markdown_content[insertion_point:]

    # Write updated markdown
    with open(os.path.join(base_dir, 'company_technology_stack_analysis.md'), 'w', encoding='utf-8') as f:
        f.write(final_content)

    # Count companies
    company_count = len(re.findall(r'^## \d+\.', final_content, re.MULTILINE))
    print(f'\n✓ SUCCESS: Added companies 402-501 to markdown')
    print(f'✓ Total companies in markdown: {company_count}')
    print("="*80)
