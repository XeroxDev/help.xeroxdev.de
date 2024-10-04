# This hook adds target="_blank" rel="noreferrer" to all external links
# This is a security measure to prevent external sites from tracking users
import re


def on_page_content(html, **kwargs):
    def replace_link(match):
        link = match.group(0)
        if 'href' in link and 'http' in link:
            if 'target="_blank"' not in link:
                link = link[:-1] + ' target="_blank" rel="noreferrer">'
        return link

    return re.sub(r'<a [^>]*>', replace_link, html)
