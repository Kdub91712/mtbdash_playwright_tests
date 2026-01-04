import re
from playwright.sync_api import Page, expect

# Check Some Buttons
def test_get_colorado_chatter_sort_button(page: Page):
    page.goto("https://www.mtbdash.com/chatter?state=colorado")

    expect(page.get_by_role("button", name="Sort ASC/DESC")).to_be_visible()   


# Try a search
def test_search(page: Page):
    page.goto("https://www.mtbdash.com")
    page.get_by_placeholder("Search a brand, bike part, trail, city, state etc.").fill('Shimano')   
    # page.screenshot(path="full_page_screenshot.png", full_page=True)      
    page.get_by_role("button", name="Search").click()
    expect(page.get_by_role("link", name="Try Another Search")).to_be_visible()   
    expect(page).to_have_title(re.compile("MTB DASH - Shimano mountain biking"))   

# broken
def test_get_city_trail_videos_washington(page: Page):

    page.goto("https://www.mtbdash.com/washington")  
    page.locator('.city_select').select_option('Vancouver')

    # Click things to do
    expect(page.get_by_role("link", name="Trail Videos")).to_be_visible()  
    page.get_by_role("link", name="Trail Videos").click()

    page.screenshot(path="full_page_screenshot.png", full_page=True)    

    # Validate Video Link
    expect(page.get_by_role("link", name="Best MTB Trail in Washington? - YouTube")).to_be_visible()         

        