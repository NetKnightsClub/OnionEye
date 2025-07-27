import requests

def get_page(url):
    try:
        response = requests.get(
            url,
            timeout=10,
            proxies={"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}
        )
        if response.status_code != 200:
            return None, f"Status Code {response.status_code}"
        return response.text, None
    except requests.exceptions.RequestException as e:
        return None, str(e)


# hehe im a comment!
