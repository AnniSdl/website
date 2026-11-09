"""Packt eine gebaute Hugo-Seite in EINE HTML-Datei (CSS, Schriften, Bilder eingebettet).
Aufruf: python3 vorschau.py <public-ordner> <seite/index.html> <ausgabe.html> <url-prefix>
"""
import base64, re, sys, pathlib

root = pathlib.Path(sys.argv[1]); page = root / sys.argv[2]; out = pathlib.Path(sys.argv[3]); prefix = sys.argv[4]
html = page.read_text()

def local(url):
    # prefix = Pfad, unter dem die Seite gebaut wurde, z. B. "/website/"
    url = url.split('#')[0].split('?')[0]
    url = re.sub(r'^https?://[^/]+', '', url)
    if url.startswith(prefix): url = url[len(prefix):]
    return root / url.lstrip('/')

def data_uri(path):
    mime = {'.woff2': 'font/woff2', '.webp': 'image/webp', '.jpg': 'image/jpeg', '.png': 'image/png', '.svg': 'image/svg+xml'}[path.suffix]
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode()

# Sicherheitsregel entfernen (würde eingebettetes CSS blockieren) – nur in der Vorschau
html = re.sub(r'<meta http-equiv=Content-Security-Policy[^>]*>', '', html)
html = re.sub(r'<meta http-equiv="Content-Security-Policy"[^>]*>', '', html)

# CSS einbetten, Schriften darin als data-URI
def css_repl(m):
    href = m.group(1)
    css_path = local(href)
    css = css_path.read_text()
    css = re.sub(r'url\("?\.\./fonts/([^")]+)"?\)', lambda f: f'url("{data_uri(root / "fonts" / f.group(1))}")', css)
    return f'<style>{css}</style>'
html = re.sub(r'<link rel=stylesheet href=([^ >]+)[^>]*>', css_repl, html)

# Bilder: srcset weg, src als data-URI
html = re.sub(r' srcset="[^"]*"', '', html)
html = re.sub(r' srcset=[^ >]+', '', html)
html = re.sub(r'loading=lazy', '', html)
def img_repl(m):
    return f'src="{data_uri(local(m.group(1)))}"'
html = re.sub(r'src="?([^" >]+\.(?:webp|jpg|png))"?', img_repl, html)

# Hinweis oben, dass dies eine Vorschau ist
html = html.replace('<body>', '<body><div style="background:#183f3b;color:#fffdf8;text-align:center;padding:.5rem 1rem;font:15px system-ui">Vorschau – Links zu anderen Seiten funktionieren hier nicht</div>', 1)
out.write_text(html)
print(out, round(out.stat().st_size / 1024), 'KB')
