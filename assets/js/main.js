/**
 * St. Vincent Pallotti College of Engineering & Technology (SVPCET)
 * Modern Institutional Client Architecture (High-Impact & Panoramic)
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initNavScrollControls();
  initMobileDrawer();
  initSearchModal();
  initProgramFilter();
  initFeeCalculator();
  initNoticeTabs();
  initStatsCounter();
  initCampusGalleryTabs();
  initPlacementTicker();
  initRecruiterModal();
});

/* -------------------------------------------------------------
   0. Navigation Bar Horizontal Scroll Controls & Wheel Support
   ------------------------------------------------------------- */
function initNavScrollControls() {
  const nav = document.getElementById('desktopMainNavBar');
  const leftBtn = document.getElementById('navScrollLeftBtn');
  const rightBtn = document.getElementById('navScrollRightBtn');
  const fadeLeft = document.getElementById('navFadeLeft');
  const fadeRight = document.getElementById('navFadeRight');

  // Support any horizontal scroll tabs (e.g. department page tabs or notice tabs)
  const allScrollContainers = document.querySelectorAll('.horizontal-scroll-nav, #desktopMainNavBar');

  allScrollContainers.forEach(container => {
    // Enable mouse wheel to horizontal scroll
    container.addEventListener('wheel', (e) => {
      if (Math.abs(e.deltaY) > Math.abs(e.deltaX) && container.scrollWidth > container.clientWidth) {
        e.preventDefault();
        container.scrollLeft += e.deltaY;
      }
    }, { passive: false });

    // Enable drag-to-scroll
    let isDown = false;
    let startX = 0;
    let scrollStart = 0;

    container.addEventListener('mousedown', (e) => {
      if (e.target.closest('a') || e.target.closest('button')) return;
      isDown = true;
      startX = e.pageX - container.offsetLeft;
      scrollStart = container.scrollLeft;
      container.style.cursor = 'grabbing';
      container.style.userSelect = 'none';
    });

    const stopDrag = () => {
      if (!isDown) return;
      isDown = false;
      container.style.cursor = '';
      container.style.userSelect = '';
    };

    container.addEventListener('mouseleave', stopDrag);
    container.addEventListener('mouseup', stopDrag);
    container.addEventListener('mousemove', (e) => {
      if (!isDown) return;
      e.preventDefault();
      const x = e.pageX - container.offsetLeft;
      const walk = (x - startX) * 1.5;
      container.scrollLeft = scrollStart - walk;
    });
  });

  if (!nav) return;

  const updateScrollIndicators = () => {
    const maxScroll = nav.scrollWidth - nav.clientWidth;
    const currentScroll = nav.scrollLeft;

    if (maxScroll > 15) {
      if (currentScroll > 20) {
        leftBtn?.classList.remove('opacity-0', 'pointer-events-none');
        fadeLeft?.classList.remove('opacity-0');
      } else {
        leftBtn?.classList.add('opacity-0', 'pointer-events-none');
        fadeLeft?.classList.add('opacity-0');
      }

      if (currentScroll < maxScroll - 20) {
        rightBtn?.classList.remove('opacity-0', 'pointer-events-none');
        fadeRight?.classList.remove('opacity-0');
      } else {
        rightBtn?.classList.add('opacity-0', 'pointer-events-none');
        fadeRight?.classList.add('opacity-0');
      }
    } else {
      leftBtn?.classList.add('opacity-0', 'pointer-events-none');
      rightBtn?.classList.add('opacity-0', 'pointer-events-none');
      fadeLeft?.classList.add('opacity-0');
      fadeRight?.classList.add('opacity-0');
    }
  };

  leftBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    nav.scrollBy({ left: -280, behavior: 'smooth' });
    setTimeout(updateScrollIndicators, 300);
  });

  rightBtn?.addEventListener('click', (e) => {
    e.preventDefault();
    nav.scrollBy({ left: 280, behavior: 'smooth' });
    setTimeout(updateScrollIndicators, 300);
  });

  nav.addEventListener('scroll', updateScrollIndicators, { passive: true });
  window.addEventListener('resize', updateScrollIndicators, { passive: true });
  setTimeout(updateScrollIndicators, 150);
}

/* -------------------------------------------------------------
   1. Sticky Header with Scroll Detection
   ------------------------------------------------------------- */
