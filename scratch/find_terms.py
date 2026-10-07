import os
import glob

search_terms = {
    'Rasheed': None,
    'Blessing': None,
    'TrueAccord': None,
    'Chatbase': None,
    'Spar AI': None,
    'Marcus Johnson': None,
    'Sarah Jenkins': None,
    'Employment Letter': None,
    'John Johnson': None,
    'Forensic Search': None,
    'Active Call time': None,
    'Delivered promises': None,
    'Collection Velocity': None,
    'CRITICAL': None,
}

files = glob.glob(r'images\UI\*.svg') + glob.glob(r'images\UI\*.png') + glob.glob(r'images\*.svg') + glob.glob(r'images\*.png')

results = {term: [] for term in search_terms}

for f in files:
    try:
        with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        for term in search_terms:
            if term.lower() in content.lower():
                results[term].append(os.path.basename(f))
    except Exception as e:
        pass

for term, found in results.items():
    print(f"[{term}]: {found}")
