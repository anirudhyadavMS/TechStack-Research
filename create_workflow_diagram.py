import sys

# Try to use matplotlib and other visualization libraries
try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
    import matplotlib.lines as mlines
except ImportError:
    print("Installing matplotlib...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "matplotlib", "--quiet"])
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
    import matplotlib.lines as mlines

# Create figure
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(5, 11.5, 'Fortune 500 Tech Stack Research - Update Chain of Thought',
        fontsize=18, fontweight='bold', ha='center')

# Define colors
color_start = '#4CAF50'
color_process = '#2196F3'
color_decision = '#FF9800'
color_complete = '#9C27B0'

# Helper function to create boxes
def create_box(ax, x, y, width, height, text, color, text_size=10):
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                          boxstyle="round,pad=0.1",
                          edgecolor='black', facecolor=color,
                          linewidth=2, alpha=0.8)
    ax.add_patch(box)
    ax.text(x, y, text, fontsize=text_size, ha='center', va='center',
            weight='bold', wrap=True)

# Helper function to create arrows
def create_arrow(ax, x1, y1, x2, y2):
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=20,
                           linewidth=2, color='black')
    ax.add_patch(arrow)

# Step 1: Initial State
create_box(ax, 5, 10.5, 3, 0.6, 'START:\n201 Companies Analyzed', color_start)
create_arrow(ax, 5, 10.2, 5, 9.6)

# Step 2: Added 3P Connectors
create_box(ax, 5, 9.3, 3.5, 0.8,
           'STEP 1: Added 3P Connectors\n(Microsoft Copilot)\n5 companies',
           color_process, 9)
ax.text(7.8, 9.3, '📊 Excel\nData', fontsize=8, ha='left',
        bbox=dict(boxstyle='round', facecolor='lightyellow'))
create_arrow(ax, 5, 8.9, 5, 8.3)

# Step 3: Replace Google Cloud
create_box(ax, 5, 8.0, 3.5, 0.8,
           'STEP 2: Replace Google Cloud\nwith Gmail & Google Drive\n42→35 mentions',
           color_process, 9)
ax.text(7.8, 8.0, '🔄 Better\nGranularity', fontsize=8, ha='left',
        bbox=dict(boxstyle='round', facecolor='lightyellow'))
create_arrow(ax, 5, 7.6, 5, 7.0)

# Step 4: Decision Point
create_box(ax, 5, 6.7, 3.5, 0.8,
           'DECISION: Remove 3P Connectors\nPromote to Target Apps',
           color_decision, 9)
create_arrow(ax, 5, 6.3, 5, 5.7)

# Step 5: Update Target Apps
create_box(ax, 5, 5.4, 3.5, 1.0,
           'STEP 3: Update Target Apps\nQualcomm: +2 apps\nEY: +3 apps\nKoch: +3 apps\nLTI & Wells Fargo: Remove 3P',
           color_process, 8.5)
ax.text(7.8, 5.4, '✅ 5 companies\nupdated', fontsize=8, ha='left',
        bbox=dict(boxstyle='round', facecolor='lightyellow'))
create_arrow(ax, 5, 4.9, 5, 4.3)

# Step 6: Consolidate Sections
create_box(ax, 5, 4.0, 3.5, 0.8,
           'STEP 4: Combine Sections\nTarget Apps + Other → Tech Stack\n34 companies',
           color_process, 9)
ax.text(7.8, 4.0, '🎯 Unified\nView', fontsize=8, ha='left',
        bbox=dict(boxstyle='round', facecolor='lightyellow'))
create_arrow(ax, 5, 3.6, 5, 3.0)

# Step 7: Final State
create_box(ax, 5, 2.5, 3.5, 1.0,
           'FINAL STATE:\n✓ No 3P Connectors\n✓ Gmail/Drive instead of Google Cloud\n✓ Single Tech Stack section\n✓ 15 target apps tracked',
           color_complete, 9)

