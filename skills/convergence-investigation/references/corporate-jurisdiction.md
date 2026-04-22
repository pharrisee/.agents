# Corporate-Jurisdiction Verification — Footer Signal to Registry Confirmation

A common discovery pattern: secondary sources (press, social media, marketing copy) describe a company by its operational headquarters or its founders' location, while the legal entity is incorporated elsewhere. The website footer often discloses the legal entity name and suffix. That single character pattern — the entity suffix — can reframe the corporate story entirely.

## Why this matters

Companies are routinely described in the press by their operational headquarters, not their incorporation jurisdiction. The jurisdiction matters because:

- It governs which regulator has authority
- It affects which national security and disclosure frameworks apply
- It determines which corporate registry has officer / shareholder records
- It often reveals the route by which foreign investment was structured (cross-border VC frequently routes through tax-friendly intermediate jurisdictions)
- It may reveal a deliberate jurisdictional arbitrage (legal entity in one country to access its courts, operational base in another for talent or markets, IP holding in a third for tax)

When the operational and legal jurisdictions diverge, that gap is itself the finding worth investigating.

## The signal-to-confirmation pipeline

### Signal phase: identify the discrepancy

Look for legal entity designations in:

- Website footer copyright text (e.g., `© Company Name <Suffix>`)
- Privacy policy and Terms of Service — usually disclose the legal entity in the first paragraph
- Contact page — registered office address, often distinct from operational HQ
- Job postings — entity that pays the salary may differ from the operational HQ shown to customers
- App store listings — developer entity is the legal seller and is often different from the brand
- Press releases distributed via PR wire services — issuer entity is sometimes the parent, sometimes a subsidiary

Common entity suffixes and their jurisdictions:

| Suffix | Jurisdiction | Registry |
|--------|--------------|----------|
| Pte Ltd | Singapore | ACRA (BizFile+) |
| Pty Ltd | Australia | ASIC |
| Ltd / Limited | UK / many Commonwealth countries | Companies House (UK), or the relevant national registry |
| Inc. / Corp. | US (varies by state) | State Secretary of State + SEC if public |
| LLC | US (varies by state) | State Secretary of State |
| GmbH | Germany / Austria / Switzerland | Handelsregister (DE), Firmenbuch (AT), Handelsregister (CH) |
| BV | Netherlands | Kamer van Koophandel |
| SA / SAS / SARL | France | Infogreffe |
| AB | Sweden | Bolagsverket |
| AG | Germany / Switzerland | Handelsregister (DE) / Handelsregister (CH) |
| OÜ | Estonia | e-Business Register |
| HE / ΗΕ | Cyprus | Cyprus Department of Registrar |
| K.K. | Japan | Houmukyoku |
| Sdn Bhd | Malaysia | SSM |
| LLP | UK / India / others | Companies House (UK), MCA (India) |
| S.A. de C.V. | Mexico | Public Registry of Commerce |
| BVI Ltd | British Virgin Islands | BVI Financial Services Commission |

A discrepancy between secondary-source narrative ("US-based startup") and legal suffix ("Pte Ltd") is the signal.

### Confirmation phase: query the registry

Each major registry has a public lookup interface. Use `web_fetch` against:

- **Companies House (UK)** — https://find-and-update.company-information.service.gov.uk/ (fully free, very rich data including officers, filings, persons of significant control)
- **ASIC (Australia)** — https://connectonline.asic.gov.au/ (free company search)
- **ACRA (Singapore)** — https://www.acra.gov.sg/ (BizFile+ for paid records; some basic info free)
- **OpenCorporates** — https://opencorporates.com/ (aggregator across many jurisdictions, useful when registry is paywalled)
- **SEC EDGAR (US public companies)** — https://www.sec.gov/edgar/searchedgar/ (filings for SEC-registered entities)
- **Cyprus Department of Registrar** — https://efiling.drcor.mcit.gov.cy/ (officer searches; reveals nominee patterns)
- **InfoGreffe (France)** — https://www.infogreffe.fr/
- **Handelsregister (Germany)** — https://www.handelsregister.de/

Confirm:
- Legal name (exact spelling)
- Registration number
- Date of incorporation
- Registered office address
- Officer list (directors, secretary, beneficial owners)
- Filing history (annual returns, share allotments — these reveal funding rounds)
- Persons of Significant Control (UK) or beneficial owners (other jurisdictions)

If the registry is paywalled and OpenCorporates is incomplete, document the gap and tier the finding as `high` rather than `confirmed`.

### Pattern phase: detect nominee and shell structures

When the corporate verification reveals one of the following, flag it:

- **Nominee director patterns** — same person listed as director across many unrelated entities (often a corporate-services-provider individual whose name appears on dozens of unrelated company filings)
- **Shell hopping** — operational entity is in jurisdiction X, payments flow through entity in jurisdiction Y (often Delaware, Cyprus, or BVI), IP is held in jurisdiction Z
- **Sudden incorporation** — the legal entity was created shortly before a funding round or product launch, suggesting the structure was built specifically for that round
- **Mismatched parent/subsidiary** — public narrative claims independence but corporate records show ownership by a known parent
- **Officer turnover at suspicious times** — directors resigning en masse before a contentious announcement, or a single director added immediately before a transaction

These patterns matter because they often indicate either tax optimisation (mundane) or deliberate jurisdictional arbitrage (more significant). Distinguish based on context — many legitimate businesses use multi-jurisdictional structures for non-evasive reasons.

### Sole-trader and consultant entities

Not every limited company is a multi-jurisdictional play. A common legitimate pattern is the sole-practitioner consultant who incorporates a personal-services company:

- Single director who is also sole PSC / shareholder
- Registered office at home or accountant's address
- One or two SIC codes matching their profession
- Generic email address (often Gmail or similar) rather than a corporate domain
- Long, stable history without dramatic restructuring

This pattern is unremarkable on its own. Flag it only if combined with other signals (sudden formation, anomalous accounting, links to disputed activity).

## Output

Add to the report a "Corporate structure" subsection with:

- Legal entity name and number
- Jurisdiction
- Registered office
- Officer list (current; flag any nominee patterns)
- Funding history if visible from filings
- Discrepancy between operational narrative and legal structure (the headline finding if there is one) — or explicit note that no discrepancy exists

Add to graph:
- Entity as a node (`type: "concept"`, `category: "company"`)
- Jurisdiction as a property
- Officers as person nodes if they appear elsewhere in the project
- Edges from entity to officers and to parent/subsidiary entities

Confidence: `confirmed` for direct registry data; `high` for OpenCorporates aggregated data; `medium` for inferences about the *purpose* of the structure.

## Special case: when the entity won't confirm

If the company has no website, no registry presence, no filings — that itself is a finding. Document the negative result. Genuinely shell entities often look exactly like this. So do non-existent entities being impersonated for fraud.

## Special case: email addresses on personal domains

When a company contact email is on a personal domain (Gmail, Outlook.com, ProtonMail) rather than a corporate domain matching the business name, this is worth noting but is not by itself suspicious. Many legitimate sole-trader and small-business operations use personal email infrastructure to keep costs down. Treat as a contextual data point, not a red flag.
