import hashlib

def cache(url):
    if url not in cached_pages:
        cached_pages.update({url: hashlib.sha256('webpages'.encode() + url.encode()).hexdigest()})
    else:
        print(url)

cached_pages = {}

cache('https://www.ya1.ru')
cache('https://www.ya1.ru')
cache('https://www.ya2.ru')

print(cached_pages)