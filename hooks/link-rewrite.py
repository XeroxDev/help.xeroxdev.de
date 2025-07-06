import re

def on_page_content(html, **kwargs):
    def replace_link(match):
        link = match.group(0)
        if 'href' in link and 'http' in link:
            if 'target="_blank"' not in link:
                link = link[:-1] + ' target="_blank" rel="noopener noreferrer">'
        return link

    return re.sub(r'<a [^>]*>', replace_link, html)
