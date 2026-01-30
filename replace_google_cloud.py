import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

print("Replacing Google Cloud references in markdown...")

# Strategy 1: Replace "- Google Cloud" bullet points with two separate bullets
# Pattern: "- Google Cloud" at start of line (with optional surrounding text in parens)
content = re.sub(
    r'^(\s*)-\s+Google Cloud(?:\s*\([^)]*\))?\s*$',
    r'\1- Gmail\n\1- Google Drive',
    content,
    flags=re.MULTILINE
)

# Strategy 2: Replace in comma-separated lists
# "AWS, Google Cloud, Azure" -> "AWS, Gmail, Google Drive, Azure"
content = re.sub(
    r'(,\s*)Google Cloud(\s*,)',
    r'\1Gmail, Google Drive\2',
    content
)

# Strategy 3: Replace end of list mentions
# "AWS and Google Cloud" -> "AWS, Gmail, and Google Drive"
content = re.sub(
    r'\s+and\s+Google Cloud\s*$',
    ', Gmail, and Google Drive',
    content,
    flags=re.MULTILINE
)

# Strategy 4: Replace "Google Cloud Platform" references in Other Notable Apps sections
content = re.sub(
    r'^(\s*)-\s+Google Cloud Platform(?:\s*\([^)]*\))?\s*$',
    r'\1- Gmail\n\1- Google Drive',
    content,
    flags=re.MULTILINE
)

# Count remaining
remaining = content.count('Google Cloud')
print(f"\nRemaining 'Google Cloud' mentions: {remaining}")
print("(These are likely in detailed descriptions, partnerships, etc.)")

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ Markdown file updated!")