function initStickyHeader() {
  const header = document.getElementById('mainHeader');
  if (!header) return;

  const onScroll = () => {
    if (window.scrollY > 40) {
      header.classList.add('scrolled', 'shadow-md');
    } else {
      header.classList.remove('scrolled', 'shadow-md');
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* -------------------------------------------------------------
   2. Mobile Menu Drawer
   ------------------------------------------------------------- */
function initMobileDrawer() {
  const openBtn = document.getElementById('openMobileMenuBtn');
  const closeBtn = document.getElementById('closeMobileMenuBtn');
  const drawer = document.getElementById('mobileMenuDrawer');
  const backdrop = document.getElementById('mobileDrawerBackdrop');

  if (!openBtn || !drawer) return;

  const toggle = (show) => {
    if (show) {
      drawer.classList.remove('translate-x-full');
      backdrop.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    } else {
      drawer.classList.add('translate-x-full');
      backdrop.classList.add('hidden');
      document.body.style.overflow = '';
    }
  };

  openBtn.addEventListener('click', () => toggle(true));
  closeBtn?.addEventListener('click', () => toggle(false));
  backdrop?.addEventListener('click', () => toggle(false));

  document.querySelectorAll('.mobile-acc-trigger').forEach(trigger => {
    trigger.addEventListener('click', () => {
      const targetId = trigger.getAttribute('data-target');
      const content = document.getElementById(targetId);
      const icon = trigger.querySelector('.acc-icon');
      if (!content) return;

      const isExpanded = !content.classList.contains('hidden');
      document.querySelectorAll('.mobile-acc-content').forEach(c => c.classList.add('hidden'));
      document.querySelectorAll('.acc-icon').forEach(i => i.classList.remove('rotate-180'));

      if (!isExpanded) {
        content.classList.remove('hidden');
        icon?.classList.add('rotate-180');
      }
    });
  });
}

/* -------------------------------------------------------------
   3. Quick Search Modal (Ctrl + K)
   ------------------------------------------------------------- */
function initSearchModal() {
  const modal = document.getElementById('searchModal');
  const openBtns = document.querySelectorAll('.trigger-search-modal');
  const closeBtn = document.getElementById('closeSearchModalBtn');
  const searchInput = document.getElementById('globalSearchInput');
  const resultsContainer = document.getElementById('searchResultsContainer');

  if (!modal) return;

  const openModal = () => {
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    setTimeout(() => searchInput?.focus(), 50);
  };

  const closeModal = () => {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
    if (searchInput) searchInput.value = '';
    renderSearchIndex('');
  };

  openBtns.forEach(btn => btn.addEventListener('click', openModal));
  closeBtn?.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      modal.classList.contains('hidden') ? openModal() : closeModal();
    }
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      closeModal();
    }
  });

  const searchablePages = [
    { title: 'Computer Science & Engineering (B.Tech & M.Tech)', category: 'Academic Department', url: 'department-template.html' },
    { title: 'Artificial Intelligence & Machine Learning', category: 'Academic Department', url: '#departments' },
    { title: 'Data Science (B.Tech CSE Track)', category: 'Academic Department', url: '#departments' },
    { title: 'Cyber Security (B.Tech Defense Track)', category: 'Academic Department', url: '#departments' },
    { title: 'Robotics & Artificial Intelligence', category: 'Academic Department', url: '#departments' },
    { title: 'Computer Science & Business Systems (TCS Curated)', category: 'Academic Department', url: '#departments' },
    { title: 'Electrical Engineering (NBA Accredited)', category: 'Academic Department', url: '#departments' },
    { title: 'Electronics & Telecommunication (5G/VLSI)', category: 'Academic Department', url: '#departments' },
    { title: 'Mechanical Engineering (CAD/CAM & EV)', category: 'Academic Department', url: '#departments' },
    { title: 'Civil Engineering (Smart Infrastructure)', category: 'Academic Department', url: '#departments' },
    { title: 'B.Tech Admissions 2026-27 & CAP Eligibility', category: 'Admissions', url: '#admissions' },
    { title: 'Interactive Fee Structure & Concessions Calculator', category: 'Admissions & Fees', url: '#fee-calculator' },
    { title: 'Corporate Recruitment & CDC Placement Records', category: 'Corporate Hub', url: '#corporate' },
    { title: 'Autonomous Exam Cell & Winter 2026 Timetables', category: 'Academics & Exams', url: '#notices' },
    { title: 'Texcelrators Drone Innovation Lab', category: 'Research & Labs', url: '#research' },
    { title: 'Residential Hostels & Sports Complex', category: 'Campus Life', url: '#campus-life' },
    { title: 'NAAC A Grade & NBA Accreditations Portfolio', category: 'Governance & NIRF', url: '#about' },
    { title: '24x7 Campus Security Guards & Emergency Gate Numbers', category: 'Safety & Contacts', url: '#contact' }
  ];

  function renderSearchIndex(query) {
    if (!resultsContainer) return;
    const cleanQ = query.trim().toLowerCase();
    const filtered = cleanQ
      ? searchablePages.filter(p => p.title.toLowerCase().includes(cleanQ) || p.category.toLowerCase().includes(cleanQ))
      : searchablePages.slice(0, 6);

    if (filtered.length === 0) {
      resultsContainer.innerHTML = `
        <div class="py-8 text-center text-slate-500">
          <p class="font-medium">No results found for "${escapeHtml(query)}"</p>
          <p class="text-sm mt-1">Try searching for "CSE", "Fees", "Placements", "Corporate", or "Exam".</p>
        </div>
      `;
      return;
    }

    resultsContainer.innerHTML = filtered.map(item => `
      <a href="${item.url}" class="search-result-item flex items-center justify-between p-3.5 rounded-xl hover:bg-brand-50 transition border border-transparent hover:border-brand-200 group">
        <div>
          <span class="text-[10px] uppercase font-bold tracking-wider text-brand-700 bg-brand-100 px-2 py-0.5 rounded-full">${item.category}</span>
          <h4 class="font-semibold text-slate-800 group-hover:text-brand-700 mt-1 text-sm">${item.title}</h4>
        </div>
        <svg class="w-5 h-5 text-slate-400 group-hover:text-brand-600 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
        </svg>
      </a>
    `).join('');

    resultsContainer.querySelectorAll('.search-result-item').forEach(el => {
      el.addEventListener('click', () => closeModal());
    });
  }

  searchInput?.addEventListener('input', (e) => {
    renderSearchIndex(e.target.value);
  });
  renderSearchIndex('');
}

