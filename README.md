# OnionEye

**An eye on the ToR Browser network... get it, Onion Eye? 👁️🧅**

---

## What is OnionEye?

OnionEye is a lightweight Python tool designed to skim and crawl the Tor network and regular websites, hunting down .onion and regular HTTP/HTTPS links. It’s built for cybersecurity enthusiasts, researchers, and curious minds who want to explore and analyze hidden services through the Tor proxy — all without the usual bloated overhead.

---

## Features

- **Multi-seed crawling:** Start from multiple seed URLs and explore links recursively.
- **Tor SOCKS5 proxy support:** Route all requests safely over your local Tor proxy.
- **Link extraction:** Parses HTML to find both regular and .onion links.
- **JavaScript detection:** Quickly detects if a page requires JS (for awareness).
- **Configurable depth:** Limit how deep the crawler dives.
- **Modular and extensible:** Clean Python modules to easily tweak or extend.

---

## Requirements

- Python 3.7+
- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- Tor running locally with SOCKS5 proxy enabled (usually on `127.0.0.1:9050`)

---

## Setup

1. Install required Python packages:

```pip install requests beautifulsoup4```

    Make sure you have Tor installed and running. On most systems:
    
```sudo systemctl start tor```

or launch the Tor Browser which provides the SOCKS proxy.

    Update your seeds.json with your desired starting URLs.

---

# Usage

Run the crawler with:

```./startscript.sh```
(You may have to `chmod u+x startscript.sh` first)

You’ll see the scan progress in your terminal with info about discovered links and whether they require JavaScript.

---

# Project Structure

```
OnionEye/
├── tor_skimmer/
│   ├── fetcher.py       # Handles HTTP requests through Tor proxy
│   ├── parser.py        # Extracts links and detects JS presence
│   ├── scanner.py       # Core crawler logic
│   ├── storage.py       # JSON export helpers (future use)
├── seeds.json           # List of starting seed URLs
├── run.py               # CLI entry point to launch scan
├── README.md            # This file
```

---

# Contributing

Contributions are welcome! Feel free to open issues or pull requests for:

    More efficient crawling

    Better JS detection

    Web UI integration

    Exporting scan results

    Anything else cool you dream up!

  ---

# Disclaimer

Use OnionEye responsibly and legally. Do NOT scan or scrape sites without permission. The author is not responsible for any misuse.

---

# License

```MIT License — See LICENSE for details.```

Made with ❤️ by DrKel and the NetKnights Cybersecurity Club

Ready to get your eye on the onions? 🧅👁️
