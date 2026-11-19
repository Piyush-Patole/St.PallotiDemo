import os, json

os.makedirs('departments', exist_ok=True)

with open('assets/data/departments_full.json', 'r', encoding='utf-8') as f:
    departments = json.load(f)

def get_initials(name):
    clean = name.replace('Dr.', '').replace('Mrs.', '').replace('Mr.', '').replace('Prof.', '').strip()
    parts = clean.split()
    if len(parts) >= 2:
        return (parts[0][0] + parts[-1][0]).upper()
    elif len(parts) == 1:
        return parts[0][:2].upper()
    return 'FC'

def build_portal_html(dept):
    slug = dept['slug']
    name = dept['name']
    degree = dept['degree']
    intake = dept['intake']
    dte_code = dept['dte_code']
    nba_status = dept['nba_status']
    tagline = dept['tagline']
    overview = dept['overview']
    placement_rate = dept['placement_rate']
    top_recruiters = dept['top_recruiters']
    labs = dept['labs']
    vision = dept['vision']
    mission = dept['mission']
    hod = dept['hod'] or {}
    faculty = dept['faculty'] or []
    syllabus_links = dept['syllabus_links'] or []
    peos = dept['peos'] or []
    psos = dept['psos'] or []

    hod_name = hod.get('name', 'Head of Department')
    hod_desig = hod.get('designation', 'Associate Professor & HOD')
    hod_qual = hod.get('qual', 'Ph.D., M.Tech, B.E.')
    hod_img = hod.get('img', '')
    hod_initials = get_initials(hod_name)

    # Mission items HTML
    mission_html = ""
    for m in mission:
        mission_html += f'<li class="flex items-start space-x-3"><span class="w-2 h-2 rounded-full bg-emerald-500 mt-2 shrink-0"></span><span>{m}</span></li>'

    # Faculty Cards HTML
    faculty_cards_html = ""
    for fac in faculty:
        f_name = fac.get('name', 'Faculty')
        f_desig = fac.get('designation', 'Assistant Professor')
        f_qual = fac.get('qual', 'M.Tech, Ph.D.')
        f_img = fac.get('img', '')
        f_initials = get_initials(f_name)

        img_tag = f'<img src="{f_img}" alt="{f_name}" class="w-16 h-16 rounded-2xl object-cover border border-slate-200" onerror="this.style.display=\'none\'; this.nextElementSibling.style.display=\'flex\';">' if f_img else ''
        fallback_initials = f'<div class="w-16 h-16 rounded-2xl bg-brand-100 border border-brand-200 text-brand-900 font-bold font-display text-lg flex items-center justify-center shrink-0" {"style=\'display:none;\'" if f_img else ""}>{f_initials}</div>'

        faculty_cards_html += f'''
        <div class="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-4 hover-lift">
          <div class="flex items-center space-x-4">
            <div class="relative shrink-0">
              {img_tag}
              {fallback_initials}
            </div>
            <div>
              <h4 class="text-base font-bold text-navy-950 font-display leading-tight">{f_name}</h4>
              <p class="text-xs text-brand-600 font-bold font-display mt-0.5">{f_desig}</p>
              <span class="text-xs text-slate-500 font-body block mt-0.5">{f_qual}</span>
            </div>
          </div>
          <div class="text-xs text-slate-600 bg-slate-50 p-3.5 rounded-2xl font-body space-y-1">
            <p><strong>Department:</strong> {name}</p>
            <p><strong>Affiliation:</strong> Autonomous Faculty Council</p>
          </div>
        </div>'''

    # Labs HTML
    labs_html = ""
    for idx, lab in enumerate(labs, 1):
        lab_name = lab.get('name', f'Laboratory {idx}')
        lab_focus = lab.get('focus', 'Advanced practical experiments and research.')
        labs_html += f'''
        <div class="p-7 rounded-3xl bg-white border border-slate-200 shadow-sm hover-lift flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="text-xs uppercase font-extrabold text-brand-600 font-display">Specialized Lab #{idx:02d}</span>
              <span class="w-3 h-3 rounded-full bg-emerald-400"></span>
            </div>
            <h4 class="text-xl font-bold text-navy-950 mb-2 font-display">{lab_name}</h4>
            <p class="text-sm text-slate-600 leading-relaxed font-body">{lab_focus}</p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500 font-display">
            <span>High-Precision Infrastructure</span>
            <span class="font-bold text-brand-700">Autonomous Wing</span>
          </div>
        </div>'''

    # Recruiters Pills
    recruiters_pills_html = ""
    for r in top_recruiters:
        recruiters_pills_html += f'<span class="px-4 py-2 bg-slate-100 text-navy-950 font-bold rounded-xl text-sm border border-slate-200 font-display">{r}</span>'

    # Syllabus Download Rows
    syllabus_rows_html = ""
    semesters = [
        ("Sem I & II", "First Year Foundation & Core Science", "42 Credits", "Physics/Chemistry, Engineering Mathematics, Programming, Basic Engineering"),
        ("Sem III & IV", "Core Disciplinary Foundations", "44 Credits", f"Fundamental {name} core theory, numerical analysis, experimental laboratories"),
        ("Sem V & VI", "Advanced Professional Specialization", "46 Credits", "Advanced discipline electives, industrial tool applications, collaborative mini-projects"),
        ("Sem VII & VIII", "Capstone Industry Project & Internship", "38 Credits", "Full semester corporate internship, major technical capstone, engineering ethics")
    ]
    for sem_title, sem_desc, sem_cr, sem_sub in semesters:
        syllabus_rows_html += f'''
        <tr class="hover:bg-white transition">
          <td class="py-5 px-6 font-bold text-slate-900 font-display text-base">{sem_title}</td>
          <td class="py-5 px-6 font-semibold text-navy-950">{sem_desc}</td>
          <td class="py-5 px-6">{sem_cr}</td>
          <td class="py-5 px-6">{sem_sub}</td>
          <td class="py-5 px-6 text-right font-display">
            <a href="https://stvincentngp.edu.in/pages/syllabus" target="_blank" rel="noopener" class="text-brand-600 hover:underline font-bold">Download Scheme &rarr;</a>
          </td>
        </tr>'''

    # HOD Image/Avatar
    hod_img_tag = f'<img src="{hod_img}" alt="{hod_name}" class="w-20 h-20 rounded-2xl object-cover border-2 border-brand-600" onerror="this.style.display=\'none\'; this.nextElementSibling.style.display=\'flex\';">' if hod_img else ''
    hod_fallback_avatar = f'<div class="w-20 h-20 rounded-2xl bg-brand-200 border-2 border-brand-600 flex items-center justify-center text-brand-900 font-black text-2xl font-display shrink-0" {"style=\'display:none;\'" if hod_img else ""}>{hod_initials}</div>'

    html = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Department of {name} | SVPCET Nagpur (Autonomous)</title>
  <meta name="description" content="Department of {name} at St. Vincent Pallotti College of Engineering &amp; Technology, Nagpur. Autonomous B.Tech programs, advanced labs, renowned faculty, and high-impact placements.">
  <link rel="icon" type="image/png" href="../assets/img/logo.png">

  <!-- Google Fonts: Outfit (Display & Headings) + Plus Jakarta Sans (Body) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Tailwind CSS via CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              50: '#f0f9fb',
              100: '#e0f4f8',
              500: '#11abc9',
              600: '#0098b8',
              700: '#007690',
              900: '#0b4857',
            }},
            navy: {{
              700: '#162b48',
              800: '#0c1b30',
              900: '#071527',
              950: '#030d1a',
            }}
          }},
          fontFamily: {{
            display: ['Outfit', 'sans-serif'],
            body: ['Plus Jakarta Sans', 'sans-serif'],
          }}
        }}
      }}
    }}
  </script>
  <link rel="stylesheet" href="../assets/css/styles.css">
