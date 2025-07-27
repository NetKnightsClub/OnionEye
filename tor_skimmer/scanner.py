from tor_skimmer.fetcher import get_page
from tor_skimmer.parser import extract_links, skim_page_for_js
from datetime import datetime

def log_dead_site(url: str, reason: str = "Unknown"):
    timestamp = datetime.utcnow().strftime("%Y/%m/%d")
    with open("dead_onions.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {url} — {reason}\n")

def scan_sites(seeds, max_depth=3):
    visited = set()
    to_visit = [(seed, 0) for seed in seeds]  # (url, depth)
    site_statuses = {}  # This will be returned: {url: True/False}

    while to_visit:
        url, depth = to_visit.pop(0)
        if url in visited or depth > max_depth:
            continue
        visited.add(url)

        print(f"📡 Scanning: {url} (Depth: {depth})")
        html, error = get_page(url)

        if not html:
            print(f"⚠️ Failed to load {url} | Reason: {error}")
            site_statuses[url] = False
            log_dead_site(url, error)  # <-- LOG IT!
            continue

        site_statuses[url] = True
        links = extract_links(html, url)
        print(f"🔗 Found {len(links)} links on {url}")

        for link in links:
            if link not in visited:
                page_html, link_error = get_page(link)
                if page_html:
                    has_js = skim_page_for_js(page_html)
                    print(f"   ➜ {link} | JS Required: {has_js}")
                    to_visit.append((link, depth + 1))
                else:
                    print(f"   ❌ Could not load {link} | Reason: {link_error}")
                    site_statuses[link] = False
                    log_dead_site(link, link_error)

    return site_statuses


# something something, funny really funny, you fall out of your chair now
