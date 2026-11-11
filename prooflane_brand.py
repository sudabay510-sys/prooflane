from helpers import L, LM, opt, env_names

Q = [
    {"id": "genre", "type": "choice", "prompt": "What do you mostly photograph?",
     "options": [opt("wedding", "Weddings & elopements"), opt("portrait", "Portraits & families"), opt("brand", "Brand / headshots"), opt("product", "Product / e-commerce"), opt("events", "Events")]},
    {"id": "jobs", "type": "choice", "prompt": "How many paid shoots do you do in a typical month?",
     "options": [opt("1", "0–2"), opt("4", "3–6"), opt("8", "7–12"), opt("15", "13+")]},
    {"id": "leads", "type": "choice", "multi": True, "prompt": "Where do inquiries come from?", "help": "Select all that apply.",
     "options": [opt("ig", "Instagram"), opt("referral", "Referrals & past clients"), opt("google", "Google / website"), opt("directory", "Directories & vendor lists"), opt("venue", "Venues / planners")]},
    {"id": "weak", "type": "choice", "prompt": "Which stage leaks the most?",
     "options": [opt("inquiry", "Inquiry → reply (slow or no reply)"), opt("book", "Reply → booked (people go quiet)"), opt("prep", "Booked → shoot day (prep is chaotic)"), opt("deliver", "Shoot → delivery (late galleries)"), opt("after", "After delivery (no reviews/referrals)")]},
    {"id": "reply_time", "type": "choice", "prompt": "How fast do you usually reply to a new inquiry?",
     "options": [opt("hour", "Within an hour"), opt("day", "Same day"), opt("days", "1–3 days"), opt("week", "Sometimes longer")]},
    {"id": "contract", "type": "choice", "prompt": "How do contracts and deposits work today?",
     "options": [opt("tool", "A CRM / studio tool handles it"), opt("pdf", "PDF contract + manual invoice"), opt("informal", "Mostly informal / by message"), opt("none", "No consistent process")]},
    {"id": "turnaround", "type": "choice", "prompt": "Your typical gallery turnaround?",
     "options": [opt("1w", "Under 1 week"), opt("3w", "1–3 weeks"), opt("6w", "4–6 weeks"), opt("long", "Longer than 6 weeks")]},
    {"id": "voice", "type": "choice", "prompt": "How do you want to sound to clients?",
     "options": [opt("warm", "Warm & reassuring"), opt("editorial", "Editorial & refined"), opt("fun", "Fun & easygoing"), opt("direct", "Direct & professional")]},
    {"id": "hours", "type": "choice", "prompt": "Hours per week for admin (not editing)?",
     "options": [opt("1", "Under 2"), opt("3", "2–4"), opt("6", "5–8"), opt("10", "8+")]},
]


def plan(a):
    genre = L(Q[0]["options"], a.get("genre"))
    weak = a.get("weak", "inquiry")
    voice = L(Q[7]["options"], a.get("voice")).lower()
    leads = LM(Q[2]["options"], a.get("leads") or ["ig"])
    fix = {
        "inquiry": ["Write a 3-paragraph inquiry reply template (thanks → fit questions → next step).", "Check inquiries at two set times daily.", "Add a ‘still deciding?’ follow-up on day 3."],
        "book": ["Send a one-page ‘how booking works’ guide with every quote.", "Follow up on day 2 and day 7 with one helpful detail each.", "Offer a short call slot instead of long email threads."],
        "prep": ["Send a prep questionnaire 3 weeks out.", "Build a genre shot-list template you adapt per client.", "Confirm timeline, location, and contacts 72 hours before."],
        "deliver": ["Publish your turnaround in the contract and welcome email.", "Send a ‘sneak peek’ within 72 hours.", "Block culling and editing days on your calendar right after each shoot."],
        "after": ["Send a gallery-delivered email with care instructions.", "Ask for an honest review 7 days after delivery — no incentives that break platform rules.", "Add an anniversary / one-year check-in reminder."],
    }.get(weak)
    return {
        "title": f"ProofLane workflow plan — {genre}",
        "summary": f"Your weakest stage is {L(Q[3]['options'], weak).lower()}. Leads come from {leads}. Scripts are written to sound {voice}. This is a workflow plan — it doesn’t promise bookings or income.",
        "preview_sections": [
            {"title": "Fix your leakiest stage first", "bullets": fix},
            {"title": "Your 5-stage client timeline", "bullets": ["Inquiry: reply template + fit questions", "Booking: guide, contract, deposit step", "Prep: questionnaire + shot list", "Shoot day: 72-hour confirmation", "Delivery: sneak peek → gallery → review ask"]},
            {"title": "Contract note", "body": "Contract templates in the full plan are starting points only. Have a local attorney review your contract — ProofLane isn’t legal advice."},
        ],
        "locked_sections": [
            {"title": "Email script library", "teaser": "Inquiry, follow-up, booking, prep, delivery, and review-request scripts."},
            {"title": f"{genre} shot-list templates", "teaser": "Editable lists by session type."},
            {"title": "Delivery checklist", "teaser": "Culling, backup, gallery, and handoff steps."},
            {"title": "Seasonal booking calendar", "teaser": "When to open dates and send past-client notes."},
        ],
    }


