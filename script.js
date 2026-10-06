/**
 * Autopilot Media — Interactive Engine (Vanilla JavaScript)
 * Modules:
 * 1. Sticky Navbar & Mobile Navigation Drawer
 * 2. Real-Time Growth Calculator & Live Simulator
 * 3. Testimonial Carousel Controls
 * 4. Accessible Accordion FAQ Engine
 * 5. IntersectionObserver Scroll Reveals & Smooth Navigation
 */

document.addEventListener('DOMContentLoaded', () => {

  /* =========================================================================
     1. NAVBAR SCROLL STATE, MEGA MENU & MOBILE DRAWER
     ========================================================================= */
  const navbar = document.getElementById('mainNavbar');
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const mobileDrawer = document.getElementById('mobileDrawer');
  const mobileLinks = document.querySelectorAll('.mobile-link, .mobile-sublink');
  const mobileServicesToggle = document.getElementById('mobileServicesToggle');
  const mobileServicesMenu = document.getElementById('mobileServicesMenu');
  const navItemDropdown = document.querySelector('.nav-item-dropdown');

  // Handle sticky navbar background and height on scroll
  const handleNavScroll = () => {
    if (navbar) {
      if (window.scrollY > 40) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    }
  };

  window.addEventListener('scroll', handleNavScroll, { passive: true });
  handleNavScroll();

  // Mobile menu toggle
  const toggleMobileMenu = () => {
    if (!mobileDrawer || !mobileMenuBtn) return;
    const isOpen = mobileDrawer.classList.toggle('open');
    mobileMenuBtn.classList.toggle('active', isOpen);
    mobileMenuBtn.setAttribute('aria-expanded', isOpen);
    mobileDrawer.setAttribute('aria-hidden', !isOpen);
    document.body.style.overflow = isOpen ? 'hidden' : '';
  };

  if (mobileMenuBtn && mobileDrawer) {
    mobileMenuBtn.addEventListener('click', toggleMobileMenu);

    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        if (mobileDrawer.classList.contains('open')) {
          toggleMobileMenu();
        }
      });
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        if (mobileDrawer.classList.contains('open')) {
          toggleMobileMenu();
        }
        if (navItemDropdown) {
          navItemDropdown.classList.remove('is-open');
        }
      }
    });

    // Close drawer when clicking outside on tablet/desktop viewports
    document.addEventListener('click', (e) => {
      if (mobileDrawer.classList.contains('open')) {
        if (!mobileDrawer.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
          toggleMobileMenu();
        }
      }
    });
  }

  // Mobile Services Accordion Toggle
  if (mobileServicesToggle && mobileServicesMenu) {
    mobileServicesToggle.addEventListener('click', (e) => {
      e.preventDefault();
      const isExpanded = mobileServicesToggle.classList.toggle('active');
      mobileServicesToggle.setAttribute('aria-expanded', isExpanded);
      mobileServicesMenu.classList.toggle('open', isExpanded);
    });
  }

  // Desktop Mega Menu Hover Intent with Grace Period (prevents premature hiding)
  if (navItemDropdown) {
    let dropdownTimer = null;
    navItemDropdown.addEventListener('mouseenter', () => {
      if (dropdownTimer) {
        clearTimeout(dropdownTimer);
        dropdownTimer = null;
      }
      navItemDropdown.classList.add('is-open');
    });

    navItemDropdown.addEventListener('mouseleave', () => {
      dropdownTimer = setTimeout(() => {
        navItemDropdown.classList.remove('is-open');
      }, 300); // 300ms grace period so cursor can move into mega menu without closing
    });

    // Click outside to close dropdown if opened via touch/focus
    document.addEventListener('click', (e) => {
      if (!navItemDropdown.contains(e.target)) {
        navItemDropdown.classList.remove('is-open');
      }
    });
  }

  /* =========================================================================
     2. INTERACTIVE GROWTH CALCULATOR & LIVE SIMULATOR
     ========================================================================= */
  const adSpendInput = document.getElementById('adSpendInput');
  const aovInput = document.getElementById('aovInput');
  const cvrInput = document.getElementById('cvrInput');
  const roasInput = document.getElementById('roasInput');

  const adSpendDisplay = document.getElementById('adSpendDisplay');
  const aovDisplay = document.getElementById('aovDisplay');
  const cvrDisplay = document.getElementById('cvrDisplay');
  const roasDisplay = document.getElementById('roasDisplay');

  const calcRevenue = document.getElementById('calcRevenue');
  const calcOrders = document.getElementById('calcOrders');
  const calcOptimizedROAS = document.getElementById('calcOptimizedROAS');
  const calcGrowth = document.getElementById('calcGrowth');

  const compCurrentVal = document.getElementById('compCurrentVal');
  const compOptimizedVal = document.getElementById('compOptimizedVal');
  const compBarCurrent = document.getElementById('compBarCurrent');
  const compBarOptimized = document.getElementById('compBarOptimized');

  // Currency Formatter in Lakhs / Crores
  const formatCurrencyINR = (amount) => {
    if (amount >= 10000000) {
      return `₹${(amount / 10000000).toFixed(2)} Cr`;
    } else if (amount >= 100000) {
      return `₹${(amount / 100000).toFixed(2)} L`;
    } else {
      return `₹${Math.round(amount).toLocaleString('en-IN')}`;
    }
  };

  const formatRawINR = (amount) => {
    return `₹${Number(amount).toLocaleString('en-IN')}`;
  };

  // Live Simulator Calculation Engine
  const updateSimulator = () => {
    if (!adSpendInput) return;

    const spend = parseFloat(adSpendInput.value) || 500000;
    const aov = parseFloat(aovInput.value) || 2400;
    const cvr = parseFloat(cvrInput.value) || 2.2;
    const currentROAS = parseFloat(roasInput.value) || 2.8;

    // Update input display pills
    adSpendDisplay.textContent = formatRawINR(spend);
    aovDisplay.textContent = formatRawINR(aov);
    cvrDisplay.textContent = `${cvr.toFixed(1)}%`;
    roasDisplay.textContent = `${currentROAS.toFixed(1)}x`;

    // Baseline current revenue
    const currentRevenue = spend * currentROAS;

    // Autopilot Growth Engine Multiplier (Synergistic impact of CRO + Creative Testing + Attribution)
    // Brands with lower current conversion rate or ROAS unlock higher percentage upside (+30% to +48%)
    const efficiencyUpliftFactor = 0.38 + (cvr < 2.0 ? 0.08 : 0) + (currentROAS < 2.5 ? 0.04 : 0);
    const optimizedROAS = Number((currentROAS * (1 + efficiencyUpliftFactor)).toFixed(2));
    const optimizedRevenue = spend * optimizedROAS;
    const estimatedOrders = Math.round(optimizedRevenue / aov);
    const growthPercent = Number((((optimizedRevenue - currentRevenue) / currentRevenue) * 100).toFixed(1));

    // Update output elements with smooth numeric display
    calcRevenue.textContent = formatCurrencyINR(optimizedRevenue);
    calcOrders.textContent = estimatedOrders.toLocaleString('en-IN');
    calcOptimizedROAS.textContent = `${optimizedROAS.toFixed(2)}x`;
    calcGrowth.textContent = `+${growthPercent}%`;

    // Update comparative visual bars
    compCurrentVal.textContent = formatCurrencyINR(currentRevenue);
    compOptimizedVal.textContent = formatCurrencyINR(optimizedRevenue);

    const currentBarPct = Math.min(100, Math.max(15, (currentRevenue / optimizedRevenue) * 100));
    compBarCurrent.style.width = `${currentBarPct.toFixed(1)}%`;
    compBarOptimized.style.width = '100%';
  };

  // Attach input listeners
  [adSpendInput, aovInput, cvrInput, roasInput].forEach(input => {
    if (input) {
      input.addEventListener('input', updateSimulator);
    }
  });

  // Initial calculation
  updateSimulator();

  /* =========================================================================
     3. TESTIMONIALS CAROUSEL NAVIGATION
     ========================================================================= */
  const testimonialsTrack = document.getElementById('testimonialsTrack');
  const prevBtn = document.getElementById('prevTestimonial');
  const nextBtn = document.getElementById('nextTestimonial');

  if (testimonialsTrack && prevBtn && nextBtn) {
    const getScrollStep = () => {
      const card = testimonialsTrack.querySelector('.testimonial-card');
      return card ? card.offsetWidth + 24 : 400;
    };

    nextBtn.addEventListener('click', () => {
      testimonialsTrack.scrollBy({
        left: getScrollStep(),
        behavior: 'smooth'
      });
    });

    prevBtn.addEventListener('click', () => {
      testimonialsTrack.scrollBy({
        left: -getScrollStep(),
        behavior: 'smooth'
      });
    });
  }

  /* =========================================================================
     4. ACCESSIBLE ACCORDION FAQ ENGINE
     ========================================================================= */
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const btn = item.querySelector('.faq-question-btn');
    if (!btn) return;

    btn.addEventListener('click', () => {
      const isAlreadyActive = item.classList.contains('active');

      // Close all other open accordion items (single-open accordion rule)
      faqItems.forEach(otherItem => {
        if (otherItem !== item) {
          otherItem.classList.remove('active');
          const otherBtn = otherItem.querySelector('.faq-question-btn');
          if (otherBtn) {
            otherBtn.setAttribute('aria-expanded', 'false');
          }
        }
      });

      // Toggle current item
      if (isAlreadyActive) {
        item.classList.remove('active');
        btn.setAttribute('aria-expanded', 'false');
      } else {
        item.classList.add('active');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  /* =========================================================================
     5. INTERSECTION OBSERVER SCROLL REVEAL ANIMATIONS
     ========================================================================= */
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const revealElements = document.querySelectorAll('.reveal');

  if (!prefersReducedMotion && 'IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px'
    });

    revealElements.forEach(el => revealObserver.observe(el));
  } else {
    // If reduced motion is preferred or observer unsupported, reveal immediately
    revealElements.forEach(el => el.classList.add('active'));
  }

  /* =========================================================================
     6. SMOOTH ANCHOR LINK SCROLLING WITH OFFSET
     ========================================================================= */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || targetId === '') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        const navHeight = navbar ? navbar.offsetHeight : 72;
        const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navHeight;
        
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  console.log('🚀 Autopilot Media engine initialized.');
});