# Stats boxes on the side
stats_y = 8.5
create_box(ax, 1.5, stats_y, 2, 1.5,
           'BEFORE:\n\n2 Sections:\n• Target Apps\n• Other Apps\n\n8 Target Apps',
           '#FFCDD2', 9)

create_box(ax, 1.5, stats_y - 2.5, 2, 1.5,
           'AFTER:\n\n1 Section:\n• Tech Stack\n  (unified)\n\n15 Target Apps',
           '#C8E6C9', 9)

# Impact metrics
create_box(ax, 8.5, 8.5, 2, 1.5,
           'IMPACT:\n\n✓ Cleaner UI\n✓ Better tracking\n✓ More apps\n✓ Simplified',
           '#E1BEE7', 9)

create_box(ax, 8.5, 6, 2, 1.5,
           'FILES:\n\n📄 MD: 161KB\n🌐 HTML: 21KB\n📋 5 Updates\n📊 Documentation',
           '#FFF9C4', 8.5)

# Legend
legend_y = 1.2
legend_elements = [
    mpatches.Patch(color=color_start, label='Start/End State'),
    mpatches.Patch(color=color_process, label='Process Steps'),
    mpatches.Patch(color=color_decision, label='Decision Points'),
    mpatches.Patch(color=color_complete, label='Completion')
]
ax.legend(handles=legend_elements, loc='lower center', ncol=4,
          bbox_to_anchor=(0.5, -0.05), frameon=True, fontsize=9)

# Add timeline at bottom
ax.text(5, 0.3, 'Timeline: Session Date - January 28, 2026',
        fontsize=10, ha='center', style='italic')

plt.tight_layout()
plt.savefig('workflow_chain_of_thought.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
print("✓ Workflow diagram created: workflow_chain_of_thought.png")
print("  Resolution: 300 DPI")
print("  Size: ~14x10 inches")

# Create a simpler Mermaid diagram as well
mermaid_diagram = """
# Fortune 500 Tech Stack Research - Chain of Thought

```mermaid
flowchart TD
    Start([START: 201 Companies<br/>Analyzed]) --> Step1

    Step1[STEP 1: Added 3P Connectors<br/>from Excel Data<br/>5 companies] --> Step2

    Step2[STEP 2: Replace Google Cloud<br/>with Gmail & Google Drive<br/>42→35 mentions] --> Decision

    Decision{DECISION:<br/>Remove 3P Connectors?<br/>Promote to Target Apps} --> Step3

    Step3[STEP 3: Update Target Apps<br/>• Qualcomm: +2 apps<br/>• EY: +3 apps<br/>• Koch: +3 apps<br/>• LTI & Wells Fargo: Remove 3P] --> Step4

    Step4[STEP 4: Consolidate Sections<br/>Target Apps + Other → Tech Stack<br/>34 companies updated] --> Final

    Final([FINAL STATE:<br/>✓ No 3P Connectors<br/>✓ Gmail/Drive tracked<br/>✓ Single Tech Stack<br/>✓ 15 target apps])

    style Start fill:#4CAF50
    style Step1 fill:#2196F3
    style Step2 fill:#2196F3
    style Decision fill:#FF9800
    style Step3 fill:#2196F3
    style Step4 fill:#2196F3
    style Final fill:#9C27B0
```

## Key Metrics

**BEFORE:**
- 2 separate sections (Target Apps + Other Apps)
- 8 target apps tracked
- 3P Connectors in separate section
- Google Cloud as single entry

**AFTER:**
- 1 unified Tech Stack section
- 15 target apps tracked
- No 3P Connectors (converted to target apps)
- Gmail and Google Drive tracked separately

**FILES UPDATED:**
- company_technology_stack_analysis.md (161 KB)
- company_technology_stack_analysis.html (21 KB)
- generate_html.py
- 5 documentation files created
"""

with open('workflow_chain_of_thought.md', 'w', encoding='utf-8') as f:
    f.write(mermaid_diagram)

print("✓ Mermaid diagram created: workflow_chain_of_thought.md")
print("\nBoth files saved successfully!")
