import re
from playwright.sync_api import Page, expect

# Check Some Links
def test_get_things_to_do_link_florida(page: Page):
    page.goto("https://www.mtbdash.com/florida")

    page.locator('.city_select').select_option('Miami')

    # Click things to do
    expect(page.get_by_role("link", name="Things to do")).to_be_visible()  
    page.get_by_role("link", name="Things to do").click()

    # Validate Bike Shop and Hotel
    expect(page.get_by_role("link", name="Top 10 Hotels in Miami, FL | Hotels.com")).to_be_visible()    
    expect(page.get_by_role("link", name="Elite Cycling & Fitness | Miami, FL Bike Shop")).to_be_visible()  

def test_get_things_to_do_link_canada(page: Page):
    page.goto("https://www.mtbdash.com/canada")

    page.locator('.city_select').select_option('Toronto')

    # Click things to do
    expect(page.get_by_role("link", name="Things to do")).to_be_visible()  
    page.get_by_role("link", name="Things to do").click()

    # Validate Restaurant and Bike Shop
    expect(page.get_by_role("link", name="Steakhouse & Sushi | Aera Restaurant Toronto")).to_be_visible()    
    expect(page.get_by_role("link", name="KindHuman Bicycles. Toronto Bike Shop and Bike Repairs.")).to_be_visible()              

def test_get_things_to_do_hiking_link(page: Page):
    page.goto("https://www.mtbdash.com/things_to_do?city=Toronto&state=canada")

    expect(page.get_by_role("link", name="Hiking")).to_be_visible()                   