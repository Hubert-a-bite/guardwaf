BOTS = ["curl", "wget", "python-requests", "bot", "scrapy"]

def is_bot(ua: str) -> bool:
    ua = ua.lower()
    return any(bot in ua for bot in BOTS)
