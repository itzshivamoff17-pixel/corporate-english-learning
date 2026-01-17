#!/usr/bin/env python3
"""
Update Modules 21-40 with REAL Corporate Vocabulary Content
"""

import os

# Data for Modules 21-40
VOCAB_BATCH_2 = {
    21: {
        "title": "Time Management Vocab",
        "category": "Productivity",
        "intro": "Manage your time effectively and communicate your availability clearly.",
        "items": [
            ("Bandwidth", "The energy or mental capacity to deal with a situation.", "I don't have the bandwidth to take on another project right now."),
            ("Time block", "To schedule a specific time for deep work.", "I'm going to time block my afternoon for coding."),
            ("Prioritize", "To treat something as more important than other things.", "We need to prioritize the critical bugs over new features."),
            ("Crunch time", "A period of intense work just before a deadline.", "It's crunch time for the team as we approach the release."),
            ("Deep work", "Professional activities performed in a state of distraction-free concentration.", "I need two hours of deep work to finish this algorithm."),
            ("Procrastinate", "To delay or postpone action.", "Don't procrastinate on writing the documentation; do it now."),
            ("Schedule", "A plan for carrying out a process or procedure.", "Let's check the schedule to see if we're on track."),
            ("Deadline", "The latest time or date by which something should be completed.", "The deadline for the proposal is Friday at 5 PM."),
            ("Buffer", "Extra time allowed to deal with unexpected delays.", "We added a two-day buffer to the schedule just in case."),
            ("Efficiency", "Achieving maximum productivity with minimum wasted effort.", "We need to improve the efficiency of our meetings."),
        ]
    },
    22: {
        "title": "Resource Allocation",
        "category": "Project Management",
        "intro": "Assigning the right people and tools to the right tasks.",
        "items": [
            ("Allocate", "To distribute resources for a particular purpose.", "We need to allocate more RAM to the database server."),
            ("Resource leveling", "Smoothing out the usage of resources over time.", "We used resource leveling to avoid burning out the team."),
            ("Capacity planning", "Determining the production capacity needed to meet changing demands.", "Capacity planning shows we need to hire two more engineers."),
            ("Utilization", "The action of making practical and effective use of something.", "Server utilization is peaking at 90% during the day."),
            ("Constraint", "A limitation or restriction.", "Budget is the main constraint for this project."),
            ("Headcount", "The number of people employed.", "We got approval to increase headcount by three."),
            ("Burn rate", "The rate at which a company spends money.", "Our burn rate is too high; we need to cut costs."),
            ("Assets", "Items of value owned by the company.", "Our intellectual property is one of our biggest assets."),
            ("Optimization", "Making the best or most effective use of a resource.", "Resource optimization helped us reduce cloud costs by 20%."),
            ("Deployment", "The action of bringing resources into effective action.", "The deployment of the new team was swift and effective."),
        ]
    },
    23: {
        "title": "Risk Management Terms",
        "category": "Project Management",
        "intro": "Identify, assess, and control threats to your organization's capital and earnings.",
        "items": [
            ("Mitigate", "To make less severe or painful.", "We have a plan to mitigate the risk of data loss."),
            ("Contingency plan", "A plan designed to take account of a possible future event.", "Do we have a contingency plan if the API goes down?"),
            ("Assessment", "The evaluation of the nature, quality, or ability of someone or something.", "The security assessment revealed three vulnerabilities."),
            ("Exposure", "The state of being exposed to contact with something harmful.", "Our exposure to currency fluctuations is minimal."),
            ("Liability", "The state of being responsible for something, especially by law.", "We need to minimize our legal liability."),
            ("Compliance", "The action or fact of complying with a wish or command.", "We must ensure we are in compliance with GDPR."),
            ("Audit", "An official inspection of an individual's or organization's accounts.", "The annual security audit is scheduled for next month."),
            ("Forecast", "To predict or estimate.", "The risk forecast suggests high volatility in Q3."),
            ("Avoidance", "The action of keeping away from or not doing something.", "Risk avoidance is our primary strategy here."),
            ("Acceptance", "The action of consenting to receive or undertake something.", "Risk acceptance means we acknowledge the risk but choose to proceed."),
        ]
    },
    24: {
        "title": "Quality Assurance",
        "category": "Quality",
        "intro": "Ensuring your product meets the standards before it reaches the user.",
        "items": [
            ("Regression testing", "Re-running functional and non-functional tests to ensure previously developed and tested software still performs after a change.", "We need to run regression testing before the release."),
            ("Bug triage", "The process of reviewing and prioritizing reported bugs.", "Let's do a bug triage session to clean up the backlog."),
            ("Acceptance criteria", "Conditions that a software product must satisfy to be accepted by a user.", "Please review the acceptance criteria before writing code."),
            ("Code coverage", "A measure used to describe the degree to which the source code of a program is executed when a particular test suite runs.", "Our goal is 80% code coverage for the backend."),
            ("Edge case", "A problem or situation that occurs only at an extreme maximum or minimum operating parameter.", "Did you test the edge case where the input is null?"),
            ("Smoke test", "A preliminary test to reveal simple failures severe enough to reject a prospective software release.", "Run a smoke test to make sure the build handles basic operations."),
            ("Usability testing", "Evaluating a product or service by testing it with representative users.", "Usability testing showed that users couldn't find the logout button."),
            ("Benchmark", "A standard or point of reference against which things may be compared.", "We are using the competitor's speed as a benchmark."),
            ("Performance testing", "Testing the speed, responsiveness and stability of a computer, network, software program or device under a workload.", "Performance testing revealed a memory leak."),
            ("Sanity check", "A basic test to quickly evaluate whether a claim or the result of a calculation can possibly be true.", "Can you do a quick sanity check on these numbers?"),
        ]
    },
    25: {
        "title": "Code Review Language",
        "category": "Technical",
        "intro": "Phrases for giving and receiving constructive code feedback.",
        "items": [
            ("Nitpick", "A minor or trivial comment.", "Nitpick: There is an extra space here."),
            ("LGTM", "Looks Good To Me.", "Reviewed the changes. LGTM!"),
            ("Blocking", "A comment that must be addressed before merging.", "Blocking: This introduces a security vulnerability."),
            ("Refactor", "Restructuring existing computer code without changing its external behavior.", "We should refactor this function to be more readable."),
            ("DRY", "Don't Repeat Yourself principle.", "Let's apply DRY here and move this logic to a helper function."),
            ("Performance implication", "How a change affects speed/efficiency.", "Have you considered the performance implication of this loop?"),
            ("Follow-up", "Something to be done later.", "Let's add a TODO for a follow-up task to clean this up."),
            ("Consistency", "Conformity in the application of something.", "Please maintain consistency with the existing naming conventions."),
            ("Readability", "The ease with which a reader can understand a written text.", "Optimizing for readability is often better than clever one-liners."),
            ("Merge conflict", "When two branches have competing commits.", "I need to resolve the merge conflict before I can push."),
        ]
    },
    26: {
        "title": "Architecture Discussion",
        "category": "Technical",
        "intro": "Terms used when designing high-level system structures.",
        "items": [
            ("Monolith", "A single tiered software application in which usage, data access, and functionality are combined.", "The legacy app is a monolith that is hard to scale."),
            ("Microservices", "An architectural style that structures an application as a collection of services.", "We are breaking the monolith into microservices."),
            ("Scalability", "The capability of a system, network, or process to handle a growing amount of work.", "Vertical scalability has limits; we should look at horizontal scaling."),
            ("Latency", "The delay before a transfer of data begins following an instruction for its transfer.", "We need to reduce latency for our users in Asia."),
            ("Throughput", "The amount of material or items passing through a system or process.", "The new queue system increased our message throughput."),
            ("Redundancy", "The inclusion of extra components similar to those that failure would be fatal.", "We added improved redundancy to the database cluster."),
            ("Availability", "The probability that a system will work as required when required.", "Our SLA guarantees 99.9% availability."),
            ("Coupling", "The degree of interdependence between software modules.", "Loose coupling allows us to change components without breaking others."),
            ("Cohesion", "The degree to which the elements inside a module belong together.", "High cohesion makes the code easier to understand."),
            ("Trade-off", "A balance achieved between two desirable but incompatible features.", "The trade-off here is between consistency and availability (CAP theorem)."),
        ]
    },
    27: {
        "title": "Database Terminology",
        "category": "Technical",
        "intro": "Essential words for discussing data storage and retrieval.",
        "items": [
            ("Schema", "The organization or structure for a database.", "We need to update the schema to support the new user fields."),
            ("Index", "A data structure that improves the speed of data retrieval.", "Adding an index on the email column sped up the query by 10x."),
            ("Query", "A request for data or information from a database table or combination of tables.", "The reporting query is taking too long to run."),
            ("Transaction", "A unit of work performed against a database.", "Ensure the payment processing is wrapped in a transaction."),
            ("Normalization", "The process of organizing data in a database.", "Normalization reduces data redundancy."),
            ("Replication", "The process of copying data from one server to another.", "We use replication to ensure data safety if the primary falls."),
            ("Sharding", "Partitioning a database horizontally.", "We implemented sharding to handle the massive user growth."),
            ("ACID", "Atomicity, Consistency, Isolation, Durability.", "Our banking system relies on ACID compliance."),
            ("NoSQL", "Non-relational databases.", "We chose a NoSQL database for its flexible schema."),
            ("Migration", "Moving data from one system to another.", "The data migration will happen this weekend."),
        ]
    },
    28: {
        "title": "Cloud Computing Terms",
        "category": "Technical",
        "intro": "Vocabulary for the modern cloud infrastructure era.",
        "items": [
            ("SaaS", "Software as a Service.", "We are switching to a SaaS model for our product."),
            ("IaaS", "Infrastructure as a Service.", "AWS is our primary IaaS provider."),
            ("PaaS", "Platform as a Service.", "Using a PaaS like Heroku speeds up development."),
            ("Serverless", "A cloud computing execution model where the cloud provider runs the server.", "The image processing function is serverless."),
            ("Virtualization", "Creating a virtual version of something.", "Virtualization allows us to run multiple OSs on one server."),
            ("Elasticity", "The degree to which a system is able to adapt to workload changes.", "Cloud elasticity handles our traffic spikes automatically."),
            ("Provisioning", "Setting up IT infrastructure.", "Automated provisioning saves us hours of work."),
            ("Orchestration", "Automated configuration, coordination, and management of computer systems.", "Kubernetes is the standard for container orchestration."),
            ("Multi-cloud", "The use of multiple cloud computing and storage services.", "A multi-cloud strategy prevents vendor lock-in."),
            ("Edge computing", "Computing that is done at or near the source of the data.", "Edge computing reduces latency for IoT devices."),
        ]
    },
    29: {
        "title": "Security Vocabulary",
        "category": "Technical",
        "intro": "Critical terms for protecting systems and data.",
        "items": [
            ("Vulnerability", "A weakness which can be exploited.", "We need to patch the vulnerability in OpenSSL."),
            ("Exploit", "A piece of software, data or sequence of commands that takes advantage of a bug or vulnerability.", "The zero-day exploit affected millions of devices."),
            ("Encryption", "The process of converting information or data into a code.", "All data at rest must use AES-256 encryption."),
            ("Authentication", "The process or action of verifying the identity of a user or process.", "We are implementing multi-factor authentication (MFA)."),
            ("Authorization", "The function of specifying access rights/privileges to resources.", "Authentication is who you are; authorization is what you can do."),
            ("Phishing", "The fraudulent practice of sending emails purporting to be from reputable companies.", "The security training covers how to spot phishing emails."),
            ("Firewall", "A network security system that monitors and controls incoming and outgoing network traffic.", "The firewall blocks all traffic on port 22 except from our VPN."),
            ("Penetration testing", "Simulated cyber attack against your computer system to check for exploitable vulnerabilities.", "We hired a firm to conduct penetration testing."),
            ("Compliance", "Conforming to a rule, such as a specification, policy, standard or law.", "HIPAA compliance is mandatory for health data."),
            ("Breach", "An incident where data is inadvertently exposed.", "We must notify users within 72 hours of a data breach."),
        ]
    },
    30: {
        "title": "DevOps Terminology",
        "category": "Technical",
        "intro": "Bridging the gap between Development and Operations.",
        "items": [
            ("Pipeline", "A set of automated processes for software delivery.", "The deployment pipeline failed at the testing stage."),
            ("Artifact", "A byproduct produced during the development of software.", "The build artifact is stored in the registry."),
            ("Infrastructure as Code", "Managing and provisioning computer data centers through machine-readable definition files.", "We use Terraform for Infrastructure as Code (IaC)."),
            ("Continuous Integration", "The practice of merging all developers' working copies to a shared mainline several times a day.", "Continuous Integration catches bugs early."),
            ("Monitoring", "Observing the state of a system.", "We need better monitoring on the payment service."),
            ("Logging", "Recording events that happen in a system.", "Centralized logging helps us debug issues across services."),
            ("Rollback", "Reverting to a previous state.", "The deployment failed, initiating rollback now."),
            ("Canary release", "Rolling out software to a small subset of users first.", "We are doing a canary release to 5% of users."),
            ("Blue-green deployment", "A technique that reduces downtime and risk by running two identical production environments.", "Blue-green deployment allows zero-downtime updates."),
            ("Post-mortem", "An analysis of an event after it has occurred.", "Let's schedule a post-mortem to discuss the outage."),
        ]
    },
    31: {
        "title": "Agile Methodology",
        "category": "Methodology",
        "intro": "Terms for the iterative approach to project management.",
        "items": [
            ("Sprint", "A set period of time during which specific work has to be completed.", "We are in the middle of a two-week sprint."),
            ("Backlog", "A list of tasks required to support a larger strategic plan.", "We need to groom the backlog before the next planning session."),
            ("User story", "A tool used in Agile to capture a description of a software feature from an end-user perspective.", "As a user, I want to reset my password."),
            ("Epic", "A large body of work that can be broken down into a number of smaller stories.", "The user profile redesign is a large epic."),
            ("Velocity", "A measure of the amount of work a team can tackle during a single sprint.", "Our team velocity has increased over the last three sprints."),
            ("Stand-up", "A daily meeting for the team to sync up.", "See you at the daily stand-up at 10 AM."),
            ("Iterative", "Relating to or involving iteration, especially of a mathematical or computational process.", "We take an iterative approach to product design."),
            ("MVP", "Minimum Viable Product.", "Let's focus on the MVP features for now."),
            ("Stakeholder", "A person with an interest or concern in something.", "We need to keep the stakeholders informed."),
            ("Retrospective", "A meeting held after a product ships to discuss what happened during the product development and release process.", "We discussed the communication issues in the retrospective."),
        ]
    },
    32: {
        "title": "Scrum Terminology",
        "category": "Methodology",
        "intro": "Specific vocabulary for the Scrum framework.",
        "items": [
            ("Scrum Master", "The person responsible for ensuring the team adheres to Scrum theory, practice, and rules.", "Our Scrum Master removes blockers for the team."),
            ("Product Owner", "The person responsible for maximizing the value of the product.", "The Product Owner prioritizes the backlog items."),
            ("Sprint Planning", "A meeting where the team determines the product backlog items they will work on during that sprint.", "Sprint Planning is scheduled for Monday morning."),
            ("Daily Scrum", "A 15-minute time-boxed event for the Development Team.", "Keep the Daily Scrum short and focused."),
            ("Sprint Review", "A meeting to inspect the Increment and adapt the Product Backlog if needed.", "We will demo the new feature at the Sprint Review."),
            ("Increment", "The sum of all the Product Backlog items completed during a Sprint.", "The increment must be in useable condition."),
            ("Definition of Done", "A shared understanding of what it means for work to be complete.", "We need to update our Definition of Done to include unit tests."),
            ("Time-box", "A fixed period of time to accomplish a task.", "Let's time-box this discussion to 15 minutes."),
            ("Burndown Chart", "A graphical representation of work left to do versus time.", "The burndown chart shows we are ahead of schedule."),
            ("Impediment", "Anything that prevents a team member from performing work.", "Please raise any impediments immediately."),
        ]
    },
    33: {
        "title": "Sprint Planning",
        "category": "Agile",
        "intro": "Phrases for planning your work cycle.",
        "items": [
            ("Capacity", "The amount of work a team can undertake.", "Do we have the capacity to take on this extra card?"),
            ("Estimation", "Roughly calculating the effort required.", "We use story points for estimation."),
            ("Story point", "A unit of measure for expressing an estimate of the overall effort.", "This complex feature is an 8-pointer."),
            ("Scope creep", "Uncontrolled changes or continuous growth in a project's scope.", "We need to watch out for scope creep in this sprint."),
            ("Prioritization", "Arranging items in order of importance.", "Prioritization is key when resources are limited."),
            ("Carry over", "Work that was not completed in a sprint and moves to the next.", "We have two tickets carrying over from the last sprint."),
            ("Commitment", "The work the team agrees to completes.", "We don't want to over-commit and under-deliver."),
            ("Dependencies", "Relationships between tasks where one relies on another.", "We have a dependency on the UI team needed their part first."),
            ("Goal", "The objective to be met.", "The sprint goal is to finish the checkout flow."),
            ("Breakdown", "Splitting a task into smaller parts.", "Let's breakdown this story into sub-tasks."),
        ]
    },
    34: {
        "title": "Retrospective Phrases",
        "category": "Agile",
        "intro": "Reflecting on the past to improve the future.",
        "items": [
            ("What went well?", "Positive feedback.", "Let's start with what went well this sprint."),
            ("What could be improved?", "Constructive criticism.", "What processes could be improved next time?"),
            ("Action item", "Task to do.", "Let's create an action item to update the docs."),
            ("Kudos", "Praise and honor.", "Kudos to the dev team for the late-night fix."),
            ("Start, Stop, Continue", "A framework for feedback.", "What should we start doing, stop doing, and continue doing?"),
            ("Botched", "Messed up (informal).", "We botched the deployment, let's discuss why."),
            ("Improvement", "Getting better.", "Continuous improvement is our philosophy."),
            ("Transparent", "Open and honest.", "We need to be transparent about our failures."),
            ("Blameless", "Focusing on the process, not the person.", "This is a blameless post-mortem."),
            ("Root cause", "The main reason.", "The root cause was a misconfiguration."),
        ]
    },
    35: {
        "title": "Stakeholder Communication",
        "category": "Leadership",
        "intro": "Talking to the people who have a vested interest in the project.",
        "items": [
            ("Alignment", "Agreement and coordination.", "We need alignment across all stakeholders."),
            ("Expectations", "A strong belief that something will happen.", "Managing stakeholder expectations is crucial."),
            ("Update", "New information.", "I'll send a status update by EOD."),
            ("Concerns", "Anxiety or worry.", "Please address the client's concerns about security."),
            ("Roadmap", "A strategic plan that defines a goal or desired outcome.", "The feature is on the Q3 roadmap."),
            ("Milestone", "A significant stage or event.", "We hit a key milestone with the beta release."),
            ("Deliverable", "A tangible or intangible good or service produced.", "The design document is the key deliverable this week."),
            ("Feedback", "Information about reactions to a product.", "We incorporated the stakeholder feedback."),
            ("Sign-off", "Official approval.", "We are waiting for executive sign-off."),
            ("Transparency", "The condition of being transparent.", "Stakeholders appreciate transparency about delays."),
        ]
    },
    36: {
        "title": "Client Interaction",
        "category": "Client Relations",
        "intro": "Professional phrases for dealing with customers.",
        "items": [
            ("Onboarding", "The action or process of integrating a new people.", "The client onboarding process needs to be smoother."),
            ("Touchpoint", "Any point of contact between a buyer and a seller.", "The weekly call is a key touchpoint."),
            ("Pain point", "A specific problem.", "We are solving a major pain point for the client."),
            ("Value proposition", "An innovation, service, or feature intended to make a company or product attractive to customers.", "Our value proposition is speed and reliability."),
            ("Upsell", "To persuade a customer to buy something additional or more expensive.", "We managed to upsell them to the Enterprise plan."),
            ("Retention", "The continued possession, use, or control of something.", "Client retention is our top metric."),
            ("Churn", "The rate at which customers stop doing business with an entity.", "We need to reduce churn by improving support."),
            ("Satisfaction", "Fulfillment of one's wishes, expectations, or needs.", "Customer satisfaction scores are up."),
            ("Rapport", "A close and harmonious relationship.", "Building rapport with the client takes time."),
            ("Escalation", "Moving a situation to a higher level.", "Handle the escalation with care."),
        ]
    },
    37: {
        "title": "Vendor Management",
        "category": "Business",
        "intro": "Dealing with third-party suppliers and partners.",
        "items": [
            ("Procurement", "The action of obtaining or procuring something.", "Procurement has approved the new software license."),
            ("SLA", "Service Level Agreement.", "The vendor missed the SLA for uptime."),
            ("Contract", "A written or spoken agreement.", "Review the contract terms before signing."),
            ("Negotiation", "Discussion aimed at reaching an agreement.", "We are in negotiation for a better rate."),
            ("Vendor lock-in", "Dependency on a single supplier.", "We want to avoid vendor lock-in with AWS."),
            ("Outsourcing", "Obtaining (goods or a service) from an outside or foreign supplier.", "We are outsourcing the QA testing."),
            ("RFP", "Request for Proposal.", "We sent out an RFP to three vendors."),
            ("Evaluated", "Form an idea of the amount, number, or value of; assess.", "We evaluated three different tools."),
            ("Compliance", "The state of being in accordance with established guidelines.", "Ensure the vendor meets our security compliance standards."),
            ("Renewal", "The action of extending the period of validity.", "The contract renewal is coming up next month."),
        ]
    },
    38: {
        "title": "Budget Discussion",
        "category": "Finance",
        "intro": "Talking about money and resources professionally.",
        "items": [
            ("Allocation", "The action or process of allocating or distributing something.", "The budget allocation for marketing has increased."),
            ("Forecast", "A prediction or estimate of future events.", "The financial forecast looks promising."),
            ("Quarterly", "Done, produced, or occurring once every quarter of a year.", "We review the budget quarterly."),
            ("Fiscal year", "A year as reckoned for taxing or accounting purposes.", "The fiscal year ends in March."),
            ("ROI", "Return on Investment.", "What represents the ROI of this new tool?"),
            ("Cost-benefit analysis", "A systematic approach to estimating the strengths and weaknesses of alternatives.", "We did a cost-benefit analysis before buying."),
            ("Overhead", "Business expenses not directly attributed to creating a product or service.", "We need to reduce our overhead costs."),
            ("Capital expenditure (CapEx)", "Money spent by a business or organization on acquiring or maintaining fixed assets.", "Servers are a major CapEx."),
            ("Operating expenditure (OpEx)", "Money a business spends on an ongoing, day-to-day basis.", "Cloud costs are considered OpEx."),
            ("Variance", "The fact or quality of being different, divergent, or inconsistent.", "There is a variance between the budget and actual spend."),
        ]
    },
    39: {
        "title": "ROI & Metrics",
        "category": "Analytics",
        "intro": "Measuring success using data.",
        "items": [
            ("KPI", "Key Performance Indicator.", "Our main KPI is daily active users."),
            ("Metric", "A system or standard of measurement.", "We need to define the success metrics."),
            ("Benchmark", "A standard or point of reference against which things may be compared.", "Our load time is below the industry benchmark."),
            ("Conversion rate", "The percentage of users who take a desired action.", "We improved the signup conversion rate by 5%."),
            ("Dashboard", "A graphical user interface that often provides at-a-glance views of key performance indicators.", "Check the analytics dashboard for real-time data."),
            ("Analytics", "The systematic computational analysis of data or statistics.", "Analytics show a drop in engagement."),
            ("Heatmap", "A representation of data in the form of a map or diagram in which data values are represented as colors.", "The heatmap shows users aren't clicking the button."),
            ("Funnel", "A model describing the various stages of a prospect's journey.", "Where are users dropping off in the sales funnel?"),
            ("Engagement", "The fact of being occupied or having one's attention captured.", "User engagement is higher on mobile."),
            ("Bounce rate", "The percentage of visitors to a particular website who navigate away from the site after viewing only one page.", "A high bounce rate indicates irrelevant content."),
        ]
    },
    40: {
        "title": "Performance Review",
        "category": "HR",
        "intro": "Discussing your work performance with your manager.",
        "items": [
            ("Evaluation", "The making of a judgment about the amount, number, or value of something; assessment.", "The annual performance evaluation is scheduled."),
            ("Feedback", "Information about reactions to a product, a person's performance of a task, etc.", "I appreciate the constructive feedback."),
            ("Goal setting", "The process of identifying something that you want to accomplish and establishing measurable goals and timeframes.", "Let's work on goal setting for next year."),
            ("Self-assessment", "Assessment or evaluation of oneself or one's actions and attitudes.", "Please complete your self-assessment by Friday."),
            ("Strengths", "A good or beneficial quality or attribute of a person or thing.", "Analytical thinking is one of your key strengths."),
            ("Weaknesses", "A quality or feature regarded as a disadvantage or fault.", "Public speaking is a weakness I want to improve."),
            ("Promotion", "Activity that supports or provides active encouragement for the furtherance of a cause, venture, or aim.", "We are discussing your promotion to Senior Engineer."),
            ("Raise", "An increase in salary.", "A performance-based raise was approved."),
            ("Career path", "A sequence of jobs that leads to your short- and long-term career goals.", "Let's discuss your career path within the company."),
            ("Mentorship", "The guidance provided by a mentor, especially an experienced person in a company or educational institution.", "I would like more mentorship opportunities."),
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
    
    # Helper to get title - using a wider range logic would be better in a full app, 
    # but strictly for this script's context to generate valid sidebar links:
    # We will just generate generic titles for non-batch items to keep the script simple 
    # but functional for the sidebar links
    
    for i in range(1, 101):
        num = i
        title = f"Module {num}" # Default
        
        # If in current batch, use real title
        if num in VOCAB_BATCH_2:
            title = VOCAB_BATCH_2[num]["title"]
            
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

# Execute update for modules 21-40
if __name__ == "__main__":
    output_dir = "pages/lessons/corporate-vocabulary"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Updating Modules 21-40 with REAL content...")
    
    for module_num, data in VOCAB_BATCH_2.items():
        filename = f"module-{module_num:03d}.html"
        filepath = os.path.join(output_dir, filename)
        
        html_content = generate_module_html(module_num, data)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Updated Module {module_num}: {data['title']}")
    
    print("\n✅ Successfully updated Modules 21-40 with real corporate vocabulary!")
