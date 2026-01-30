import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

original_content = content

print("Replacing Google Cloud in Other Notable Apps sections...")

# Find and replace Google Cloud in bullet point lists
# Pattern: "- Google Cloud" or "- Google Cloud Platform" in bullet lists
# Replace with two separate bullets for Gmail and Google Drive

# Pattern 1: Simple bullet with Google Cloud (with optional description in parens)
pattern1 = r'^(\s*)-\s+Google Cloud(?:\s+Platform)?(?:\s+\([^)]+\))?\s*$'
replacement1 = r'\1- Gmail\n\1- Google Drive'

content = re.sub(pattern1, replacement1, content, flags=re.MULTILINE)

# Pattern 2: Google Cloud with description after dash
# "- Google Cloud - description" or "- Google Cloud: description"
pattern2 = r'^(\s*)-\s+Google Cloud(?:\s+Platform)?(?:\s*[:\-]\s*[^\n]+)?\s*$'

def replace_with_context(match):
    indent = match.group(1)
    return f"{indent}- Gmail\n{indent}- Google Drive"

content = re.sub(pattern2, replace_with_context, content, flags=re.MULTILINE)

# Pattern 3: Google Cloud in parenthetical contexts like "(major cloud platform)"
# Remove these entirely if standalone
content = re.sub(
    r'^(\s*)-\s+Google Cloud\s+\(major cloud platform\)\s*$',
    r'\1- Gmail\n\1- Google Drive',
    content,
    flags=re.MULTILINE
)

# Pattern 4: SAP mentions that reference Google Cloud
# "- SAP (ERP on Google Cloud)" -> "- SAP"
content = re.sub(
    r'(\-\s+SAP[^)]*)\s*\([^)]*on Google Cloud[^)]*\)',
    r'\1',
    content
)

# Count changes
lines_changed = original_content.count('\n') - content.count('\n')
original_gc_count = original_content.count('Google Cloud')
new_gc_count = content.count('Google Cloud')

print(f"\n✓ Replacements made!")
print(f"  'Google Cloud' mentions reduced: {original_gc_count} -> {new_gc_count}")
print(f"  Net line change: {-lines_changed} lines added")

# Show sample of remaining Google Cloud mentions
remaining_mentions = []
for i, line in enumerate(content.split('\n')):
    if 'Google Cloud' in line:
        remaining_mentions.append((i+1, line.strip()))

if remaining_mentions:
    print(f"\n  Remaining 'Google Cloud' mentions: {len(remaining_mentions)}")
    print("  (These are in detailed text, URLs, sources, etc.)")
    if len(remaining_mentions) <= 10:
        print("\n  Locations:")
        for line_num, line_text in remaining_mentions:
            preview = line_text[:100] + '...' if len(line_text) > 100 else line_text
            print(f"    Line {line_num}: {preview}")

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ Markdown file updated successfully!")