</head>
<body class="bg-[#fafbfc] text-slate-800 font-body antialiased selection:bg-brand-500 selection:text-white">

  <!-- Top Utility Bar (Panoramic & Clean) -->
  <div class="bg-navy-950 text-slate-300 text-xs sm:text-sm py-2 sm:py-2.5 px-4 sm:px-6 border-b border-navy-800 hidden md:block">
    <div class="max-w-[1720px] mx-auto flex items-center justify-between">
      <div class="flex items-center space-x-6">
        <a href="../index.html" class="text-brand-300 hover:text-white flex items-center font-bold font-display">&larr; Back to Main SVPCET Portal</a>
        <span class="text-slate-700">|</span>
        <span class="text-slate-400">DTE Choice Code: <strong class="text-slate-200">{dte_code}</strong></span>
      </div>
      <div class="flex items-center space-x-6 font-display">
        <span class="text-amber-300 font-extrabold">{nba_status}</span>
        <span class="text-slate-700">|</span>
        <a href="../index.html#notices" class="hover:text-white font-medium">Exam Cell</a>
        <span class="text-slate-700">|</span>
        <a href="../index.html#fee-calculator" class="hover:text-white font-medium">Fee Estimator</a>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-0 z-40">
    <div class="max-w-[1720px] mx-auto px-4 sm:px-8 lg:px-14 py-3 sm:py-4 flex items-center justify-between">
      <a href="../index.html" class="flex items-center space-x-2.5 sm:space-x-4 shrink-0">
        <img src="../assets/img/logo.png" alt="SVPCET Emblem" class="h-10 sm:h-14 w-auto object-contain">
        <div class="border-l-2 border-slate-200 pl-2.5 sm:pl-4">
          <span class="text-[9px] sm:text-xs uppercase font-extrabold text-brand-600 tracking-widest font-display block">Department of</span>
          <h1 class="text-sm sm:text-xl lg:text-2xl font-black text-navy-950 leading-tight font-display max-w-[200px] sm:max-w-none truncate sm:whitespace-normal">{name}</h1>
        </div>
      </a>
      <div class="flex items-center space-x-2 sm:space-x-4 font-display shrink-0">
        <a href="../index.html" class="hidden sm:inline-flex items-center px-4 py-2.5 rounded-xl text-xs sm:text-sm font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 transition">
          &larr; Home
        </a>
        <a href="../index.html#admissions" class="px-3.5 sm:px-6 py-2 sm:py-2.5 rounded-xl text-xs sm:text-sm font-bold text-white bg-brand-600 hover:bg-brand-700 transition shadow-md shadow-brand-600/25 whitespace-nowrap">
          <span class="hidden sm:inline">Apply 2026-27</span>
          <span class="sm:hidden">Apply</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Breadcrumbs -->
  <div class="bg-slate-100/80 border-b border-slate-200 py-2 sm:py-2.5 px-4 sm:px-8 lg:px-14">
    <div class="max-w-[1720px] mx-auto text-xs sm:text-sm text-slate-500 flex items-center space-x-2 sm:space-x-3 font-medium overflow-x-auto whitespace-nowrap scrollbar-none">
      <a href="../index.html" class="hover:text-brand-600">Home</a>
      <span>/</span>
      <a href="../index.html#departments" class="hover:text-brand-600">Academics</a>
      <span>/</span>
      <span class="text-slate-800 font-bold font-display">{name}</span>
    </div>
  </div>

  <!-- Department Hero Banner (Panoramic & Spacious) -->
  <section class="bg-navy-950 text-white py-12 sm:py-20 lg:py-28 relative overflow-hidden">
    <div class="absolute inset-0 opacity-15 bg-[radial-gradient(#11abc9_1px,transparent_1px)] [background-size:28px_28px]"></div>

    <div class="relative max-w-[1720px] mx-auto px-4 sm:px-8 lg:px-14">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
        <div class="lg:col-span-8 space-y-4 sm:space-y-6">
          <div class="inline-flex items-center space-x-2 px-3.5 sm:px-4 py-1.5 rounded-full text-xs sm:text-sm font-bold bg-brand-500/20 text-brand-300 border border-brand-500/30 font-display">
            <span>Autonomous Curriculum | {nba_status}</span>
          </div>
          <h2 class="text-2xl sm:text-4xl md:text-5xl lg:text-6xl font-black text-white leading-tight font-display break-words">
            {tagline}
          </h2>
          <p class="text-slate-300 text-sm sm:text-lg lg:text-xl max-w-3xl leading-relaxed font-body">
            {overview}
          </p>
          <div class="flex flex-wrap gap-2.5 sm:gap-4 pt-2 sm:pt-3 font-display">
            <div class="bg-white/10 px-4 sm:px-5 py-2.5 sm:py-3 rounded-2xl border border-white/15">
              <span class="text-xs text-slate-400 block font-body">Sanctioned Intake:</span>
              <strong class="text-white text-sm sm:text-lg">{intake}</strong>
            </div>
            <div class="bg-white/10 px-4 sm:px-5 py-2.5 sm:py-3 rounded-2xl border border-white/15">
              <span class="text-xs text-slate-400 block font-body">Head of Department:</span>
              <strong class="text-white text-sm sm:text-lg">{hod_name}</strong>
            </div>
            <div class="bg-white/10 px-4 sm:px-5 py-2.5 sm:py-3 rounded-2xl border border-white/15">
              <span class="text-xs text-slate-400 block font-body">Placement Track:</span>
              <strong class="text-emerald-400 text-sm sm:text-lg">{placement_rate}</strong>
            </div>
          </div>
        </div>

        <div class="lg:col-span-4">
          <div class="bg-white/10 backdrop-blur-2xl p-6 sm:p-8 rounded-3xl border border-white/20 space-y-4 sm:space-y-5">
            <h3 class="text-sm sm:text-base font-extrabold uppercase tracking-widest text-brand-300 font-display">Quick Navigation</h3>
            <ul class="space-y-2.5 sm:space-y-3.5 text-xs sm:text-sm text-slate-200 font-body">
              <li><a href="#overview" class="hover:text-white flex items-center">&rarr; About &amp; Vision-Mission</a></li>
              <li><a href="#faculty" class="hover:text-white flex items-center">&rarr; Faculty Directory ({len(faculty)} Educators)</a></li>
              <li><a href="#syllabus" class="hover:text-white flex items-center">&rarr; Autonomous Syllabus (Schemes 1-8)</a></li>
              <li><a href="#laboratories" class="hover:text-white flex items-center">&rarr; Specialized Laboratories ({len(labs)} Labs)</a></li>
              <li><a href="#placements" class="hover:text-white flex items-center">&rarr; Placements &amp; Recruiting Partners</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Department Navigation Tabs -->
  <section class="sticky top-[58px] sm:top-[74px] z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm font-display">
    <div class="max-w-[1720px] mx-auto px-4 sm:px-8 lg:px-14 relative flex items-center overflow-x-auto scrollbar-none">
      <nav class="flex space-x-6 sm:space-x-10 text-xs sm:text-sm md:text-base font-bold py-3.5 sm:py-4 whitespace-nowrap shrink-0 horizontal-scroll-nav w-full" aria-label="Department Tabs">
        <a href="#overview" class="text-brand-600 border-b-2 border-brand-600 pb-3.5 sm:pb-4 -mb-3.5 sm:-mb-4 shrink-0 font-extrabold">Overview &amp; Vision</a>
        <a href="#faculty" class="text-slate-600 hover:text-brand-600 pb-3.5 sm:pb-4 -mb-3.5 sm:-mb-4 shrink-0">Faculty Directory</a>
        <a href="#syllabus" class="text-slate-600 hover:text-brand-600 pb-3.5 sm:pb-4 -mb-3.5 sm:-mb-4 shrink-0">Autonomous Syllabus</a>
        <a href="#laboratories" class="text-slate-600 hover:text-brand-600 pb-3.5 sm:pb-4 -mb-3.5 sm:-mb-4 shrink-0">Laboratories &amp; Facilities</a>
        <a href="#placements" class="text-slate-600 hover:text-brand-600 pb-3.5 sm:pb-4 -mb-3.5 sm:-mb-4 shrink-0">Placements &amp; Recruiters</a>
      </nav>
    </div>
  </section>

  <!-- Section 1: Overview, Vision & Mission -->
  <section id="overview" class="py-12 sm:py-16 lg:py-20 bg-white">
    <div class="max-w-[1720px] mx-auto px-4 sm:px-8 lg:px-14">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 lg:gap-12">
        
        <div class="lg:col-span-2 space-y-6 sm:space-y-8">
          <div>
            <h3 class="text-2xl sm:text-3xl font-extrabold text-navy-950 mb-3 sm:mb-4 font-display">About the Department</h3>
            <p class="text-sm sm:text-base lg:text-lg text-slate-600 leading-relaxed font-body">
              {overview}
            </p>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8">
            <div class="p-6 sm:p-8 rounded-3xl bg-slate-50 border border-slate-200">
              <div class="w-12 h-12 rounded-2xl bg-brand-100 text-brand-700 flex items-center justify-center font-black text-xl mb-4 font-display">V</div>
              <h4 class="text-xl font-bold text-navy-950 mb-3 font-display">Vision</h4>
              <p class="text-sm sm:text-base text-slate-600 leading-relaxed font-body">
                {vision}
              </p>
            </div>

            <div class="p-6 sm:p-8 rounded-3xl bg-slate-50 border border-slate-200">
              <div class="w-12 h-12 rounded-2xl bg-emerald-100 text-emerald-700 flex items-center justify-center font-black text-xl mb-4 font-display">M</div>
              <h4 class="text-xl font-bold text-navy-950 mb-3 font-display">Mission</h4>
              <ul class="text-sm sm:text-base text-slate-600 leading-relaxed font-body space-y-2">
                {mission_html}
              </ul>
            </div>
          </div>
        </div>

        <div class="bg-brand-50 rounded-3xl p-6 sm:p-8 border border-brand-100 flex flex-col justify-between">
          <div>
            <div class="flex items-center space-x-4 sm:space-x-5 mb-5">
              <div class="relative shrink-0">
                {hod_img_tag}
                {hod_fallback_avatar}
              </div>
              <div>
                <h4 class="text-base sm:text-lg font-bold text-navy-950 font-display">{hod_name}</h4>
                <p class="text-xs sm:text-sm text-brand-700 font-extrabold font-display">{hod_desig}</p>
                <p class="text-xs text-slate-500 font-medium">{hod_qual}</p>
              </div>
            </div>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed italic font-body">
              "We prepare engineers not just with textbook theories, but through hands-on laboratory experimentation, industrial internships, and high-standard ethics to thrive in competitive global landscapes."
            </p>
          </div>
          <div class="mt-6 sm:mt-8 pt-4 sm:pt-5 border-t border-brand-200 text-xs sm:text-sm text-slate-500">
            DTE Choice Code: <strong class="text-brand-900 font-display">{dte_code}</strong>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- Section 2: Faculty Directory -->
  <section id="faculty" class="py-12 sm:py-16 lg:py-20 bg-slate-50 border-t border-slate-200">
    <div class="max-w-[1720px] mx-auto px-4 sm:px-8 lg:px-14">
      <div class="mb-8 sm:mb-12">
        <span class="text-xs uppercase font-extrabold tracking-widest text-brand-600 font-display">Faculty Directory</span>
        <h3 class="text-2xl sm:text-4xl lg:text-5xl font-black text-navy-950 mt-2 font-display">Distinguished Educators &amp; Researchers</h3>
        <p class="text-sm sm:text-base lg:text-lg text-slate-600 mt-2 font-body">Academic excellence, doctoral research, and committed mentorship at {name}.</p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 sm:gap-8">
        {faculty_cards_html}
      </div>
    </div>
  </section>

  <!-- Section 3: Autonomous Syllabus Repository -->
  <section id="syllabus" class="py-12 sm:py-16 lg:py-20 bg-white border-t border-slate-200">
    <div class="max-w-[1720px] mx-auto px-4 sm:px-8 lg:px-14">
      <div class="mb-8 sm:mb-10">
        <span class="text-xs uppercase font-extrabold tracking-widest text-brand-600 font-display">Curriculum &amp; Ordinances</span>
        <h3 class="text-2xl sm:text-4xl lg:text-5xl font-black text-navy-950 mt-2 font-display">Autonomous Syllabus Scheme (2026-27)</h3>
        <p class="text-sm sm:text-base lg:text-lg text-slate-600 mt-2 font-body">Curated in consultation with the Board of Studies (BOS) and academic/industry advisory councils.</p>
      </div>

      <div class="bg-slate-50 rounded-3xl border border-slate-200 overflow-hidden shadow-sm">
        <div class="overflow-x-auto">
          <table class="min-w-[640px] w-full text-left text-xs sm:text-sm font-body">
            <thead class="bg-slate-100 text-slate-700 uppercase font-bold text-xs tracking-wider border-b border-slate-200 font-display">
              <tr>
                <th class="py-3.5 sm:py-4 px-4 sm:px-6">Semester</th>
                <th class="py-3.5 sm:py-4 px-4 sm:px-6">Scheme Title</th>
                <th class="py-3.5 sm:py-4 px-4 sm:px-6">Total Credits</th>
                <th class="py-3.5 sm:py-4 px-4 sm:px-6">Key Subjects</th>
                <th class="py-3.5 sm:py-4 px-4 sm:px-6 text-right">Syllabus PDF</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 text-slate-600">
              {syllabus_rows_html}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 4: Laboratories & Facilities -->
  <section id="laboratories" class="py-12 sm:py-16 lg:py-20 bg-slate-50 border-t border-slate-200">
    <div class="max-w-[1720px] mx-auto px-4 sm:px-8 lg:px-14">
      <div class="mb-8 sm:mb-12">
        <span class="text-xs uppercase font-extrabold tracking-widest text-brand-600 font-display">Practical Infrastructure</span>
        <h3 class="text-2xl sm:text-4xl lg:text-5xl font-black text-navy-950 mt-2 font-display">Specialized Laboratories &amp; Research Centers</h3>
        <p class="text-sm sm:text-base lg:text-lg text-slate-600 mt-2 font-body">Hands-on experimentation with industry-grade software suites and high-precision apparatus.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
        {labs_html}
      </div>
    </div>
  </section>

  <!-- Section 5: Placements & Recruiters -->
  <section id="placements" class="py-12 sm:py-16 lg:py-20 bg-white border-t border-slate-200">
    <div class="max-w-[1720px] mx-auto px-4 sm:px-8 lg:px-14">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
        <div class="lg:col-span-6 space-y-4 sm:space-y-6">
          <span class="text-xs uppercase font-extrabold tracking-widest text-emerald-600 font-display">Career Development Centre</span>
          <h3 class="text-2xl sm:text-4xl lg:text-5xl font-black text-navy-950 font-display leading-tight">
            High-Impact Career Outcomes &amp; Corporate Conversion
          </h3>
          <p class="text-sm sm:text-base lg:text-lg text-slate-600 leading-relaxed font-body">
            Graduates from the Department of {name} are consistently recruited by tier-1 MNCs, specialized engineering firms, and core industry leaders.
          </p>
          <div class="flex items-center space-x-6 pt-2 font-display">
            <div>
              <span class="text-2xl sm:text-3xl font-black text-navy-950 block">{placement_rate}</span>
              <span class="text-xs text-slate-500 font-body">Placement &amp; Higher Studies</span>
            </div>
            <div class="h-10 w-px bg-slate-200"></div>
            <div>
              <span class="text-2xl sm:text-3xl font-black text-brand-600 block">6-Month</span>
              <span class="text-xs text-slate-500 font-body">Dedicated Industry Internship Track</span>
            </div>
          </div>
        </div>

        <div class="lg:col-span-6 bg-slate-50 p-6 sm:p-8 rounded-3xl border border-slate-200 space-y-5 sm:space-y-6">
          <h4 class="text-xs sm:text-sm font-bold uppercase tracking-wider text-slate-700 font-display">Prominent Hiring Partners</h4>
          <div class="flex flex-wrap gap-2.5 sm:gap-3">
            {recruiters_pills_html}
          </div>
          <div class="pt-4 border-t border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <span class="text-xs text-slate-500 font-medium">Placement Assistance via CDC</span>
            <a href="../index.html#corporate" class="text-xs sm:text-sm font-bold text-brand-700 hover:text-brand-900 font-display">View Central Placement Portal &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-navy-950 text-slate-400 py-8 sm:py-12 px-4 sm:px-8 text-xs sm:text-sm border-t border-navy-800 text-center font-body">
    <p>&copy; 2026 Department of {name} | St. Vincent Pallotti College of Engineering &amp; Technology, Nagpur</p>
    <div class="mt-4 flex flex-wrap justify-center gap-4 sm:gap-6 font-display font-medium">
      <a href="../index.html" class="hover:text-white">Main Portal</a>
      <a href="../index.html#admissions" class="hover:text-white">Admissions</a>
      <a href="../index.html#notices" class="hover:text-white">Exam Cell</a>
      <a href="../index.html#contact" class="hover:text-white">Contact Us</a>
    </div>
  </footer>

  <script src="../assets/js/main.js"></script>
</body>
</html>'''
    return html

for dept in departments:
    slug = dept['slug']
    html_content = build_portal_html(dept)
    out_path = os.path.join('departments', f"{slug}.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated: {out_path} ({len(html_content)} bytes)")

# Also update department-template.html with the rich CSE portal
cse_dept = next(d for d in departments if d['slug'] == 'computer-science-and-engineering')
cse_root_html = build_portal_html(cse_dept).replace('../assets/', 'assets/').replace('../index.html', 'index.html')
with open('department-template.html', 'w', encoding='utf-8') as f:
    f.write(cse_root_html)

print("Updated department-template.html successfully!")
print("All 13 branch portals successfully generated in departments/!")
