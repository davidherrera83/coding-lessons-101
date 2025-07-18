import pytest

# Testing Google Search Functionality by searching for "puppies" in the browser using Pylenium
def test_google_search(py):
    # Visit the HerokupApp The Internet homepage
    py.visit('https://the-internet.herokuapp.com/')
    # Wait for the page to load
    py.wait(2)
    # Verify the title of the page
    assert py.get('a[href="/abtest"]').should().have_text('A/B Testing')