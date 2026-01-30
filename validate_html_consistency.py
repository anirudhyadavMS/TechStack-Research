#!/usr/bin/env python3
"""
Validation Script: HTML Consistency Check
Verifies that HTML stat tiles match actual company data counts
"""
import json
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

print("="*80)
print("HTML CONSISTENCY VALIDATION")
print("="*80)

base_dir = r'C:\Users\anirudhyadav\Fortune500_TechStack_Research_2026'

# Read HTML
with open(os.path.join(base_dir, 'company_technology_stack_analysis.html'), 'r', encoding='utf-8') as f:
    html = f.read()

# Extract companies data
match = re.search(r'const companies = (\[.*?\]);', html, re.DOTALL)
if not match:
    print("❌ ERROR: Could not find companies array in HTML")
    sys.exit(1)

companies = json.loads(match.group(1))

print(f'\nHTML contains {len(companies)} companies\n')

# Count apps in HTML data
html_counts = {
    'Salesforce': sum(1 for c in companies if 'Salesforce' in c.get('apps', [])),
    'ServiceNow': sum(1 for c in companies if 'ServiceNow' in c.get('apps', [])),
    'Jira': sum(1 for c in companies if 'Jira' in c.get('apps', [])),
    'Confluence': sum(1 for c in companies if 'Confluence' in c.get('apps', [])),
    'Slack': sum(1 for c in companies if 'Slack' in c.get('apps', [])),
    'Gmail': sum(1 for c in companies if 'Gmail' in c.get('apps', [])),
    'Google Drive': sum(1 for c in companies if 'Google Drive' in c.get('apps', [])),
    'Gong': sum(1 for c in companies if 'Gong' in c.get('apps', [])),
    'Dropbox': sum(1 for c in companies if 'Dropbox' in c.get('apps', [])),
    'Box': sum(1 for c in companies if 'Box' in c.get('apps', [])),
}

# Extract stat tiles
tiles = {}
tile_ids = ['salesforce', 'servicenow', 'jira', 'slack']
for tile_id in tile_ids:
    tile_match = re.search(rf'id="{tile_id}-count">(\d+)<', html)
    if tile_match:
        app_name = tile_id.replace('servicenow', 'ServiceNow').title()
        if tile_id == 'servicenow':
            app_name = 'ServiceNow'
        elif tile_id == 'salesforce':
            app_name = 'Salesforce'
        elif tile_id == 'jira':
            app_name = 'Jira'
        elif tile_id == 'slack':
            app_name = 'Slack'
        tiles[app_name] = int(tile_match.group(1))

# Extract total from tiles
total_tile_match = re.search(r'<div class="stat-number">(\d+)</div>\s*<div class="stat-label">Companies</div>', html)
if total_tile_match:
    total_tile = int(total_tile_match.group(1))
else:
    total_tile = None

print('Stat Tiles vs Actual Data:')
print('-' * 80)

all_match = True

# Check total companies
if total_tile:
    if total_tile == len(companies):
        print(f'✓ Total Companies: {total_tile} (matches)')
    else:
        print(f'❌ Total Companies: Tile shows {total_tile} but data has {len(companies)}')
        all_match = False

# Check each app
for app in tiles.keys():
    if tiles[app] == html_counts[app]:
        print(f'✓ {app:20s}: {tiles[app]:3d} (matches)')
    else:
        print(f'❌ {app:20s}: Tile shows {tiles[app]:3d} but data has {html_counts[app]:3d}')
        all_match = False

# Show counts for apps not in tiles
print('\nOther Target Apps (not in stat tiles):')
print('-' * 80)
other_apps = ['Confluence', 'Gmail', 'Google Drive', 'Gong', 'Dropbox', 'Box']
for app in other_apps:
    if app in html_counts:
        print(f'  {app:20s}: {html_counts[app]:3d}')

print('\n' + '='*80)
if all_match:
    print('✅ ALL CHECKS PASSED - Stat tiles match actual data')
    print('\nThe dashboard is consistent and ready to use.')
else:
    print('❌ VALIDATION FAILED - Stat tiles do not match data')
    print('\nRecommended actions:')
    print('  1. Run: python fix_stat_tiles_final.py')
    print('  2. Re-run this script to verify')
    print('  3. Open dashboard to confirm visually')
print('='*80)
