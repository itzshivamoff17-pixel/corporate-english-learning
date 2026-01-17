#!/usr/bin/env python3
"""
Generate 100 Corporate Vocabulary modules for ProSpeak English
Each module contains 10 vocabulary items (words/phrases) with examples
"""

import os

# Module topics and content
MODULES = [
    # Modules 1-2 already created manually
    {
        "num": 3,
        "title": "Email Opening Phrases",
        "items": [
            ("I hope this email finds you well", "A polite opening (though becoming outdated)", "I hope this email finds you well. I wanted to follow up on our discussion from last week."),
            ("I'm reaching out to...", "Modern, direct way to state your purpose", "I'm reaching out to discuss the API integration timeline."),
            ("Following up on...", "To continue a previous conversation", "Following up on our meeting yesterday, here are the action items."),
            ("As per our conversation", "Referring back to a previous discussion", "As per our conversation, I've attached the updated proposal."),
            ("I wanted to touch base on...", "To check in or discuss briefly", "I wanted to touch base on the deployment schedule for Q2."),
            ("Quick question:", "For brief, urgent queries", "Quick question: Do we have approval to proceed with the migration?"),
            ("I'm writing to inform you that...", "Formal notification", "I'm writing to inform you that the server maintenance is scheduled for Saturday."),
            ("Just a heads up that...", "Informal warning or notification", "Just a heads up that the staging environment will be down for 2 hours."),
            ("I wanted to loop you in on...", "To include someone in a conversation", "I wanted to loop you in on the security audit findings."),
            ("Per your request", "In response to something asked", "Per your request, I've compiled the performance metrics for last quarter."),
        ]
    },
    {
        "num": 4,
        "title": "Email Closing Phrases",
        "items": [
            ("Please let me know if you have any questions", "Standard polite closing", "I've attached the report. Please let me know if you have any questions."),
            ("Looking forward to your feedback", "When expecting a response", "I've sent the proposal. Looking forward to your feedback by Friday."),
            ("Thanks in advance", "Thanking before action is taken", "Could you review the PR? Thanks in advance."),
            ("Let me know if this works for you", "When proposing a time/plan", "I suggest we meet on Tuesday at 2 PM. Let me know if this works for you."),
            ("Feel free to reach out", "Inviting further communication", "Feel free to reach out if you need any clarification."),
            ("I appreciate your time", "Thanking for attention/effort", "I appreciate your time in reviewing this document."),
            ("Best regards / Kind regards", "Professional sign-off", "Best regards,\nJohn"),
            ("Talk soon", "Casual, friendly closing", "Talk soon!\nSarah"),
            ("I'll keep you posted", "Promising updates", "I'll keep you posted on the deployment progress."),
            ("Awaiting your response", "Formal, expecting reply", "Awaiting your response on the budget approval."),
        ]
    },
    {
        "num": 5,
        "title": "Technical Jargon - Part 1",
        "items": [
            ("Bandwidth", "Capacity to handle work (not just network)", "I don't have the bandwidth to take on another project this sprint."),
            ("Bottleneck", "A point of congestion slowing down a process", "The database is the bottleneck in our system."),
            ("Edge case", "An unusual or extreme scenario", "We need to handle the edge case where the user has no internet."),
            ("Tech debt", "Accumulated shortcuts that need fixing later", "We have a lot of tech debt in the authentication module."),
            ("Scalability", "Ability to handle growth", "We need to improve the scalability of our API before launch."),
            ("Latency", "Delay in data transfer", "The latency between the server and client is too high."),
            ("Throughput", "Amount of work completed in a time period", "We increased throughput by 30% after optimizing the pipeline."),
            ("Idempotent", "Operation that can be repeated without changing the result", "The API endpoint should be idempotent to handle retries safely."),
            ("Deprecate", "To phase out old code/features", "We will deprecate the v1 API next quarter."),
            ("Rollback", "Reverting to a previous version", "We had to rollback the deployment due to a critical bug."),
        ]
    },
]

