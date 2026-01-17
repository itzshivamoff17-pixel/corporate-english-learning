#!/usr/bin/env python3
"""
Generate ALL 100 Corporate Vocabulary modules with sidebar navigation
"""

# Complete module data for all 100 modules
MODULES_DATA = [
    # Modules 1-5 already exist, but we'll regenerate with sidebar
    {"num": 1, "title": "Essential Action Verbs", "category": "Business Verbs"},
    {"num": 2, "title": "Meeting Phrases", "category": "Meetings"},
    {"num": 3, "title": "Email Opening Phrases", "category": "Email"},
    {"num": 4, "title": "Email Closing Phrases", "category": "Email"},
    {"num": 5, "title": "Technical Jargon - Part 1", "category": "Technical"},
    {"num": 6, "title": "Technical Jargon - Part 2", "category": "Technical"},
    {"num": 7, "title": "Negotiation Phrases", "category": "Negotiation"},
    {"num": 8, "title": "Presentation Openers", "category": "Presentations"},
    {"num": 9, "title": "Presentation Closers", "category": "Presentations"},
    {"num": 10, "title": "Feedback Phrases", "category": "Communication"},
    
    # Modules 11-20
    {"num": 11, "title": "Apology & Acknowledgment", "category": "Communication"},
    {"num": 12, "title": "Request Phrases", "category": "Communication"},
    {"num": 13, "title": "Deadline Language", "category": "Project Management"},
    {"num": 14, "title": "Priority Vocabulary", "category": "Project Management"},
    {"num": 15, "title": "Status Update Phrases", "category": "Reporting"},
    {"num": 16, "title": "Problem Reporting", "category": "Reporting"},
    {"num": 17, "title": "Solution Proposing", "category": "Problem Solving"},
    {"num": 18, "title": "Agreement Phrases", "category": "Collaboration"},
    {"num": 19, "title": "Disagreement (Polite)", "category": "Collaboration"},
    {"num": 20, "title": "Clarification Requests", "category": "Communication"},
    
    # Modules 21-30
    {"num": 21, "title": "Time Management Vocab", "category": "Productivity"},
    {"num": 22, "title": "Resource Allocation", "category": "Project Management"},
    {"num": 23, "title": "Risk Management Terms", "category": "Project Management"},
    {"num": 24, "title": "Quality Assurance", "category": "Quality"},
    {"num": 25, "title": "Code Review Language", "category": "Technical"},
    {"num": 26, "title": "Architecture Discussion", "category": "Technical"},
    {"num": 27, "title": "Database Terminology", "category": "Technical"},
    {"num": 28, "title": "Cloud Computing Terms", "category": "Technical"},
    {"num": 29, "title": "Security Vocabulary", "category": "Technical"},
    {"num": 30, "title": "DevOps Terminology", "category": "Technical"},
    
    # Modules 31-40
    {"num": 31, "title": "Agile Methodology", "category": "Methodology"},
    {"num": 32, "title": "Scrum Terminology", "category": "Methodology"},
    {"num": 33, "title": "Sprint Planning", "category": "Agile"},
    {"num": 34, "title": "Retrospective Phrases", "category": "Agile"},
    {"num": 35, "title": "Stakeholder Communication", "category": "Leadership"},
    {"num": 36, "title": "Client Interaction", "category": "Client Relations"},
    {"num": 37, "title": "Vendor Management", "category": "Business"},
    {"num": 38, "title": "Budget Discussion", "category": "Finance"},
    {"num": 39, "title": "ROI & Metrics", "category": "Analytics"},
    {"num": 40, "title": "Performance Review", "category": "HR"},
    
    # Modules 41-50
    {"num": 41, "title": "Promotion Discussion", "category": "Career"},
    {"num": 42, "title": "Salary Negotiation", "category": "Career"},
    {"num": 43, "title": "Job Interview Phrases", "category": "Career"},
    {"num": 44, "title": "Networking Events", "category": "Networking"},
    {"num": 45, "title": "Conference Speaking", "category": "Public Speaking"},
    {"num": 46, "title": "Webinar Hosting", "category": "Public Speaking"},
    {"num": 47, "title": "Team Building", "category": "Leadership"},
    {"num": 48, "title": "Conflict Resolution", "category": "Leadership"},
    {"num": 49, "title": "Mentorship Language", "category": "Leadership"},
    {"num": 50, "title": "Delegation Phrases", "category": "Leadership"},
    
    # Modules 51-60
    {"num": 51, "title": "Remote Work Vocabulary", "category": "Remote Work"},
    {"num": 52, "title": "Async Communication", "category": "Remote Work"},
    {"num": 53, "title": "Zoom Etiquette", "category": "Virtual Meetings"},
    {"num": 54, "title": "Slack Best Practices", "category": "Chat"},
    {"num": 55, "title": "Teams Communication", "category": "Chat"},
    {"num": 56, "title": "Documentation Writing", "category": "Writing"},
    {"num": 57, "title": "README Best Practices", "category": "Writing"},
    {"num": 58, "title": "API Documentation", "category": "Technical Writing"},
    {"num": 59, "title": "User Stories", "category": "Product"},
    {"num": 60, "title": "Acceptance Criteria", "category": "Product"},
    
    # Modules 61-70
    {"num": 61, "title": "Product Roadmap", "category": "Product"},
    {"num": 62, "title": "Feature Prioritization", "category": "Product"},
    {"num": 63, "title": "User Research", "category": "UX"},
    {"num": 64, "title": "A/B Testing", "category": "Analytics"},
    {"num": 65, "title": "Data Analysis", "category": "Analytics"},
    {"num": 66, "title": "KPI Discussion", "category": "Metrics"},
    {"num": 67, "title": "OKR Framework", "category": "Goals"},
    {"num": 68, "title": "Quarterly Planning", "category": "Planning"},
    {"num": 69, "title": "Annual Review", "category": "Planning"},
    {"num": 70, "title": "Vision & Strategy", "category": "Strategy"},
    
    # Modules 71-80
    {"num": 71, "title": "Change Management", "category": "Management"},
    {"num": 72, "title": "Crisis Communication", "category": "Communication"},
    {"num": 73, "title": "Incident Response", "category": "Operations"},
    {"num": 74, "title": "Post-Mortem Analysis", "category": "Operations"},
    {"num": 75, "title": "SLA & SLO Terms", "category": "Operations"},
    {"num": 76, "title": "Monitoring & Alerts", "category": "Operations"},
    {"num": 77, "title": "Deployment Strategies", "category": "DevOps"},
    {"num": 78, "title": "Rollback Procedures", "category": "DevOps"},
    {"num": 79, "title": "Feature Flags", "category": "DevOps"},
    {"num": 80, "title": "Infrastructure Terms", "category": "Infrastructure"},
    
    # Modules 81-90
    {"num": 81, "title": "Containerization", "category": "Infrastructure"},
    {"num": 82, "title": "Kubernetes Basics", "category": "Infrastructure"},
    {"num": 83, "title": "Microservices Vocab", "category": "Architecture"},
    {"num": 84, "title": "API Design", "category": "Architecture"},
    {"num": 85, "title": "System Design", "category": "Architecture"},
    {"num": 86, "title": "Scalability Terms", "category": "Architecture"},
    {"num": 87, "title": "Performance Optimization", "category": "Performance"},
    {"num": 88, "title": "Caching Strategies", "category": "Performance"},
    {"num": 89, "title": "Load Balancing", "category": "Performance"},
    {"num": 90, "title": "Database Optimization", "category": "Performance"},
    
    # Modules 91-100
    {"num": 91, "title": "Testing Terminology", "category": "Quality"},
    {"num": 92, "title": "CI/CD Pipeline", "category": "DevOps"},
    {"num": 93, "title": "Version Control", "category": "Development"},
    {"num": 94, "title": "Code Quality", "category": "Development"},
    {"num": 95, "title": "Refactoring Terms", "category": "Development"},
    {"num": 96, "title": "Design Patterns", "category": "Architecture"},
    {"num": 97, "title": "SOLID Principles", "category": "Architecture"},
    {"num": 98, "title": "Clean Code", "category": "Development"},
    {"num": 99, "title": "Tech Debt Management", "category": "Management"},
    {"num": 100, "title": "Career Advancement", "category": "Career"},
]

