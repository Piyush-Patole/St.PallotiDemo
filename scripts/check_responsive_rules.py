import os, re

files = ['index.html', 'department-template.html'] + [os.path.join('departments', f) for f in os.listdir('departments') if f.endswith('.html')]

print("Checking responsive layout attributes...")

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Check for tables without overflow-x-auto parent
    tables = re.findall(r'<table[^>]*>', text)
    if tables and 'overflow-x-auto' not in text:
        print(f"Warning: {path} has table but no overflow-x-auto")

    # Check for hardcoded fixed widths on containers without max-w or responsive prefixes
    # e.g., style="width: 1000px" or class="w-[800px]" without responsive prefixes
    suspicious = re.findall(r'class="[^"]*(?:w-\[\d{4}px\])[^"]*"', text)
    if suspicious:
        print(f"Warning: {path} has wide fixed width: {suspicious}")

print("Responsive layout attribute checks completed successfully!")
