#!/usr/bin/env python3
"""
Update Modules 61-80 with REAL Corporate Vocabulary Content
"""

import os

# Data for Modules 61-80
VOCAB_BATCH_4 = {
    61: {
        "title": "Digital Marketing",
        "category": "Marketing",
        "intro": "Essential terms for the digital landscape.",
        "items": [
            ("SEO", "Search Engine Optimization.", "We need to improve our SEO to rank higher on Google."),
            ("Organic traffic", "Visitors who come from unpaid search results.", "Our organic traffic has doubled since the blog launch."),
            ("PPC", "Pay-Per-Click advertising.", "We are running a PPC campaign on LinkedIn."),
            ("Conversion rate", "Percentage of visitors who take a desired action.", "The landing page has a 5% conversion rate."),
            ("CTR", "Click-Through Rate.", "The email subject line had a high CTR."),
            ("Bounce rate", "Percentage of visitors who leave after one page.", "A high bounce rate means the content isn't relevant."),
            ("Lead generation", "Process of identifying potential customers.", "Webinars are great for lead generation."),
            ("Retargeting", "Advertising to people who visited your site.", "We are using Facebook for retargeting ads."),
            ("Influencer", "Person with ability to influence buyers.", "We partnered with a tech influencer for the launch."),
            ("Viral", "Spreading quickly online.", "The video went viral on Twitter."),
        ]
    },
    62: {
        "title": "Content Strategy",
        "category": "Marketing",
        "intro": "Planning and managing content creation.",
        "items": [
            ("Editorial calendar", "Schedule of content publication.", "Add the new article to the editorial calendar."),
            ("Evergreen content", "Content that stays relevant for a long time.", "We need more evergreen content for the blog."),
            ("Copywriting", "Writing text for advertising/marketing.", "Good copywriting drives sales."),
            ("CTAs", "Call to Action buttons/links.", "Make the CTAs more visible."),
            ("Engagement", "Interaction (likes, comments, shares).", "Social media engagement is down this week."),
            ("Brand voice", "Consistent personality in communication.", "Ensure the tone matches our brand voice."),
            ("Infographic", "Visual representation of data.", "Let's create an infographic for the report."),
            ("Whitepaper", "Authoritative report/guide.", "The whitepaper explains our technology in depth."),
            ("Case study", "Detailed analysis of a specific instance.", "We need a case study from a healthcare client."),
            ("Guest post", "Article written for another website.", "I wrote a guest post for TechCrunch."),
        ]
    },
    63: {
        "title": "Brand Management",
        "category": "Marketing",
        "intro": "Building and protecting the company image.",
        "items": [
            ("Brand awareness", "How recognizable a brand is.", "Our goal is to increase brand awareness in Europe."),
            ("Positioning", "Where the brand sits in the market.", "Our positioning is 'luxury yet accessible'."),
            ("Value proposition", "Why customers should buy from you.", "Our value proposition focuses on speed."),
            ("Rebranding", "Changing the corporate image.", "The rebranding campaign launches next month."),
            ("Logo", "Visual symbol of the brand.", "Please send the high-res logo file."),
            ("Tagline", "Catchphrase or slogan.", "Our new tagline is 'Innovate Everywhere'."),
            ("Brand equity", "Value of the brand name.", "Apple has massive brand equity."),
            ("Target audience", "Specific group of consumers.", "Our target audience is Gen Z."),
            ("Differentiator", "What makes you unique.", "Security is our key differentiator."),
            ("Touchpoint", "Interaction with the customer.", "Every customer touchpoint must be positive."),
        ]
    },
    64: {
        "title": "Sales Pipeline",
        "category": "Sales",
        "intro": "Managing the flow of potential deals.",
        "items": [
            ("Prospect", "Potential customer.", "The prospect is interested in a demo."),
            ("Lead", "Contact that might become a customer.", "Marketing generated 50 new leads today."),
            ("Qualified lead", "Lead that fits the buyer profile.", "We focus only on marketing-qualified leads (MQLs)."),
            ("Cold call", "Unsolicited call to a prospect.", "I hate making cold calls."),
            ("Gatekeeper", "Person who controls access to decision maker.", "The receptionist is the gatekeeper."),
            ("Decision maker", "Person who signs the check.", "We need to get a meeting with the decision maker."),
            ("Pipeline", "Stages of the sales process.", "I have 5 deals in my pipeline."),
            ("Forecasting", "Predicting future sales.", "The sales forecast for Q4 looks strong."),
            ("Quota", "Target sales amount.", "I hit my quota for the month."),
            ("Conversion", "Turning a lead into a customer.", "We need to improve our conversation from demo to trial."),
        ]
    },
    65: {
        "title": "Closing the Deal",
        "category": "Sales",
        "intro": "Finalizing the sale.",
        "items": [
            ("Objection handling", "Responding to concerns.", "Good objection handling is key to closing."),
            ("Pain point", "Problem the customer has.", "Focus on solving their pain points."),
            ("Value add", "Extra feature/service that adds value.", "The free training is a great value add."),
            ("Upsell", "Selling a more expensive version.", "Try to upsell them to the Pro plan."),
            ("Cross-sell", "Selling related products.", "We can cross-sell the security module."),
            ("Contract", "Legal agreement.", "The contract is with legal for review."),
            ("Seal the deal", "To finalize the agreement.", "Let's go to dinner to seal the deal."),
            ("Low-hanging fruit", "Easy sales targets.", "Let's target the low-hanging fruit first."),
            ("Discount", "Price reduction.", "I can offer a 10% discount if you sign today."),
            ("Commission", "Payment based on sales.", "The commission structure has changed."),
        ]
    },
    66: {
        "title": "Account Management",
        "category": "Sales",
        "intro": "Managing existing client relationships.",
        "items": [
            ("Retention", "Keeping customers.", "Customer retention is cheaper than acquisition."),
            ("Churn", "Losing customers.", "We need to reduce our churn rate."),
            ("Renewal", "Extending a contract.", "The subscription renewal is due in May."),
            ("Onboarding", "Getting new clients set up.", "The onboarding process takes 2 weeks."),
            ("QBR", "Quarterly Business Review.", "Schedule a QBR with the client."),
            ("Advocate", "Customer who recommends you.", "Turn your best clients into advocates."),
            ("Reference", "Client willing to vouch for you.", "Can we use you as a reference?"),
            ("Touch base", "Brief contact.", "I'll touch base with them next week."),
            ("Relationship building", "Developing trust.", "Sales is all about relationship building."),
            ("SLA", "Service Level Agreement.", "We are meeting our SLA obligations."),
        ]
    },
    67: {
        "title": "Customer Support Basics",
        "category": "Support",
        "intro": "Handling customer inquiries.",
        "items": [
            ("Ticket", "Record of a support request.", "Please submit a support ticket."),
            ("Triage", "Sorting tickets by urgency.", "I'm on triage duty this week."),
            ("Escalate", "Pass to a higher level.", "Escalate this ticket to Tier 2 support."),
            ("Resolution", "Fixing the issue.", "Time to resolution is our main metric."),
            ("SLA breach", "Failing to answer in time.", "We had 3 SLA breaches yesterday."),
            ("Knowledge base", "Help articles.", "Check the knowledge base for a solution."),
            ("Troubleshoot", "Diagnose and fix.", "Let's troubleshoot the connection issue."),
            ("Workaround", "Temporary fix.", "Provide the customer with a workaround."),
            ("Bug report", "Documenting a software error.", "File a bug report for the engineering team."),
            ("Feedback", "User comments.", "Collect feedback on the new feature."),
        ]
    },
    68: {
        "title": "Empathy in Support",
        "category": "Support",
        "intro": "Handling frustrated customers.",
        "items": [
            ("I understand your frustration", "Validating feelings.", "I understand your frustration with the downtime."),
            ("Apologize for the inconvenience", "Formal apology.", "We apologize for the inconvenience caused."),
            ("Rest assured", "Promising action.", "Rest assured, we are working on a fix."),
            ("Make it right", "Fixing a mistake.", "We want to make it right."),
            ("Bear with me", "Asking for patience.", "Please bear with me while I check the logs."),
            ("Prioritize", "Treat as important.", "We have prioritized your request."),
            ("Get to the bottom of this", "Find the root cause.", "I'll get to the bottom of this issue."),
            ("Valued customer", "Showing appreciation.", "You are a valued customer."),
            ("Follow up", "Check back later.", "I will follow up with you tomorrow."),
            ("Thank you for your patience", "Polite closing.", "Thank you for your patience."),
        ]
    },
    69: {
        "title": "Technical Support",
        "category": "Support",
        "intro": "Dealing with technical issues.",
        "items": [
            ("Logs", "System records.", "Please send us your server logs."),
            ("Reproduce", "Make the error happen again.", "I cannot reproduce the bug on my end."),
            ("Screenshot", "Image of the screen.", "Can you send a screenshot of the error?"),
            ("Browser cache", "Stored web data.", "Try clearing your browser cache."),
            ("Incognito mode", "Private browsing.", "Does it work in Incognito mode?"),
            ("Remote access", "Control computer from afar.", "Can we set up a remote access session?"),
            ("Configuration", "Settings.", "Check your firewall configuration."),
            ("Version", "Software release.", "What version of the app are you running?"),
            ("Patch", "Software fix.", "We are releasing a patch tonight."),
            ("Downtime", "Period when system is down.", "We experienced 10 minutes of downtime."),
        ]
    },
    70: {
        "title": "Recruiting & Hiring",
        "category": "HR",
        "intro": "Finding new talent.",
        "items": [
            ("Job description (JD)", "Details of the role.", "We need to update the JD."),
            ("Sourcing", "Finding candidates.", "I'm sourcing candidates on LinkedIn."),
            ("Screening", "Initial check.", "The recruiter is doing the phone screening."),
            ("Shortlist", "List of top candidates.", "We have a shortlist of 3 people."),
            ("Culture fit", "Alignment with values.", "We assess for culture fit."),
            ("Pipeline", "Candidates in process.", "We have a strong candidate pipeline."),
            ("Offer letter", "Formal job proposal.", "We sent the offer letter yesterday."),
            ("Onboarding", "Integration process.", "Onboarding starts on Monday."),
            ("Headhunter", "Recruiter.", "We hired a headhunter for the VP role."),
            ("Referral", "Recommendation.", "Employee referrals get a bonus."),
        ]
    },
    71: {
        "title": "HR Policies",
        "category": "HR",
        "intro": "Rules and regulations.",
        "items": [
            ("PTO", "Paid Time Off.", "I have 10 days of PTO left."),
            ("Benefits", "Non-wage compensation.", "The benefits package includes dental."),
            ("Compensation", "Salary and payment.", "We review compensation annually."),
            ("Performance review", "Evaluation.", "My performance review is tomorrow."),
            ("Severance", "Pay after termination.", "The severance package is generous."),
            ("Compliance", "Following laws.", "HR ensures legal compliance."),
            ("Grievance", "Formal complaint.", "He filed a grievance against his manager."),
            ("Diversity & Inclusion (D&I)", "Programs for equality.", "We are committed to D&I initiatives."),
            ("Handbook", "Employee manual.", "Check the employee handbook."),
            ("Probation", "Trial period.", " The probation period is 3 months."),
        ]
    },
    72: {
        "title": "Company Culture",
        "category": "HR",
        "intro": "The vibe of the workplace.",
        "items": [
            ("Core values", "Guiding principles.", "Integrity is one of our core values."),
            ("Transparency", "Openness.", "We value transparency in decision making."),
            ("Hierarchy", "Ranking system.", "We have a flat hierarchy."),
            ("Collaboration", "Working together.", "Cross-team collaboration is encouraged."),
            ("Work-life balance", "Equilibrium.", "We support a healthy work-life balance."),
            ("Remote-first", "Prioritizing remote work.", "We are a remote-first company."),
            ("Casual dress code", "Informal clothing.", "The dress code is business casual."),
            ("Team bonding", "Socializing.", "We are going for drinks for team bonding."),
            ("Open door policy", "Management is accessible.", "My manager has an open door policy."),
            ("Innovation", "New ideas.", "We foster a culture of innovation."),
        ]
    },
    73: {
        "title": "Legal Contracts",
        "category": "Legal",
        "intro": "Understanding agreements.",
        "items": [
            ("NDA", "Non-Disclosure Agreement.", "You must sign an NDA before we talk."),
            ("Liability", "Responsibility.", "The clause limits our liability."),
            ("Clause", "Section of a contract.", "Read the termination clause carefully."),
            ("Breach", "Breaking the contract.", "That is a material breach of contract."),
            ("Intellectual Property (IP)", "Creations of the mind.", "The company owns all IP created."),
            ("Terms of Service (ToS)", "Rules for users.", "We updated our Terms of Service."),
            ("Due diligence", "Investigation.", "Investors are doing due diligence."),
            ("Indemnity", "Protection against loss.", "The indemnity clause protects us."),
            ("Jurisdiction", "Legal territory.", "This contract is under NY jurisdiction."),
            ("Amendment", "Change to contract.", "We added an amendment to the agreement."),
        ]
    },
    74: {
        "title": "Compliance Terms",
        "category": "Legal",
        "intro": "Following the rules.",
        "items": [
            ("GDPR", "General Data Protection Regulation.", "We must be GDPR compliant."),
            ("Audit", "Official inspection.", "We passed the security audit."),
            ("Regulation", "Rule or law.", "Banking regulations are strict."),
            ("Privacy Policy", "Data handling rules.", "Update the privacy policy on the site."),
            ("Consent", "Permission.", "User consent is required for cookies."),
            ("Data breach", "Leaked info.", "Report the data breach immediately."),
            ("Risk assessment", "Evaluating danger.", "Conduct a risk assessment."),
            ("Whistleblower", "Person revealing wrongdoing.", "Whistleblowers are protected by law."),
            ("Code of Conduct", "Behavior rules.", "Violating the Code of Conduct can lead to firing."),
            ("Governance", "Management framework.", "Data governance is a priority."),
        ]
    },
    75: {
        "title": "Intellectual Property",
        "category": "Legal",
        "intro": "Protecting ideas.",
        "items": [
            ("Copyright", "Right to copy.", "The images are under copyright."),
            ("Trademark", "Brand symbol protection.", "We registered the logo as a trademark."),
            ("Patent", "Invention protection.", "We filed a patent for the algorithm."),
            ("License", "Permission to use.", "The software uses an MIT license."),
            ("Infringement", "Breaking IP law.", "We received a copyright infringement notice."),
            ("Open source", "Publicly available code.", "We contribute to open source projects."),
            ("Trade secret", "Confidential business info.", "The recipe is a trade secret."),
            ("Royalty", "Payment for use.", "We pay royalties to the artist."),
            ("Domain", "Website address.", "We bought the .com domain."),
            ("Fair use", "Limited use without permission.", "This falls under fair use."),
        ]
    },
    76: {
        "title": "Startup Funding",
        "category": "Startup",
        "intro": "Getting money to grow.",
        "items": [
            ("Seed round", "Early funding.", "We just raised our Seed round."),
            ("Series A", "First significant venture funding.", "We are preparing for our Series A."),
            ("VC", "Venture Capitalist.", "We are pitching to VCs next week."),
            ("Angel investor", "Individual investor.", " An angel investor wrote us a check."),
            ("Bootstrapping", "Self-funding.", "We are bootstrapping until we have revenue."),
            ("Equity", "Ownership shares.", "Employees get equity options."),
            ("Valuation", "Create worth.", "The company valuation is $10M."),
            ("Runway", "Time until money runs out.", "We have 12 months of runway left."),
            ("Burn rate", "Spending speed.", "We need to lower our burn rate."),
            ("Pitch deck", "Presentation for investors.", "Send them the pitch deck."),
        ]
    },
    77: {
        "title": "Startup Growth",
        "category": "Startup",
        "intro": "Scaling the business.",
        "items": [
            ("Product-Market Fit (PMF)", "Product satisfies market demand.", "We have not found PMF yet."),
            ("MVP", "Minimum Viable Product.", "Launch the MVP to test the market."),
            ("Pivot", "Change strategy.", "We decided to pivot to B2B."),
            ("Scalability", "Ability to grow.", "The architecture lacks scalability."),
            ("Disrupt", "Change an industry drastically.", "We aim to disrupt the insurance market."),
            ("Unicorn", "Startup worth $1B+.", "They just became a unicorn."),
            ("Growth hacking", "Creative low-cost marketing.", "We used growth hacking to get users."),
            ("Early adopter", "First customers.", "Focus on the early adopters."),
            ("Traction", "Momentum/Progress.", "We are seeing good traction."),
            ("Exit strategy", "Plan to sell/IPO.", "Our exit strategy is an acquisition."),
        ]
    },
    78: {
        "title": "Business Strategy",
        "category": "Strategy",
        "intro": "High-level planning.",
        "items": [
            ("SWOT analysis", "Strengths, Weaknesses, Opportunities, Threats.", "Let's do a SWOT analysis."),
            ("USP", "Unique Selling Proposition.", "What is our USP?"),
            ("Roadmap", "Plan for future.", "The features are on the roadmap."),
            ("Stakeholder", "Interested party.", "Manage stakeholder expectations."),
            ("Vision statement", "Future goal.", "The vision statement inspires the team."),
            ("Mission statement", "Current purpose.", "Our mission statement is to organize information."),
            ("Core competency", "Main strength.", "Design is our core competency."),
            ("Market share", "Percentage of sales.", "We want to increase our market share."),
            ("Benchmark", "Standard to compare.", "Benchmark against competitors."),
            ("Synergy", "Combined value.", "We look for synergy in the partnership."),
        ]
    },
    79: {
        "title": "Executive Management",
        "category": "Strategy",
        "intro": "C-Suite language.",
        "items": [
            ("Bottom line", "Net profit.", "It helps the bottom line."),
            ("ROI", "Return on Investment.", "The ROI of this project is low."),
            ("Quarterly results", "Financial report every 3 months.", "Results were above expectations."),
            ("Board of Directors", "Governing body.", "The Board approved the budget."),
            ("Strategic alignment", "Goals matching actions.", "Ensure strategic alignment across teams."),
            ("Operational excellence", "Efficiency.", "We strive for operational excellence."),
            ("Capital allocation", "Spending money.", "Capital allocation is key."),
            ("Succession planning", "Preparing future leaders.", "We need a succession plan for the CEO."),
            ("Restructuring", "Reorganizing.", "The company is undergoing restructuring."),
            ("M&A", "Mergers and Acquisitions.", "We are exploring M&A opportunities."),
        ]
    },
    80: {
        "title": "Crisis Management",
        "category": "Strategy",
        "intro": "Handling big problems.",
        "items": [
            ("PR disaster", "Public relations failure.", "The tweet was a PR disaster."),
            ("Damage control", "Minimizing harm.", "We are in damage control mode."),
            ("Contingency plan", "Plan B.", "Activate the contingency plan."),
            ("Press release", "Official statement.", "Issue a press release immediately."),
            ("Scenario planning", "Preparing for different futures.", "Do scenario planning for the recession."),
            ("Accountability", "Taking responsibility.", "Accept accountability for the error."),
            ("Turnaround", "Recovery.", "The CEO led a successful turnaround."),
            ("Post-mortem", "Analysis after failure.", "Conduct a post-mortem on the outage."),
            ("Stakeholder comms", "Talking to partners.", "Keep stakeholder comms clear."),
            ("Resilience", "Ability to recover.", "Building business resilience is vital."),
        ]
    }
}

