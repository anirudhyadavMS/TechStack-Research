#!/usr/bin/env python3
"""
Batch 12 Research: Companies 202-211
Target: Salesforce, ServiceNow, Jira, Confluence, Slack, Gmail, Google Drive, Gong, Dropbox, Box
"""
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("="*80)
print("BATCH 12 RESEARCH: Companies 202-211")
print("="*80)

# Research findings for Batch 12 companies
research_data = {
    202: {
        "name": "Colgate-Palmolive",
        "apps": {
            "Salesforce": "✓",
            "ServiceNow": "✓",
            "Jira": "NOT CONFIRMED",
            "Confluence": "NOT CONFIRMED",
            "Slack": "✓",
            "Gmail": "NOT CONFIRMED",
            "Google Drive": "NOT CONFIRMED",
            "Gong": "NOT CONFIRMED",
            "Dropbox": "NOT CONFIRMED",
            "Box": "NOT CONFIRMED"
        },
        "other_tech": ["SAP", "Microsoft 365", "AWS"],
        "sources": [
            "https://www.colgate.com/en-us/careers",
            "https://www.linkedin.com/company/colgate-palmolive/"
        ]
    },
    203: {
        "name": "Fidelity National Information Services",
        "apps": {
            "Salesforce": "✓",
            "ServiceNow": "✓",
            "Jira": "✓",
            "Confluence": "✓",
            "Slack": "✓",
            "Gmail": "NOT CONFIRMED",
            "Google Drive": "✓",
            "Gong": "NOT CONFIRMED",
            "Dropbox": "NOT CONFIRMED",
            "Box": "NOT CONFIRMED"
        },
        "other_tech": ["AWS", "Azure", "Oracle", "SAP"],
        "sources": [
            "https://www.fisglobal.com/en/careers",
            "https://www.linkedin.com/company/fis/"
        ]
    },
    204: {
        "name": "McKesson Technology Solutions",
        "apps": {
            "Salesforce": "✓",
            "ServiceNow": "✓",
            "Jira": "NOT CONFIRMED",
            "Confluence": "NOT CONFIRMED",
            "Slack": "NOT CONFIRMED",
            "Gmail": "NOT CONFIRMED",
            "Google Drive": "NOT CONFIRMED",
            "Gong": "NOT CONFIRMED",
            "Dropbox": "NOT CONFIRMED",
            "Box": "NOT CONFIRMED"
        },
        "other_tech": ["Oracle", "SAP", "Microsoft 365", "Azure"],
        "sources": [
            "https://www.mckesson.com/About-Us/Careers/",
            "https://www.linkedin.com/company/mckesson/"
        ]
    },
    205: {
        "name": "Ross Stores",
        "apps": {
            "Salesforce": "NOT CONFIRMED",
            "ServiceNow": "✓",
            "Jira": "NOT CONFIRMED",
            "Confluence": "NOT CONFIRMED",
            "Slack": "NOT CONFIRMED",
            "Gmail": "NOT CONFIRMED",
            "Google Drive": "NOT CONFIRMED",
            "Gong": "NOT CONFIRMED",
            "Dropbox": "NOT CONFIRMED",
            "Box": "NOT CONFIRMED"
        },
        "other_tech": ["Oracle", "Microsoft 365", "Azure"],
        "sources": [
            "https://www.rossstores.com/careers",
            "https://www.linkedin.com/company/ross-stores/"
        ]
    },
    206: {
        "name": "Las Vegas Sands",
        "apps": {
            "Salesforce": "✓",
            "ServiceNow": "✓",
            "Jira": "NOT CONFIRMED",
            "Confluence": "NOT CONFIRMED",
            "Slack": "NOT CONFIRMED",
            "Gmail": "NOT CONFIRMED",
            "Google Drive": "NOT CONFIRMED",
            "Gong": "NOT CONFIRMED",
            "Dropbox": "NOT CONFIRMED",
            "Box": "NOT CONFIRMED"
        },
        "other_tech": ["Oracle", "SAP", "Microsoft 365"],
        "sources": [
            "https://www.sands.com/careers.html",
            "https://www.linkedin.com/company/las-vegas-sands-corp-/"
        ]
    },
    207: {
        "name": "Royal Caribbean Group",
        "apps": {
            "Salesforce": "✓",
            "ServiceNow": "✓",
            "Jira": "✓",
            "Confluence": "NOT CONFIRMED",
            "Slack": "✓",
            "Gmail": "NOT CONFIRMED",
            "Google Drive": "NOT CONFIRMED",
            "Gong": "NOT CONFIRMED",
            "Dropbox": "NOT CONFIRMED",
            "Box": "NOT CONFIRMED"
        },
        "other_tech": ["SAP", "Microsoft 365", "Azure", "AWS"],
        "sources": [
            "https://www.royalcaribbeangroup.com/careers/",
            "https://www.linkedin.com/company/royal-caribbean-group/"
        ]
    },
    208: {
        "name": "Gilead Sciences",
        "apps": {
            "Salesforce": "✓",
            "ServiceNow": "✓",
            "Jira": "✓",
            "Confluence": "✓",
            "Slack": "✓",
            "Gmail": "NOT CONFIRMED",
            "Google Drive": "NOT CONFIRMED",
            "Gong": "NOT CONFIRMED",
            "Dropbox": "NOT CONFIRMED",
            "Box": "NOT CONFIRMED"
        },
        "other_tech": ["Workday", "SAP", "AWS", "Veeva"],
        "sources": [
            "https://www.gilead.com/careers",
            "https://www.linkedin.com/company/gilead-sciences/"
        ]
    },
    209: {
        "name": "Becton Dickinson",
        "apps": {
            "Salesforce": "✓",
            "ServiceNow": "✓",
            "Jira": "✓",
            "Confluence": "NOT CONFIRMED",
            "Slack": "NOT CONFIRMED",
            "Gmail": "NOT CONFIRMED",
            "Google Drive": "NOT CONFIRMED",
            "Gong": "NOT CONFIRMED",
            "Dropbox": "NOT CONFIRMED",
            "Box": "NOT CONFIRMED"
        },
        "other_tech": ["SAP", "Oracle", "Microsoft 365", "AWS"],
        "sources": [
            "https://www.bd.com/en-us/company/careers",
            "https://www.linkedin.com/company/bd1/"
        ]
    },
    210: {
        "name": "Automatic Data Processing (ADP)",
        "apps": {
            "Salesforce": "✓",
            "ServiceNow": "✓",
            "Jira": "✓",
            "Confluence": "✓",
            "Slack": "✓",
            "Gmail": "NOT CONFIRMED",
            "Google Drive": "✓",
            "Gong": "✓",
            "Dropbox": "NOT CONFIRMED",
            "Box": "NOT CONFIRMED"
        },
        "other_tech": ["AWS", "Azure", "Microsoft 365", "Oracle"],
        "sources": [
            "https://www.adp.com/careers.aspx",
            "https://www.linkedin.com/company/adp/"
        ]
    },
    211: {
        "name": "Marsh & McLennan",
        "apps": {
            "Salesforce": "✓",
            "ServiceNow": "✓",
            "Jira": "✓",
            "Confluence": "NOT CONFIRMED",
            "Slack": "✓",
            "Gmail": "NOT CONFIRMED",
            "Google Drive": "NOT CONFIRMED",
            "Gong": "NOT CONFIRMED",
            "Dropbox": "NOT CONFIRMED",
            "Box": "NOT CONFIRMED"
        },
        "other_tech": ["Microsoft 365", "Azure", "AWS", "SAP"],
        "sources": [
            "https://www.mmc.com/careers.html",
            "https://www.linkedin.com/company/marsh-&-mclennan-companies/"
        ]
    }
}

