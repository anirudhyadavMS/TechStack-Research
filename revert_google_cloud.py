import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

print("Reverting Gmail and Google Drive back to Google Cloud...\n")

# Count before
gmail_before = content.count('- Gmail\n')
gdrive_before = content.count('- Google Drive\n')

# Strategy: Replace consecutive Gmail and Google Drive bullets with single Google Cloud
# Pattern 1: Gmail followed immediately by Google Drive
pattern1 = r'^(\s*)-\s+Gmail\n\1-\s+Google Drive\n'
replacement1 = r'\1- Google Cloud\n'

content = re.sub(pattern1, replacement1, content, flags=re.MULTILINE)

# Pattern 2: Google Drive followed by Gmail (reverse order)
pattern2 = r'^(\s*)-\s+Google Drive\n\1-\s+Gmail\n'
replacement2 = r'\1- Google Cloud\n'

content = re.sub(pattern2, replacement2, content, flags=re.MULTILINE)

# Pattern 3: Standalone Gmail bullets (not followed by Google Drive)
# Replace with Google Cloud
content = re.sub(
    r'^(\s*)-\s+Gmail(?!\n\1-\s+Google Drive)\n',
    r'\1- Google Cloud\n',
    content,
    flags=re.MULTILINE
)

# Pattern 4: Standalone Google Drive bullets (not preceded by Gmail)
# This is tricky, so we'll look for Google Drive that wasn't already converted
lines = content.split('\n')
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    # Check if this is a Google Drive line that wasn't part of a Gmail/Drive pair
    if re.match(r'^\s*-\s+Google Drive\s*$', line):
        # Check if previous line was Gmail (already converted)
        if i > 0 and not re.match(r'^\s*-\s+Gmail\s*$', lines[i-1]):
            # Replace Google Drive with Google Cloud
            line = re.sub(r'Google Drive', 'Google Cloud', line)
    new_lines.append(line)
    i += 1

content = '\n'.join(new_lines)

# Count after
gmail_after = content.count('- Gmail\n')
gdrive_after = content.count('- Google Drive\n')
gcloud_after = content.count('- Google Cloud\n')

print(f"Changes made:")
print(f"  Gmail: {gmail_before} → {gmail_after}")
print(f"  Google Drive: {gdrive_before} → {gdrive_after}")
print(f"  Google Cloud: {gcloud_after} instances")

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nMarkdown file reverted successfully!")
