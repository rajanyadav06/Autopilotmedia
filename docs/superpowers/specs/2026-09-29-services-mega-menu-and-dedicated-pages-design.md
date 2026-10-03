# Services Mega Menu & Dedicated Service Pages — Design Specification

**Date:** 2026-09-29  
**Status:** Approved by User  
**Brand Identity:** Autopilot Media  
**Stack:** Plain HTML5, Vanilla CSS3, Vanilla JavaScript (No heavy third-party libraries)

---

## 1. Executive Summary

This project delivers:
1. **Interactive Mega Menu on "Services" in Navbar:**
   - Desktop: Smooth hover-triggered floating glassmorphic container (`backdrop-filter: blur(20px)`, dark surface `#0d1114`, lime borders).
   - Sequence: **3 / 3 / 2 Grid Sequence** displaying all 8 core services:
     - **Column 1:**
       1. Performance Marketing (`service-performance-marketing.html`)
       2. Website Development (`service-website-development.html`)
       3. Social Media Management (`service-social-media.html`)
     - **Column 2:**
       4. Content Creation (`service-content-creation.html`)
       5. SEO / AEO / GEO (`service-seo-aeo-geo.html`)
       6. Influencer Marketing (`service-influencer-marketing.html`)
     - **Column 3:**
       7. AI Automation (`service-ai-automation.html`)
       8. Landing Page & CRO (`service-landing-page-cro.html`)
       - *Plus Enterprise Growth CTA Card:* Fast direct route to founders for custom enterprise solutions.
   - Mobile: Expandable accordion inside the existing sliding mobile drawer with smooth chevron indicator.
2. **8 Dedicated Service Pages:**
   - Standalone root-level HTML pages implementing the brand's ultra-premium performance agency aesthetic.
   - Unified shared header, footer, interactive lead forms, and service-tailored copy and deliverables.

---

## 2. Navigation & Mega Menu Architecture

### 2.1 Desktop Interaction
- The `Services` navigation item becomes a parent menu wrapper `.nav-item-dropdown`.
- Contains:
  - Trigger link `<a href="index.html#services" class="nav-link nav-dropdown-trigger">Services <svg class="dropdown-chevron">...</svg></a>`
  - Dropdown container `.mega-menu` (`opacity: 0`, `visibility: hidden`, `transform: translateY(10px)`, `transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1)`).
- On `:hover` (with intent delay buffer to prevent flicker), `.mega-menu` becomes visible (`opacity: 1`, `visibility: visible`, `transform: translateY(0)`).
- Visual Design:
  - Width: ~960px, centered below the navbar container.
  - Background: `rgba(13, 17, 20, 0.96)` with `backdrop-filter: blur(20px)`.
  - Border: `1px solid rgba(255, 255, 255, 0.1)`.
  - Box Shadow: `0 24px 60px rgba(0, 0, 0, 0.6), 0 0 30px rgba(200, 255, 0, 0.05)`.
  - 3-column CSS Grid (`grid-template-columns: 1fr 1fr 1fr; gap: 16px; padding: 24px;`).

### 2.2 Mega Menu Item Cards
Each service item card inside the mega menu includes:
- Distinct service number badge (`01` to `08`) with lime accent on hover.
- Curated SVG micro-icon.
- Service title (bold 15px, `#ffffff`).
- 1-line benefit description (12px, `#8a8a8a`).
- Hover state: Background lights up to `rgba(255, 255, 255, 0.04)`, border gains lime glow `rgba(200, 255, 0, 0.3)`, arrow slides 4px right.

### 2.3 Mobile Navigation Drawer
- In `.mobile-nav-drawer`, "Services" features an expandable accordion toggle.
- When clicked, it expands smoothly to reveal all 8 service links in a clean vertical stack.

---

## 3. Dedicated Service Pages Specification

### 3.1 File List (Root Directory)
1. `service-performance-marketing.html`
2. `service-website-development.html`
3. `service-social-media.html`
4. `service-content-creation.html`
5. `service-seo-aeo-geo.html`
6. `service-influencer-marketing.html`
7. `service-ai-automation.html`
8. `service-landing-page-cro.html`

### 3.2 Service Page Sections Rhythm
Each dedicated page maintains the established multi-section narrative flow:
1. **Header & Navbar:** Unified sticky navbar with working mega menu, consistent logo, and "Talk to Expert →" CTA.
2. **Hero Section (Dark `#050505`):**
   - Eyebrow pill tag (e.g. `● META & GOOGLE PERFORMANCE ENGINE`).
   - High-impact headline addressing pain points & profitability.
   - Core value proposition subtitle.
   - Primary CTA (`Book Discovery Call →`) + secondary CTA (`See Deliverables`).
   - 3 Key Metric Badges (e.g., `4.8x Avg ROAS`, `₹12Cr+ Ad Spend Managed`, `-28% Avg CAC`).
3. **What's Included / Deliverables (Light `#f7f7f2`):**
   - 4-to-6 core deliverables presented in modern structured cards.
4. **The Execution Process (Dark `#0a0a0a`):**
   - 4-step framework: Audit & Baseline → Creative & Strategy → Launch & Scale → Attribution & Iteration.
5. **Why Brands Switch to Us (Dark `#050505`):**
   - Direct comparison against traditional agencies (no fluff, full transparency, weekly sprint reporting).
6. **Lead Capture / Consultation CTA (Dark `#111111`):**
   - High-converting form with name, email, brand URL, monthly budget select, and phone number.
7. **Service FAQs (Light `#f7f7f2`):**
   - 4-5 accordion FAQs addressing timeline, minimum budget, tech stack, and onboarding.
8. **Footer:** Standard Autopilot Media footer.

---

## 4. Technical Implementation & Shared Styles

- **Style Integration:**
  - Add mega menu styles to `style.css` so `index.html`, `about.html`, `contact.html`, `portfolio.html`, and all 8 new service pages share the exact same mega menu rules.
  - Include the mega menu CSS in `courses.html` and `free-tools.html` internal stylesheets for 100% cross-site consistency.
- **JavaScript Enhancements (`script.js`):**
  - Add mobile accordion expand/collapse logic for mobile drawer services menu.
  - Desktop hover delay handling for touch laptops/tablets.
- **Accessibility & SEO:**
  - ARIA attributes: `aria-haspopup="true"`, `aria-expanded="false"`, `role="menu"`.
  - Canonical links, Open Graph tags, descriptive meta titles and descriptions for all 8 service pages.
