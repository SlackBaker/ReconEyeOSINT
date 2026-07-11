import httpx


sites = {
    "https://www.facebook.com/",
    "https://www.instagram.com/",
    "https://www.twitter.com/",
    "https://www.linkedin.com/in/",
    "https://www.youtube.com/@",
    "https://www.tiktok.com/@",
    "https://www.reddit.com/",
    "https://www.github.io/",
    "https://www.pinterest.com/",
    "https://www.threads.com/",
    "https://www.snapchat.com/",
    "https://www.steampowered.com/",
    "https://www.xbox.com/"
}

def checknickname():
    nickname = input("Write your nickname: ")
    found = []
    header = {"User-Agent": "Mozilla/5.0"}

    for site in sites:
        url = site + nickname
        try:
            r = httpx.get(url, timeout=5, headers=header)

            if r.status_code == 200:
                print(f"[+] Found: {url}")
                found.append(url)
            else:
                print(f"[-] Not found on {site}")

        except httpx.RequestError:
            print(f"[!] Error connecting to {site}")

    return found