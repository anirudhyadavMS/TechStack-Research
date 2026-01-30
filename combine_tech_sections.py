import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

print("Combining Target Applications and Other Technologies into Tech Stack...\n")

# Pattern to find and replace both sections
# This will find:
# **Target Apps Found:**
# - apps...
# **Other Notable Apps:**
# - apps...
# And replace with:
# **Tech Stack:**
# - apps... (combined)

def combine_sections(match):
    full_match = match.group(0)

    # Extract all bullet points from both sections
    apps = []

    # Find all bullet point lines (- something)
    bullet_lines = re.findall(r'^- (.+)$', full_match, re.MULTILINE)

    # Deduplicate while preserving order
    seen = set()
    unique_apps = []
    for app in bullet_lines:
        # Normalize the app name to check for duplicates
        app_normalized = app.lower().strip()
        if app_normalized and app_normalized not in seen:
            seen.add(app_normalized)
            unique_apps.append(app)

    # Build new section
    result = "**Tech Stack:**\n"
    for app in unique_apps:
        result += f"- {app}\n"

    return result

# Pattern that matches both Target Apps Found and Other Notable Apps sections
# This pattern looks for both sections and captures everything between them and after
pattern = r'\*\*Target Apps Found:\*\*\n((?:- [^\n]+\n)*)\n?\*\*Other Notable Apps:\*\*\n((?:- [^\n]+\n)*)'

# Replace both sections with combined Tech Stack
content = re.sub(pattern, combine_sections, content)

# Also handle cases where only "Target Apps Found" exists (no Other Notable Apps)
# Replace standalone "**Target Apps Found:**" with "**Tech Stack:**"
content = re.sub(r'\*\*Target Apps Found:\*\*', '**Tech Stack:**', content)

# Replace any remaining "**Other Notable Apps:**" with nothing (already combined above)
# This catches edge cases
content = re.sub(r'\n\*\*Other Notable Apps:\*\*\n', '\n', content)

# Count changes
sections_found = content.count('**Tech Stack:**')

print(f"✓ Combined sections into Tech Stack")
print(f"  Total Tech Stack sections: {sections_found}")

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ Markdown file updated successfully!")