/* -------------------------------------------------------------
   4. Academic Programs Interactive Filter
   ------------------------------------------------------------- */
function initProgramFilter() {
  const buttons = document.querySelectorAll('.program-filter-btn');
  const cards = document.querySelectorAll('.program-card');
  const searchInput = document.getElementById('programSearchInput');

  if (!buttons.length || !cards.length) return;

  let currentCategory = 'all';

  function filterCards() {
    const query = searchInput ? searchInput.value.trim().toLowerCase() : '';
    cards.forEach(card => {
      const category = card.getAttribute('data-category');
      const title = card.getAttribute('data-title')?.toLowerCase() || '';
      const matchesCat = currentCategory === 'all' || category === currentCategory;
      const matchesQuery = !query || title.includes(query);

      if (matchesCat && matchesQuery) {
        card.classList.remove('hidden');
      } else {
        card.classList.add('hidden');
      }
    });
  }

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => {
        b.classList.remove('bg-brand-600', 'text-white', 'shadow-sm');
        b.classList.add('bg-white', 'text-slate-700', 'hover:bg-slate-100');
      });
      btn.classList.remove('bg-white', 'text-slate-700', 'hover:bg-slate-100');
      btn.classList.add('bg-brand-600', 'text-white', 'shadow-sm');

      currentCategory = btn.getAttribute('data-filter');
      filterCards();
    });
  });

  searchInput?.addEventListener('input', filterCards);
}

/* -------------------------------------------------------------
   5. Interactive Fee & Eligibility Estimator
   ------------------------------------------------------------- */
