import requests
from utils import generate_test_cases


def test_xss(target):
    payloads = [
        "<script>alert(1)</script>",
        "<img src=x onerror=alert(1)>"
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

            if payload in response.text:
                print("\n[!!!] XSS Vulnerability Found")
                print("URL:", response.url)
                print("Payload:", payload)
                print("Parameter:", data)

                return True

    return False
