# Autopilot Media Homepage — Design Specification

**Date:** 2026-09-26  
**Status:** Approved  
**Brand Identity:** Autopilot Media  
**Stack:** Plain HTML5, CSS3, Vanilla JavaScript (No frameworks/heavy libraries)

---

## 1. Executive Summary & Core Rules

- **Wireframe Structure (Reference 2):** Strict execution of the 13-part sequence:
  1. Navbar
  2. Hero Section
  3. Clients Logo Slider (Marquee)
  4. About Us
  5. Calculator / Live Simulator
  6. Our Services
  7. Our Framework
  8. Why Brands Fail
  9. Why Choose Us
  10. Testimonials
  11. CTA Section
  12. FAQ Accordion
  13. Footer
- **Visual Design System (Reference 1):** Ultra-premium performance agency aesthetic. High-contrast dark (`#050505`) and light off-white (`#f7f7f2`) section alternating rhythm, sharp modern Inter typography, thin borders (`rgba(255,255,255,0.12)` / `rgba(0,0,0,0.1)`), lime green (`#c8ff00`) pill tags, high-impact metrics, rounded dashboard cards (20px border radius), and interactive micro-animations.
- **Brand Assets:** Uses the approved brand logo (`assets/logo.png` - Autopilot Media) with clean high-DPI rendering.

---

## 2. Design Tokens & Styling System

```css
:root {
  --black: #050505;
  --near-black: #0a0a0a;
  --dark-surface: #111111;
  --dark-surface-2: #161616;
  --white: #ffffff;
  --off-white: #f7f7f2;
  --light-surface: #ffffff;
  --lime: #c8ff00;
  --lime-soft: #e8ff9a;
  --lime-dim: rgba(200, 255, 0, 0.12);
  --gray: #8a8a8a;
  --gray-dark: #555555;
  --light-gray: #e8e8e2;
  --border-dark: rgba(255, 255, 255, 0.12);
  --border-dark-hover: rgba(200, 255, 0, 0.4);
  --border-light: rgba(0, 0, 0, 0.1);
  --border-light-hover: rgba(0, 0, 0, 0.25);
  --font-main: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-full: 9999px;
  --transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}
```

---

## 3. Section Specifications

### 00. Navbar
- Sticky top with backdrop blur (`backdrop-filter: blur(16px)`), height 72px.
- Left: `assets/logo.png` (height 32px), crisp rendering.
- Center/Right Links: About, Calculator, Services, Framework, Why Us, FAQ.
- Right: Lime pill button `Start Growing →` with arrow hover slide.
- Mobile: Hamburger toggle button opening full-screen mobile menu drawer.

### 01. Hero Section (Dark `#050505`)
- Eyebrow badge: `● D2C PERFORMANCE GROWTH SYSTEM` with glowing green dot.
- Headline: "Turn marketing into a <span class="highlight-pill">predictable</span> growth engine."
- Paragraph: "We build data-driven growth systems that connect strategy, creative, acquisition and conversion into one measurable engine."
- CTAs: Primary lime button `Build My Growth System →` + secondary outline button `See How It Works`.
- Live Dashboard Visual:
  - Header: `LIVE GROWTH ENGINE` + pulse badge.
  - Metrics Grid: Revenue `₹12.8L` (+38.4%), Blended ROAS `4.82x`, Conversion `6.4%`, CAC `₹412`.
  - Sparkline: Interactive animated SVG multi-point line chart with gradient fill.

### 02. Clients Logo Slider (Dark `#050505`)
- Heading: `TRUSTED BY AMBITIOUS BRANDS` (subtle uppercase tracking).
- Infinite CSS marquee with seamless duplicate loops.
- Client logos: NOVA, MONO, VERDE, ARC, NORTH, LUMA, FORM, BANARAS, AMARAA, IZI.
- Pauses smoothly on `:hover`, items gain lime tint on hover.

### 03. About Us (Light Off-White `#f7f7f2`)
- Two-column split layout:
  - Left: Headline "Growth is not one campaign. It's a system." + narrative explaining integration of creative, performance media, CRO, and analytics.
  - Right: 4 large stat cards (`4.8x` Average ROAS, `38%` Average MoM Growth, `120+` Campaigns Scaled, `3+` Growth Channels).

