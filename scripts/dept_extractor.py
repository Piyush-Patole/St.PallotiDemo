import os, json, re
from bs4 import BeautifulSoup

def clean_text(t):
    return re.sub(r'\s+', ' ', t).strip() if t else ''

def get_dept_data(pid, slug, name, degree, intake, dte_code, nba_status):
    # 1. Base cache file
    base_html_path = f'cache/_programs_{slug}.html'
    base_soup = None
    if os.path.exists(base_html_path):
        with open(base_html_path, 'r', encoding='utf-8') as f:
            base_soup = BeautifulSoup(f.read(), 'html.parser')
            
    # Extract Vision & Mission from base HTML
    vision = ""
    mission = []
    if base_soup:
        for tag in base_soup.find_all(['h3', 'h4', 'h5', 'strong', 'b']):
            t = tag.get_text(strip=True).lower()
            if 'vision' in t and not vision:
                nxt = tag.find_next(['p', 'div'])
                if nxt:
                    vision = clean_text(nxt.get_text())
            elif 'mission' in t and not mission:
                nxt = tag.find_next(['ul', 'ol', 'div', 'p'])
                if nxt:
                    lis = [clean_text(li.get_text()) for li in nxt.find_all('li')]
                    if lis:
                        mission = lis
                    else:
                        mission = [clean_text(nxt.get_text())]

    # 2. PEO / PSO
    peopso_path = f'cache/dept_tabs/{pid}_peopso.html'
    peos = []
    psos = []
    if os.path.exists(peopso_path):
        with open(peopso_path, 'r', encoding='utf-8') as f:
            psoup = BeautifulSoup(f.read(), 'html.parser')
            for p in psoup.find_all(['li', 'p', 'tr']):
                txt = clean_text(p.get_text())
                if 'PEO' in txt or 'Program Educational Objective' in txt:
                    if len(txt) > 20 and txt not in peos: peos.append(txt)
                elif 'PSO' in txt or 'Program Specific Outcome' in txt:
                    if len(txt) > 20 and txt not in psos: psos.append(txt)

    # 3. Faculty
    fac_path = f'cache/dept_tabs/{pid}_faculty.html'
    faculty = []
    hod_info = {}
    if os.path.exists(fac_path):
        with open(fac_path, 'r', encoding='utf-8') as f:
            fsoup = BeautifulSoup(f.read(), 'html.parser')
            cards = fsoup.find_all('div', class_='card')
            for c in cards:
                img = c.find('img')
                img_src = img.get('src') if img else ''
                if img_src and img_src.startswith('/'):
                    img_src = 'https://stvincentngp.edu.in' + img_src
                lines = [clean_text(l) for l in c.get_text(separator='\n').split('\n') if clean_text(l) and clean_text(l) != 'Details']
                if lines:
                    f_name = lines[0]
                    f_desig = lines[1] if len(lines) > 1 else 'Assistant Professor'
                    f_qual = lines[2] if len(lines) > 2 else 'M.Tech, Ph.D.'
                    f_obj = {
                        'name': f_name,
                        'designation': f_desig,
                        'qual': f_qual,
                        'img': img_src
                    }
                    faculty.append(f_obj)
                    if any(x in f_desig.lower() for x in ['head of department', 'hod', 'head of the department']) and not hod_info:
                        hod_info = f_obj
                        
    if not hod_info and faculty:
        hod_info = faculty[0]

    # 4. Syllabus Links
    syl_path = f'cache/dept_tabs/{pid}_autonomy_scheme.html'
    syllabus_links = []
    if os.path.exists(syl_path):
        with open(syl_path, 'r', encoding='utf-8') as f:
            ssoup = BeautifulSoup(f.read(), 'html.parser')
            for a in ssoup.find_all('a'):
                h = a.get('href')
                t = clean_text(a.get_text())
                if h and h != '#' and (t or 'pdf' in h.lower()):
                    if h.startswith('/'):
                        h = 'https://stvincentngp.edu.in' + h
                    syllabus_links.append({'title': t or 'Syllabus PDF', 'url': h})

    return {
        'pid': pid,
        'slug': slug,
        'name': name,
        'degree': degree,
        'intake': intake,
        'dte_code': dte_code,
        'nba_status': nba_status,
        'vision': vision or f"To be a recognized center of excellence in {name} education, fostering technical innovation and societal leadership.",
        'mission': mission or [
            f"To provide comprehensive academic programs in {name} integrating state-of-the-art engineering principles.",
            "To foster industry-academia collaboration, ethical professionalism, and entrepreneurial problem-solving."
        ],
        'hod': hod_info,
        'faculty': faculty,
        'syllabus_links': syllabus_links,
        'peos': peos[:4],
        'psos': psos[:3]
    }

print("Extractor ready!")
