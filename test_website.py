
import re
from playwright.sync_api import Page, expect

def test_website_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))

def test_website_url(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_url(re.compile("playwright.dev"))
