from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
from dotenv import load_dotenv
load_dotenv()
base_url = os.getenv("BASE_URL")
@given('I have logged in as a voter')
def step_impl(context):
    context.browser.get(base_url+'login/')
    context.browser.find_element('name', 'username').send_keys('jsmith')
    context.browser.find_element('name', 'password').send_keys('admin')
    context.browser.find_element('xpath', f"//input[@type='submit' and @value='Sign In']").click()

@given('I am on the main voter dashboard')
def step_impl(context):
    context.browser.get(base_url+'user_panel/?user=2')

@when('I click on to view races for the election')
def step_impl(context):
    context.browser.find_element('xpath', f"//a[@href='vote_races/?user=2&ballot=1&voter=1']").click()

@when('I click on to view the candidates for the race')
def step_impl(context):
    context.browser.find_element('xpath', f"//a[@href='view_candidates/?ballot=1&race=3&voter=1&user=2']").click()

@when('I click on the candidate I want to vote for')
def step_impl(context):
    context.browser.find_element('xpath', f"//a[@href='/vote_for_candidate/?action=vote&candidate_id=6&voter=1&race=3&user=2&ballot=1\"']").click()

@then('I should see my vote has been submitted')
def step_impl(context):
    assert "Your vote has been submitted." in context.browser.page_source
