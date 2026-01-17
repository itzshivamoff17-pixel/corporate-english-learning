#!/usr/bin/env python3
"""
Update Modules 1-20 with REAL Corporate Vocabulary Content
"""

import os

# Data for Modules 1-20
VOCAB_BATCH_1 = {
    1: {
        "title": "Essential Action Verbs",
        "category": "Business Verbs",
        "intro": "Strong verbs drive action. Use these to sound decisive and active properly describing your contributions.",
        "items": [
            ("Facilitate", "To make a process or meeting easier or smoother.", "I will facilitate the retrospective meeting this afternoon."),
            ("Leverage", "To use something (resources, influence) to maximum advantage.", "We should leverage the existing API to save development time."),
            ("Streamline", "To make a process more efficient by simplifying it.", "We need to streamline the onboarding process for new hires."),
            ("Align", "To bring into agreement or close cooperation.", "Let's meet to align on the quarterly goals."),
            ("Escalate", "To raise a focused issue to a higher authority.", "If we can't solve this blocker by noon, I'll escalate it to management."),
            ("Spearhead", "To lead a movement, campaign, or attack.", "Sarah will spearhead the new marketing initiative."),
            ("Expedite", "To make an action or process happen sooner or be accomplished more quickly.", "Can we expedite the approval process for this hotfix?"),
            ("Mitigate", "To make less severe, serious, or painful (usually risks).", "We added redundancy to mitigate the risk of server failure."),
            ("Optimise", "To make the best or most effective use of a situation or resource.", "We need to optimize the database queries for better performance."),
            ("Delegate", "To entrust (a task or responsibility) to another person.", "I will delegate the documentation task to the junior dev."),
        ]
    },
    2: {
        "title": "Meeting Phrases",
        "category": "Meetings",
        "intro": "Meetings are where decisions happen. Use these phrases to control the flow and sound professional.",
        "items": [
            ("Let's circle back", "To delay discussing a topic until later.", "That's a rabbit hole. Let's circle back to it at the end if we have time."),
            ("Take this offline", "To discuss a detailed topic privately or with a smaller group.", "This is getting too technical for the general meeting. Let's take this offline."),
            ("Hard stop", "A specific time when you absolutely must leave.", "I have a hard stop at 3 PM for a client call."),
            ("Action item", "A specific task that needs to be done.", "Let's assign action items before we wrap up."),
            ("Touch base", "To briefly contact or update someone.", "Let's touch base early next week to see where we stand."),
            ("On the same page", "To have a shared understanding.", "I want to make sure we're all on the same page regarding the deadline."),
            ("Table this", "To postpone a discussion indefinitely.", "Let's table this discussion until we have more data."),
            ("Piggyback", "To add to what someone else has just said.", "I'd like to piggyback on what John just mentioned about performance."),
            ("Floor is yours", "Inviting someone else to speak.", "Thanks for the intro. Sarah, the floor is yours."),
            ("Wrap up", "To finish the meeting.", "We have 5 minutes left, so let's wrap up and review next steps."),
        ]
    },
    3: {
        "title": "Email Opening Phrases",
        "category": "Email",
        "intro": "The first line of your email sets the tone. Move beyond 'I hope you are well'.",
        "items": [
            ("Reaching out to...", "Direct and professional purpose statement.", "I'm reaching out to request access to the staging environment."),
            ("Following up on...", "Connecting to a previous interaction.", "Following up on our conversation yesterday, here is the report."),
            ("Looping in...", "Adding someone to the thread.", "I'm looping in Mike as he is the subject matter expert here."),
            ("As discussed,", "Reference to a verbal agreement.", "As discussed, I will proceed with the blue design theme."),
            ("Quick question regarding...", "Low-pressure request for information.", "Quick question regarding the timeline for the Q3 release."),
            ("Just a friendly reminder...", "Polite nudge for action.", "Just a friendly reminder that timecards are due by 5 PM."),
            ("Writing to inform you...", "Formal notification.", "Broadcasting: I'm writing to inform you that the server will be down for maintenance."),
            ("Wanted to touch base...", "Casual check-in.", "Wanted to touch base on the progress of the React migration."),
            ("Thanks for the update.", "Acknowledging receipt of info.", "Thanks for the update. I will review the docs this evening."),
            ("Connecting you with...", "Introduction.", "Connecting you with Jane, who leads our Design team."),
        ]
    },
    4: {
        "title": "Email Closing Phrases",
        "category": "Email",
        "intro": "End your emails clearly. Your closing should indicate what happens next.",
        "items": [
            ("Looking forward to...", "Expressing anticipation.", "Looking forward to your feedback on the proposal."),
            ("Let me know if...", "Offering further help.", "Let me know if you have any questions or blockers."),
            ("Best regards,", "Standard professional sign-off.", "Best regards,\nShivam"),
            ("Thanks in advance,", "Presumptive gratitude (use with tasks).", "Thanks in advance for reviewing this quickly."),
            ("Keep me posted.", "Request for updates.", "Good luck with the deployment. Keep me posted."),
            ("Happy to help.", "Offering support.", "Reach out if you get stuck. Happy to help."),
            ("Talk soon,", "Casual sign-off for colleagues.", "Talk soon,\nAlex"),
            ("Awaiting your reply.", "Direct and urgent.", "Urgent: Awaiting your reply so we can proceed."),
            ("Cheers,", "Friendly, common in tech/startups.", "Cheers,\nTeam Lead"),
            ("Sincerely,", "Very formal (use for contracts/resignations).", "Sincerely,\nJohn Doe"),
        ]
    },
    5: {
        "title": "Technical Jargon - Part 1",
        "category": "Technical",
        "intro": "Speak the language of engineers and product managers.",
        "items": [
            ("Bandwidth", "Mental or time capacity to do work.", "I don't have the bandwidth to take on another project this sprint."),
            ("Bottleneck", "A point of congestion efficiently slowing down a system.", "The QA process is currently the bottleneck for our release."),
            ("Legacy code", "Old code that is difficult to maintain but vital.", "We are refactoring the legacy code to improve stability."),
            ("Tech debt", "The implied cost of additional rework caused by choosing an easy solution now.", "If we skip writing tests, we are building up tech debt."),
            ("Deploy", "To push code to a server/environment.", "We will deploy the hotfix to production tonight."),
            ("Scalability", "The capability of a system to handle a growing amount of work.", "We need to ensure the database has the scalability to handle Black Friday traffic."),
            ("Latency", "The delay before a transfer of data begins.", "Users are complaining about high latency on the dashboard."),
            ("Uptime", "The time a system is functional and working.", "We are aiming for 99.9% uptime this year."),
            ("Bug bash", "A designated time for a team to hunt for bugs.", "Let's schedule a bug bash before the major release."),
            ("Feature creep", "The excessive ongoing expansion or addition of new features.", "We need to stop feature creep or we will miss the deadline."),
        ]
    },
    6: {
        "title": "Technical Jargon - Part 2",
        "category": "Technical",
        "intro": "More essential technical terms for modern software development.",
        "items": [
            ("Microservices", "Structuring an app as a collection of services.", "Moving to microservices will decouple our teams."),
            ("CI/CD", "Continuous Integration and Continuous Deployment.", "Our CI/CD pipeline runs tests automatically on every commit."),
            ("Containerization", "Packing software into standardized units (e.g. Docker).", "Containerization ensures the app runs the same on my laptop and production."),
            ("API Gateway", "An entry point for a defined group of microservices.", "The API Gateway handles authentication and rate limiting."),
            ("Orchestration", "Automated configuration and coordination of systems (e.g. Kubernetes).", "Kubernetes handles the orchestration of our docker containers."),
            ("Agile", "Iterative approach to software development.", "We work in an Agile environment with 2-week sprints."),
            ("Scrum", "A framework for Agile management.", "We have our daily Scrum meeting at 10 AM."),
            ("Full stick", "Common typo for Full stack (Frontend + Backend).", "He is a full stack developer."),
            ("MVP", "Minimum Viable Product.", "Let's launch the MVP first and add bells and whistles later."),
            ("POC", "Proof of Concept.", "Build a quick POC to see if this library works for us."),
        ]
    },
    7: {
        "title": "Negotiation Phrases",
        "category": "Negotiation",
        "intro": "Negotiation isn't just about salary. It's about deadlines, scope, and resources.",
        "items": [
            ("Middle ground", "A compromise.", "Let's find a middle ground between the design quality and the deadline."),
            ("Push back", "To resist or oppose a request.", "I have to push back on this timeline; it's too aggressive."),
            ("Non-negotiable", "Something that cannot be changed.", "Security compliance is non-negotiable for this release."),
            ("Trade-off", "Giving up one thing to get another.", "The trade-off for faster performance is higher memory usage."),
            ("Win-win", "A situation where everyone benefits.", "This partnership is a win-win for both departments."),
            ("Low-hanging fruit", "The most easily achieved of a set of tasks.", "Fixing the typos is low-hanging fruit; let's do it today."),
            ("Ballpark figure", "Rough estimate.", "Can you give me a ballpark figure for the cloud costs?"),
            ("Play hardball", "To act aggressively in negotiation.", "The vendor is playing hardball on the license fees."),
            ("Sign off", "Official approval.", "We need the CTO's sign off before we proceed."),
            ("Go to bat for", "To support or defend someone.", "I will go to bat for you to get that promotion."),
        ]
    },
    8: {
        "title": "Presentation Openers",
        "category": "Presentations",
        "intro": "Grab attention in the first 30 seconds of your presentation.",
        "items": [
            ("Let's kick things off", "To start the meeting/presentation.", "Let's kick things off by reviewing last quarter's numbers."),
            ("Thanks for joining", "Polite welcome.", "Thanks for joining everyone. I know you are busy."),
            ("The purpose of this...", "Setting the agenda.", "The purpose of this presentation is to align on the new roadmap."),
            ("Give you an overview", "Summarizing what will come.", "I'll give you an overview of the architecture changes."),
            ("Walk you through", "To explain step-by-step.", "I'm going to walk you through the user journey."),
            ("Dive right in", "To start immediately without small talk.", "We have a lot to cover, so let's dive right in."),
            ("Before we begin", "Pre-conditions.", "Before we begin, please mute your microphones."),
            ("Show of hands", "Asking for audience interaction.", "Quick show of hands: who has used the new tool?"),
            ("Setting the stage", "Providing context.", "Let me set the stage by explaining the market conditions."),
            ("Takeaway", "What you want people to remember.", "My key takeaway for you today is that speed matters."),
        ]
    },
    9: {
        "title": "Presentation Closers",
        "category": "Presentations",
        "intro": "End strong. The last thing you say is often what people remember most.",
        "items": [
            ("To wrap up", "Signals the end.", "To wrap up, we are on track for Q4."),
            ("Key takeaways", "Main points to remember.", "Here are the 3 key takeaways from today's session."),
            ("Call to action", "What the audience should do next.", "My call to action for you is to upgrade your passwords."),
            ("Floor for questions", "Opening Q&A.", "I'd like to open the floor for questions."),
            ("Any questions?", "Standard Q&A prompt.", "Does anyone have any questions regarding the deployment?"),
            ("Thank you for your time", "Polite closing.", "Thank you for your time today."),
            ("Feel free to reach out", "Invitation for follow-up.", "If you think of questions later, feel free to reach out on Slack."),
            ("In summary", "Final recap.", "In summary, the project is a success."),
            ("Moving forward", "Next steps.", "Moving forward, we will meet weekly."),
            ("Over to you", "Passing control.", "That's it from me. Over to you, Sarah."),
        ]
    },
    10: {
        "title": "Feedback Phrases",
        "category": "Communication",
        "intro": "Giving and receiving feedback is a superpower. Do it gracefully.",
        "items": [
            ("Constructive criticism", "Helpful feedback.", "I have some constructive criticism about the code structure."),
            ("Areas for improvement", "Polite way to say 'weaknesses'.", "One area for improvement is documentation."),
            ("Positive feedback", "Praise.", "We received a lot of positive feedback from beta testers."),
            ("Take it onboard", "To accept and act on feedback.", "Thanks, I'll take that feedback onboard."),
            ("My 2 cents", "My humble opinion.", "Just my 2 cents, but I think the button should be blue."),
            ("Play devil's advocate", "To argue the opposite side to test the idea.", "Let me play devil's advocate: what if the API fails?"),
            ("Echo that", "To agree with someone.", "I want to echo what Mike said about quality."),
            ("Room for growth", "Potential to improve.", "There is room for growth in your presentation skills."),
            ("Constructive", "Serving a useful purpose.", "Let's keep the discussion constructive."),
            ("Feedback loop", "Continuous cycle of feedback.", "We need to shorten the feedback loop between dev and QA."),
        ]
    },
    11: {
        "title": "Apology & Acknowledgment",
        "category": "Communication",
        "intro": "Mistakes happen. Own them professionally without over-apologizing.",
        "items": [
            ("My bad", "Casual apology (use with peers).", "My bad, I forgot to push the commit."),
            ("I overlooked that", "Admitting you missed something.", "I overlooked that requirement. I'll add it now."),
            ("Slip through the cracks", "To be forgotten or missed.", "Sorry, your email slipped through the cracks."),
            ("Drop the ball", "To make a mistake/fail.", "I dropped the ball on the client report. It won't happen again."),
            ("Misunderstanding", "Polite way to say confusion.", "I think there was a misunderstanding about the deadline."),
            ("Bear with me", "Ask for patience.", "Please bear with me while I pull up the data."),
            ("Apologize for the inconvenience", "Formal apology.", "We apologize for the inconvenience caused by the outage."),
            ("Make it right", "To fix a mistake.", "We messed up, but we will make it right."),
            ("Own it", "To take responsibility.", "I own that mistake. I pushed the bad code."),
            ("Good catch", "Thanking someone for finding an error.", "Good catch! I didn't see that typos."),
        ]
    },
    12: {
        "title": "Request Phrases",
        "category": "Communication",
        "intro": "How to ask for things without sounding demanding.",
        "items": [
            ("Do you have bandwidth?", "Do you have time?", "Do you have bandwidth to review my PR today?"),
            ("Could you do me a favor?", "Asking for help.", "Could you do me a favor and check the logs?"),
            ("It would be great if", "Polite suggestion.", "It would be great if you could update the ticket."),
            ("I'd appreciate it", "Gratitude.", "I'd appreciate it if you keep me in the loop."),
            ("Is it possible to", "Checking feasibility.", "Is it possible to delay the meeting by 10 minutes?"),
            ("Can I pick your brain?", "Asking for advice/knowledge.", "Can I pick your brain about the new architecture?"),
            ("Point me in the right direction", "Asking for guidance.", "Can you point me in the right direction for the docs?"),
            ("Spare a minute?", "Asking for brief time.", "Can you spare a minute to look at this error?"),
            ("Requesting access", "Standard IT request.", "I am requesting access to the AWS console."),
            ("Nudge", "To remind gently.", "I'm giving this a nudge since it's urgent."),
        ]
    },
    13: {
        "title": "Deadline Language",
        "category": "Project Management",
        "intro": "Managing time expectations is critical in corporate roles.",
        "items": [
            ("ETA", "Estimated Time of Arrival (Completion).", "What is the ETA for the fix?"),
            ("Hard deadline", "Cannot be moved.", "The compliance audit has a hard deadline of Friday."),
            ("Push out", "To delay.", "Can we push out the release date by a week?"),
            ("Pull in", "To do sooner.", "We need to pull in the security features to Sprint 1."),
            ("Tight deadline", "Not much time.", "It's a tight deadline, but I think we can make it."),
            ("Down to the wire", "Until the last moment.", "It's going to be down to the wire to finish this."),
            ("Ahead of schedule", "Early.", "Good news, we are ahead of schedule."),
            ("Behind schedule", "Late.", "We are falling behind schedule due to bugs."),
            ("Timeline", "Schedule of events.", "Here is the proposed timeline for the project."),
            ("Due date", "When something must be done.", "The due date for the report is EOD."),
        ]
    },
    14: {
        "title": "Priority Vocabulary",
        "category": "Project Management",
        "intro": "When everything is important, nothing is. Learn to qualify importance.",
        "items": [
            ("Blocker", "Something stopping progress.", "The API failure is a blocker for the frontend team."),
            ("Critical path", "Essential steps that cannot be delayed.", "Database migration is on the critical path."),
            ("Must-have", "Essential feature.", "Dark mode is a must-have for launch."),
            ("Nice-to-have", "Optional feature.", "Animated icons are nice-to-have, but not essential."),
            ("Low priority", "Do it later.", "Fixing the typo is low priority."),
            ("High priority", "Do it now.", "Production outage is high priority."),
            ("Showstopper", "A bug so bad it stops the release.", "We found a showstopper bug in testing."),
            ("Triage", "Assigning degrees of urgency.", "Let's triage the new bug reports."),
            ("Back burner", "To delay something.", "Put the redesign on the back burner for now."),
            ("Front and center", "Main focus.", "Security should be front and center in this design."),
        ]
    },
    15: {
        "title": "Status Update Phrases",
        "category": "Reporting",
        "intro": "Keep your manager confident with clear status updates.",
        "items": [
            ("On track", "Proceeding as planned.", "The project is on track for Q1 launch."),
            ("At risk", "Might be late/fail.", "The deadline is at risk due to the third-party delay."),
            ("Trending", "Moving in a direction.", "Tickets are trending down this week."),
            ("Blocked", "Cannot proceed.", "I am blocked by the missing credentials."),
            ("In progress", "Currently doing it.", "The migration is in progress."),
            ("Done done", "Completely finished (tested, deployed).", "Is the feature done, or 'done done'?"),
            ("Status quo", "Existing state of affairs.", "We will maintain the status quo for now."),
            ("Update", "New information.", "I have an update on the hiring process."),
            ("Green / Yellow / Red", "Status indicators.", "The project status is currently Yellow."),
            ("Milestone", "Significant point in progress.", "We hit a major milestone today."),
        ]
    },
    16: {
        "title": "Problem Reporting",
        "category": "Reporting",
        "intro": "How to sound professional when things go wrong.",
        "items": [
            ("Hiccup", "A small problem.", "We had a small hiccup with the deployment."),
            ("Roadblock", "A major barrier.", "The legal review is a roadblock."),
            ("Bottleneck", "Congestion point.", "Network speed is the bottleneck."),
            ("Glitch", "Temporary technical failure.", "It was just a temporary glitch."),
            ("Pain point", "A specific problem for users.", "Login is a major pain point for customers."),
            ("Root cause", "The core reason.", "We are investigating the root cause of the crash."),
            ("Issue", "Professional word for problem.", "We are facing an issue with the server."),
            ("Discrepancy", "Difference between two things.", "There is a discrepancy in the logs."),
            ("Red flag", "Warning sign.", "The silence from the vendor is a red flag."),
            ("Fire fighting", "Fixing urgent problems constantly.", "We are just fire fighting instead of building."),
        ]
    },
    17: {
        "title": "Solution Proposing",
        "category": "Problem Solving",
        "intro": "Don't just bring problems, bring solutions.",
        "items": [
            ("Workaround", "Temporary fix.", "We have a workaround until the patch is ready."),
            ("Patch", "Small fix.", "I'll submit a patch for that bug."),
            ("Remedy", "To solve/correct.", "How do we remedy this situation?"),
            ("Proposal", "Suggested plan.", "Here is my proposal for the new architecture."),
            ("Recommendation", "Advice on what to do.", "My recommendation is to switch vendors."),
            ("Action plan", "Steps to solve it.", "Let's draw up an action plan."),
            ("Think outside the box", "Creative solution.", "We need to think outside the box to solve this scaling issue."),
            ("Silver bullet", "A simple magic solution (usually doesn't exist).", "There is no silver bullet for security."),
            ("Band-aid", "Temporary, poor fix.", "Restarting the server is just a band-aid."),
            ("Sustainable", "Able to be maintained.", "We need a sustainable solution, not a hack."),
        ]
    },
    18: {
        "title": "Agreement Phrases",
        "category": "Collaboration",
        "intro": "Ways to say 'Yes' and show support.",
        "items": [
            ("On board", "Agree to participate.", "I'm on board with the new strategy."),
            ("Sign off", "Formal approval.", "I need your sign off on this budget."),
            ("Green light", "Permission to proceed.", "We got the green light to hire 2 devs."),
            ("Thumbs up", "Approval.", "I give this design a thumbs up."),
            ("Second that", "I agree with the previous speaker.", "I second that motion."),
            ("Makes sense", "Logical.", "That explanation makes sense to me."),
            ("Aligned", "In agreement/coordination.", "We are fully aligned on the goals."),
            ("Buy-in", "Support from stakeholders.", "We need to get buy-in from the marketing team."),
            ("Consensus", "General agreement.", "We reached a consensus on the color scheme."),
            ("Eye to eye", "Agreeing.", "We don't always see eye to eye, but we respect each other."),
        ]
    },
    19: {
        "title": "Disagreement (Polite)",
        "category": "Collaboration",
        "intro": "Disagree without being disagreeable.",
        "items": [
            ("I see it differently", "Polite disagreement.", "I see it differently; I think React is the better choice."),
            ("Play devil's advocate", "Testing the argument.", "Let me play devil's advocate: what if user growth stalls?"),
            ("Push back", "Resist.", "I have to push back on that feature."),
            ("Reservations", "Doubts.", "I have some reservations about using a beta library."),
            ("Beg to differ", "Polite formal disagreement.", "I beg to differ on that statistic."),
            ("Not necessarily", "Soft disagreement.", "That's not necessarily true in all cases."),
            ("Respectfully disagree", "Professional disagreement.", "I respectfully disagree with that assessment."),
            ("With all due respect", "Preface to disagreement (use carefully).", "With all due respect, that solution won't work."),
            ("My concern is", "Stating a problem.", "My concern is that this will slow down performance."),
            ("Let's agree to disagree", "Stop arguing.", "We're going in circles. Let's agree to disagree."),
        ]
    },
    20: {
        "title": "Clarification Requests",
        "category": "Communication",
        "intro": "Never guess. Ask clearly until you understand.",
        "items": [
            ("Elaborate", "Explain more.", "Can you elaborate on the third point?"),
            ("Specifics", "Details.", "Can you give me the specifics of the error?"),
            ("Clarify", "Make clear.", "Just to clarify, is the deadline Friday or Monday?"),
            ("In other words", "Rephrasing to check understanding.", "So in other words, we are canceling the project?"),
            ("Missed that", "Didn't hear/understand.", "Sorry, I missed that last part."),
            ("Come again?", "Repeat please.", "Could you come again? The audio cut out."),
            ("Break it down", "Simplify.", "Can you break it down for non-technical folks?"),
            ("What do you mean by...", "Asking for definition.", "What do you mean by 'heavy' load?"),
            ("Context", "Background info.", "Can you give me some context on this ticket?"),
            ("Example", "Show instance.", "Can you give me an example of that use case?"),
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
    
    # We need headers for all 100 modules to build the sidebar correctly
    # For now, we'll use a mix of real data and placeholder titles for 21-100
    # to maintain the visual structure the user expects.
    
    # Imports placeholders for sidebar generation ease
    # (In a real full script we'd carry the full list, here we simulate the next 80 for the specific sidebar view)
    
    # Helper to get title
    def get_title(num):
        if num in VOCAB_BATCH_1:
            return VOCAB_BATCH_1[num]["title"]
        return f"Module {num}" # Simpler fallback for this batch script since we are only writing 1-20 files

    for i in range(1, 101):
        num = i
        title = get_title(num)
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

# Execute update for modules 1-20
if __name__ == "__main__":
    output_dir = "pages/lessons/corporate-vocabulary"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Updating Modules 1-20 with REAL content...")
    
    for module_num, data in VOCAB_BATCH_1.items():
        filename = f"module-{module_num:03d}.html"
        filepath = os.path.join(output_dir, filename)
        
        html_content = generate_module_html(module_num, data)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Updated Module {module_num}: {data['title']}")
    
    print("\n✅ Successfully updated Modules 1-20 with real corporate vocabulary!")
