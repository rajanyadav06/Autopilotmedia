# Autopilot Media Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a single-page homepage for Autopilot Media in vanilla HTML5, CSS3, and JavaScript, strictly adhering to the Reference 2 wireframe sequence and Reference 1 high-contrast dark/light performance agency aesthetic.

**Architecture:** Plain HTML/CSS/JS without heavy frameworks. Centralized CSS design system with CSS custom properties (`--black`, `--near-black`, `--white`, `--off-white`, `--lime`, etc.), fluid clamp typography, responsive layouts (desktop, tablet, mobile down to 360px), and vanilla JS modules for interactivity (live calculator, accordion, carousel, sticky nav, and IntersectionObserver animations).

**Tech Stack:** HTML5, CSS3, Vanilla JavaScript, Google Fonts (Inter), SVG, high-DPI Autopilot Media logo.

**Spec:** `docs/superpowers/specs/2026-09-26-autopilot-media-homepage-design.md`

## Global Constraints

- Must follow the exact 13-part wireframe sequence: Navbar → Hero → Clients Logo Slider → About Us → Calculator / Live Simulator → Our Services → Our Framework → Why Brands Fail → Why Choose Us → Testimonials → CTA → FAQ → Footer.
- Styling strictly inspired by Reference 1: Dark `#050505` and off-white `#f7f7f2` alternating rhythm, lime green `#c8ff00` highlights/CTAs, thin subtle borders, 20px rounded cards.
- Logo: Must use `assets/logo.png`.
- Zero external UI libraries (No React, Tailwind, Bootstrap, or jQuery).
- Zero console errors, fully responsive, zero horizontal overflow.

---

### Task 1: Foundational CSS Architecture & HTML Scaffold

**Files:**
- Create: `style.css`
- Create: `index.html` (Head metadata, Open Graph, Google Fonts, base wrapper)
- Asset verify: `assets/logo.png`

- [ ] **Step 1: Write `style.css` with core design tokens, reset, typography, and utility classes**
- [ ] **Step 2: Write `index.html` skeleton with SEO meta tags, favicon, and section anchors**
- [ ] **Step 3: Verify base styles and fonts load properly**

---

### Task 2: Sticky Header & Navbar with Mobile Navigation Drawer

**Files:**
- Modify: `index.html` (Navbar semantic HTML)
- Modify: `style.css` (Sticky navbar styles, desktop links, lime CTA, mobile drawer)
- Modify: `script.js` (Backdrop blur on scroll, mobile hamburger toggle, keyboard escape)

- [ ] **Step 1: Add semantic `<header>` and `<nav>` with Autopilot Media logo, nav links, CTA, and hamburger button**
- [ ] **Step 2: Add CSS for sticky header, glassmorphism blur on scroll, and responsive mobile drawer**
- [ ] **Step 3: Add vanilla JS in `script.js` for scroll detection and mobile menu toggle**
- [ ] **Step 4: Verify navigation links and mobile toggle behavior**

---

### Task 3: Hero Section & Live Growth Engine Visual

**Files:**
- Modify: `index.html` (Hero section HTML)
- Modify: `style.css` (Hero typography, highlighted lime pills, 2-column grid, dashboard card styling)
- Modify: `script.js` (Interactive sparkline hover or animated indicators)

- [ ] **Step 1: Markup Hero section with eyebrow badge, headline with lime highlight pill, body copy, and dual CTA buttons**
- [ ] **Step 2: Build the right-column Live Growth Engine dashboard card with metrics (`₹12.8L`, `4.82x ROAS`, `+38.4%`), mini sparkline SVG, and live status badge**
- [ ] **Step 3: Style hero with high contrast dark aesthetic and mobile stacked layout**
- [ ] **Step 4: Verify hero layout on desktop and mobile**

---

### Task 4: Clients Logo Slider (Infinite Marquee)

**Files:**
- Modify: `index.html` (Clients section HTML)
- Modify: `style.css` (CSS keyframe infinite marquee, pause on hover, grayscale to lime hover effect)