### 04. Calculator / Live Simulator (Dark `#0a0a0a`)
- Heading: "See what your growth could look like."
- Interactive Vanilla JS Simulator:
  - Inputs (with real-time sliders & numeric badges):
    1. Monthly Ad Spend (Range: ₹1,00,000 – ₹50,00,000 | Default: ₹5,00,000)
    2. Average Order Value (Range: ₹500 – ₹10,000 | Default: ₹2,400)
    3. Current Conversion Rate (Range: 0.5% – 8.0% | Default: 2.2%)
    4. Current ROAS (Range: 1.0x – 8.0x | Default: 2.8x)
  - Outputs (Calculated via Autopilot Media optimization multipliers):
    - Projected Monthly Revenue (formatted in ₹ Lakhs / Crores)
    - Projected Orders
    - Optimized Blended ROAS (+25% to +45% efficiency boost)
    - Net Growth Gain (%)
  - Mini SVG reactive growth bar comparison (Current vs. Autopilot Optimized).
  - Disclaimer note included.

### 05. Our Services (Light Off-White `#f7f7f2`)
- Heading: "Everything your growth engine needs."
- 6-card grid:
  1. Strategy (Growth strategy, funnel planning, positioning and channel planning)
  2. Paid Acquisition (Meta, Google and performance campaign management)
  3. Creative Systems (Ad creative concepts, testing systems, hooks and iterations)
  4. Conversion Optimization (Landing pages, CRO, offers and checkout optimization)
  5. Analytics (Tracking, dashboards, attribution and performance reporting)
  6. Retention (Email, remarketing, lifecycle and repeat-purchase systems)
- Hover interactions: Lime accent border, arrow motion, card elevation.

### 06. Our Framework (Dark `#050505`)
- Heading: `ONE SYSTEM. EVERY GROWTH LEVER.`
- 7-step connected pathway:
  `Strategy → Offer → Creative → Acquisition → Conversion → Retention → Scale`
- Desktop: Horizontal step progression with lime directional connectors.
- Mobile: Vertical responsive timeline.

### 07. Why Brands Fail (Light Off-White `#f7f7f2`)
- Heading: "Most brands don't have a traffic problem. They have a system problem."
- 6 diagnostic editorial cards:
  1. No Clear Offer
  2. Creative Isn't Tested Consistently
  3. Marketing Channels Operate Separately
  4. Landing Pages Leak Conversions
  5. Decisions Are Made Without Useful Data
  6. Growth Depends On One Winning Campaign

### 08. Why Choose Us (Dark `#0a0a0a`)
- Split layout:
  - Left: Giant typography statement: "We don't just run campaigns. We build the system behind growth."
  - Right: High-contrast verified checklist (Strategy before spend, Creative testing system, Transparent reporting, Conversion-focused execution, Weekly optimization, One connected growth process) + mini attribution live dashboard widget.

### 09. Testimonials (Light Off-White `#f7f7f2`)
- Clean testimonial carousel with navigation controls (prev/next dots & arrows).
- Quote, founder name, brand, role, and verified metric badge (`+42% Revenue`, `5.1x ROAS`, `₹75L to ₹85L/mo`).

### 10. CTA (Dark `#050505`)
- Full-width dark container with glowing lime ambient backdrop.
- Headline: "READY TO TURN GROWTH INTO A PREDICTABLE SYSTEM?"
- Subtitle: "Let's find the biggest opportunity in your funnel and build a plan around it."
- Primary button: `Build My Growth System →` (large lime button).
- Secondary button: `Book a Strategy Call`.

### 11. FAQ Accordion (Light Off-White `#f7f7f2`)
- Clean single-expand accordion with 8 questions specified in the brief.
- Smooth CSS transition, rotating plus/minus icon, full keyboard & ARIA accessibility.

### 12. Footer (Dark `#050505`)
- Brand logo, company bio, quick links, contact info (`hello@autopilotmedia.in`), social channels, copyright 2026, privacy and terms.

---

## 4. Verification & Responsive Breakpoints
- Desktop: 1440px / 1280px / 1200px
- Tablet: 1024px / 768px
- Mobile: 430px / 390px / 360px
- Zero console errors, zero layout shifts, zero horizontal scrollbars.
