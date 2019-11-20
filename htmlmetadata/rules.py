def get_attribute(name):
    def extract(node):
        return node.attrs.get(name, "").strip()

    return extract


def get_element_text(node):
    return node.text.strip()


def make_absolute_url(value):
    if value.startswith("//"):
        return "https:{}".format(value)
    return value


def cleanup_keywords(value):
    return list(set(map(lambda key: key.strip(), value.split(","))))


def cleanup_language(value):
    if "_" in value:
        return value.split("_", 1)[0]

    return value.split("-", 1)[0]


__all__ = ['Rules']

Rules = {
    "description": {
        "rules": [
            ['meta[property="og:description"]', get_attribute("content")],
            ['meta[name="description"]', get_attribute("content")],
        ]
    },
    "date": {
        "rules": [
            ["meta[property='article:published_time']", get_attribute("content")],
            ["meta[itemprop*='datePublished']", get_attribute("content")],
            ["meta[name='dcterms.modified']", get_attribute("content")],
            ["meta[name='dcterms.date']", get_attribute("content")],
            ["meta[name='DC.date.issued']", get_attribute("content")],
            ["meta[name='dc.date.issued']", get_attribute("content")],
            ["meta[name='dc.date.modified']", get_attribute("content")],
            ["meta[name='dc.date.created']", get_attribute("content")],
            ["meta[name='DC.date']", get_attribute("content")],
            ["meta[name='DC.Date']", get_attribute("content")],
            ["meta[name='dc.date']", get_attribute("content")],
            ["meta[name='date']", get_attribute("content")],
            ["time[itemprop*='pubDate']", get_attribute("content")],
            ["time[itemprop*='pubdate']", get_attribute("content")],
            ["span[itemprop*='datePublished']", get_attribute("content")],
            ["span[property*='datePublished']", get_attribute("content")],
            ["p[itemprop*='datePublished']", get_attribute("content")],
            ["p[property*='datePublished']", get_attribute("content")],
            ["div[itemprop*='datePublished']", get_attribute("content")],
            ["div[property*='datePublished']", get_attribute("content")],
            ["li[itemprop*='datePublished']", get_attribute("content")],
            ["li[property*='datePublished']", get_attribute("content")],
            ["time", get_attribute("datetime")],
            ["span[class*='date']", get_element_text],
            ["p[class*='date']", get_element_text],
            ["div[class*='date']", get_element_text],
        ]
    },
    "icon": {
        "rules": [
            ['link[rel="apple-touch-icon"]', get_attribute("href")],
            ['link[rel="apple-touch-icon-precomposed"]', get_attribute("href")],
            ['link[rel="icon"]', get_attribute("href")],
            ['link[rel="fluid-icon"]', get_attribute("href")],
            ['link[rel="shortcut icon"]', get_attribute("href")],
            ['link[rel="Shortcut Icon"]', get_attribute("href")],
            ['link[rel="mask-icon"]', get_attribute("href")],
        ],
        "processors": [make_absolute_url],
    },
    "image": {
        "rules": [
            ['meta[name="twitter:image"]', get_attribute("content")],
            ['meta[property="twitter:image"]', get_attribute("content")],
            ['meta[property="og:image:secure_url"]', get_attribute("content")],
            ['meta[property="og:image:src"]', get_attribute("content")],
            ['meta[property="og:image:url"]', get_attribute("content")],
            ['meta[property="og:image0"]', get_attribute("content")],
            ['meta[property="og:image"]', get_attribute("content")],
            ['meta[name="thumbnail"]', get_attribute("content")],
            ["article img[src]", get_attribute("src")],
            ["#content img[src]", get_attribute("src")],
        ],
        "processors": [make_absolute_url],
    },
    "keywords": {
        "rules": [
            ['meta[name="keywords"]', get_attribute("content")],
            ['meta[name="news_keywords"]', get_attribute("content")],
        ],
        "processors": [cleanup_keywords],
    },
    "title": {
        "rules": [
            ['meta[property="og:title"]', get_attribute("content")],
            ['meta[name="twitter:title"]', get_attribute("content")],
            ['meta[property="twitter:title"]', get_attribute("content")],
            ['meta[name="hdl"]', get_attribute("content")],
            ["title", get_element_text],
        ]
    },
    "language": {
        "rules": [
            ["html[lang]", get_attribute("lang")],
            ['meta[name="language"]', get_attribute("content")],
            ['meta[name="lang"]', get_attribute("content")],
            ["meta[http-equiv=content-language]", get_attribute("content")],
        ],
        "processors": [cleanup_language],
    },
    "type": {
        "rules": [
            ['meta[property="og:type"]', get_attribute("content")],
            ['meta[name="twitter:card"]', get_attribute("content")],
        ]
    },
    "author": {
        "rules": [
            ['meta[property="article:author"]', get_attribute("content")],
            ['meta[property="og:article:author"]', get_attribute("content")],
            ['meta[name="author"]', get_attribute("content")],
            ['meta[name="dcterms.creator"]', get_attribute("content")],
            ['meta[name="DC.creator"]', get_attribute("content")],
            ['meta[name="DC.Creator"]', get_attribute("content")],
            ['meta[name="dc.creator"]', get_attribute("content")],
            ['meta[name="creator"]', get_attribute("content")],
        ]
    },
    "url": {
        "rules": [
            ["a.amp-canurl", get_attribute("href")],
            ['link[rel="canonical"]', get_attribute("href")],
            ['meta[property="og:url"]', get_attribute("content")],
        ],
        "processors": [make_absolute_url],
    },
    "provider": {
        "rules": [
            ['meta[property="og:site_name"]', get_attribute("content")],
            ['meta[name="twitter:creator"]', get_attribute("content")],
            ['meta[name="twitter:site"]', get_attribute("content")],
        ]
    },
}
