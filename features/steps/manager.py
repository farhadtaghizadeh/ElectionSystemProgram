from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
from dotenv import load_dotenv
load_dotenv()
base_url = os.getenv("BASE_URL")

@given('I have logged in as a manager')
def step_impl(context):
    context.browser.get(base_url+'login/')
    context.browser.find_element('name', 'username').send_keys('bpoll')
    context.browser.find_element('name', 'password').send_keys('Bobby123!')
    context.browser.find_element('xpath', f"//input[@type='submit' and @value='Sign In']").click()

@given('I have navigated to the "{page_name}" manager page')
def step_impl(context, page_name):
    context.browser.get(base_url+'manager_panel/'+page_name+'/?user=3')


@when("As a manager, I click to approve the voter")
def step_impl(context):
    context.browser.find_element('xpath', f"//a[@href='/process-approval/?voter_id=2&action=approve&user=3']").click()