BRAND = {
    "name": "ProofLane", "slug": "prooflane", "port": 5106,
    "tagline": "The inquiry-to-delivery workflow plan for independent photographers.",
    "eyebrow": "For independent photographers",
    "hero_title": "From first inquiry to final gallery — without dropped threads.",
    "hero_lede": "ProofLane asks about your genre, lead sources, and where clients slip away, then builds a stage-by-stage workflow with scripts and checklists.",
    "cta_primary": "Map my client workflow", "cta_short": "Start quiz",
    "cta_band_title": "You’re great behind the camera.",
    "cta_band_text": "Let the plan handle the follow-ups, prep, and delivery steps around it.",
    "honesty_line": "Workflow education only. No booking-volume or income guarantees.",
    "audience_line": "Wedding, portrait, brand, and product photographers who aren’t ready for a full CRM — or want a clear plan on top of one.",
    "personas": [
        {"title": "Newer pro", "text": "Booking a few shoots a month and making up the process each time."},
        {"title": "Busy season shooter", "text": "Great clients, chaotic inbox, late galleries."},
        {"title": "CRM owner", "text": "You have the tool — you need the order of operations."},
    ],
    "journey": [
        {"stage": "Inquiry", "pain": "Replies go out days late.", "fix": "A reply template and two daily inbox windows."},
        {"stage": "Booking", "pain": "Leads go quiet after the quote.", "fix": "A booking guide and day-2/day-7 follow-ups."},
        {"stage": "Shoot prep", "pain": "Last-minute timeline scrambles.", "fix": "Questionnaire + shot list + 72-hour confirm."},
        {"stage": "Delivery", "pain": "Galleries slip and reviews never come.", "fix": "Sneak-peek rule, delivery checklist, honest review ask."},
    ],
    "how_steps": [
        {"title": "Quiz your workflow", "text": "Genre, lead sources, turnaround, and weak stage."},
        {"title": "Preview your plan", "text": "Your leakiest stage fixed first, plus the full timeline."},
        {"title": "Start your plan", "text": "Enter your email, then complete checkout on Gumroad."},
    ],
    "features": [
        {"title": "Stage-by-stage timeline", "text": "Inquiry → booking → prep → shoot → delivery."},
        {"title": "Script library", "text": "Emails in your voice for every stage."},
        {"title": "Shot-list templates", "text": "By genre, ready to adapt."},
        {"title": "Seasonal packs", "text": "Subscription: booking calendars and refreshed scripts."},
    ],
    "sample_peek": ["2 daily inbox windows", "Day-2 and day-7 follow-ups", "72-hour shoot confirmation", "Sneak peek within 72 hours"],
    "trust_points": [
        {"title": "Not a CRM clone", "text": "A plan layer that works with whatever tools you use."},
        {"title": "Ethical review asks", "text": "No review gating or incentives that break platform rules."},
        {"title": "Contracts need a lawyer", "text": "Templates are starting points, not legal advice."},
    ],
    "faq": [
        {"q": "Do I need HoneyBook or another CRM?", "a": "No. ProofLane works with a CRM, a spreadsheet, or plain email."},
        {"q": "Will this book me more weddings?", "a": "We don’t promise bookings or income. The plan tightens the steps you control."},
        {"q": "Are the contract templates legally reviewed?", "a": "No. Treat them as outlines and have a local attorney review your contract."},
        {"q": "How does billing work?", "a": "Choose Monthly or Quarterly, save your email, then complete payment on Gumroad. Renews automatically. Cancel anytime from your Gumroad library."},
    ],
    "pricing": [
        {"id": "monthly", "name": "Monthly", "price": "$29", "period": "/ month",
             "intro": "$29", "renewal": "$29 / month", "renewal_note": "Renews automatically. Cancel anytime from your Gumroad library.",
             "includes": ['Workflow timeline', 'Script library', 'Delivery checklist']},
        {"id": "quarterly", "name": "Quarterly", "price": "$69", "period": "every 3 months",
             "intro": "$69", "renewal": "$69 every 3 months", "renewal_note": "Renews automatically. Cancel anytime from your Gumroad library.", "featured": True,
             "includes": ['Everything in Monthly', 'Genre shot-list packs', 'Seasonal booking calendar']},
    ],
    "checkout_url": "https://solvfix.gumroad.com/l/xugyi",
    "disclaimer_short": "Workflow education only. Not legal advice. No booking or income guarantees.",
    "disclaimer_long": "ProofLane provides general client-workflow education and templates for photographers. It is not affiliated with HoneyBook or any CRM. It does not guarantee inquiries, bookings, or income, and contract outlines are not legal advice — consult a licensed attorney. Payments are processed by Gumroad, not on this site.",
    "font_url": "https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,500;0,6..96,700;1,6..96,500&family=Work+Sans:wght@400;500;600&display=swap",
    "fonts": ("Cormorant Garamond", "Karla"),
    "questions": Q, "generate_plan": plan,
    "voice": "Quietly confident and editorial, like a seasoned second shooter who keeps everyone on time.",
    "palette": {"Background (ink)": "#141414", "Alt": "#1C1C1C", "Card": "#202020", "Text": "#F2EEE8", "Muted": "#A8A29A", "Accent (darkroom amber)": "#E3A857", "Accent hover": "#C98E3E"},
    "logo_svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none"><rect width="64" height="64" rx="10" fill="#E3A857"/><rect x="14" y="20" width="36" height="26" rx="5" stroke="#141414" stroke-width="3.5"/><circle cx="32" cy="33" r="7" stroke="#141414" stroke-width="3.5"/><path d="M24 20l3-5h10l3 5" stroke="#141414" stroke-width="3.5" stroke-linejoin="round"/></svg>',
    "css_vars": """
  --bg:#141414;--bg-alt:#1A1A1A;--card:#202020;--ink:#F2EEE8;--muted:#A8A29A;--line:#34302B;
  --accent:#E3A857;--accent-2:#C98E3E;--on-accent:#141414;--radius:4px;
  --font-display:'Cormorant Garamond', Georgia, serif;--font-body:'Karla', system-ui, sans-serif;
  --shadow-card:0 20px 50px rgba(0,0,0,.45);--shadow-btn:0 8px 22px rgba(227,168,87,.22);
  --cta-band-bg:#E3A857;--cta-band-ink:#141414;--cta-band-btn:#141414;--cta-band-btn-ink:#E3A857;--tracking:-0.01em;
""",
    "personality": "background:radial-gradient(800px 400px at 15% 0%, #3A2C1A 0%, transparent 60%), var(--bg);",
    "extra_css": "h1{font-weight:600;font-size:clamp(2.3rem,5vw,3.8rem)}.hero-card{border-color:#4A3D2C}.btn-ghost{color:var(--ink)}.flash{color:var(--ink)}.input{color:var(--ink)}",
    "dos": ["Use photographer vocabulary (cull, sneak peek, gallery).", "Keep the dark ‘darkroom’ look with amber highlights."],
    "donts": ["Imply affiliation with HoneyBook, Pixieset, or any CRM.", "Promise more weddings, bookings, or income."],
}
BRAND.update(env_names("prooflane"))
