from typing import TypedDict, Annotated, List, Optional
from operator import add


class JobLead(TypedDict):
    company: str
    role: str
    jd_url: str
    jd_text: str
    match_score: Optional[float]


class OutreachRecord(TypedDict):
    company: str
    role: str
    email_sent: bool
    linkedin_sent: bool
    cold_email_body: str
    timestamp: str


class AgentState(TypedDict):
    # --- Input ---
    target_companies: List[str]          # ["Tata Elxsi", "Netradyne", "Minus Zero"]

    # --- Research phase output ---
    job_leads: Annotated[List[JobLead], add]   # agents append, never overwrite

    # --- Tailor phase output ---
    tailored_emails: Annotated[List[dict], add]

    # --- Outreach phase output ---
    outreach_log: Annotated[List[OutreachRecord], add]

    # --- Control flow ---
    current_company: Optional[str]       # which company is being processed right now
    errors: Annotated[List[str], add]    # any failures get logged here, not crash the system
    status: str                          # "researching" | "tailoring" | "sending" | "done"