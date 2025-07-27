import requests

TOR_PROXY = 'socks5h://127.0.0.1:9050'

def get_page(url, user_agent="DrKelBot/1.0", timeout=10):
    headers = {'User-Agent': user_agent}
    proxies = {'http': TOR_PROXY, 'https': TOR_PROXY}
    try:
        resp = requests.get(url, headers=headers, proxies=proxies, timeout=timeout)
        if resp.status_code == 200:
            return resp.text
        else:
            print(f"Non-200 status code {resp.status_code} for {url}")
            return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

# hehe im a comment!
