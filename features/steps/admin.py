from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
from dotenv import load_dotenv
load_dotenv()
base_url = os.getenv("BASE_URL")

@given('I have logged in as an admin')
def step_impl(context):
    context.browser.get(base_url+'login/')
    context.browser.find_element('name', 'username').send_keys('admin')
    context.browser.find_element('name', 'password').send_keys('admin')
    context.browser.find_element('xpath', f"//input[@type='submit' and @value='Sign In']").click()

@given('I have navigated to the "{page_name}" admin page')
def step_impl(context, page_name):
    context.browser.get(base_url+'admin_panel/'+page_name+'/?user=1')

@given('I see a precinct labeled "{voting_location}" with a polling manager named: "{polling_manager_name}"')
def step_impl(context, voting_location, polling_manager_name):
    voting_lower = voting_location.replace(" ", "_").lower()
    text = f"//td[@id=\'polling_manager_for_" + voting_lower + "\']"
    assert voting_location in context.browser.page_source
    element = context.browser.find_element('xpath', text)
    assert element.text == polling_manager_name



@when('I navigate back to the "{page_name}" admin page')
def step_impl(context, page_name):
    context.browser.get(base_url+'admin_panel/'+page_name+'/?user=1')

@when('I fill out the race form with name: "{name}"')
def step_impl(context, name):
    context.browser.find_element('name', 'name').send_keys(name)
@when('I click on the Create "{element_type}" button')
def step_impl(context,element_type):
    """
        Find the input button on the html page which has value = Submit
        and invoke .click()
    """
    text = f"//button[contains(text(), \'Create " + element_type + "\')]"

    context.browser.find_element('xpath', text).click()


@when('I fill out the precinct form fields with voting location: "{voting_location}" and election office address: "{election_office_address}"')
def step_impl(context, voting_location, election_office_address):
    context.browser.find_element('id', 'voting_location').send_keys(voting_location)
    context.browser.find_element('id', 'election_office').send_keys(election_office_address)


@when('I fill out the form fields with election titled: "{title}" and start date of "{start_date}" and start time of "{start_time}" and end date of "{end_date}" and end time of "{end_time}"')
def step_impl(context, title, start_date, start_time, end_date, end_time):
    context.browser.find_element('xpath', f"//input[@id='title']").send_keys(title)
    element = WebDriverWait(context.browser, 10).until(lambda x: x.find_element('xpath', f"//input[@id='start_date']"))
    element.send_keys(start_date)
    context.browser.find_element('xpath', f"//input[@id='start_time']").send_keys(start_time)
    element2 = WebDriverWait(context.browser, 10).until(lambda x: x.find_element('xpath', f"//input[@id='end_date']"))
    element2.send_keys(end_date)
    context.browser.find_element('xpath', f"//input[@id='end_time']").send_keys(end_time)

@given("I see a voter needing approval")
def step_impl(context):
    assert "Jimmy Jason Jib" in context.browser.page_source


@when("I click to approve the voter")
def step_impl(context):
    context.browser.find_element('xpath', f"//a[@href='/process-approval/?voter_id=2&action=approve&user=1']").click()

@then("I should see the voter has been approved")
def step_impl(context):
    assert "VoterJimmy Jib has been approved." in context.browser.page_source

@when('I submit the form')
def step_impl(context):
    context.browser.find_element('xpath', f"//input[@type='submit' and @value='Submit']").click()


@when('I fill out the information for a candidate with first name: "{first_name}", last name: "{last_name}", party: "{party}", and description: "{description}"')
def step_impl(context, first_name, last_name, party, description):
    context.browser.find_element('id', 'first_name').send_keys(first_name)
    context.browser.find_element('id', 'last_name').send_keys(last_name)
    context.browser.find_element('id', 'party').send_keys(party)
    context.browser.find_element('id', 'description').send_keys(description)

@then('I should see a candidate in the list with first name: "{first_name}", last name: "{last_name}", party: "{party}"')
def step_impl(context, first_name, last_name, party):
    assert first_name in context.browser.page_source
    assert last_name in context.browser.page_source
    assert party in context.browser.page_source


@when('I submit the search')
def step_impl(context):
    context.browser.find_element('xpath', f"//input[@type='submit' and @value='Search']").click()

@then('I should see the content: "{text}"')
def step_impl(context, text):
    assert text in context.browser.page_source

@then('I should see my election titled: "{title}" with start date and time of "{start_date_and_time}" and end date and time of "{end_date_and_time}"')
def step_impl(context, title, start_date_and_time, end_date_and_time):
    assert title in context.browser.page_source
    assert start_date_and_time in context.browser.page_source
    assert end_date_and_time in context.browser.page_source


@given('I click to update the polling manager for "{voting_location}"')
def step_impl(context, voting_location):
    voting_lower = voting_location.replace(" ", "_").lower()
    text = f"//a[@id=\'assign_manager_button_for_" + voting_lower + "\']"
    context.browser.find_element('xpath', text).click()

@when('I click to search for voters')
def step_impl(context):
    text = f"//button[contains(text(), 'Search Users')]"
    context.browser.find_element("xpath", text).click()

@when('I search for voter with first name "{voter_name}"')
def step_impl(context, voter_name):
    context.browser.find_element("id", "first_name").send_keys(voter_name)


@given('I see a poll manager with username "{username}")')
def step_impl(context, username):
    assert username in context.browser.page_source

@when('I click to assign the polling manager with username "{username}"')
def step_impl(context, username):
    text = f'//a[@id="assign_'+username+'"]'
    context.browser.find_element('xpath', text).click()

@then('I should see the polling manager "{username}" assigned to precinct "{voting_location}"')
def step_impl(context, username, voting_location):
    voting_lower = voting_location.replace(" ", "_").lower()
    text = f'//td[@id="polling_manager_for_'+voting_lower+'"]'
    element = context.browser.find_element('xpath', text)
    assert username == element.text


@when('I fill the form with zip code for location: "{zip_code}" with start of "{zip_start}" and end of "{zip_end}"')
def step_impl(context, zip_code, zip_start, zip_end):
    context.browser.find_element('id', 'zip').send_keys(zip_code)
    context.browser.find_element('id', 'zip4start').send_keys(zip_start)
    context.browser.find_element('id', 'zip4end').send_keys(zip_end)


@when('I fill the poll manager form with username: "{username}", email: "{email_address}", and password: "{password}"')
def step_impl(context, username, email_address, password):
    context.browser.find_element('id', 'username').send_keys(username)
    context.browser.find_element('id', 'email_address').send_keys(email_address)
    context.browser.find_element('id', 'password').send_keys(password)
    context.browser.find_element('id', 'confirm').send_keys(password)

@then('I should see a poll manager with username: "{username}" in the poll manager list')
def step_impl(context, username):
    assert username in context.browser.page_source

@then('I should see a zip code for location: "{zip_code}" with start of "{zip_start}" and end of "{zip_end}"')
def step_impl(context, zip_code, zip_start, zip_end):
    element1 = context.browser.find_element('id', zip_code + '_with_range_' + zip_start + '_to_' + zip_end)
    element2 = context.browser.find_element('id', zip_code + '_start_range_for_' + zip_start + '_to_' + zip_end)
    element3 = context.browser.find_element('id', zip_code + '_end_range_for_' + zip_start + '_to_' + zip_end)
    assert zip_code == element1.text
    assert zip_start == element2.text
    assert zip_end == element3.text