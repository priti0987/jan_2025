from playwright.sync_api import sync_playwright

import time

def test_Home():
    with sync_playwright() as p :
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.amazon.com")
        page.locator("//input[@id='twotabsearchtextbox']").fill("mobile")
        page.locator("//*[@id='nav-search-submit-button']").click()
        time.sleep(2)
        results = page.locator("div span div[data-component-type='s-search-result']")
        c = results.count()
        assert c > 0
        time.sleep(5)
        for i in range(c):
            title = results.nth(i).locator("h2 span").inner_text()
            #assert "mobile" in title
            #print(title)
        results.nth(0).click()
        time.sleep(2)
        page.click("input#add-to-cart-button")