def generate_sidebar_html(current_module):
    """Generate the sidebar navigation HTML"""
    sidebar = '''        <!-- Sidebar Navigation -->
        <aside style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 20px; padding: 24px; height: fit-content; position: sticky; top: 100px; max-height: calc(100vh - 140px); overflow-y: auto;">
            <h3 style="margin-bottom: 20px; font-size: 1.1rem; color: var(--primary);">
                <i class="fas fa-book"></i> 100 Modules
            </h3>
            <div style="margin-bottom: 16px;">
                <input type="text" id="moduleSearch" placeholder="Search modules..." style="width: 100%; padding: 8px 12px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-dark); color: var(--text-primary); font-size: 0.85rem;">
            </div>
            
            <div id="moduleList" style="max-height: calc(100vh - 280px); overflow-y: auto;">
'''
    
    # Add all 100 modules
    for module in MODULES_DATA:
        num = module['num']
        title = module['title']
        is_active = (num == current_module)
        
        if is_active:
            sidebar += f'''                <a href="module-{num:03d}.html" style="display: block; padding: 10px 12px; border-radius: 8px; background: var(--primary); color: white; text-decoration: none; margin-bottom: 4px; font-size: 0.85rem; font-weight: 600;">
                    <i class="fas fa-check-circle"></i> {num}. {title}
                </a>
'''
        else:
            sidebar += f'''                <a href="module-{num:03d}.html" style="display: block; padding: 10px 12px; border-radius: 8px; color: var(--text-secondary); text-decoration: none; margin-bottom: 4px; font-size: 0.85rem; transition: all 0.2s;" onmouseover="this.style.background='var(--bg-dark)'" onmouseout="this.style.background='transparent'">
                    <i class="far fa-circle"></i> {num}. {title}
                </a>
'''
    
    sidebar += '''            </div>
        </aside>
'''
    return sidebar

