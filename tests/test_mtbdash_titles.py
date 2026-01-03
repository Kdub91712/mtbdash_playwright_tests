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
        