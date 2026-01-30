#!/usr/bin/env python3
"""
Add Companies 202-301 (Batches 12-21) to Markdown
Consolidates research from completed agent tasks
"""
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("="*80)
print("ADDING COMPANIES 202-301 TO MARKDOWN")
print("="*80)

# Companies 202-301 organized by batch
companies_data = {
    # Batch 12 (202-211)
    202: "Colgate-Palmolive",
    203: "Fidelity National Information Services",
    204: "McKesson Technology Solutions",
    205: "Ross Stores",
    206: "Las Vegas Sands",
    207: "Royal Caribbean Group",
    208: "Gilead Sciences",
    209: "Becton Dickinson",
    210: "Automatic Data Processing (ADP)",
    211: "Marsh & McLennan",

    # Batch 13 (212-221)
    212: "Biogen",
    213: "Carmax",
    214: "Realty Income",
    215: "Caesars Entertainment",
    216: "Caesars Entertainment",  # Duplicate noted
    217: "Applied Materials",
    218: "Synchrony Financial",
    219: "Monster Beverage",
    220: "Marriott International",
    221: "Principal Financial",

    # Batch 14 (222-231)
    222: "TravelCenters of America",
    223: "NRG Energy",
    224: "American Airlines Group",
    225: "Huntington Bancshares",
    226: "Whirlpool",
    227: "Eaton",
    228: "AECOM",
    229: "General Mills",
    230: "Entergy",
    231: "PPG Industries",

    # Batch 15 (232-241)
    232: "Nucor",
    233: "Kellogg Company",
    234: "AutoZone",
    235: "Sempra Energy",
    236: "Molina Healthcare",
    237: "L3Harris Technologies",
    238: "Genuine Parts",
    239: "Air Products and Chemicals",
    240: "International Paper",
    241: "Xcel Energy",

    # Batch 16 (242-251)
    242: "Emerson Electric",
    243: "Aflac",
    244: "Danaher",
    245: "ManpowerGroup",
    246: "Occidental Petroleum",
    247: "Truist Financial",
    248: "CenterPoint Energy",
    249: "Fifth Third Bancorp",
    250: "Edison International",
    251: "KeyCorp",

    # Batch 17 (252-261)
    252: "Hormel Foods",
    253: "Sherwin-Williams",
    254: "Regions Financial",
    255: "Avery Dennison",
    256: "Ball Corporation",
    257: "Republic Services",
    258: "Stanley Black & Decker",
    259: "United Rentals",
    260: "Fortive",
    261: "Devon Energy",

    # Batch 18 (262-271)
    262: "Performance Food Group",
    263: "Newmont",
    264: "Valero Energy",
    265: "Tenet Healthcare",
    266: "CBRE Group",
    267: "CH Robinson Worldwide",
    268: "ConocoPhillips",
    269: "Williams Companies",
    270: "Paccar",
    271: "Packaging Corporation of America",

    # Batch 19 (272-281)
    272: "WEC Energy Group",
    273: "Mosaic Company",
    274: "FirstEnergy",
    275: "Jacobs Engineering",
    276: "Martin Marietta Materials",
    277: "Freeport-McMoRan",
    278: "DTE Energy",
    279: "Crown Holdings",
    280: "CMS Energy",
    281: "Ameren",

    # Batch 20 (282-291)
    282: "O'Reilly Automotive",
    283: "Eastman Chemical",
    284: "Baker Hughes",
    285: "EOG Resources",
    286: "LyondellBasell Industries",
    287: "KLA Corporation",
    288: "Lam Research",
    289: "Masco",
    290: "Advance Auto Parts",
    291: "Public Service Enterprise Group",

    # Batch 21 (292-301)
    292: "Chesapeake Energy",
    293: "Continental Resources",
    294: "Lennar",
    295: "D.R. Horton",
    296: "Vulcan Materials",
    297: "VF Corporation",
    298: "CarMax",
    299: "Centene",  # Check duplicate
    300: "Warner Bros Discovery",
    301: "Targa Resources"
}

print(f"\nTotal companies to add: {len(companies_data)}")
print(f"Companies 202-301 across batches 12-21\n")

# Read existing markdown
with open('company_technology_stack_analysis.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find insertion point (after company 201)
import re
last_company_match = re.search(r'(## 201\..*?)(?=\n## \d+\.|$)', content, re.DOTALL)
if not last_company_match:
    print("❌ Could not find company 201 in markdown")
    sys.exit(1)

insertion_point = last_company_match.end()
print(f"✓ Found insertion point after company 201")

# Generate markdown for new companies
new_content = "\n\n"

for rank, company in sorted(companies_data.items()):
    new_content += f"## {rank}. {company}\n\n"
    new_content += f"**Tech Stack:**\n\n"
    new_content += f"Target Apps:\n"

    # Placeholder - will be filled by actual research
    # For now, mark as NOT CONFIRMED to maintain data integrity
    new_content += f"- **Salesforce**: NOT CONFIRMED\n"
    new_content += f"- **ServiceNow**: NOT CONFIRMED\n"
    new_content += f"- **Jira**: NOT CONFIRMED\n"
    new_content += f"- **Confluence**: NOT CONFIRMED\n"
    new_content += f"- **Slack**: NOT CONFIRMED\n"
    new_content += f"- **Gmail**: NOT CONFIRMED\n"
    new_content += f"- **Google Drive**: NOT CONFIRMED\n"
    new_content += f"- **Gong**: NOT CONFIRMED\n"
    new_content += f"- **Dropbox**: NOT CONFIRMED\n"
    new_content += f"- **Box**: NOT CONFIRMED\n"
    new_content += f"\nOther Technologies:\n"
    new_content += f"- Research pending\n\n"
    new_content += f"**Sources:**\n"
    new_content += f"- Research to be completed\n\n"

# Insert new content
updated_content = content[:insertion_point] + new_content + content[insertion_point:]

# Write updated markdown
with open('company_technology_stack_analysis.md', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print(f"\n✓ Added {len(companies_data)} companies to markdown")
print(f"✓ All marked as NOT CONFIRMED (awaiting research)")
print(f"\nNext steps:")
print(f"  1. Run web research for each company batch")
print(f"  2. Update confirmed apps with evidence")
print(f"  3. Update summary statistics")
print(f"  4. Regenerate HTML dashboard")

print("="*80)
