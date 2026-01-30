#!/usr/bin/env python3
"""
Consolidate Batches 22-31 (Companies 302-401) into Markdown
Complete research data from all 10 agent batches
"""
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

print("="*80)
print("CONSOLIDATING BATCHES 22-31 INTO MARKDOWN (Companies 302-401)")
print("="*80)

# Complete research data from all 10 batches compiled from agent outputs
all_research = """
## 302. Altria Group

**Tech Stack:**

Target Apps:
- **Salesforce**: NOT CONFIRMED
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- Oracle
- SAP
- Microsoft Office
- Workday

**Sources:**
- https://www.appsruntheworld.com/customers-database/customers/view/alcoa-corporation-united-states

## 303. Edison International

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- Palantir Foundry
- MicroStrategy
- Rackspace Cloud

**Sources:**
- https://www.cloudcreations.com/ongoing-salesforce-solutions-cal-edison/

## 304. KeyCorp

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- Google Cloud Platform
- Kubernetes
- Oracle
- Workday

**Sources:**
- https://www.americanbanker.com/news/keybank-moves-more-applications-to-google-cloud

## 305. Alcoa

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- Oracle
- SAP
- Microsoft Power BI
- Workday

**Sources:**
- https://alcoa.wd5.myworkdayjobs.com/Careers

## 306. Boston Scientific

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: ✓
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- SAP S/4 HANA
- Workday
- Microsoft Dynamics 365

**Sources:**
- https://www.salesforce.com/plus/experience/world_tour/series/best_of_world_tour_boston_2024/episode/episode-s1e8

## 307. DaVita

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: ✓
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- VMware Cloud
- AWS
- Azure

**Sources:**
- https://enlyft.com/tech/company/davita.com

## 308. PPL Corporation

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- Microsoft Azure
- Microsoft 365
- MicroStrategy

**Sources:**
- https://www.appsruntheworld.com/customers-database/customers/view/ppl-electric-utilities-usa

## 309. Hasbro

**Tech Stack:**

Target Apps:
- **Salesforce**: NOT CONFIRMED
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- Microsoft Azure
- Azure DevOps
- GitHub
- SAP PLM

**Sources:**
- https://jobs.hasbro.com/

## 310. Omnicom Group

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- AWS
- Microsoft Azure
- Google Cloud Platform

**Sources:**
- https://aws.amazon.com/solutions/case-studies/omnicom-case-study/

## 311. Ross Stores

**Tech Stack:**

Target Apps:
- **Salesforce**: NOT CONFIRMED
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- Oracle
- VMware
- MicroStrategy

**Sources:**
- https://www.appsruntheworld.com/customers-database/customers/view/ross-stores-inc-united-states

## 312. United Airlines Holdings

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: ✓
- **Jira**: ✓
- **Confluence**: ✓
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- AWS
- Atlassian Cloud
- Docusign

**Sources:**
- https://www.servicenow.com/community/knowledge-blog/united-airlines-expanding-the-employee-experience-beyond-hr/ba-p/2331367

## 313. Domino's Pizza

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- Microsoft Azure
- AWS
- Microsoft Dynamics 365

**Sources:**
- https://ir.dominos.com/news-releases/news-release-details/dominosr-and-microsoft-cook-ai-driven-innovation-alliance

## 314. Hilton Worldwide

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: ✓
- **Jira**: ✓
- **Confluence**: ✓
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- AWS
- Oracle HCM Cloud

**Sources:**
- https://www.whereoware.com/work/hotel-customer-service-platform-reduces-training-80

## 315. Alaska Air Group

**Tech Stack:**

Target Apps:
- **Salesforce**: NOT CONFIRMED
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- Microsoft Azure
- Microsoft 365
- GitHub

**Sources:**
- https://news.microsoft.com/source/features/digital-transformation/how-alaska-airlines-uses-technology

## 316. S&P Global

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- Workday

**Sources:**
- https://careers.spglobal.com/jobs/323672

## 317. Clorox

**Tech Stack:**

Target Apps:
- **Salesforce**: NOT CONFIRMED
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- Workday
- SAP S/4HANA Cloud

**Sources:**
- https://www.constellationr.com/blog-news/insights/clorox-go-live-new-sap-erp-system

## 318. Campbell Soup

**Tech Stack:**

Target Apps:
- **Salesforce**: NOT CONFIRMED
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- Microsoft Azure
- AWS
- SAP HANA

**Sources:**
- https://www.microsoft.com/en/customers/story/862081-campbell-soup-company-consumer-goods-azure

## 319. Dr Pepper Snapple Group

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: ✓
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- SAP
- Workday
- Google Cloud Platform

**Sources:**
- https://www.sap.com/documents/2025/03/aa905017-fc7e-0010-bca6-c68f7e60039b.html

## 320. AutoNation

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- CDK Global DMS

**Sources:**
- https://www.salary.com/research/salary/employer/autonation-inc/customer-relationship-crm-supervisor-salesforce-salary

## 321. T-Mobile US

**Tech Stack:**

Target Apps:
- **Salesforce**: ✓
- **ServiceNow**: NOT CONFIRMED
- **Jira**: NOT CONFIRMED
- **Confluence**: NOT CONFIRMED
- **Slack**: NOT CONFIRMED
- **Gmail**: NOT CONFIRMED
- **Google Drive**: NOT CONFIRMED
- **Gong**: NOT CONFIRMED
- **Dropbox**: NOT CONFIRMED
- **Box**: NOT CONFIRMED

Other Technologies:
- AWS
- Google Cloud
- Microsoft Azure
- Microsoft 365

**Sources:**
- https://www.ibm.com/services/client-stories/t-mobile

"""

# Note: The script will be continued in parts due to length
# Save current portion
with open('batches_22_31_part1.txt', 'w', encoding='utf-8') as f:
    f.write(all_research)

print("✓ Created research data part 1 (companies 302-321)")
print("  Total: 20 companies")
print("\nNote: Due to data volume, will process in chunks")
print("="*80)
