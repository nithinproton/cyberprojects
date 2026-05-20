import argparse

from crawler import get_inputs
from xss import test_xss
from sqli import test_sqli


# ==============================
# ASCII BANNER (IVS - OWASP)
# ==============================

def banner():
    print(r"""
██╗██╗   ██╗███████╗    ██████╗ ██╗    ██╗ █████╗ ███████╗██████╗
██║██║   ██║██╔════╝   ██╔═══██╗██║    ██║██╔══██╗██╔════╝██╔══██╗
██║██║   ██║███████╗   ██║   ██║██║ █╗ ██║███████║███████╗██████╔╝
██║╚██╗ ██╔╝╚════██║   ██║   ██║██║███╗██║██╔══██║╚════██║██╔═══╝
██║ ╚████╔╝ ███████║   ╚██████╔╝╚███╔███╔╝██║  ██║███████║██║
╚═╝  ╚═══╝  ╚══════╝    ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝

Intelligent Vulnerability Scanner (IVS)
KOLIKO CAPSTONE - OWASP Inspired Security Tool
---------------------------------------------------------------
""")


# ==============================
# MAIN SCAN FUNCTION
# ==============================

def scan(target):

    print("=" * 65)
    print(f"[ TARGET ] {target}")
    print("=" * 65)

    # Phase 0: Input Discovery
    print("\n[ PHASE 0 ] Input Discovery (Crawler)\n")

    targets = get_inputs(target)

    if not targets:
        print("[-] No input fields found. Exiting.")
        return

    print("[+] Input Points Discovered:\n")

    for idx, t in enumerate(targets, 1):

        print(f"{idx}. URL : {t['url']}")
        print(f"   Method : {t['method'].upper()}")
        print(f"   Inputs : {t['inputs']}\n")

    # Initialize results
    xss_found = False
    sqli_found = False

    # ==============================
    # PHASE 1: XSS TESTING
    # ==============================

    print("=" * 65)
    print("[ PHASE 1 ] XSS Testing (OWASP A7)")
    print("=" * 65)

    for t in targets:

        result = test_xss(t)

        if result:
            xss_found = True

    # ==============================
    # PHASE 2: SQLi TESTING
    # ==============================

    print("\n" + "=" * 65)
    print("[ PHASE 2 ] SQL Injection Testing (OWASP A1)")
    print("=" * 65)

    for t in targets:

        result = test_sqli(t)

        if result:
            sqli_found = True

    # ==============================
    # FINAL REPORT
    # ==============================

    print("\n" + "=" * 65)
    print("[ FINAL REPORT ]")
    print("=" * 65)

    print(f"XSS Vulnerability Found : {'YES' if xss_found else 'NO'}")
    print(f"SQL Injection Found     : {'YES' if sqli_found else 'NO'}")

    if xss_found or sqli_found:
        print("\n[ STATUS ] Vulnerabilities Detected!")

    else:
        print("\n[ STATUS ] Target appears secure (basic tests)")

    print("=" * 65)


# ==============================
# ENTRY POINT (CLI)
# ==============================

if __name__ == "__main__":

    banner()

    parser = argparse.ArgumentParser(
        description="IVS - Intelligent Vulnerability Scanner (OWASP Based)"
    )

    parser.add_argument(
        "target",
        help="Target URL (e.g., http://127.0.0.1:5000)"
    )

    args = parser.parse_args()

    scan(args.target)
