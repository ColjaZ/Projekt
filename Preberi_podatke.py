import re

vzorec_bloka = re.compile(r'(?=<div[^>]+id="question-summary-\d+")')

vzorec_nesprejeti = re.compile(
    r'<div[^>]+id="question-summary-(?P<id>\d+)"[^>]*>.*?'
    r'<span[^>]+stats-item-number">(?P<votes>-?\d+)</span>.*?'
    r'<div[^>]+title="(?P<answers>\d+)\s+answers?".*?'
    r'<div[^>]+title="(?P<views>[\d,]+k?)\s+views".*?'
    r'<a[^>]+class="[^"]*\bs-link\b[^"]*"[^>]*>(?P<title>.*?)</a>.*?',
    flags=re.DOTALL
)
vzorec_sprejeti = re.compile(
    r'<div[^>]+id="question-summary-(?P<id>\d+)"[^>]*>.*?'
    r'<span[^>]+stats-item-number">(?P<votes>-?\d+)</span>.*?'
    r'<div[^>]+has-accepted-answer"[^>]*>.*?'
    r'<span[^>]+stats-item-number">(?P<answers>\d+)</span>.*?'
    r'<div[^>]+title="(?P<views>[\d,]+k?)\s+views".*?'
    r'<a[^>]+class="[^"]*\bs-link\b[^"]*"[^>]*>(?P<title>.*?)</a>.*?',
    flags=re.DOTALL
)

vzorec_oznaka = re.compile(r'<a[^>]+class="[^"]*\bpost-tag\b[^"]*"[^>]*>([^<]+)</a>')

vzorec_avtor = re.compile(
    r'<a href="/users/(?P<user_id>\d+)/[^"]+"[^>]*class="flex--item">'
    r'(?P<author>[^<]+)</a>'
)

vzorec_cas = re.compile(r"<span[^>]+class='relativetime'[^>]*>(?P<time>[^<]+)</span>")

vzorec_sprejetodg = re.compile(r'\bhas-accepted-answer\b')

vzorec_ugled = re.compile(
    r'<li[^>]+class="s-user-card--rep"[^>]*>.*?'
    r'<span[^>]*>(?P<rep>[\d,]+)</span>',
    flags=re.DOTALL
)

def izloci_podatke_vprasanja(blok):
    m = vzorec_sprejeti.search(blok) or vzorec_nesprejeti.search(blok) #drugacna html koda za sprejete odgovore vs brez sprejetih odgovorov
    vprasanje = m.groupdict()
    vprasanje['id'] = int(vprasanje['id'])
    vprasanje['votes']   = int(vprasanje['votes'])
    vprasanje['answers'] = int(vprasanje['answers'])
    v = vprasanje['views'].lower().replace(',','')
    vprasanje['views'] = int(float(v[:-1])*1000) if v.endswith('k') else int(v)
    vprasanje['tags'] = vzorec_oznaka.findall(blok)
    author = vzorec_avtor.search(blok)
    vprasanje["author"] = author.group("author") if author else None
    reputation = vzorec_ugled.search(blok)
    vprasanje['reputation'] = int(reputation.group("rep").replace(",", "")) if reputation else None
    vprasanje['has_accepted_answer'] = bool(vzorec_sprejetodg.search(blok))
    time = vzorec_cas.search(blok)
    vprasanje["time"] = time.group("time") if time else None
    return vprasanje