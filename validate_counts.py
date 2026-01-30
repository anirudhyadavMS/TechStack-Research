#!/usr/bin/env python3
"""
Validation Script: Count Validation
Verifies that summary statistics match actual counts from markdown
"""
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("="*80)
print("MARKDOWN COUNT VALIDATION")
print("="*80)

with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Count company sections
companies = len(re.findall(r'^## \d+\.', content, re.MULTILINE))

# Count each target app (handle both formats: **App** ✓ and **App**: ✓)
apps = {
    'Salesforce': len(re.findall(r'\*\*Salesforce\*\*\s*:?\s*✓', content)),
    'ServiceNow': len(re.findall(r'\*\*ServiceNow\*\*\s*:?\s*✓', content)),
    'Jira': len(re.findall(r'\*\*Jira\*\*\s*:?\s*✓', content)),
    'Confluence': len(re.findall(r'\*\*Confluence\*\*\s*:?\s*✓', content)),
    'Slack': len(re.findall(r'\*\*Slack\*\*\s*:?\s*✓', content)),
    'Gmail': len(re.findall(r'\*\*Gmail\*\*\s*:?\s*✓', content)),
    'Google Drive': len(re.findall(r'\*\*Google Drive\*\*\s*:?\s*✓', content)),
    'Gong': len(re.findall(r'\*\*Gong\*\*\s*:?\s*✓', content)),
    'Dropbox': len(re.findall(r'\*\*Dropbox\*\*\s*:?\s*✓', content)),
    'Box': len(re.findall(r'\*\*Box\*\*\s*:?\s*✓', content)),
}

print(f'\nTotal Companies Found: {companies}\n')

print('Target App Counts (from actual data):')
print('-' * 80)
for app, count in apps.items():
    print(f'  {app:20s}: {count:3d}')

# Extract summary stats and compare
print('\n' + '='*80)
print('SUMMARY SECTION VALIDATION')
print('='*80)

summary_match = re.search(r'Summary Statistics.*?(\d+) Fortune 500 Companies', content, re.DOTALL)
summary_total = None
if summary_match:
    summary_total = int(summary_match.group(1))
    if summary_total != companies:
        print(f'\n❌ MISMATCH: Summary says {summary_total} companies but found {companies} company sections')
        print(f'   ACTION: Update summary to show {companies} companies')
    else:
        print(f'\n✓ Total Companies: {companies} (matches summary)')

# Check each app in summary
all_match = True
for app, actual_count in apps.items():
    pattern = rf'\*\*{re.escape(app)}\*\*: (\d+) companies'
    match = re.search(pattern, content)
    if match:
        summary_count = int(match.group(1))
        if summary_count != actual_count:
            print(f'❌ {app}: Summary shows {summary_count} but actual count is {actual_count}')
            all_match = False
        else:
            print(f'✓ {app}: {actual_count}')
    else:
        print(f'⚠️  {app}: Not found in summary section')
        all_match = False

print('\n' + '='*80)
if all_match and summary_total == companies:
    print('✅ ALL CHECKS PASSED - Summary matches actual data')
else:
    print('❌ VALIDATION FAILED - Summary needs to be updated')
    print('\nRecommended actions:')
    print('  1. Update summary section to match actual counts above')
    print('  2. Re-run this script to verify')
    print('  3. Regenerate HTML after fixing summary')
print('='*80)
