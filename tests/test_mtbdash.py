import re
from playwright.sync_api import Page, expect

# Check Some Title Tags
def test_has_title(page: Page):
    page.goto("https://www.mtbdash.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("MTB DASH - Mountain Bike Trail Conditions and Videos"))

def test_fat_bike_page_has_title(page: Page):
    page.goto("https://www.mtbdash.com/fatbikes")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("MTB DASH - Fat Biking Videos"))

def test_scenic_trails_page_has_title(page: Page):
    page.goto("https://www.mtbdash.com/scenictrails")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("MTB DASH - Scenic Mountain Bike Trails"))

def test_city_page_has_title(page: Page):
    page.goto("https://www.mtbdash.com/things_to_do?city=Boulder&state=colorado")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("MTB DASH - Things to do in Boulder Colorado"))    



# Check Some Links
def test_get_southwest_link(page: Page):
    page.goto("https://www.mtbdash.com/")

    page.get_by_role("link", name="South West").click()

    expect(page.get_by_role("heading", name="Greatest Hits for Colorado")).to_be_visible()

def test_get_colorado_bike_reviews_link(page: Page):
    page.goto("https://www.mtbdash.com/colorado")

    expect(page.get_by_role("link", name="More Bike Reviews")).to_be_visible()  

def test_get_colorado_trail_chatter_link(page: Page):
    page.goto("https://www.mtbdash.com/colorado")

    expect(page.get_by_role("link", name="Watch or Listen to more Episodes on Spotify")).to_be_visible()    

def test_get_colorado_trail_associations_link(page: Page):
    page.goto("https://www.mtbdash.com/groups?state=colorado")

    expect(page.get_by_role("link", name="Donate to Colorado Trail Associations")).to_be_visible()      

def test_get_bike_park_video_link(page: Page):
    page.goto("https://www.mtbdash.com/bikeparks")

    expect(page.get_by_role("link", name="More Bike Park Videos")).to_be_visible()

def test_get_register_bike_link(page: Page):
    page.goto("https://www.mtbdash.com/washington")

    expect(page.get_by_role("link", name="Register your bike!")).to_be_visible()                      


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

        