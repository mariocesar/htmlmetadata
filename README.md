# HTMLmetadata
Extract metadata from html pages using Open Graph metadata, HTML metadata, and a series of fallbacks

> Inspired in https://metascraper.js.org

# Install

```bash
pip install htmlmetadata
```

# Use

You can use it by calling the module directly.

```
python -m htmlmetadata http://schema.org/docs/about.html                                                                            
{
  "request": {
    "url": "http://schema.org/docs/about.html"
  },
  "summary": {
    "description": "Schema.org is a set of extensible schemas that enables webmasters to embed\n    structured data on their web pages for use by search engines and other applications.",
    "title": "about page - schema.org",
    "language": "en"
  }
}
```

Or use it directly in your code.

```python
from htmlmetadata import extract_metadata

data = extract_metadata("http://schema.org/docs/about.html")
```
