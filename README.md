from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com", wait_until="networkidle")
    with open("page.html", "w", encoding="utf-8") as f:
        f.write(page.content())
    browser.close()
