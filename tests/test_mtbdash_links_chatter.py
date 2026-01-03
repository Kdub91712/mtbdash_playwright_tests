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

def test_get_general_chatter_link(page: Page):
    page.goto("https://www.mtbdash.com/general_chatter")

    expect(page.get_by_role("link", name="Link").first).to_be_visible()    

def test_get_gear_chatter_link(page: Page):
    page.goto("https://www.mtbdash.com/chatter?state=gear")

    expect(page.get_by_role("link", name="Link").first).to_be_visible()              

# def test_get_europe_conditions_link(page: Page):
#     # todo
#     page.goto("https://www.mtbdash.com")    
#     page.get_by_role("link", name="Europe").nth(0).click()
#     page.get_by_role("link", name="Trail Chatter").click()    
#     page.screenshot(path="full_page_screenshot.png", full_page=True) 
#     expect(page.locator('.more_chatter_div').first).to_have_text('condition updates')             

# def test_get_canada_chatter_link(page: Page):
#     # todo
#     page.goto("https://www.mtbdash.com/chatter?state=canada") 
#     page.get_by_role("link", name="Canada").nth(1).click()
#     page.goto("https://www.mtbdash.com/canada")
#     page.get_by_role("link", name="Canada").nth(0).click()     

#     page.screenshot(path="full_page_screenshot.png", full_page=True) 

#     expect(page.get_by_role("link", name="Link").first).to_be_visible()        

def test_get_colorado_trail_chatter_link(page: Page):
    page.goto("https://www.mtbdash.com/colorado")

    expect(page.get_by_role("link", name="Watch or Listen to more Episodes on Spotify")).to_be_visible()          

# def test_get_nearby_hiking_chatter_link(page: Page):
#     page.goto("https://www.mtbdash.com/chatter?state=maine")    
#     page.goto("https://www.mtbdash.com/things_to_do?city=South%20Berwick&state=maine")
#     page.screenshot(path="full_page_screenshot.png", full_page=True)
#     expect(page.get_by_role("link", name="Women's hiking groups in southern Maine?")).to_be_visible()         

        