def generate_sidebar_html(current_module):
    """Generate the sidebar navigation HTML (Reusable)"""
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
    
    for i in range(1, 101):
        num = i
        title = f"Module {num}" # Default
        
        # If in current batch, use real title
        if num in VOCAB_BATCH_4:
            title = VOCAB_BATCH_4[num]["title"]
            
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

def generate_module_html(module_num, data):
    """Generate complete HTML for a module with REAL DATA"""
    title = data['title']
    category = data['category']
    intro = data.get('intro', "Master these essential terms.")
    items = data['items']
    
    prev_num = module_num - 1 if module_num > 1 else None
    next_num = module_num + 1 if module_num < 100 else None
    
    sidebar_html = generate_sidebar_html(module_num)
    
    # Generate Vocab Cards
    cards_html = ""
    for term, definition, example in items:
        cards_html += f'''            <div class="vocab-card">
                <h3 class="item-title">{term}</h3>
                <p><strong>Meaning:</strong> {definition}</p>
                <div class="example">
                    <strong>Example:</strong> "{example}"
                </div>
            </div>
'''

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
            <p style="font-size: 1.1rem; margin-bottom: 40px;">{intro}</p>

{cards_html}

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

# Execute update for modules 61-80
if __name__ == "__main__":
    output_dir = "pages/lessons/corporate-vocabulary"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Updating Modules 61-80 with REAL content...")
    
    for module_num, data in VOCAB_BATCH_4.items():
        filename = f"module-{module_num:03d}.html"
        filepath = os.path.join(output_dir, filename)
        
        html_content = generate_module_html(module_num, data)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Updated Module {module_num}: {data['title']}")
    
    print("\n✅ Successfully updated Modules 61-80 with real corporate vocabulary!")
