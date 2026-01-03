import re
from playwright.sync_api import Page, expect

# Check Some Links        
def test_get_race_chatter_link(page: Page):
    page.goto("https://www.mtbdash.com/races")

    expect(page.get_by_role("link", name="Link").first).to_be_visible()

def test_get_hardtail_chatter_link(page: Page):
    page.goto("https://www.mtbdash.com/hardtails")

    expect(page.get_by_role("link", name="Link").first).to_be_visible()  

def test_get_ebike_chatter_link(page: Page):
    page.goto("https://www.mtbdash.com/ebikes")

    expect(page.get_by_role("link", name="Link").first).to_be_visible()      

def test_get_repair_chatter_link(page: Page):
    page.goto("https://www.mtbdash.com/bikerepair")

    expect(page.get_by_role("link", name="Link").first).to_be_visible()          

def test_get_colorado_trail_chatter_link(page: Page):
    page.goto("https://www.mtbdash.com/colorado")

    expect(page.get_by_role("link", name="Watch or Listen to more Episodes on Spotify")).to_be_visible()     

        