# Add more modules programmatically
def generate_more_modules():
    """Generate topics for modules 6-100"""
    topics = [
        # Technical terms
        ("Technical Jargon - Part 2", [
            ("Microservices", "Architecture style with small, independent services", "We're migrating from a monolith to microservices."),
            ("CI/CD", "Continuous Integration/Continuous Deployment", "Our CI/CD pipeline runs tests automatically on every commit."),
            ("Load balancer", "Distributes traffic across servers", "The load balancer ensures no single server gets overwhelmed."),
            ("Cache", "Temporary storage for faster access", "We added a Redis cache to reduce database load."),
            ("API Gateway", "Entry point for API requests", "All requests go through the API gateway for authentication."),
            ("Containerization", "Packaging code with dependencies (Docker)", "We use containerization for consistent deployments."),
            ("Orchestration", "Automated management of containers (Kubernetes)", "Kubernetes handles the orchestration of our services."),
            ("Monorepo", "Single repository for multiple projects", "We use a monorepo to share code across teams."),
            ("Feature flag", "Toggle to enable/disable features", "We use feature flags to test new features with a subset of users."),
            ("Blue-green deployment", "Two identical environments for zero-downtime", "We use blue-green deployment to minimize downtime."),
        ]),
        
        # More business phrases
        ("Negotiation Phrases", [
            ("Let's find a middle ground", "Compromise solution", "Let's find a middle ground that works for both teams."),
            ("I see your point, however...", "Polite disagreement", "I see your point, however, I think we should prioritize security first."),
            ("What if we...", "Proposing alternative", "What if we delay the feature to ensure quality?"),
            ("I'm open to suggestions", "Inviting input", "I'm open to suggestions on how to improve the process."),
            ("Can we explore other options?", "Requesting alternatives", "This approach seems risky. Can we explore other options?"),
            ("I'd like to push back on that", "Disagreeing professionally", "I'd like to push back on that timeline—it seems too aggressive."),
            ("Let's table this for now", "Postpone discussion", "Let's table this for now and revisit after the demo."),
            ("I'm willing to compromise on...", "Showing flexibility", "I'm willing to compromise on the deadline if we can add more resources."),
            ("What are the trade-offs?", "Asking about pros/cons", "What are the trade-offs of using this framework?"),
            ("Can we agree on...?", "Seeking consensus", "Can we agree on the MVP scope for launch?"),
        ]),
    ]
    
    # Generate 95 more topics with variations
    for i in range(len(topics), 98):
        module_num = i + 3  # Starting from module 3
        MODULES.append({
            "num": module_num,
            "title": f"Advanced Corporate Vocabulary {module_num - 5}",
            "items": generate_generic_items(module_num)
        })

def generate_generic_items(module_num):
    """Generate generic vocabulary items for filler modules"""
    # This is a placeholder - you would expand this with real content
    return [
        (f"Term {i}", f"Definition for term {i}", f"Example sentence for term {i} in module {module_num}.")
        for i in range(1, 11)
    ]

def create_module_html(module_data):
    """Generate HTML for a single module"""
    num = module_data["num"]
    title = module_data["title"]
    items = module_data["items"]
    
    prev_num = f"{num-1:03d}" if num > 1 else None
    next_num = f"{num+1:03d}" if num < 100 else None
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module {num}: {title} - Corporate Vocabulary</title>
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

    <div class="container" style="padding: 120px 0 80px; max-width: 900px;">
        <div style="background: var(--bg-card); padding: 16px 24px; border-radius: 12px; margin-bottom: 32px; border-left: 4px solid var(--primary); border: 1px solid var(--border-color);">
            <div style="display: flex; align-items: center; gap: 12px; color: var(--text-muted); font-size: 0.9rem;">
                <i class="fas fa-book" style="color: var(--primary);"></i>
                <span>Corporate Vocabulary & Phrases</span>
                <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
                <span style="color: var(--primary-light); font-weight: 600;">Module {num}: {title}</span>
            </div>
        </div>

        <span class="section-badge">Vocabulary - Module {num}/100</span>
        <h1>{title}</h1>
        <p style="font-size: 1.1rem; margin-bottom: 40px;">Master these essential terms and phrases for professional communication.</p>

'''
    
    # Add vocabulary items
    for term, definition, example in items:
        html += f'''        <div class="vocab-card">
            <h3 class="item-title">"{term}"</h3>
            <p><strong>Meaning:</strong> {definition}</p>
            <div class="example">
                <strong>Example:</strong> {example}
            </div>
        </div>

'''
    
    # Add navigation
    prev_link = f'<a href="module-{prev_num}.html" class="btn btn-outline"><i class="fas fa-arrow-left"></i> Previous Module</a>' if prev_num else '<a href="../../courses.html" class="btn btn-outline"><i class="fas fa-arrow-left"></i> Back to Courses</a>'
    next_link = f'<a href="module-{next_num}.html" class="btn btn-primary">Next Module <i class="fas fa-arrow-right"></i></a>' if next_num else '<a href="../../courses.html" class="btn btn-primary">Complete Course <i class="fas fa-check-circle"></i></a>'
    
    html += f'''        <div style="margin-top: 60px; padding-top: 32px; border-top: 1px solid var(--border-color); display: flex; justify-content: space-between;">
            {prev_link}
            {next_link}
        </div>
    </div>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; 2026 ProSpeak English.</p>
            </div>
        </div>
    </footer>
</body>
</html>'''
    
    return html

# Main execution
if __name__ == "__main__":
    output_dir = "pages/lessons/corporate-vocabulary"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate modules 3-5 from predefined data
    for module in MODULES:
        filename = f"module-{module['num']:03d}.html"
        filepath = os.path.join(output_dir, filename)
        
        html_content = create_module_html(module)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Created {filename}")
    
    print(f"\nGenerated {len(MODULES)} modules successfully!")