function initFeeCalculator() {
  const programSelect = document.getElementById('calcProgramSelect');
  const categorySelect = document.getElementById('calcCategorySelect');
  const tuitionVal = document.getElementById('calcTuitionFee');
  const devVal = document.getElementById('calcDevFee');
  const otherVal = document.getElementById('calcOtherFee');
  const totalVal = document.getElementById('calcTotalFee');
  const eligibilityNote = document.getElementById('calcEligibilityNote');

  if (!programSelect || !categorySelect) return;

  const feeData = {
    btech: {
      eligibility: "10+2 with Physics, Mathematics & Chem/CS with min 45% (40% for reserved category in Maharashtra) + Valid MHT-CET or JEE Main.",
      categories: {
        OPEN_MSB: { tuition: 110000, dev: 15000, other: 5000, total: 130000 },
        OPEN_OMB: { tuition: 110000, dev: 15000, other: 5500, total: 130500 },
        OBC_EBC: { tuition: 55000, dev: 15000, other: 5000, total: 75000 },
        SC_ST: { tuition: 0, dev: 0, other: 3500, total: 3500 },
        TFWS_VJNT: { tuition: 0, dev: 15000, other: 5000, total: 20000 }
      }
    },
    mtech: {
      eligibility: "B.E. / B.Tech degree with minimum 50% marks (45% for reserved) + Valid GATE score.",
      categories: {
        OPEN_MSB: { tuition: 75000, dev: 10000, other: 5000, total: 90000 },
        OPEN_OMB: { tuition: 75000, dev: 10000, other: 5000, total: 90000 },
        OBC_EBC: { tuition: 45000, dev: 10000, other: 5000, total: 60000 },
        SC_ST: { tuition: 0, dev: 0, other: 3500, total: 3500 },
        TFWS_VJNT: { tuition: 35000, dev: 10000, other: 5000, total: 50000 }
      }
    },
    mca: {
      eligibility: "Graduation with 50% marks (45% for reserved) with Mathematics at 10+2 or degree level + MAH-MCA-CET.",
      categories: {
        OPEN_MSB: { tuition: 70000, dev: 10000, other: 5000, total: 85000 },
        OPEN_OMB: { tuition: 70000, dev: 10000, other: 5000, total: 85000 },
        OBC_EBC: { tuition: 35000, dev: 10000, other: 5000, total: 50000 },
        SC_ST: { tuition: 0, dev: 0, other: 3500, total: 3500 },
        TFWS_VJNT: { tuition: 20000, dev: 10000, other: 5000, total: 35000 }
      }
    },
    mba: {
      eligibility: "Any bachelor degree with minimum 50% marks (45% for reserved) + MAH-MBA-CET / CAT / CMAT score.",
      categories: {
        OPEN_MSB: { tuition: 80000, dev: 10000, other: 5000, total: 95000 },
        OPEN_OMB: { tuition: 80000, dev: 10000, other: 5000, total: 95000 },
        OBC_EBC: { tuition: 40000, dev: 10000, other: 5000, total: 55000 },
        SC_ST: { tuition: 0, dev: 0, other: 3500, total: 3500 },
        TFWS_VJNT: { tuition: 25000, dev: 10000, other: 5000, total: 40000 }
      }
    }
  };

  const update = () => {
    const prog = programSelect.value;
    const cat = categorySelect.value;
    const pData = feeData[prog];
    if (!pData) return;

    const cData = pData.categories[cat] || pData.categories['OPEN_MSB'];
    if (tuitionVal) tuitionVal.textContent = '₹ ' + cData.tuition.toLocaleString('en-IN');
    if (devVal) devVal.textContent = '₹ ' + cData.dev.toLocaleString('en-IN');
    if (otherVal) otherVal.textContent = '₹ ' + cData.other.toLocaleString('en-IN');
    if (totalVal) totalVal.textContent = '₹ ' + cData.total.toLocaleString('en-IN');
    if (eligibilityNote) eligibilityNote.textContent = pData.eligibility;
  };

  programSelect.addEventListener('change', update);
  categorySelect.addEventListener('change', update);
  update();
}

/* -------------------------------------------------------------
   6. Live Notice Board Tabs
   ------------------------------------------------------------- */
function initNoticeTabs() {
  const tabs = document.querySelectorAll('.notice-tab-btn');
  const panels = document.querySelectorAll('.notice-tab-panel');

  if (!tabs.length || !panels.length) return;

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const targetId = tab.getAttribute('data-target');

      tabs.forEach(t => {
        t.classList.remove('border-brand-600', 'text-brand-700', 'font-semibold');
        t.classList.add('border-transparent', 'text-slate-500', 'hover:text-slate-700');
      });
      tab.classList.add('border-brand-600', 'text-brand-700', 'font-semibold');
      tab.classList.remove('border-transparent', 'text-slate-500');

      panels.forEach(p => {
        if (p.id === targetId) {
          p.classList.remove('hidden');
        } else {
          p.classList.add('hidden');
        }
      });
    });
  });
}

/* -------------------------------------------------------------
   7. Campus Life Gallery Tabs
   ------------------------------------------------------------- */
function initCampusGalleryTabs() {
  const buttons = document.querySelectorAll('.campus-gallery-btn');
  const items = document.querySelectorAll('.campus-gallery-item');

  if (!buttons.length || !items.length) return;

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetFilter = btn.getAttribute('data-filter');

      buttons.forEach(b => {
        b.classList.remove('bg-brand-600', 'text-white', 'shadow-md');
        b.classList.add('bg-white', 'text-slate-700', 'hover:bg-slate-100');
      });
      btn.classList.add('bg-brand-600', 'text-white', 'shadow-md');
      btn.classList.remove('bg-white', 'text-slate-700');

      items.forEach(item => {
        const cat = item.getAttribute('data-category');
        if (targetFilter === 'all' || cat === targetFilter) {
          item.classList.remove('hidden');
        } else {
          item.classList.add('hidden');
        }
      });
    });
  });
}

