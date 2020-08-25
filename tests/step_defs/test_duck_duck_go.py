# coding=utf-8
"""DuckDuckGo Web Browsing feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('../features/duck_duck_go.feature', 'Basic DuckDuckGo Search')
def test_basic_duckduckgo_search():
    """Basic DuckDuckGo Search."""


@given('the DuckDuckGo home page is displayed')
def the_duckduckgo_home_page_is_displayed():
    """the DuckDuckGo home page is displayed."""
    print("the DuckDuckGo home page is displayed: ")
    pass


@when('the user searches for "panda"')
def the_user_searches_for_panda():
    """the user searches for "panda"."""
    print("the DuckDuckGo home page is displayed")
    pass


@then('results are shown for "panda"')
def results_are_shown_for_panda():
    """results are shown for "panda"."""
    print("the DuckDuckGo home page is displayed")
    pass

