import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_inputs(url):
    targets = []

    try:
        response = requests.get(url, timeout=5)

    except:
        return targets

    soup = BeautifulSoup(response.text, "html.parser")

    for form in soup.find_all("form"):

        action = form.get("action")
        method = form.get("method", "get").lower()

        inputs = []

        for input_tag in form.find_all("input"):

            name = input_tag.get("name")

            if name:
                inputs.append(name)

        if action and inputs:

            targets.append({
                "url": urljoin(url, action),
                "method": method,
                "inputs": inputs
            })

    return targets
