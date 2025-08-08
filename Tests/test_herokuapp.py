import pytest
from Pages.Herokuapp import Herokuapp

# Testing Google Search Functionality by searching for "puppies" in the browser using Pylenium
def test_navigate_to_herokuapp(herokuapp, py):
    # Visit the HerokupApp The Internet homepage
    herokuapp.visit_herokuapp()
    # Verify the title of the page
    assert py.get('a[href="/abtest"]').should().have_text('A/B Testing')

def test_authentication(herokuapp, py):
    # Visit the HerokupApp The Internet homepage
    py.visit('https://the-internet.herokuapp.com/')
    # Click Form Authentication Example
    example = 'a[href="/login"]'
    herokuapp.click_on_example(example)
    # Verify we are in the correct "Login Page" before interacting with Form
    py.should().contain_url("/login")
    # Fill in the form and hit Enter
    py.get("#username").type("tomsmith")
    py.get("#password").type("SuperSecretPassword!")
    py.get("button").click()
    # Verify Authentication Worked
    assert py.get("#flash").should().be_visible()