from tor_skimmer.fetcher import get_page
from tor_skimmer.parser import extract_links, skim_page_for_js

def scan_sites(seeds, max_depth=3):
    visited = set()
    to_visit = [(seed, 0) for seed in seeds]  # Track depth per URL

    while to_visit:
        url, depth = to_visit.pop(0)
        if url in visited or depth > max_depth:
            continue
        visited.add(url)

        print(f"Scanning: {url} (Depth: {depth})")
        html = get_page(url)
        if not html:
            print(f"Failed to load {url}")
            continue

        links = extract_links(html, url)
        print(f"Found {len(links)} links on {url}")

        for link in links:
            if link not in visited:
                page_html = get_page(link)
                if page_html:
                    has_js = skim_page_for_js(page_html)
                    print(f" - {link} | JS Required: {has_js}")
                    to_visit.append((link, depth + 1))

# something something, funny really funny, you fall out of your chair now
