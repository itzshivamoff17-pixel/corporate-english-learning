#!/usr/bin/env python3
"""
Update Modules 41-60 with REAL Corporate Vocabulary Content
"""

import os

# Data for Modules 41-60
VOCAB_BATCH_3 = {
    41: {
        "title": "Promotion Discussion",
        "category": "Career",
        "intro": "Phrases to advocate for your own career growth.",
        "items": [
            ("Track record", "A person's past performance or professional achievements.", "My track record shows consistent project delivery ahead of schedule."),
            ("Next level", " The next stage of career progression.", "I'm ready to take my skills to the next level as a Senior Engineer."),
            ("Vision", "The ability to think about or plan the future with imagination or wisdom.", "I have a clear vision for how this team can scale."),
            ("Strategic", "Relating to the identification of long-term or overall aims and interests at means of achieving them.", "I've been taking on more strategic responsibilities lately."),
            ("Leadership", "The action of leading a group of people or an organization.", "I demonstrated leadership by mentoring the two junior devs."),
            ("Initiative", "The power or opportunity to act or take charge before others do.", "I took the initiative to refactor the legacy codebase."),
            ("Impact", "A marked effect or influence.", "My work on the cache system had a significant business impact."),
            ("Visibility", "The state of being able to be seen.", "I want to increase the visibility of our team's work."),
            ("Scope", "The extent of the area or subject matter that something deals with.", "My role's scope has expanded significantly this year."),
            ("Advocate", "To publicly recommend or support.", "I'm hoping you will advocate for my promotion."),
        ]
    },
    42: {
        "title": "Salary Negotiation",
        "category": "Career",
        "intro": "Professional terms to discuss compensation.",
        "items": [
            ("Compensation package", "The total value of salary, benefits, bonuses, and equity.", "I'm looking for a competitive compensation package."),
            ("Market rate", "The average pay for a specific role in a specific area.", "Based on my research, the market rate is 15% higher."),
            ("Base salary", "Fixed amount of money paid to an employee.", "I'm looking for an increase in my base salary."),
            ("Equity", "Ownership interest in a company (stocks/options).", "I'm interested in the equity component of the offer."),
            ("Performance bonus", "Extra money for meeting goals.", "Is there a performance bonus structure?"),
            ("Sign-on bonus", "One-time payment when starting a job.", "A sign-on bonus would help bridge the gap."),
            ("Total rewards", "Everything an employee gets from their employer.", "I value the total rewards, including the healthcare benefits."),
            ("Counter-offer", "An offer made in response to another offer.", "I have received a counter-offer from my current company."),
            ("Review cycle", "The period when salaries are reviewed.", "When is the next salary review cycle?"),
            ("Adjustment", "A small change.", "I'm asking for a market adjustment to my salary."),
        ]
    },
    43: {
        "title": "Job Interview Phrases",
        "category": "Career",
        "intro": "Key phrases to use when being interviewed.",
        "items": [
            ("Walk you through", "To explain step-by-step.", "Let me walk you through my design process."),
            ("My approach was", "Explaining your method.", "My approach was to prioritize user privacy first."),
            ("Outcome", "The result.", "The outcome was a 20% reduction in load times."),
            ("Challenge", "A difficult task.", "The biggest challenge was handling the data migration."),
            ("Collaborate", "Work together.", "I collaborated closely with the product manager."),
            ("Adaptable", "Able to adjust to new conditions.", "I am adaptable and can learn new tech stacks quickly."),
            ("Proactive", "Creating or controlling a situation rather than just responding to it.", "I am proactive about identifying potential bugs."),
            ("Detail-oriented", "Paying attention to the small things.", "I am detail-oriented when it comes to API design."),
            ("Cultural fit", "How well you match the company values.", "I believe I am a strong cultural fit for your team."),
            ("Fast-paced", "Moving or developing very quickly.", "I thrive in a fast-paced environment."),
        ]
    },
    44: {
        "title": "Networking Events",
        "category": "Networking",
        "intro": "What to say when meeting new professionals.",
        "items": [
            ("What brings you here?", "Standard icebreaker.", "Hi, I'm Alex. What brings you to this conference?"),
            ("What do you do?", "Asking about profession.", "So, what do you do at Google?"),
            ("Connect", "To establish a relationship.", "Let's connect on LinkedIn."),
            ("Business card", "Card with contact info (digital or physical).", "Do you have a business card?"),
            ("Follow up", "Contacting someone after meeting.", "I'd like to follow up on our discussion about AI."),
            ("Field", "Industry or area of work.", "How long have you been in the security field?"),
            ("Opportunity", "A set of circumstances that makes it possible to do something.", "I'm looking for new opportunities in fintech."),
            ("Insight", "Deep understanding.", "That's a great insight into the market."),
            ("Introduce", "Presenting someone to another.", "Let me introduce you to my colleague."),
            ("Keep in touch", "Maintain contact.", "It was great meeting you. Let's keep in touch."),
        ]
    },
    45: {
        "title": "Conference Speaking",
        "category": "Public Speaking",
        "intro": "Vocabulary for presenting on stage.",
        "items": [
            ("Keynote", "The main speech at a conference.", "I'm delivering the keynote on Tuesday."),
            ("Panel", "A small group of people discussing a topic.", "I'm sitting on a panel about diversity in tech."),
            ("Abstract", "Summary of a talk proposal.", "I submitted an abstract for PyCon."),
            ("Slide deck", "The presentation slides.", "I need to finalize my slide deck."),
            ("Audience", "The assembled spectators or listeners.", "Know your audience before you design your talk."),
            ("Q&A", "Questions and Answers.", "We will have time for Q&A at the end."),
            ("Microphone check", "Testing audio.", "Can we do a quick microphone check?"),
            ("Stage fright", "Nervousness before speaking.", "I always get a little stage fright."),
            ("Engaging", "Charming and attractive.", "You want your story to be engaging."),
            ("Takeaway", "Key point to remember.", "The main takeaway is that simplicity wins."),
        ]
    },
    46: {
        "title": "Webinar Hosting",
        "category": "Public Speaking",
        "intro": "Terms specific to online presentations.",
        "items": [
            ("Housekeeping", "Administrative details.", "Just a little housekeeping before we start."),
            ("Poll", "A survey.", "I'm going to launch a poll to see who is using React."),
            ("Chat box", "Where attendees type.", "Feel free to drop questions in the chat box."),
            ("Screen share", "Showing your desktop.", "Let me screen share so you can see the demo."),
            ("Recording", "Captured video.", "The recording will be sent out via email."),
            ("Mute", "Turn off audio.", "Please keep your microphone on mute."),
            ("Lag", "Delay.", "Sorry, there is a bit of lag on my connection."),
            ("Attendees", "People present.", "We have over 500 attendees today!"),
            ("Handout", "Downloadable resource.", "You can download the handout from the sidebar."),
            ("Sign off", "End the broadcast.", "Thanks for joining. Signing off now!"),
        ]
    },
    47: {
        "title": "Team Building",
        "category": "Leadership",
        "intro": "Building a cohesive and effective team.",
        "items": [
            ("Morale", "The confidence and enthusiasm of a group.", "Team morale is low after the layoffs."),
            ("Icebreaker", "Activity to relieve tension.", "Let's do a quick icebreaker game."),
            ("Offsite", "Meeting away from the office.", "We are planning a team offsite next month."),
            ("Trust", "Firm belief in reliability.", "Ideally, we build trust through transparency."),
            ("Collaboration", "Working together.", "We need to foster better collaboration."),
            ("Diversity", "Including people from different backgrounds.", "Diversity of thought improves our products."),
            ("Inclusion", "Providing equal access and opportunities.", "Inclusion means everyone feels their voice is heard."),
            ("Psychological safety", "Believe you won't be punished for mistakes.", "Psychological safety is key for high-performing teams."),
            ("Engagement", "Emotional commitment.", "We want to improve employee engagement."),
            ("Synergy", "Combined effect is greater than sum (buzzword).", "There is great synergy between the two teams."),
        ]
    },
    48: {
        "title": "Conflict Resolution",
        "category": "Leadership",
        "intro": "Handling disagreements professionally.",
        "items": [
            ("Mediate", "Intervene to settle a dispute.", "I had to mediate between the dev and the PM."),
            ("De-escalate", "Reduce the intensity.", "Try to de-escalate the situation calmly."),
            ("Perspective", "Point of view.", "Let's try to understand their perspective."),
            ("Compromise", "Agreement reached by each side making concessions.", "We reached a compromise on the timeline."),
            ("Constructive", "Serving a useful purpose.", "Keep the feedback constructive."),
            ("Tension", "Mental or emotional strain.", "There was some tension in the meeting."),
            ("Resolution", "A firm decision or solution.", "We need to find a resolution quickly."),
            ("Empathy", "Understanding feelings of others.", "Lead with empathy when delivering bad news."),
            ("Active listening", "Fully concentrating on what is being said.", "Practice active listening; don't just wait to speak."),
            ("Common ground", "Shared opinions or interests.", "Let's start by finding common ground."),
        ]
    },
    49: {
        "title": "Mentorship Language",
        "category": "Leadership",
        "intro": "Guiding others in their career.",
        "items": [
            ("Guidance", "Advice or information aimed at resolving a problem.", "Thank you for your guidance on this project."),
            ("Role model", "A person looked to by others as an example.", "She is a role model for women in tech."),
            ("Check-in", "Brief meeting.", "Let's have a weekly check-in."),
            ("Growth mindset", "Belief that abilities can be developed.", " encourage a growth mindset."),
            ("Potential", "Latent qualities or abilities.", "I see a lot of potential in him."),
            ("Sponsor", "Someone who advocates for you.", "You need a sponsor to get promoted to Exec level."),
            ("Mentee", "The person being mentored.", "My mentee just landed a new job!"),
            ("Shadowing", "Observing someone at work.", "You can shadow me during the client call."),
            ("Empower", "Make someone stronger and more confident.", "I want to empower you to make decisions."),
            ("Soft skills", "Personal attributes (communication, etc.).", "Engineers need soft skills too."),
        ]
    },
    50: {
        "title": "Delegation Phrases",
        "category": "Leadership",
        "intro": "How to assign work effectively.",
        "items": [
            ("Hand off", "Transfer responsibility.", "I want to hand off this module to you."),
            ("Own", "Take full responsibility.", "I want you to own the frontend architecture."),
            ("Support", "Help.", "I will be here to support you."),
            ("Accountable", "Responsible for.", "You are accountable for the quality of the code."),
            ("Checkpoints", "Review moments.", "Let's set up a few checkpoints to review progress."),
            ("Empowered", "Given authority.", "You are empowered to choose the library."),
            ("Bandwidth", "Capacity.", "I don't have the bandwidth, so I'm delegating this."),
            ("Trust", "Firm belief.", "I trust your judgment on this."),
            ("Review", "Assess.", "I will review it before we ship."),
            ("Autonomy", "Freedom from external control.", "I'm giving you full autonomy on this feature."),
        ]
    },
    51: {
        "title": "Remote Work Vocabulary",
        "category": "Remote Work",
        "intro": "Terms for valid distributed teams.",
        "items": [
            ("Async", "Asynchronous (not happening at same time).", "We work async because of time zones."),
            ("Distributed", "Spread out.", "We are a fully distributed team."),
            ("Hybrid", "Mix of office and remote.", "We have a hybrid work policy."),
            ("Time zone", "Region with standard time.", "What time zone are you in?"),
            ("Overlap", "Time when both people are working.", "We only have 2 hours of overlap."),
            ("Wfh", "Work From Home.", "I am WFH today."),
            ("Digital nomad", "Person earning a living working online from various locations.", "He is a digital nomad living in Bali."),
            ("Sync", "Synchronize (meet at same time).", "Let's sync up later."),
            ("Availability", "When you are free.", "Please update your availability on the calendar."),
            ("Retreat", "Company gathering.", "The annual company retreat is in Mexico."),
        ]
    },
    52: {
        "title": "Async Communication",
        "category": "Remote Work",
        "intro": "Communicating without requiring immediate response.",
        "items": [
            ("Thread", "Sequence of messages.", "Please reply in the thread to keep the channel clean."),
            ("Ping", "Send a message.", "Ping me when you are online."),
            ("DM", "Direct Message.", "I sent you a DM."),
            ("Notification", "Alert.", "I turned off notifications to focus."),
            ("Status", "Current state/availability.", "Set your status to 'In a meeting'."),
            ("Documentation", "Written record.", "Async requres good documentation."),
            ("Handover", "Transferring work.", "Leave a detailed handover note before your vacation."),
            ("Blocker", "Something stopping you.", "Post any blockers in the daily standup channel."),
            ("Update", "New info.", "Read my update in the ticket."),
            ("Context switching", "Changing focus often.", "Async reduces context switching."),
        ]
    },
    53: {
        "title": "Zoom Etiquette",
        "category": "Virtual Meetings",
        "intro": "Manners for video calls.",
        "items": [
            ("Mute", "Silent mode.", "You're on mute!"),
            ("Background noise", "Sounds behind you.", "Sorry about the background noise."),
            ("Breakout room", "Sub-meeting.", "Let's split into breakout rooms."),
            ("Share screen", "Show your display.", "Can I share my screen?"),
            ("Laggy", "Slow/delayed.", "Your video is a bit laggy."),
            ("Frozen", "Video stuck.", "You are frozen."),
            ("Cut out", "Audio dropped.", "You cut out for a second."),
            ("Camera on/off", "Video preference.", "Is this a camera on or off meeting?"),
            ("Jump", "Leave quickly.", "I have to jump to another call."),
            ("Hard stop", "Must leave time.", "I have a hard stop at the hour."),
        ]
    },
    54: {
        "title": "Slack Best Practices",
        "category": "Chat",
        "intro": "Using work chat effectively.",
        "items": [
            ("Channel", "Chat room.", "Post it in the #general channel."),
            ("Thread", "Reply chain.", "Please use a thread for discussion."),
            ("Mention", "Tagging someone (@name).", "Don't mention @channel unless it's urgent."),
            ("Reaction", "Emoji response.", "Please add a checkmark reaction when you've read this."),
            ("Huddle", "Quick audio call.", "Let's hop on a Huddle."),
            ("Pinned", "Saved message.", "Check the pinned items for the links."),
            ("Snooze", "Delay notification.", "I snoozed notifications until tomorrow."),
            ("Status", "User state.", "I set my status to 'Heads Down'."),
            ("Direct Message", "Private chat.", "This should be a direct message, not public."),
            ("Etiquette", "Code of polite behavior.", "Follow proper Slack etiquette."),
        ]
    },
    55: {
        "title": "Teams Communication",
        "category": "Chat",
        "intro": "Vocabulary for Microsoft Teams users.",
        "items": [
            ("Team", "Group of people.", "I added you to the Engineering Team."),
            ("Channel", "Section within a team.", "Check the 'Announcements' channel."),
            ("Post", "Message.", "I made a post about the holiday party."),
            ("Files", "Tab for documents.", "The specs are in the Files tab."),
            ("Wiki", "Tab for notes.", "Update the team Wiki."),
            ("Meeting", "Calendar event.", "Did you accept the meeting invite?"),
            ("Availability", "Status (Busy, Away).", "His availability shows as 'Do Not Disturb'."),
            ("Together Mode", "View with avatars in seats.", "Let's switch to Together Mode for the photo."),
            ("Live", "Real-time.", "The document updates live."),
            ("Integration", "Connection to other app.", "We set up the Jira integration."),
        ]
    },
    56: {
        "title": "Documentation Writing",
        "category": "Writing",
        "intro": "If it isn't documented, it doesn't exist.",
        "items": [
            ("Wiki", "Knowledge base.", "Update the internal wiki."),
            ("Readme", "First file to read.", "Check the README.md for setup instructions."),
            ("Changelog", "Log of changes.", "Update the changelog with your PR."),
            ("Tutorial", "Step-by-step guide.", "I wrote a tutorial for the new API."),
            ("Reference", "Lookup guide.", "The API reference is automatically generated."),
            ("Onboarding doc", "Guide for new hires.", "Read the onboarding doc first."),
            ("Deprecated", "Marked for removal.", "This function is deprecated."),
            ("Glossary", "List of terms.", "Add 'Widget' to the glossary."),
            ("Architecture Decision Record (ADR)", "Log of design choices.", "We need to write an ADR for choosing Postgres."),
            ("Version", "Iteration number.", "Is this documentation for Version 1 or 2?"),
        ]
    },
    57: {
        "title": "README Best Practices",
        "category": "Writing",
        "intro": "Making your project accessible.",
        "items": [
            ("Prerequisites", "What you need before starting.", "List Node.js as a prerequisite."),
            ("Installation", "How to set up.", "The installation steps are unclear."),
            ("Usage", "How to use.", "Add a usage example."),
            ("License", "Legal usage rights.", "Everything needs an MIT license."),
            ("Contributing", "How to help.", "Read the CONTRIBUTING.md file."),
            (" Badges", "Status icons.", "Add the build passing badge."),
            ("Table of Contents", "List of sections.", "The TOC helps navigation."),
            ("FAQ", "Frequently Asked Questions.", "Add an FAQ section."),
            ("Support", "How to get help.", "Open an issue for support."),
            ("Acknowledgements", "Credits.", "Thanks to the contributors."),
        ]
    },
    58: {
        "title": "API Documentation",
        "category": "Technical Writing",
        "intro": "Describing how your interface works.",
        "items": [
            ("Endpoint", "URL to access.", "The /users endpoint returns a list."),
            ("Method", "HTTP verb (GET, POST).", "This endpoint uses the POST method."),
            ("Parameters", "Input variables.", "The query parameters are optional."),
            ("Request body", "Data sent.", "The request body must be JSON."),
            ("Response", "Data returned.", "The response includes the user ID."),
            ("Status code", "HTTP result (200, 404).", "It returns a 404 status code if not found."),
            ("Authentication", "Login method.", "Authentication is via Bearer token."),
            ("Rate limit", "Max requests allowed.", "The rate limit is 100 requests per minute."),
            ("Example", "Sample code.", "Provide a curl example."),
            ("Error", "Problem description.", "Document the possible error messages."),
        ]
    },
    59: {
        "title": "User Stories",
        "category": "Product",
        "intro": "Describing features from the user's view.",
        "items": [
            ("As a...", "User role.", "As a registered user..."),
            ("I want to...", "Action.", "...I want to reset my password..."),
            ("So that...", "Benefit.", "...so that I can regain access to my account."),
            ("Acceptance criteria", "Conditions for success.", "Acceptance criteria: User receives email."),
            ("Persona", "Fictional user profile.", "This story is for the 'admin' persona."),
            ("Flow", "Sequence of steps.", "The user flow is too complicated."),
            ("Mockup", "Visual design.", "See the attached mockup."),
            ("Scenario", "Situation.", "Consider the offline scenario."),
            ("Edge case", "Rare situation.", "What about the edge case where email is null?"),
            ("Validation", "Checking correctness.", "Add form validation."),
        ]
    },
    60: {
        "title": "Acceptance Criteria",
        "category": "Product",
        "intro": "Defining exactly when a task is finished.",
        "items": [
            ("Given", "Pre-condition.", "Given I am logged in..."),
            ("When", "Action.", "...when I click logout..."),
            ("Then", "Result.", "...then I should be redirected to home."),
            ("Pass/Fail", "Result state.", "The test passed."),
            ("Requirement", "Rule.", "The password must be 8 chars is a hard requirement."),
            ("Verification", "Checking.", "Manual verification is required."),
            ("Automated", "Done by machine.", "Automated tests cover this criteria."),
            ("Scope", "Boundaries.", "This is out of scope."),
            ("Deliverable", "Output.", "The deliverable is a PDF report."),
            ("Sign-off", "Approval.", "Product owner sign-off is needed."),
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
        if num in VOCAB_BATCH_3:
            title = VOCAB_BATCH_3[num]["title"]
            
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

# Execute update for modules 41-60
if __name__ == "__main__":
    output_dir = "pages/lessons/corporate-vocabulary"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Updating Modules 41-60 with REAL content...")
    
    for module_num, data in VOCAB_BATCH_3.items():
        filename = f"module-{module_num:03d}.html"
        filepath = os.path.join(output_dir, filename)
        
        html_content = generate_module_html(module_num, data)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Updated Module {module_num}: {data['title']}")
    
    print("\n✅ Successfully updated Modules 41-60 with real corporate vocabulary!")
