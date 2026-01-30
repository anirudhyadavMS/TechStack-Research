#!/usr/bin/env python3
"""
Consolidate Batches 12-21 (Companies 202-301) into Markdown
Uses completed research data and adds to master file
"""
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("="*80)
print("CONSOLIDATING BATCHES 12-21 INTO MARKDOWN")
print("="*80)

# Read batch 12 research output
with open('batch_12_research_output.txt', 'r', encoding='utf-8') as f:
    batch_12_content = f.read()

# Read existing markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Find last company (201)
last_company_pattern = r'(## 201\..*?)(?=\n---\n\n## Summary Statistics|$)'
match = re.search(last_company_pattern, markdown_content, re.DOTALL)

if not match:
    print("❌ Could not find company 201 in markdown")
    sys.exit(1)

insertion_point = match.end()
print(f"✓ Found insertion point after company 201\n")

# Insert batch 12 content
new_content = "\n" + batch_12_content

# For now, add placeholders for remaining batches (13-21)
# These will be researched and added in subsequent scripts
placeholder_note = """
---

**NOTE:** Batches 13-21 (Companies 212-301) research in progress.
Data will be added systematically to maintain quality standards.

"""

final_content = markdown_content[:insertion_point] + new_content + placeholder_note + markdown_content[insertion_point:]

# Write updated markdown
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("✓ Added Batch 12 (Companies 202-211) to markdown")
print("✓ Companies 212-301 marked as pending research")
print("\nNext steps:")
print("  1. Create research scripts for batches 13-21")
print("  2. Add researched companies to markdown")
print("  3. Update summary statistics")
print("  4. Regenerate HTML dashboard")

print("="*80)
