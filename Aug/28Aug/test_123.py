from playwright.sync_api import sync_playwright


def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
