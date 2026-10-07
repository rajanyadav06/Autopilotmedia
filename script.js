

document.addEventListener('DOMContentLoaded', () => {

  const navbar = document.getElementById('mainNavbar');
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const mobileDrawer = document.getElementById('mobileDrawer');
  const mobileLinks = document.querySelectorAll('.mobile-link, .mobile-sublink');
  const mobileServicesToggle = document.getElementById('mobileServicesToggle');
  const mobileServicesMenu = document.getElementById('mobileServicesMenu');
  const navItemDropdown = document.querySelector('.nav-item-dropdown');

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

    document.addEventListener('click', (e) => {
      if (mobileDrawer.classList.contains('open')) {
        if (!mobileDrawer.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
          toggleMobileMenu();
        }
      }
    });
  }

  if (mobileServicesToggle && mobileServicesMenu) {
    mobileServicesToggle.addEventListener('click', (e) => {
      e.preventDefault();
      const isExpanded = mobileServicesToggle.classList.toggle('active');
      mobileServicesToggle.setAttribute('aria-expanded', isExpanded);
      mobileServicesMenu.classList.toggle('open', isExpanded);
    });
  }

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
      }, 300);
    });

    document.addEventListener('click', (e) => {
      if (!navItemDropdown.contains(e.target)) {
        navItemDropdown.classList.remove('is-open');
      }
    });
  }

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

  const updateSimulator = () => {
    if (!adSpendInput) return;

    const spend = parseFloat(adSpendInput.value) || 500000;
    const aov = parseFloat(aovInput.value) || 2400;
    const cvr = parseFloat(cvrInput.value) || 2.2;
    const currentROAS = parseFloat(roasInput.value) || 2.8;

    adSpendDisplay.textContent = formatRawINR(spend);
    aovDisplay.textContent = formatRawINR(aov);
    cvrDisplay.textContent = `${cvr.toFixed(1)}%`;
    roasDisplay.textContent = `${currentROAS.toFixed(1)}x`;

    const currentRevenue = spend * currentROAS;

    const efficiencyUpliftFactor = 0.38 + (cvr < 2.0 ? 0.08 : 0) + (currentROAS < 2.5 ? 0.04 : 0);
    const optimizedROAS = Number((currentROAS * (1 + efficiencyUpliftFactor)).toFixed(2));
    const optimizedRevenue = spend * optimizedROAS;
    const estimatedOrders = Math.round(optimizedRevenue / aov);
    const growthPercent = Number((((optimizedRevenue - currentRevenue) / currentRevenue) * 100).toFixed(1));

    calcRevenue.textContent = formatCurrencyINR(optimizedRevenue);
    calcOrders.textContent = estimatedOrders.toLocaleString('en-IN');
    calcOptimizedROAS.textContent = `${optimizedROAS.toFixed(2)}x`;
    calcGrowth.textContent = `+${growthPercent}%`;

    compCurrentVal.textContent = formatCurrencyINR(currentRevenue);
    compOptimizedVal.textContent = formatCurrencyINR(optimizedRevenue);

    const currentBarPct = Math.min(100, Math.max(15, (currentRevenue / optimizedRevenue) * 100));
    compBarCurrent.style.width = `${currentBarPct.toFixed(1)}%`;
    compBarOptimized.style.width = '100%';
  };

  [adSpendInput, aovInput, cvrInput, roasInput].forEach(input => {
    if (input) {
      input.addEventListener('input', updateSimulator);
    }
  });

  updateSimulator();

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

  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const btn = item.querySelector('.faq-question-btn');
    if (!btn) return;

    btn.addEventListener('click', () => {
      const isAlreadyActive = item.classList.contains('active');

      faqItems.forEach(otherItem => {
        if (otherItem !== item) {
          otherItem.classList.remove('active');
          const otherBtn = otherItem.querySelector('.faq-question-btn');
          if (otherBtn) {
            otherBtn.setAttribute('aria-expanded', 'false');
          }
        }
      });

      if (isAlreadyActive) {
        item.classList.remove('active');
        btn.setAttribute('aria-expanded', 'false');
      } else {
        item.classList.add('active');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

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

    revealElements.forEach(el => el.classList.add('active'));
  }

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
