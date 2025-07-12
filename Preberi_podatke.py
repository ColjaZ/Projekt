import re

with open("(highest-score)-stran-1.html", encoding="utf-8") as f:
    vsebina = f.read()

vzorec_bloka = re.compile(r'(?=<div[^>]+id="question-summary-\d+")')
bloki = vzorec_bloka.split(vsebina) #splita vse do prvega takega vzorca (bloke se ustvari kasneje i think ko poklicem to funkcijo al neki)
bloki = bloki[1:] #znebimo se prvega bloka ki ne predstavlja nobenega vprašanja

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

vzorec_tag = re.compile(r'<a[^>]+class="[^"]*\bpost-tag\b[^"]*"[^>]*>([^<]+)</a>')

vzorec_author = re.compile(
    r'<a href="/users/(?P<user_id>\d+)/[^"]+"[^>]*class="flex--item">'
    r'(?P<author>[^<]+)</a>'
)

vzorec_time = re.compile(r"<span[^>]+class='relativetime'[^>]*>(?P<time>[^<]+)</span>")

vzorec_sprejetodg = re.compile(r'\bhas-accepted-answer\b')

vzorec_reputation = re.compile(
    r'<li[^>]+class="s-user-card--rep"[^>]*>.*?'
    r'<span[^>]*>(?P<rep>[\d,]+)</span>',
    flags=re.DOTALL
)

def izloci_podatke_vprasanja(blok):
    m = vzorec_sprejeti.search(blok) or vzorec_nesprejeti.search(blok) #drugacna html koda za sprejete odgovore vs brez sprejetih odgovorov
    info = m.groupdict()
    info['id'] = int(info['id'])
    info['votes']   = int(info['votes'])
    info['answers'] = int(info['answers'])
    v = info['views'].lower().replace(',','')
    info['views'] = int(float(v[:-1])*1000) if v.endswith('k') else int(v)
    info['tags'] = vzorec_tag.findall(blok)
    author = vzorec_author.search(blok)
    if author: #preverim da ne bo samo prazen
        info["author"] = author.group("author")
    reputation = vzorec_reputation.search(blok)
    if reputation:
        info['reputation'] = int(reputation.group("rep").replace(",", ""))
    info['has_accepted_answer'] = bool(vzorec_sprejetodg.search(blok))
    time = vzorec_time.search(blok)
    if time:
        info["time"] = time.group("time")
    return info