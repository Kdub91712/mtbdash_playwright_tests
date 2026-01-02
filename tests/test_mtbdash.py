import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.mtbdash.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("MTB DASH - Mountain Bike Trail Conditions and Videos"))

def test_get_southwest_link(page: Page):
    page.goto("https://www.mtbdash.com/")

    # Click the get started link.
    page.get_by_role("link", name="South West").click()

    expect(page.get_by_role("heading", name="Greatest Hits for Colorado")).to_be_visible()

def test_get_colorado_chatter_link(page: Page):
    page.goto("https://www.mtbdash.com/chatter?state=colorado")

    expect(page.get_by_role("button", name="Sort ASC/DESC")).to_be_visible()    

def test_get_colorado_bike_reviews_link(page: Page):
    page.goto("https://www.mtbdash.com/colorado")

    expect(page.get_by_role("link", name="More Bike Reviews")).to_be_visible()  

def test_get_colorado_trail_chatter_link(page: Page):
    page.goto("https://www.mtbdash.com/colorado")

    expect(page.get_by_role("link", name="Watch or Listen to more Episodes on Spotify")).to_be_visible()    

def test_get_colorado_trail_associations_link(page: Page):
    page.goto("https://www.mtbdash.com/groups?state=colorado")

    expect(page.get_by_role("link", name="Donate to Colorado Trail Associations")).to_be_visible()      
        