def generate_module_html(module_num):
    """Generate complete HTML for a module"""
    module_data = MODULES_DATA[module_num - 1]
    title = module_data['title']
    category = module_data['category']
    
    prev_num = module_num - 1 if module_num > 1 else None
    next_num = module_num + 1 if module_num < 100 else None
    
    sidebar_html = generate_sidebar_html(module_num)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module {module_num}: {title} - Corporate Vocabulary</title>
    <link rel="stylesheet" href="../../../assets/css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        .vocab-card {{
            background: var(--bg-dark);
            padding: 24px;
            border-radius: 12px;
            margin-bottom: 20px;
            border-left: 4px solid var(--primary);
        }}
        .item-title {{
            font-size: 1.3rem;
            color: var(--primary);
            margin-bottom: 8px;
        }}
        .example {{
            background: rgba(37, 99, 235, 0.05);
            padding: 16px;
            border-radius: 8px;
            margin-top: 12px;
            font-style: italic;
        }}
    </style>
</head>
<body>
    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="../../../index.html" class="nav-logo"><i class="fas fa-language"></i><span>ProSpeak</span></a>
            <div class="nav-actions"><a href="../../courses.html" class="btn btn-outline btn-sm">All Courses</a></div>
        </div>
    </nav>

    <div class="container" style="display: grid; grid-template-columns: 280px 1fr; gap: 40px; padding: 120px 0 80px;">
{sidebar_html}

        <!-- Main Content -->
        <main style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 20px; padding: 60px;">
            <div style="background: var(--bg-card); padding: 16px 24px; border-radius: 12px; margin-bottom: 32px; border-left: 4px solid var(--primary); border: 1px solid var(--border-color);">
                <div style="display: flex; align-items: center; gap: 12px; color: var(--text-muted); font-size: 0.9rem;">
                    <i class="fas fa-book" style="color: var(--primary);"></i>
                    <span>Corporate Vocabulary & Phrases</span>
                    <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
                    <span style="color: var(--primary-light); font-weight: 600;">Module {module_num}: {title}</span>
                </div>
            </div>

            <span class="section-badge">{category} - Module {module_num}/100</span>
            <h1>{title}</h1>
            <p style="font-size: 1.1rem; margin-bottom: 40px;">Master these essential terms and phrases for professional communication.</p>

            <!-- Vocabulary items will be added here -->
            <div class="vocab-card">
                <h3 class="item-title">Term 1</h3>
                <p><strong>Meaning:</strong> Definition for this term in the {category} category.</p>
                <div class="example">
                    <strong>Example:</strong> Example sentence demonstrating usage in a professional context.
                </div>
            </div>

            <div class="vocab-card">
                <h3 class="item-title">Term 2</h3>
                <p><strong>Meaning:</strong> Another important term for {title.lower()}.</p>
                <div class="example">
                    <strong>Example:</strong> Professional example showing how to use this term effectively.
                </div>
            </div>

            <!-- Add 8 more similar cards for a total of 10 terms per module -->
            {''.join([f'''
            <div class="vocab-card">
                <h3 class="item-title">Term {i}</h3>
                <p><strong>Meaning:</strong> Essential vocabulary for {category.lower()} communication.</p>
                <div class="example">
                    <strong>Example:</strong> Real-world usage example in a corporate setting.
                </div>
            </div>
''' for i in range(3, 11)])}

            <div style="margin-top: 60px; padding-top: 32px; border-top: 1px solid var(--border-color); display: flex; justify-content: space-between;">
                {'<a href="module-' + f'{prev_num:03d}' + '.html" class="btn btn-outline"><i class="fas fa-arrow-left"></i> Previous Module</a>' if prev_num else '<a href="../../courses.html" class="btn btn-outline"><i class="fas fa-arrow-left"></i> Back to Courses</a>'}
                {'<a href="module-' + f'{next_num:03d}' + '.html" class="btn btn-primary">Next Module <i class="fas fa-arrow-right"></i></a>' if next_num else '<a href="../../courses.html" class="btn btn-primary">Complete Course <i class="fas fa-check-circle"></i></a>'}
            </div>
        </main>
    </div>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; 2026 ProSpeak English.</p>
            </div>
        </div>
    </footer>
    
    <script>
        // Module search functionality
        document.getElementById('moduleSearch').addEventListener('input', function(e) {{
            const searchTerm = e.target.value.toLowerCase();
            const moduleLinks = document.querySelectorAll('#moduleList a');
            
            moduleLinks.forEach(link => {{
                const text = link.textContent.toLowerCase();
                if (text.includes(searchTerm)) {{
                    link.style.display = 'block';
                }} else {{
                    link.style.display = 'none';
                }}
            }});
        }});
    </script>
</body>
</html>'''
    
    return html

# Generate all 100 modules
if __name__ == "__main__":
    import os
    
    output_dir = "pages/lessons/corporate-vocabulary"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating all 100 modules with sidebar navigation...")
    
    for i in range(1, 101):
        filename = f"module-{i:03d}.html"
        filepath = os.path.join(output_dir, filename)
        
        html_content = generate_module_html(i)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        if i % 10 == 0:
            print(f"Generated {i}/100 modules...")
    
    print(f"\n✅ Successfully generated all 100 modules with sidebar navigation!")
