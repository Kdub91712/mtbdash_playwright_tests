import re
from playwright.sync_api import Page, expect

# Check Some Links
def test_get_video_search_link(page: Page):
    page.goto("https://www.mtbdash.com/colorado?search=Dawson")

    expect(page.get_by_role("link", name="Video")).to_be_visible() 

def test_get_podcast_watch_link(page: Page):
    page.goto("https://www.mtbdash.com/podcasts")

    expect(page.get_by_role("link", name="Watch").first).to_be_visible() 

def test_get_podcast_all_episodes_watch_link(page: Page):
    page.goto("https://www.mtbdash.com/all_episodes")

    expect(page.get_by_role("link", name="Watch").first).to_be_visible()                   

def test_get_state_video_link(page: Page):
    page.goto("https://www.mtbdash.com/illinois")

    expect(page.get_by_role("link", name="Video").first).to_be_visible() 

def test_get_brand_groups_link(page: Page):
    page.goto("https://www.mtbdash.com/bike_brands")

    expect(page.get_by_role("link", name="Groups").first).to_be_visible() 

def test_get_state_city_link(page: Page):
    page.goto("https://www.mtbdash.com/illinois")

    expect(page.get_by_role("link", name="Carpentersville")).to_be_visible() 

def test_get_state_trail_system_link(page: Page):
    page.goto("https://www.mtbdash.com/illinois")

    expect(page.get_by_role("link", name="Trail System View")).to_be_visible()   

def test_get_state_greatest_hits_link(page: Page):
    page.goto("https://www.mtbdash.com/utah")

    expect(page.get_by_role("link", name="Gravitron")).to_be_visible() 

def test_get_things_to_do_hiking_link(page: Page):
    page.goto("https://www.mtbdash.com/things_to_do?city=Toronto&state=canada")

    expect(page.get_by_role("link", name="Hiking")).to_be_visible()              

def test_get_brand_group_link(page: Page):
    page.goto("https://www.mtbdash.com/bike_brand_groups?brand=Specialized")

    expect(page.get_by_role("link", name="SPECIALIZED BICYCLE OWNERS GROUP")).to_be_visible() 

def test_get_southwest_link(page: Page):
    page.goto("https://www.mtbdash.com/")

    page.get_by_role("link", name="South West").click()

    expect(page.get_by_role("heading", name="Greatest Hits for Colorado")).to_be_visible()

def test_get_fat_bike_video_link(page: Page):
    page.goto("https://www.mtbdash.com/fatbikes")

    expect(page.get_by_role("link", name="Link").first).to_be_visible()   

def test_get_gear_video_link(page: Page):
    page.goto("https://www.mtbdash.com/gear?state=gear")

    expect(page.get_by_role("link", name="Link").first).to_be_visible()     

def test_get_colorado_bike_reviews_link(page: Page):
    page.goto("https://www.mtbdash.com/colorado")

    expect(page.get_by_role("link", name="More Bike Reviews")).to_be_visible()  

def test_get_bike_reviews_link(page: Page):
    page.goto("https://www.mtbdash.com/bikereviews")
    page.screenshot(path="full_page_screenshot.png", full_page=True)    
    expect(page.get_by_role("link", name="The Cannondale Habit HT 2 Review - YouTube")).to_be_visible()       

def test_get_colorado_trail_associations_link(page: Page):
    page.goto("https://www.mtbdash.com/groups?state=colorado")

    expect(page.get_by_role("link", name="Donate to Colorado Trail Associations")).to_be_visible()      

def test_get_bike_park_video_link(page: Page):
    page.goto("https://www.mtbdash.com/bikeparks")

    expect(page.get_by_role("link", name="More Bike Park Videos")).to_be_visible()

def test_get_register_bike_link(page: Page):
    page.goto("https://www.mtbdash.com/washington")

    expect(page.get_by_role("link", name="Register your bike!")).to_be_visible() 

        