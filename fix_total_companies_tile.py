#!/usr/bin/env python3
"""
Fix total companies tile in HTML
"""
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read HTML
with open('company_technology_stack_analysis.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update total companies tile from 201 to 301
html = re.sub(
    r'(<div class="stat-number">)201(</div>\s*<div class="stat-label">Companies</div>)',
    r'\g<1>301\g<2>',
    html
)

# Write updated HTML
with open('company_technology_stack_analysis.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('✓ Updated total companies tile to 301')
