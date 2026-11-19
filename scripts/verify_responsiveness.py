import os, re
from html.parser import HTMLParser

class SimpleValidator(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.tags = []
        self.errors = []
        self.void_tags = {
            'meta', 'link', 'img', 'br', 'hr', 'input', 'source', 'area', 'base', 'col', 'embed', 'param', 'track', 'wbr',
            'path', 'circle', 'line', 'polyline', 'polygon', 'rect', 'ellipse', 'use'
        }

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_tags:
            line, col = self.getpos()
            self.tags.append((tag.lower(), line))

    def handle_endtag(self, tag):
        t = tag.lower()
        if t in self.void_tags:
            return
        line, col = self.getpos()
        if not self.tags:
            self.errors.append(f"L{line}: Unexpected closing tag </{t}> with empty stack")
            return
        last, last_line = self.tags.pop()
        if last != t:
            self.errors.append(f"L{line}: Tag mismatch: expected </{last}> (opened at L{last_line}), found </{t}>")

html_files = ['index.html', 'department-template.html']
for f in os.listdir('departments'):
    if f.endswith('.html'):
        html_files.append(os.path.join('departments', f))

for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    val = SimpleValidator(path)
    val.feed(content)
    if val.errors:
        print(f"ERRORS in {path}:")
        for err in val.errors:
            print("  ", err)
    elif val.tags:
        print(f"UNCLOSED TAGS in {path}: {val.tags}")
    else:
        print(f"PASSED: {path}")
