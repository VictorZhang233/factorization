"""Minimal but robust BibTeX parser that keeps the raw text of every entry."""
import re

def _skip_ws(t, i):
    while i < len(t) and t[i] in ' \t\r\n':
        i += 1
    return i

def _read_braced(t, i):
    # t[i] == '{' ; return (content, index after closing brace)
    assert t[i] == '{'
    depth = 0; j = i
    while j < len(t):
        c = t[j]
        if c == '\\':
            j += 2; continue
        if c == '{': depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return t[i+1:j], j+1
        j += 1
    raise ValueError('unbalanced braces at %d' % i)

def _read_quoted(t, i):
    assert t[i] == '"'
    depth = 0; j = i+1
    while j < len(t):
        c = t[j]
        if c == '\\':
            j += 2; continue
        if c == '{': depth += 1
        elif c == '}': depth -= 1
        elif c == '"' and depth == 0:
            return t[i+1:j], j+1
        j += 1
    raise ValueError('unterminated quote at %d' % i)

def parse_fields(body):
    fields = {}
    order = []
    i = 0
    n = len(body)
    while True:
        i = _skip_ws(body, i)
        if i >= n: break
        if body[i] == ',':
            i += 1; continue
        m = re.match(r'([A-Za-z][A-Za-z0-9_\-:.]*)\s*=\s*', body[i:])
        if not m:
            # trailing garbage
            break
        name = m.group(1).lower(); i += m.end()
        parts = []
        while True:
            i = _skip_ws(body, i)
            if i < n and body[i] == '{':
                v, i = _read_braced(body, i); parts.append(v)
            elif i < n and body[i] == '"':
                v, i = _read_quoted(body, i); parts.append(v)
            else:
                m2 = re.match(r'[A-Za-z0-9_\-:.]+', body[i:])
                if not m2: break
                parts.append(m2.group(0)); i += m2.end()
            i = _skip_ws(body, i)
            if i < n and body[i] == '#':
                i += 1; continue
            break
        fields[name] = ''.join(parts)
        order.append(name)
    return fields, order

def parse_bib(text, source=''):
    entries = []
    i = 0
    while True:
        j = text.find('@', i)
        if j < 0: break
        m = re.match(r'@\s*([A-Za-z]+)\s*([\{\(])', text[j:])
        if not m:
            i = j+1; continue
        typ = m.group(1).lower()
        if typ in ('comment', 'preamble', 'string'):
            # skip balanced block
            k = j + m.end() - 1
            if text[k] == '{':
                _, i = _read_braced(text, k)
            else:
                i = k+1
            continue
        k = j + m.end() - 1
        content, end = _read_braced(text, k)
        km = re.match(r'\s*([^,\s]+)\s*,', content)
        key = km.group(1)
        body = content[km.end():]
        fields, order = parse_fields(body)
        entries.append({'type': typ, 'key': key, 'fields': fields, 'order': order,
                        'raw': text[j:end], 'source': source})
        i = end
    return entries

def norm_doi(d):
    if not d: return None
    d = d.strip().lower()
    d = re.sub(r'^(https?://)?(dx\.)?doi\.org/', '', d)
    d = d.replace('\\_', '_')
    return d or None

def norm_arxiv(e):
    if not e: return None
    e = e.strip()
    e = re.sub(r'^arxiv:', '', e, flags=re.I)
    e = re.sub(r'v\d+$', '', e)
    return e.lower() or None