- [ ] **Step 1: Add Clients section immediately following Hero with heading `TRUSTED BY AMBITIOUS BRANDS`**
- [ ] **Step 2: Create marquee track with duplicated client logos (NOVA, MONO, VERDE, ARC, NORTH, LUMA, FORM, BANARAS, AMARAA, IZI)**
- [ ] **Step 3: Implement pure CSS continuous translation with hover-pause and no layout jump**
- [ ] **Step 4: Verify smooth scrolling and hover behavior**

---

### Task 5: About Us Section (Light Off-White Narrative & Stat Cards)

**Files:**
- Modify: `index.html` (About section HTML)
- Modify: `style.css` (Off-white background, 2-column layout, high-contrast stat cards)

- [ ] **Step 1: Add About Us section with headline "Growth is not one campaign. It's a system."**
- [ ] **Step 2: Add 4 stat cards (`4.8x` ROAS, `38%` Avg Growth, `120+` Campaigns, `3+` Channels)**
- [ ] **Step 3: Style with light background `#f7f7f2`, crisp typography, and border treatments**
- [ ] **Step 4: Verify responsive 2-column to 1-column adaptation**

---

### Task 6: Interactive Growth Calculator / Live Simulator

**Files:**
- Modify: `index.html` (Calculator card layout, sliders, output cards)
- Modify: `style.css` (Dark dashboard card, custom range sliders, reactive highlight counters)
- Modify: `script.js` (Real-time calculation formulas, currency formatting, SVG comparison graph)

- [ ] **Step 1: Build Calculator markup with 4 sliders (Ad Spend, AOV, Conversion Rate, Current ROAS) and 4 output metric cards**
- [ ] **Step 2: Implement reactive calculation logic in `script.js` with instant metric updates on input**
- [ ] **Step 3: Add visual comparison bar (Current vs. Autopilot Optimized) and legal disclaimer**
- [ ] **Step 4: Verify calculator calculations, edge cases, and mobile touch interactions**

---

### Task 7: Our Services Section (6-Card Grid)

**Files:**
- Modify: `index.html` (Services section HTML)
- Modify: `style.css` (Off-white section, 3x2 responsive card grid, hover transitions)

- [ ] **Step 1: Add Our Services section with heading "Everything your growth engine needs."**
- [ ] **Step 2: Add 6 capability cards (Strategy, Paid Acquisition, Creative Systems, CRO, Analytics, Retention)**
- [ ] **Step 3: Style cards with numbering tags, micro-icons, lime border hover glow, and arrow transitions**
- [ ] **Step 4: Verify grid responsiveness across all screen sizes**

---

### Task 8: Our Framework Section (Connected Pathway)

**Files:**
- Modify: `index.html` (Framework section HTML)
- Modify: `style.css` (Dark `#050505` background, horizontal step flow, lime connector lines, vertical timeline on mobile)

- [ ] **Step 1: Markup 7 framework stages: Strategy → Offer → Creative → Acquisition → Conversion → Retention → Scale**
- [ ] **Step 2: Style desktop horizontal sequence with connecting lines and lime step badges**
- [ ] **Step 3: Style mobile vertical timeline with seamless connecting guide lines**
- [ ] **Step 4: Verify step alignment and responsive collapse**

---

### Task 9: Why Brands Fail Section (Editorial Diagnostic Cards)

**Files:**
- Modify: `index.html` (Why Brands Fail HTML)
- Modify: `style.css` (Light off-white section, editorial cards with bold numbering and diagnosis copy)

- [ ] **Step 1: Add heading "Most brands don't have a traffic problem. They have a system problem."**
- [ ] **Step 2: Add 6 diagnostic cards highlighting failure points (No clear offer, ad fatigue, leaky landing pages, attribution chaos, etc.)**
- [ ] **Step 3: Style with bold typography, subtle borders, and editorial agency spacing**
- [ ] **Step 4: Verify layout across viewport widths**

---

### Task 10: Why Choose Us Section (Split Manifesto & Live Proof)

