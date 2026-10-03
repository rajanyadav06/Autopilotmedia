# Services Mega Menu & Dedicated Service Pages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a glassmorphic 3/3/2 mega menu for the "Services" navbar dropdown and generate 8 comprehensive, standalone dedicated service pages matching Autopilot Media's ultra-premium performance design system.

**Architecture:** 
- Desktop Mega Menu: A floating glassmorphic container (`backdrop-filter: blur(20px)`, dark translucent `#0d1114f2`, subtle lime borders, 3-column grid) anchored under "Services".
- Mobile Menu: Expandable accordion inside `.mobile-nav-drawer` revealing all 8 service links on tap.
- 8 Dedicated Service Pages: Standalone root-level HTML files sharing unified navbar, footer, lead forms, and service-tailored hero, deliverables, execution frameworks, and FAQs.

**Tech Stack:** Plain HTML5, Vanilla CSS3, Vanilla JavaScript (No frameworks/heavy external dependencies)

**Spec:** [docs/superpowers/specs/2026-09-29-services-mega-menu-and-dedicated-pages-design.md](file:///e:/Legit%20Global/Autimedia/docs/superpowers/specs/2026-09-29-services-mega-menu-and-dedicated-pages-design.md)

## Global Constraints
- Sequence of 8 Services in Mega Menu:
  - Column 1: (01) Performance Marketing, (02) Website Development, (03) Social Media Management
  - Column 2: (04) Content Creation, (05) SEO / AEO / GEO, (06) Influencer Marketing
  - Column 3: (07) AI Automation, (08) Landing Page & CRO (+ Enterprise Growth feature card)
- Root-level URLs:
  - `service-performance-marketing.html`
  - `service-website-development.html`
  - `service-social-media.html`
  - `service-content-creation.html`
  - `service-seo-aeo-geo.html`
  - `service-influencer-marketing.html`
  - `service-ai-automation.html`
  - `service-landing-page-cro.html`
- Unified Navbar CTA button: `<a href="contact.html" class="btn btn-primary btn-sm"><span>Talk to Expert</span><span class="arrow">→</span></a>` (Pill shaped, 14px font, glowing hover).
- Consistent logo across all pages with `width="180" height="34"`.

---

### Task 1: Mega Menu Styling & Responsive CSS

**Files:**
- Modify: `style.css`
- Modify: `courses.html` (internal `<style>`)
- Modify: `free-tools.html` (internal `<style>`)

- [ ] **Step 1: Add Mega Menu styles to `style.css`**
Add styles for `.nav-item-dropdown`, `.dropdown-chevron`, `.mega-menu`, `.mega-menu-grid`, `.mega-menu-col`, `.mega-menu-card`, `.mega-menu-card:hover`, `.mega-card-num`, `.mega-card-icon`, `.mega-card-title`, `.mega-card-desc`, `.mega-card-arrow`, `.mega-feature-card`, and mobile accordion styles (`.mobile-dropdown-toggle`, `.mobile-submenu`).

- [ ] **Step 2: Add matching Mega Menu styles to `courses.html` and `free-tools.html`**
Ensure `courses.html` and `free-tools.html` include the mega menu classes so hovering/opening works identically.

- [ ] **Step 3: Verify CSS syntax and classes**
Verify that all dropdown classes load without syntax errors.

---

### Task 2: Mega Menu Interactive JavaScript Engine

**Files:**
- Modify: `script.js`
- Modify: `courses.html` (internal `<script>`)
- Modify: `free-tools.html` (internal `<script>`)

- [ ] **Step 1: Add mobile accordion toggle logic to `script.js`**
Add event listener for `.mobile-dropdown-toggle` that smoothly toggles `.mobile-submenu.open` and animates the chevron.

- [ ] **Step 2: Add keyboard / touch accessibility for mega menu**
Add Escape key listener to close active mega menu and mobile submenus.

- [ ] **Step 3: Update `courses.html` and `free-tools.html` scripts**
Include the mobile accordion toggle handler in their script sections.

---

### Task 3: Implement Mega Menu HTML Across Existing 6 Pages

**Files:**
- Modify: `index.html:40-80`
- Modify: `about.html:50-95`
- Modify: `contact.html:55-100`
- Modify: `portfolio.html:70-115`
- Modify: `courses.html:665-715`
- Modify: `free-tools.html:665-715`

- [ ] **Step 1: Update desktop navbar "Services" in `index.html`**
Wrap "Services" in `.nav-item-dropdown` with trigger and `.mega-menu` 3-column grid containing 8 services and enterprise card. Update mobile drawer with accordion.

- [ ] **Step 2: Update `about.html`, `contact.html`, and `portfolio.html`**
Add identical mega menu HTML and mobile accordion to `about.html`, `contact.html`, and `portfolio.html`.

- [ ] **Step 3: Update `courses.html` and `free-tools.html`**
Add identical mega menu HTML and mobile accordion to `courses.html` and `free-tools.html`.

- [ ] **Step 4: Verify navigation links and tag balancing**
Run automated tag balance validator on all 6 updated pages.

---

### Task 4: Create Service Pages 1 & 2 (`Performance Marketing` & `Website Development`)

**Files:**
- Create: `service-performance-marketing.html`
- Create: `service-website-development.html`

- [ ] **Step 1: Build `service-performance-marketing.html`**
Include:
- Meta / OpenGraph tags and page title.
- Navbar with working Mega Menu and active state on Service 01.
- Hero: "Scale with Predictable Paid Acquisition (Meta & Google Ads)". 3 Stat pills: 4.8x Avg ROAS, ₹12Cr+ Scaled, -28% CAC.
- Deliverables Grid: Funnel Architecture, Creative Testing Engine, Attribution & Tracking, Daily Optimization & Budget Scaling.
- Process: 4-Step Engine (Audit & Tracking Fixes → Creative & Messaging → Launch & Scale → Weekly Sprints).
- High-conversion Consultation CTA Form.
- FAQ Section.
- Standard Footer.

- [ ] **Step 2: Build `service-website-development.html`**
Include:
- Hero: "Conversion-First Shopify & Custom Web Experiences". 3 Stat pills: +42% Avg CVR Uplift, <1.8s Load Speed, 100% Mobile Optimized.
- Deliverables Grid: Custom Shopify 2.0 Themes, High-Converting UI/UX, Speed & Performance Optimization, Conversion Tracking & Checkout CRO.
- Process: Wireframing → UX & Copywriting → Clean Development → QA & Conversion Launch.
- Consultation CTA Form, FAQs, Footer.

- [ ] **Step 3: Verify pages HTML and navigation**
Verify tag validity and asset paths.

---

### Task 5: Create Service Pages 3 & 4 (`Social Media Management` & `Content Creation`)

**Files:**
- Create: `service-social-media.html`
- Create: `service-content-creation.html`

- [ ] **Step 1: Build `service-social-media.html`**
Include:
- Hero: "Organic Social Systems That Build Audience Trust & Purchase Intent". 3 Stat pills: 3.4x Engagement Uplift, 12M+ Organic Views, 100% Brand-Aligned.
- Deliverables Grid: Content Calendar Strategy, Community Engagement & DMs, Platform-Specific Storytelling, Monthly Growth Analytics.
- Process: Brand Voice Discovery → Content Framework → Production & Scheduling → Community & Retention.
- Consultation CTA Form, FAQs, Footer.

- [ ] **Step 2: Build `service-content-creation.html`**
Include:
- Hero: "High-Impact Ad Creatives, Reels & Visuals Engineered to Convert". 3 Stat pills: 200+ Winning Hooks Tested, +38% CTR, 4K High-Production.
- Deliverables Grid: Performance Reels & UGC Direction, High-Converting Static Graphics, Motion Design & 3D Renders, Ad Copy & Hook Variations.
- Process: Angle Research → Scripting & Storyboarding → Production & Editing → Iteration from Ad Metrics.
- Consultation CTA Form, FAQs, Footer.

- [ ] **Step 3: Verify pages HTML and navigation**
Verify tag validity and asset paths.

---

### Task 6: Create Service Pages 5 & 6 (`SEO / AEO / GEO` & `Influencer Marketing`)

**Files:**
- Create: `service-seo-aeo-geo.html`
- Create: `service-influencer-marketing.html`

- [ ] **Step 1: Build `service-seo-aeo-geo.html`**
Include:
- Hero: "Rank Everywhere: Traditional Search, AI Overviews (AEO) & Generative Search (GEO)". 3 Stat pills: #1 AI Citations, +180% Organic Revenue, Zero Spam Links.
- Deliverables Grid: Generative Engine Optimization (GEO), AI Answer Engine Optimization (AEO), Technical SEO & Site Speed, Bottom-Funnel Intent Content.
- Process: AI Readiness Audit → Entity & Schema Mapping → High-Intent Content Production → AI Visibility Monitoring.
- Consultation CTA Form, FAQs, Footer.

- [ ] **Step 2: Build `service-influencer-marketing.html`**
Include:
- Hero: "ROI-Driven Creator & Influencer Collaborations Built for D2C Brands". 3 Stat pills: 500+ Verified Creators, 4.2x Blended Campaign ROAS, Full Whitelisting Rights.
- Deliverables Grid: Creator Sourcing & Vetting, Contract & Usage Rights Management, Performance Whitelisting (Meta Spark Ads), Attribution & Revenue Tracking.
- Process: Creator Persona Match → Outreach & Briefing → Quality Control & Approval → Paid Whitelisting Amplification.
- Consultation CTA Form, FAQs, Footer.

- [ ] **Step 3: Verify pages HTML and navigation**
Verify tag validity and asset paths.

---

### Task 7: Create Service Pages 7 & 8 (`AI Automation` & `Landing Page & CRO`)

**Files:**
- Create: `service-ai-automation.html`
- Create: `service-landing-page-cro.html`

- [ ] **Step 1: Build `service-ai-automation.html`**
Include:
- Hero: "Automate Repetitive Workflows, Lead Nurturing & Support with Custom AI Systems". 3 Stat pills: -70% Manual Ops Hours, 24/7 Instant Lead Qualification, Zero Data Leaks.
- Deliverables Grid: AI Customer Support & Chatbots, Lead Enrichment & CRM Sync, Automated Reporting Dashboards, Multi-Tool Zapier/Make Integrations.
- Process: Workflow Bottleneck Audit → AI Logic Architecture → Integration & Safe Sandbox Testing → Deployment & Monitoring.
- Consultation CTA Form, FAQs, Footer.

- [ ] **Step 2: Build `service-landing-page-cro.html`**
Include:
- Hero: "Turn More Clicks Into Customers with Data-Backed Funnels & CRO". 3 Stat pills: +36% Average Conversion Lift, 100+ A/B Tests Run, Full Heatmap & Session Tracking.
- Deliverables Grid: Custom Dedicated Landing Pages, A/B Testing & Multivariate Experiments, User Journey & Heatmap Analysis, Checkout & Cart Optimization.
- Process: Friction & Drop-Off Audit → Hypothesis & Wireframe → High-Velocity A/B Testing → Winner Rollout.
- Consultation CTA Form, FAQs, Footer.

- [ ] **Step 3: Verify pages HTML and navigation**
Verify tag validity and asset paths.

---

### Task 8: Full Site Verification & Quality Gate

**Files:**
- Inspect: All 14 HTML files (`index.html`, `about.html`, `contact.html`, `portfolio.html`, `courses.html`, `free-tools.html`, and 8 service pages)
- Inspect: `style.css` and `script.js`

- [ ] **Step 1: Run comprehensive HTML tag parser script across all 14 files**
Verify 0 unclosed tags, valid nesting, correct attribute quoting.

- [ ] **Step 2: Run link consistency checker**
Verify every link in the mega menu and navbar across all 14 pages points to an existing file or anchor without 404s.

- [ ] **Step 3: Verify mobile menu drawer and accordion behavior**
Verify mobile drawer toggle, submenu expand/collapse, and button interactions.