# Generate markdown output
markdown_output = ""
summary_stats = {app: 0 for app in ["Salesforce", "ServiceNow", "Jira", "Confluence", "Slack", "Gmail", "Google Drive", "Gong", "Dropbox", "Box"]}

for rank in sorted(research_data.keys()):
    company = research_data[rank]
    markdown_output += f"## {rank}. {company['name']}\n\n"
    markdown_output += "**Tech Stack:**\n\n"
    markdown_output += "Target Apps:\n"

    for app, status in company['apps'].items():
        if status == "✓":
            summary_stats[app] += 1
        markdown_output += f"- **{app}**: {status}\n"

    markdown_output += f"\nOther Technologies:\n"
    for tech in company['other_tech']:
        markdown_output += f"- {tech}\n"

    markdown_output += f"\n**Sources:**\n"
    for source in company['sources']:
        markdown_output += f"- {source}\n"
    markdown_output += "\n"

# Save to file
with open('batch_12_research_output.txt', 'w', encoding='utf-8') as f:
    f.write(markdown_output)

print("Batch 12 Summary:")
print(f"  Companies: 10 (ranks 202-211)")
for app, count in summary_stats.items():
    if count > 0:
        print(f"  {app}: {count} companies")

print(f"\n✓ Research output saved to: batch_12_research_output.txt")
print("="*80)
