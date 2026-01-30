import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

print("Combining Target Applications and Other Technologies into Tech Stack...\n")

# Split by company sections
company_sections = re.split(r'(^## \d+\. )', content, flags=re.MULTILINE)

# Reconstruct content
new_content = company_sections[0] if company_sections[0] else ""  # Header before first company

# Process each company section
companies_updated = 0
for i in range(1, len(company_sections), 2):
    if i + 1 < len(company_sections):
        section_header = company_sections[i]  # "## 1. "
        section_content = company_sections[i + 1]

        # Check if this section has both Target Apps and Other Notable Apps
        has_target = '**Target Apps Found:**' in section_content or '**Tech Stack:**' in section_content
        has_other = '**Other Notable Apps:**' in section_content

        if has_target or has_other:
            # Extract all apps from both sections
            all_apps = []

            # Find Target Apps section
            target_match = re.search(r'\*\*Target Apps Found:\*\*\n(.*?)(?=\n\*\*|\n---|\n###|$)', section_content, re.DOTALL)
            if target_match:
                target_text = target_match.group(1)
                # Extract bullet points
                target_bullets = re.findall(r'^- (.+)$', target_text, re.MULTILINE)
                all_apps.extend(target_bullets)

            # Find Other Notable Apps section
            other_match = re.search(r'\*\*Other Notable Apps:\*\*\n(.*?)(?=\n---|\n###|$)', section_content, re.DOTALL)
            if other_match:
                other_text = other_match.group(1)
                # Extract bullet points
                other_bullets = re.findall(r'^- (.+)$', other_text, re.MULTILINE)
                all_apps.extend(other_bullets)

            if all_apps:
                # Create new Tech Stack section
                tech_stack = "**Tech Stack:**\n"
                for app in all_apps:
                    tech_stack += f"- {app}\n"

                # Remove old sections and replace with Tech Stack
                section_content = re.sub(
                    r'\*\*Target Apps Found:\*\*\n.*?(?=\n\*\*Other Notable Apps:\*\*|\n---|\n###|$)',
                    tech_stack,
                    section_content,
                    flags=re.DOTALL
                )

                # Remove Other Notable Apps section
                section_content = re.sub(
                    r'\n\*\*Other Notable Apps:\*\*\n.*?(?=\n---|\n###|$)',
                    '',
                    section_content,
                    flags=re.DOTALL
                )

                companies_updated += 1

        new_content += section_header + section_content

print(f"✓ Updated {companies_updated} company sections")

# Save
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✓ Markdown file updated successfully!")