/* -------------------------------------------------------------
   8. Rotating Live Placement Ticker
   ------------------------------------------------------------- */
function initPlacementTicker() {
  const tickerEl = document.getElementById('livePlacementTicker');
  if (!tickerEl) return;

  const highlights = [
    { name: "Pranay Deshmukh", dept: "B.Tech CSE", company: "Persistent Systems", ctc: "₹ 12.5 LPA" },
    { name: "Ananya Roy", dept: "B.Tech AI", company: "TCS Research Digital", ctc: "₹ 9.2 LPA" },
    { name: "Saurabh Joshi", dept: "B.Tech Electrical", company: "Schneider Electric", ctc: "₹ 8.4 LPA" },
    { name: "Ritika Gedam", dept: "B.Tech Cyber Sec", company: "Capgemini Defense", ctc: "₹ 8.0 LPA" },
    { name: "Harshil Patel", dept: "B.Tech Mechanical", company: "Tata Motors Tech", ctc: "₹ 7.8 LPA" },
    { name: "Divya Meshram", dept: "B.Tech ETC", company: "Hexaware Cloud", ctc: "₹ 8.5 LPA" }
  ];

  let idx = 0;
  setInterval(() => {
    idx = (idx + 1) % highlights.length;
    const h = highlights[idx];
    tickerEl.style.opacity = '0';
    tickerEl.style.transform = 'translateY(5px)';

    setTimeout(() => {
      tickerEl.innerHTML = `
        <span class="inline-flex items-center text-xs font-semibold text-emerald-400">
          <span class="w-2 h-2 rounded-full bg-emerald-400 mr-2 animate-ping"></span>
          Placement Offer:
        </span>
        <span class="text-white font-bold ml-1.5">${h.name}</span>
        <span class="text-slate-400 ml-1">(${h.dept})</span>
        <span class="text-slate-300 ml-1">&rarr;</span>
        <span class="text-amber-300 font-bold ml-1">${h.company}</span>
        <span class="ml-1.5 px-2 py-0.5 rounded-full text-[10px] font-extrabold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">${h.ctc}</span>
      `;
      tickerEl.style.opacity = '1';
      tickerEl.style.transform = 'translateY(0)';
    }, 250);
  }, 4000);
}

/* -------------------------------------------------------------
   9. Corporate Drive Booking Modal
   ------------------------------------------------------------- */
function initRecruiterModal() {
  const modal = document.getElementById('recruiterModal');
  const openBtns = document.querySelectorAll('.trigger-recruiter-modal');
  const closeBtn = document.getElementById('closeRecruiterModalBtn');
  const form = document.getElementById('recruiterBookingForm');
  const successMsg = document.getElementById('recruiterSuccessMsg');

  if (!modal) return;

  const open = () => {
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  };
  const close = () => {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  };

  openBtns.forEach(b => b.addEventListener('click', open));
  closeBtn?.addEventListener('click', close);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) close();
  });

  form?.addEventListener('submit', (e) => {
    e.preventDefault();
    form.classList.add('hidden');
    successMsg?.classList.remove('hidden');
    setTimeout(() => {
      close();
      form.reset();
      form.classList.remove('hidden');
      successMsg?.classList.add('hidden');
    }, 3000);
  });
}

/* -------------------------------------------------------------
   10. Animated Stats Counter
   ------------------------------------------------------------- */
function initStatsCounter() {
  const counters = document.querySelectorAll('.stat-counter');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counter = entry.target;
        const target = parseInt(counter.getAttribute('data-target') || '0', 10);
        let count = 0;
        const speed = 40;
        const increment = Math.max(1, Math.ceil(target / speed));

        const timer = setInterval(() => {
          count += increment;
          if (count >= target) {
            counter.textContent = target.toLocaleString('en-IN') + '+';
            clearInterval(timer);
          } else {
            counter.textContent = count.toLocaleString('en-IN') + '+';
          }
        }, 30);

        obs.unobserve(counter);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(c => observer.observe(c));
}

function escapeHtml(str) {
  return str.replace(/[&<>'"]/g, tag => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    "'": '&#39;',
    '"': '&quot;'
  }[tag] || tag));
}
