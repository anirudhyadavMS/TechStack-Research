import re
import json
import sys
import os

base_dir = r'C:\Users\anirudhyadav\Fortune500_TechStack_Research_2026'

# Read the updated markdown
with open(os.path.join(base_dir, 'company_technology_stack_analysis.md'), 'r', encoding='utf-8') as f:
    content = f.read()

# Parse companies
companies = []
company_sections = re.split(r'^## \d+\. ', content, flags=re.MULTILINE)[1:]

for section in company_sections:
    lines = section.split('\n')
    company_name = lines[0].strip()

    # Skip summary and other non-company sections
    if 'SUMMARY' in company_name.upper() or 'FORTUNE 100' in company_name.upper() or 'DATA LIMITATIONS' in company_name.upper():
        continue

    # Extract apps
    apps = []
    target_apps = [
        'Salesforce', 'ServiceNow', 'Jira', 'Confluence', 'Slack',
        'Gmail', 'Google Drive', 'Gong', 'Dropbox', 'Box',
        # Additional apps from 3P connectors promoted to target apps
        'Azure DevOps Work Items', 'Aha', 'Azure SQL', 'FileShare', 'GitHub'
    ]

    company_text = '\n'.join(lines[:100])  # Check first 100 lines

    for app in target_apps:
        # Look for bold app name with checkmark pattern: **AppName** ✓ or **AppName**: ✓
        bold_pattern = r'\*\*' + re.escape(app) + r'\*\*\s*:?\s*✓'
        if re.search(bold_pattern, company_text):
            # Found **App** ✓ or **App**: ✓ pattern, now check it's not negated
            matches = re.finditer(bold_pattern, company_text)
            for match in matches:
                match_pos = match.start()
                # Get only the line containing this match to check for negation
                line_start = company_text.rfind('\n', 0, match_pos) + 1
                line_end = company_text.find('\n', match_pos)
                if line_end == -1:
                    line_end = len(company_text)
                line_context = company_text[line_start:line_end]

                # Check for negative indicators on the SAME LINE only
                is_not_used = any(x in line_context for x in ['NOT USED', 'NOT CONFIRMED', 'NO EVIDENCE', '❌', '✗', 'NOT FOR'])

                if not is_not_used:
                    if app not in apps:  # Avoid duplicates
                        apps.append(app)
                    break

    # Extract other notable apps
    other_apps = []
    if 'Microsoft 365' in company_text or 'Azure' in company_text:
        other_apps.append('Microsoft 365/Azure')
    if 'AWS' in company_text:
        other_apps.append('AWS')
    if 'SAP' in company_text:
        other_apps.append('SAP')
    if 'Google Cloud' in company_text:
        other_apps.append('Google Cloud')
    if 'Workday' in company_text:
        other_apps.append('Workday')
    if 'Oracle' in company_text:
        other_apps.append('Oracle')

    # Extract 3P Connectors
    connectors_3p = []
    if '### 3P Connectors' in company_text:
        # Find the section
        connectors_start = company_text.find('### 3P Connectors')
        # Find the end of this section (next ### or end)
        next_section_match = re.search(r'\n###[^#]', company_text[connectors_start + 10:])
        if next_section_match:
            connectors_end = connectors_start + 10 + next_section_match.start()
        else:
            connectors_end = connectors_start + 1000

        connectors_section = company_text[connectors_start:connectors_end]

        # Extract apps from bullet points (- **AppName**)
        connector_matches = re.findall(r'-\s+\*\*([^*]+)\*\*', connectors_section)
        connectors_3p = [c.strip() for c in connector_matches]

    # Combine apps and other_apps into single tech_stack list
    tech_stack = []

    # Add target apps (marked with checkmarks)
    for app in apps:
        tech_stack.append({'name': app, 'is_target': True})

    # Add other apps
    for app in other_apps:
        if app not in apps:  # Avoid duplicates
            tech_stack.append({'name': app, 'is_target': False})

    companies.append({
        'name': company_name,
        'apps': apps,  # Keep for backward compatibility/stats
        'other_apps': other_apps,  # Keep for backward compatibility
        'tech_stack': tech_stack,
        'connectors_3p': connectors_3p
    })

