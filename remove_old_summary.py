#!/usr/bin/env python3
"""
Remove old summary section, keep only the new one
"""
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("Removing old summary section...")

# Read markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove old summary section (the one with "Updated: 201 Companies")
old_summary_pattern = r'## Summary Statistics \(Updated: 201 Companies\).*?(?=\n---\n\n## Summary Statistics|---\n\n## Summary Statistics)'
content = re.sub(old_summary_pattern, '', content, flags=re.DOTALL)

# Also clean up any double "---\n---" patterns
content = re.sub(r'---\n\n---', '---', content)

# Write updated markdown
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Removed old summary section")
print("✓ Keeping only the updated summary with 301 companies")