**Files:**
- Modify: `index.html` (Why Choose Us HTML)
- Modify: `style.css` (Dark `#0a0a0a` section, split manifesto + checklist + mini dashboard preview)

- [ ] **Step 1: Add large statement: "We don't just run campaigns. We build the system behind growth."**
- [ ] **Step 2: Add 6 verified feature check-items (Strategy before spend, Creative testing, Transparent reporting, CRO, Weekly optimization, Connected growth)**
- [ ] **Step 3: Add mini live attribution dashboard preview widget beside checklist**
- [ ] **Step 4: Verify layout balance and responsive stacking**

---

### Task 11: Testimonials Carousel Component

**Files:**
- Modify: `index.html` (Testimonials HTML)
- Modify: `style.css` (Light off-white section, card carousel styles, quote marks, metric badges)
- Modify: `script.js` (Carousel navigation, touch swipe support, dot indicators)

- [ ] **Step 1: Add Testimonials markup with quotes, founder names, brands, roles, and verified result badges (`+42% Revenue`, `5.1x ROAS`)**
- [ ] **Step 2: Implement smooth carousel sliding logic with prev/next buttons and keyboard support**
- [ ] **Step 3: Style cards with elevated shadows, lime metric tags, and editorial quotes**
- [ ] **Step 4: Verify carousel transitions and responsiveness**

---

### Task 12: High-Impact Full-Width Dark CTA Section

**Files:**
- Modify: `index.html` (CTA section HTML)
- Modify: `style.css` (Full-width dark background, ambient radial lime glow, typography, dual CTA buttons)

- [ ] **Step 1: Add full-width CTA markup with headline "READY TO TURN GROWTH INTO A PREDICTABLE SYSTEM?"**
- [ ] **Step 2: Add supporting text and dual buttons (`Build My Growth System →` and `Book a Strategy Call`)**
- [ ] **Step 3: Style with subtle radial lime glow, high-contrast buttons, and responsive padding**
- [ ] **Step 4: Verify button hover states and click actions**

---

### Task 13: Accessible FAQ Accordion Section

**Files:**
- Modify: `index.html` (FAQ section HTML)
- Modify: `style.css` (Off-white section, accordion item borders, rotating plus/minus icon, smooth transition)
- Modify: `script.js` (Single-open accordion logic, `aria-expanded` toggle, keyboard enter/space support)

- [ ] **Step 1: Add 8 FAQ questions specified in brief with semantic `<button>` triggers and panel containers**
- [ ] **Step 2: Implement vanilla JS accordion with single open item constraint and full ARIA support**
- [ ] **Step 3: Style with smooth height animation and icon rotation**
- [ ] **Step 4: Verify keyboard navigation and screen-reader accessibility**

---

### Task 14: Dark Multi-Column Footer

**Files:**
- Modify: `index.html` (Footer semantic HTML)
- Modify: `style.css` (Dark `#050505` footer, logo, link columns, contact info, copyright sub-bar)

- [ ] **Step 1: Add footer with Autopilot Media logo, brand description, navigation links, socials, and contact details**
- [ ] **Step 2: Add bottom copyright row (`© 2026 Autopilot Media. All rights reserved.`, Privacy Policy, Terms)**
- [ ] **Step 3: Style with muted links, lime hover accents, and clean multi-column layout**
- [ ] **Step 4: Verify responsiveness on mobile and tablet**

---

### Task 15: Global Animations, Accessibility & Full Viewport Verification

**Files:**
- Modify: `style.css` (Reveal animation classes, `@media (prefers-reduced-motion)` overrides)
- Modify: `script.js` (IntersectionObserver scroll reveals)
- Verify: Full browser rendering at 1440px, 1280px, 1024px, 768px, 430px, 390px, 360px

- [ ] **Step 1: Add subtle fade-up reveal animations with `IntersectionObserver`**
- [ ] **Step 2: Ensure complete support for `prefers-reduced-motion`**
- [ ] **Step 3: Test and verify in browser at all required resolutions**
- [ ] **Step 4: Confirm zero console errors, zero layout overflow, and complete feature polish**
