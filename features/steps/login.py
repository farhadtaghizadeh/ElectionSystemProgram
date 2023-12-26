from behave import given, when, then
import os
from dotenv import load_dotenv
load_dotenv()
base_url = os.getenv("BASE_URL")

@given("I navigate to the login page")
def step_impl(context):
    """
        Navigate to login page and as the web server will run in local when we run
        end to end tests using behave, the url will be https://voterapp.org/login
    """
    context.browser.get(base_url+'login')


@given(u'I enter the admin username and password')
def step_impl(context):
    """
        Find the html element using the name attribute and input the required data
        Here entering validusername and validpassword as the step definition says:
        I enter valid username and password
    """
    context.browser.find_element('name','username').send_keys('admin')
    context.browser.find_element('name','password').send_keys('admin')


@given(u'I enter the voter username and password')
def step_impl(context):
    context.browser.find_element('name','username').send_keys('jsmith')
    context.browser.find_element('name','password').send_keys('admin')

@given(u'I enter the manager username and password')
def step_impl(context):
    context.browser.find_element('name','username').send_keys('bpoll')
    context.browser.find_element('name','password').send_keys('Bobby123!')

@when("I click Sign In")
def step_impl(context):
    """
        Find the input button on the html page which has value = Submit
        and invoke .click()
    """
    context.browser.find_element('xpath', f"//input[@type='submit' and @value='Sign In']").click()


@then("I should see the admin panel")
def step_impl(context):
    """
        If the login is successful we will be redirected to https://voterapp.org/admin_path/
        and also see the message "Login successful !!" on that page
    """
    assert context.browser.current_url == base_url+'admin_panel/?user=1'
    assert 'Welcome Admin' in context.browser.page_source


@then("I should see the voter panel")
def step_impl(context):
    assert context.browser.current_url == base_url+'user_panel/?user=2'
    assert 'John' in context.browser.page_source

@then("I should see the manager panel")
def step_impl(context):
    assert context.browser.current_url == base_url+'manager_panel/?user=3'
    assert 'Manager' in context.browser.page_source

@given(u'I enter invalid username or password')
def step_impl(context):
    """
        Find the html element using the name attribute and input the required data
        Here entering invalidusername and invalidpassword as the step definition says:
        I enter invalid username or password
    """
    context.browser.find_element('name','username').send_keys('admin  ')
    context.browser.find_element('name','password').send_keys('badwin')


@then(u'login fails')
def step_impl(context):
    """
        If the login is successful we will not be redirected to https://voterapp.org/index
        but will be on the same page: https://voterapp.org/login
        and also see the message "Invalid username or password !!" on that page
    """
    assert context.browser.current_url == base_url+'login'
    assert 'You have entered an incorrect username or password, please try again. ' in context.browser.page_source

