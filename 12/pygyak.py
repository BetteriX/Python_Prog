import urllib.request


def get_page(url: str) -> str:  # Üres url el is lehet
    response = urllib.request.urlopen(url)

    raw = response.read()
    html = raw.decode("utf-8")

    return html
