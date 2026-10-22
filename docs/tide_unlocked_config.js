/*
  UNLOCKED · Challenge 2 of the RMIT hackathon.

  Operational details live at the top of this file. Leave a value as null until
  it is confirmed: the page hides anything that is null instead of showing an
  empty player or a dummy link.
*/
window.UNLOCKED = {
  "title": "UNLOCKED",
  "challengeLabel": "Challenge 2",
  "eventName": "RMIT hackathon",
  "year": 2026,

  /* One support destination, used everywhere on the page. Ideally an invite that opens #support. */
  "discordUrl": "https://discord.gg/XBMd9ny2q5",
  /* Optional. Only add confirmed support hours, clinics or booking links. e.g. { "text": "Mentor clinic, 2–4 pm", "url": "https://…" } */
  "supportSessions": [],

  "submission": {
    "formUrl": "https://forms.gle/HRHYjnqB86j1LFS97",
    /*
      Industry challenge deadlines, one per city. zones = time-zone prefixes that pick
      which city the countdown follows for a viewer; the first city is the fallback.
    */
    "deadlineCities": [
      { "name": "Melbourne", "timeZone": "Australia/Melbourne", "deadlineIso": "2026-10-23T10:00:00+11:00", "showZone": true, "zones": ["Australia/"] },
      { "name": "Vietnam", "timeZone": "Asia/Ho_Chi_Minh", "deadlineIso": "2026-10-22T18:00:00+07:00", "zones": ["Asia/Ho_Chi_Minh", "Asia/Saigon"] },
      { "name": "Malaysia", "timeZone": "Asia/Kuala_Lumpur", "deadlineIso": "2026-10-22T18:00:00+08:00", "zones": ["Asia/Kuala_Lumpur", "Asia/Kuching"] }
    ]
  },

  /*
    Videos open in an overlay from the hero (and the build kit, for the walkthrough).
    { "url": "https://www.youtube.com/watch?v=…", "title": "…" }. While url is null the button shows "Coming soon".
  */
  "launchVideo": { "url": "https://youtu.be/gHlev6-kB3I", "title": "UNLOCKED launch" },
  "walkthroughVideo": { "url": "https://youtu.be/z0o-B3258Cg", "title": "Walkthrough: Tide’s MCP with Claude Code in VS Code" },

  /* Hackbot, the UNLOCKED assistant. Set apiUrl to null to hide it. Keep it on tide.org's /api/chat proxy: the Function App rejects direct calls (401). */
  "chat": {
    "apiUrl": "/api/chat",
    "context": "unlocked",
    /*
      "send" questions go straight to Hackbot. "prefill" ones need the student's own details,
      so they fill the message box for the student to finish instead of sending.
    */
    "suggestions": [
      { "label": "Pressure-test our idea", "prefill": "Pressure-test our idea. We want to build " },
      { "label": "What's due, and when?", "send": "What's due, and when?" },
      { "label": "What should our two-minute demo show?", "send": "What should our two-minute demo show?" },
      { "label": "Tighten our README project overview", "prefill": "Help us tighten our README project overview:\n\n" }
    ]
  },

  /* README template extras. GitHub marks README links nofollow, so these are for visibility and attribution (UTM). */
  "readmeLink": "https://tide.org/tidecloak?utm_source=github&utm_medium=readme&utm_campaign=unlocked",
  "readmeBadge": "https://tide.org/badges/built-with-tidecloak.svg",

  "inspirationIdeas": [
    {
      "name": "Care Passport",
      "tags": [
        "Health",
        "Selective disclosure"
      ],
      "icon": "plus",
      "summary": "Share selected health records with specific clinicians, with the patient controlling access.",
      "idea": "A patient-controlled health-record app. Using synthetic records, let patients share a referral, pathology result or care plan with a particular clinician.",
      "barrier": "Getting care across providers often means handing over more of your history than each provider needs, and trusting another service with the whole collection.",
      "tide": "Session-bound end-to-end encryption and clinician roles can keep records unreadable to the operator. The patient controls which records each clinician can decrypt.",
      "demo": "Give a GP one record and a physio another. Withdraw the physio’s future access and show the next decryption request being refused."
    },
    {
      "name": "Research Consent Vault",
      "tags": [
        "Research",
        "Consent"
      ],
      "icon": "flask",
      "summary": "Let participants share research data with approved researchers and withdraw future access.",
      "idea": "A research portal where participants contribute synthetic datasets, survey responses or documents and consent to specific researchers using them.",
      "barrier": "Contributing sensitive information can mean losing visibility into who may use it and whether consent still applies.",
      "tide": "Encrypted contributions and authenticated researcher roles can tie access to active consent, without giving the platform unrestricted plaintext access.",
      "demo": "Approve a researcher, open the permitted contribution, then withdraw consent and show that future access is blocked."
    },
    {
      "name": "Rental Application Passport",
      "tags": [
        "Housing",
        "Privacy"
      ],
      "icon": "home",
      "summary": "Reuse rental documents and disclose only what each property manager needs.",
      "idea": "A reusable renter profile for proof of income, references and identification. Share only the documents needed for a specific application.",
      "barrier": "Every rental application can create another complete copy of an applicant’s sensitive documents in someone else’s inbox or database.",
      "tide": "Documents can remain encrypted and open only to authorised recipients. The platform does not need a master capability to read every applicant file.",
      "demo": "Share income evidence with one property manager and references with another. Show that neither can open the other package."
    },
    {
      "name": "Blind Portfolio Review",
      "tags": [
        "Education",
        "Fairness"
      ],
      "icon": "eye",
      "summary": "Review work before revealing identity, with access controlled by the stage of the review.",
      "idea": "A staged recruitment or education review. Reviewers first see work samples and criteria; authorised staff reveal identity only at the appropriate stage.",
      "barrier": "Identity fields hidden in a screen may still be readable by the backend or an overprivileged reviewer.",
      "tide": "Role-based access to encrypted fields can make the review stage determine what a reviewer can actually decrypt.",
      "demo": "Review a portfolio anonymously. Try opening its identity fields early, then advance the process and reveal them to the permitted role."
    },
    {
      "name": "Unreleased",
      "tags": [
        "Creative work",
        "Collaboration"
      ],
      "icon": "play",
      "summary": "Share unreleased creative work with collaborators without giving the platform access to every asset.",
      "idea": "A preview workspace for musicians, filmmakers, designers and agencies. Invite collaborators to individual projects and choose which assets each person may open.",
      "barrier": "Creative collaboration puts valuable unreleased work in services that may have universal access to the content.",
      "tide": "End-to-end encryption and role-aware access let the service coordinate collaboration without needing universal decryption authority.",
      "demo": "Invite a reviewer to one unreleased track. Show that other tracks stay unreadable, including from an operator account."
    },
    {
      "name": "Supplier Evidence Exchange",
      "tags": [
        "Industry",
        "Cooperation"
      ],
      "icon": "box",
      "summary": "Give customers and auditors access to different packages of supplier evidence.",
      "idea": "A B2B portal where suppliers share certifications, audit evidence or manufacturing documents with selected customers and independent auditors.",
      "barrier": "Proving compliance can require commercially sensitive evidence to be placed in a broadly accessible shared data room.",
      "tide": "Cross-organisation identity, scoped authorisation and encrypted evidence can limit each recipient to their package. Quorum governance can protect sensitive permission changes.",
      "demo": "Open a customer-specific evidence package, then switch to an auditor with a different scope. Attempt to widen access with a single administrator."
    },
    {
      "name": "Matter Room",
      "tags": [
        "Professional services",
        "Authority"
      ],
      "icon": "file",
      "summary": "Bring clients, lawyers and experts into a matter with different access to its documents.",
      "idea": "A legal or professional-services workspace for one matter. Clients, lawyers, experts and counterparties receive different access to evidence and deal documents.",
      "barrier": "A powerful platform administrator can become a shortcut to confidential documents or to rewriting who may access them.",
      "tide": "Encrypted document access, tamper-resistant authorisation and quorum-governed changes can separate administration from authority over everyone’s data.",
      "demo": "Request access to a sensitive brief. Show that an admin account alone can neither open it nor silently rewrite the required roles."
    },
    {
      "name": "Dual-Control Expense Desk",
      "tags": [
        "Finance",
        "Shared approval"
      ],
      "icon": "check",
      "summary": "Require designated approvals for high-value expenses and protect who can become an approver.",
      "idea": "An expense workflow for high-value requests, evidence and designated approvers. Mock the payment rail and focus on the final authorised action.",
      "barrier": "An approval process is fragile if one administrator can promote themselves into the approver role.",
      "tide": "TideCloak can protect approver identities and roles. Quorum governance can prevent one compromised administrator from manufacturing the authority to approve.",
      "demo": "Submit a mock high-value payment and collect the required approvals. Try bypassing the process by changing a role with one administrator."
    },
    {
      "name": "Guild Treasury",
      "tags": [
        "Gaming",
        "Community"
      ],
      "icon": "star",
      "summary": "Manage shared community credits and purchases without giving one moderator control.",
      "idea": "A community treasury for fictional credits, shared purchases or scarce digital items. Members propose spending and officers review high-value actions.",
      "barrier": "A group’s shared resources can depend on trusting a single powerful moderator or administrator.",
      "tide": "Tamper-resistant roles and quorum governance can protect sensitive role changes, so one administrator cannot quietly give themselves treasury authority.",
      "demo": "Propose a purchase in fictional credits, collect officer approvals, then show an attempted unilateral privilege change failing."
    },
    {
      "name": "Coalition Intel Exchange",
      "tags": [
        "Public sector",
        "Selective release"
      ],
      "icon": "globe",
      "summary": "Share synthetic reports across fictional agencies according to release rules.",
      "idea": "An entirely fictional intelligence-sharing platform using synthetic reports and agencies. Attach release rules such as AUS only or AUS/NZ.",
      "barrier": "Discovering that a report exists should not automatically grant access to its contents. Cross-agency sharing needs more than a shared login.",
      "tide": "Encrypted reports, roles and policy-driven access can make release rules enforceable. Quorum governance can protect changes to sensitive permissions.",
      "demo": "Let partner analysts discover a report, then show that only the permitted organisation and role can open it. Use synthetic material throughout."
    },
    {
      "name": "CreatorVault",
      "tags": [
        "Creators",
        "Entitlements"
      ],
      "icon": "diamond",
      "summary": "Release encrypted creator content according to a subscriber’s entitlement.",
      "idea": "A creator subscription app with public posts, subscriber-only content and individually unlocked files. Use mocked subscriptions and purchases.",
      "barrier": "Premium content often depends on hidden URLs or a backend flag while the platform retains full access to every asset.",
      "tide": "Encrypted content can be released only to authenticated users with the right entitlement. The operator does not need universal plaintext access.",
      "demo": "Unlock a premium file through a mock purchase, then remove the entitlement and block future decryption requests."
    },
    {
      "name": "Community Ballot",
      "tags": [
        "Community decisions",
        "Shared governance"
      ],
      "icon": "ballot",
      "summary": "Help communities vote without giving one operator control over the election.",
      "idea": "A voting app for student societies, community groups or boards. Verify eligibility, accept one private ballot per member, and require shared approval for sensitive changes and opening the count.",
      "barrier": "Voters often have to trust one server and a handful of operators with voter records, ballots, election rules and the result.",
      "tide": "TideCloak can bind ballot submission and tally access to the right identity, role and policy. Quorum governance protects changes to those permissions, while authentication avoids a central password-hash store. Your app keeps voter identities separate from encrypted ballots and implements duplicate-vote checks and a verifiable audit trail.",
      "demo": "Run a mock student-society vote. Reject a second ballot and a lone administrator’s attempt to change eligibility or count early. Collect the required approvals, then show the result and audit trail without revealing individual choices."
    }
  ],
  /* Judging criteria. Each readmePrompt appears in the README Project overview requirement. */
  "criteria": [
    {
      "weight": 25,
      "title": "Vision & originality",
      "description": "A fresh, ambitious answer to the challenge.",
      "readmePrompt": "What new product, service, experience or way of working are you proposing? What makes your idea distinctive?"
    },
    {
      "weight": 20,
      "title": "Trust constraint insight",
      "description": "Show exactly what trust, privacy, custody or authority prevents today.",
      "readmePrompt": "What is difficult, risky or impossible today because trust, privacy or security gets in the way? Explain what becomes possible when that constraint is removed."
    },
    {
      "weight": 20,
      "title": "Value & impact",
      "description": "Create meaningful value for people, organisations or society.",
      "readmePrompt": "Who would benefit, and how would their lives or work improve? Give a concrete example of why this matters."
    },
    {
      "weight": 20,
      "title": "Why TideCloak matters",
      "description": "Show how TideCloak materially changes what your product can credibly do.",
      "readmePrompt": "How does your application use TideCloak, and how does that integration help enable your idea? Connect the technology to the possibility you are demonstrating."
    },
    {
      "weight": 15,
      "title": "Prototype & storytelling",
      "description": "Make the idea understandable and show it working.",
      "readmePrompt": "What does your prototype demonstrate today? Describe the key interaction judges should look for."
    }
  ],
  /* group "build" = building with TideCloak (shown first). group "think" = reading, shown as story cards: add image (thumbnail) and source. */
  "resources": [
    {
      "group": "think",
      "source": "Tide blog · Start here",
      "image": "/unlocked/assets/story-emergent-authority.webp",
      "name": "Beyond cybersecurity: how to think about Emergent Authority",
      "text": "The best explanation of Emergent Authority, and the kinds of products it opens up.",
      "url": "https://tide.org/blog/emergent-authority-beyond-cybersecurity"
    },
    {
      "group": "think",
      "source": "Tide blog",
      "image": "/unlocked/assets/story-rmit-presentation.webp",
      "name": "How Tide works: the RMIT presentation",
      "text": "More inspiration: Emergent Authority in the AI era.",
      "url": "https://tide.org/blog/cyber-immunity-emergent-authority-ai-era"
    },
    {
      "group": "build",
      "name": "TideCloak overview",
      "text": "What TideCloak gives your app, in plain terms.",
      "url": "https://tide.org/tidecloak"
    },
    {
      "group": "build",
      "name": "TideCloak documentation",
      "text": "Background and reference for when you want the detail.",
      "url": "https://docs.tide.org/"
    }
  ],
  "faqs": [
    {
      "question": "Do I need cybersecurity or cryptography experience?",
      "answer": "No. You need an idea and a willingness to build it. Your coding agent does the integration work with Tide’s MCP; you focus on what your app makes possible."
    },
    {
      "question": "Can I use AI coding tools?",
      "answer": "Yes, that’s the intended workflow. Our walkthrough uses Claude Code in VS Code, but any coding agent that supports MCP works. The setup page lists them."
    },
    {
      "question": "Do I have to use Tide’s MCP?",
      "answer": "No. If the MCP isn’t working well with your model or tools, or you’d rather wire things up yourself, start from the TideCloak Quickstart. It sets up a working template site with TideCloak already integrated, and you build your idea on top.",
      "link": {
        "href": "#plan-b",
        "label": "Use the Quickstart"
      }
    },
    {
      "question": "Can we use synthetic or mocked data?",
      "answer": "Yes. For health, finance, government and other sensitive scenarios, you should. Mock external systems such as payment rails or record systems, and focus on proving the experience."
    },
    {
      "question": "How complete does the prototype need to be?",
      "answer": "Small, but working, with TideCloak integrated. Focus on one convincing demonstration of the new possibility. A finished product isn’t expected."
    },
    {
      "question": "Do we have to use one of the example ideas?",
      "answer": "No. The examples are inspiration, not tracks. Original ideas from domains nobody else has considered are welcome."
    },
    {
      "question": "What do we submit, and when?",
      "answer": "Submit through the Google Form with a link to your public GitHub repository. The repository holds your code and your two-minute demo video as an .mp4 file. Your README must start with a Project overview that answers the five judging prompts. Industry challenge entries close at 10:00 am AEDT on Friday 23 October 2026 in Melbourne, and at 6:00 pm local time on Thursday 22 October 2026 in Vietnam and Malaysia.",
      "link": {
        "href": "#submit",
        "label": "What to submit"
      }
    },
    {
      "question": "What should we avoid?",
      "answer": "Don’t make the project mainly a login demo, a security tool or a generic access-control dashboard. Show what becomes newly possible for the people using it."
    },
    {
      "question": "Where do I get help?",
      "answer": "For code and integration, ask your coding agent: Tide’s MCP gives it the TideCloak tools and instructions. For setup problems, ask on the Tide Discord. For ideas and challenge questions, ask Hackbot.",
      "discord": true
    }
  ]
};
