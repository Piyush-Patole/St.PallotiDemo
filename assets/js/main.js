/**
 * St. Vincent Pallotti College of Engineering & Technology (SVPCET)
 * Modern Institutional Client Architecture
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileDrawer();
  initSearchModal();
  initProgramFilter();
  initFeeCalculator();
  initNoticeTabs();
  initStatsCounter();
});

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

  // Mobile Accordion items
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

  // Shortcut key: Ctrl + K or Cmd + K
  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      modal.classList.contains('hidden') ? openModal() : closeModal();
    }
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      closeModal();
    }
  });

  // Search indexing
  const searchablePages = [
    { title: 'Computer Science & Engineering', category: 'Academic Department', url: '#departments' },
    { title: 'Artificial Intelligence & Machine Learning', category: 'Academic Department', url: '#departments' },
    { title: 'Data Science (B.Tech)', category: 'Academic Department', url: '#departments' },
    { title: 'Cyber Security (B.Tech)', category: 'Academic Department', url: '#departments' },
    { title: 'Robotics & AI', category: 'Academic Department', url: '#departments' },
    { title: 'Computer Science & Business Systems (TCS)', category: 'Academic Department', url: '#departments' },
    { title: 'Electrical Engineering (NBA Accredited)', category: 'Academic Department', url: '#departments' },
    { title: 'Electronics & Telecommunication', category: 'Academic Department', url: '#departments' },
    { title: 'Mechanical Engineering', category: 'Academic Department', url: '#departments' },
    { title: 'Civil Engineering', category: 'Academic Department', url: '#departments' },
    { title: 'B.Tech Admissions 2026-27 & CAP Eligibility', category: 'Admissions', url: '#admissions' },
    { title: 'Fee Structure & Scholarships Calculator', category: 'Admissions', url: '#fee-calculator' },
    { title: 'Autonomous Exam Cell & Timetables', category: 'Academics & Exams', url: '#notices' },
    { title: 'Career Development & Placement Records', category: 'Placements', url: '#placements' },
    { title: 'Drone Lab (Texcelrators)', category: 'Research & Labs', url: '#research' },
    { title: 'Boys & Girls Hostels Facilities', category: 'Campus Life', url: '#hostels' },
    { title: 'NAAC A Grade & NBA Accreditations', category: 'Governance & NIRF', url: '#about' },
    { title: 'Emergency Contacts & 24x7 Security Guards', category: 'Contact & Safety', url: '#contact' }
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
          <p class="text-sm mt-1">Try searching for "CSE", "Fees", "Admissions", "Placements", or "Exam".</p>
        </div>
      `;
      return;
    }

    resultsContainer.innerHTML = filtered.map(item => `
      <a href="${item.url}" class="search-result-item flex items-center justify-between p-3 rounded-lg hover:bg-cyan-50 transition border border-transparent hover:border-cyan-200 group">
        <div>
          <span class="text-xs uppercase font-semibold tracking-wider text-cyan-700 bg-cyan-100 px-2 py-0.5 rounded-full">${item.category}</span>
          <h4 class="font-medium text-slate-800 group-hover:text-cyan-800 mt-1">${item.title}</h4>
        </div>
        <svg class="w-5 h-5 text-slate-400 group-hover:text-cyan-600 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24">
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
        b.classList.remove('bg-cyan-700', 'text-white', 'shadow-sm');
        b.classList.add('bg-slate-100', 'text-slate-700', 'hover:bg-slate-200');
      });
      btn.classList.remove('bg-slate-100', 'text-slate-700', 'hover:bg-slate-200');
      btn.classList.add('bg-cyan-700', 'text-white', 'shadow-sm');

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
        t.classList.remove('border-cyan-600', 'text-cyan-700', 'font-semibold');
        t.classList.add('border-transparent', 'text-slate-500', 'hover:text-slate-700');
      });
      tab.classList.add('border-cyan-600', 'text-cyan-700', 'font-semibold');
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
   7. Animated Stats Counter
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