print(f"Parsed {len(companies)} companies")

# Extract actual statistics from markdown
import re
stats_match = re.search(r'Summary Statistics \(Updated: (\d+) Companies\)', content)
total_companies = int(stats_match.group(1)) if stats_match else len(companies)

salesforce_match = re.search(r'\*\*Salesforce\*\*: (\d+) companies', content)
servicenow_match = re.search(r'\*\*ServiceNow\*\*: (\d+) companies', content)
jira_match = re.search(r'\*\*Jira\*\*: (\d+) companies', content)
confluence_match = re.search(r'\*\*Confluence\*\*: (\d+) companies', content)
slack_match = re.search(r'\*\*Slack\*\*: (\d+) companies', content)

salesforce_count = int(salesforce_match.group(1)) if salesforce_match else 80
servicenow_count = int(servicenow_match.group(1)) if servicenow_match else 75
jira_count = int(jira_match.group(1)) if jira_match else 38
slack_count = int(slack_match.group(1)) if slack_match else 25

print(f"Statistics from markdown: {total_companies} companies total")
print(f"  Salesforce: {salesforce_count}, ServiceNow: {servicenow_count}")
print(f"  Jira: {jira_count}, Slack: {slack_count}")

# Generate HTML
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Company Technology Stack Analysis - {total_companies} Companies (2026)</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}

        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}

        h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}

        .subtitle {{
            font-size: 1.2em;
            opacity: 0.9;
        }}

        .stats-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}

        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }}

        .stat-card:hover {{
            transform: translateY(-5px);
        }}

        .stat-number {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
        }}

        .stat-label {{
            font-size: 0.9em;
            color: #666;
            text-transform: uppercase;
        }}

        .controls {{
            padding: 30px;
            background: #f8f9fa;
        }}

        .search-box {{
            width: 100%;
            padding: 15px;
            font-size: 16px;
            border: 2px solid #ddd;
            border-radius: 10px;
            margin-bottom: 20px;
        }}

        .search-box:focus {{
            outline: none;
            border-color: #667eea;
        }}

        .filter-group {{
            margin-top: 15px;
        }}

        .filter-dropdown {{
            width: 100%;
            padding: 15px;
            font-size: 16px;
            border: 2px solid #ddd;
            border-radius: 10px;
            background: white;
            cursor: pointer;
            transition: border-color 0.3s;
        }}

        .filter-dropdown:hover {{
            border-color: #667eea;
        }}

        .filter-dropdown:focus {{
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }}

        .companies-grid {{
            padding: 30px;
            display: grid;
            gap: 20px;
        }}

        .company-card {{
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 20px;
        }}

        .company-name {{
            font-size: 1.5em;
            font-weight: bold;
            color: #333;
            margin-bottom: 15px;
        }}

        .apps-section {{
            margin-bottom: 15px;
        }}

        .section-title {{
            font-size: 0.85em;
            color: #666;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}

        .app-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}

        .app-tag {{
            padding: 6px 12px;
            background: #e7f3ff;
            color: #0066cc;
            border-radius: 5px;
            font-size: 0.85em;
        }}

        .app-tag.target {{
            background: #e7f3ff;
            color: #0066cc;
            font-weight: 500;
        }}

        .app-tag.other {{
            background: #f0f0f0;
            color: #666;
        }}

        .app-tag.connector {{
            background: #e8f5e9;
            color: #2e7d32;
            border: 1px solid #4caf50;
        }}

        .results-count {{
            padding: 20px 30px;
            background: #f8f9fa;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Fortune 500 Technology Stack Analysis</h1>
            <div class="subtitle">Comprehensive research of {total_companies} companies - 2026</div>
        </header>

        <div class="stats-container">
            <div class="stat-card">
                <div class="stat-number">{total_companies}</div>
                <div class="stat-label">Companies</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="salesforce-count">{salesforce_count}</div>
                <div class="stat-label">Salesforce</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="servicenow-count">{servicenow_count}</div>
                <div class="stat-label">ServiceNow</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="jira-count">{jira_count}</div>
                <div class="stat-label">Jira</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="slack-count">{slack_count}</div>
                <div class="stat-label">Slack</div>
            </div>
        </div>

        <div class="controls">
            <input type="text" class="search-box" id="search" placeholder="Search companies...">

            <div class="section-title">Filter by App</div>
            <div class="filter-group">
                <select class="filter-dropdown" id="app-filter">
                    <option value="all">All Companies</option>
                </select>
            </div>
        </div>

        <div class="results-count" id="results-count"></div>

        <div class="companies-grid" id="companies-container"></div>
    </div>

    <script>
        const companies = {json.dumps(companies, ensure_ascii=False)};

        let currentFilter = 'all';
        let searchTerm = '';

        // Calculate app counts
        function calculateAppCounts() {{
            const appCounts = {{}};

            companies.forEach(company => {{
                [...company.apps, ...company.other_apps].forEach(app => {{
                    appCounts[app] = (appCounts[app] || 0) + 1;
                }});
            }});

            return appCounts;
        }}

        // Initialize dropdown with app counts
        function initializeDropdown() {{
            const dropdown = document.getElementById('app-filter');
            const appCounts = calculateAppCounts();

            // Define target apps in priority order
            const targetApps = [
                'Salesforce',
                'ServiceNow',
                'Jira',
                'Confluence',
                'Slack',
                'Gmail',
                'Google Drive',
                'Box',
                'Gong',
                'Dropbox'
            ];

            // Add target apps first
            targetApps.forEach(app => {{
                if (appCounts[app]) {{
                    const option = document.createElement('option');
                    option.value = app;
                    option.textContent = `${{app}} (${{appCounts[app]}} companies)`;
                    dropdown.appendChild(option);
                }}
            }});

            // Add separator
            const separator = document.createElement('option');
            separator.disabled = true;
            separator.textContent = '─────────────────────';
            dropdown.appendChild(separator);

            // Add other apps sorted by count
            const otherApps = Object.entries(appCounts)
                .filter(([app]) => !targetApps.includes(app))
                .sort((a, b) => b[1] - a[1]);

            otherApps.forEach(([app, count]) => {{
                const option = document.createElement('option');
                option.value = app;
                option.textContent = `${{app}} (${{count}} companies)`;
                dropdown.appendChild(option);
            }});
        }}

        function filterCompanies() {{
            return companies.filter(company => {{
                const techStackNames = company.tech_stack ? company.tech_stack.map(item => item.name) : [];
                const matchesFilter = currentFilter === 'all' ||
                                      techStackNames.includes(currentFilter) ||
                                      company.apps.includes(currentFilter) ||
                                      company.other_apps.includes(currentFilter);
                const matchesSearch = searchTerm === '' ||
                                      company.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                                      techStackNames.some(app => app.toLowerCase().includes(searchTerm.toLowerCase()));
                return matchesFilter && matchesSearch;
            }});
        }}

        function renderCompanies() {{
            const filtered = filterCompanies();
            const container = document.getElementById('companies-container');
            const resultsCount = document.getElementById('results-count');

            resultsCount.textContent = `Showing ${{filtered.length}} of ${{companies.length}} companies`;

            container.innerHTML = filtered.map(company => `
                <div class="company-card">
                    <div class="company-name">${{company.name}}</div>
                    ${{company.tech_stack && company.tech_stack.length > 0 ? `
                        <div class="apps-section">
                            <div class="section-title">Tech Stack</div>
                            <div class="app-tags">
                                ${{company.tech_stack.map(item =>
                                    `<div class="app-tag ${{item.is_target ? 'target' : 'other'}}">${{item.name}}</div>`
                                ).join('')}}
                            </div>
                        </div>
                    ` : ''}}
                </div>
            `).join('');
        }}

        // Event listeners
        document.getElementById('search').addEventListener('input', (e) => {{
            searchTerm = e.target.value;
            renderCompanies();
        }});

        document.getElementById('app-filter').addEventListener('change', (e) => {{
            currentFilter = e.target.value;
            renderCompanies();
        }});

        // Initialize
        initializeDropdown();
        renderCompanies();
    </script>
</body>
</html>'''

# Save HTML
with open(os.path.join(base_dir, 'company_technology_stack_analysis.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully created HTML with {len(companies)} companies!")
