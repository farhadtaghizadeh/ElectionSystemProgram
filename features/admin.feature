Feature: Admin panel features
  # Enter feature description here

  Scenario: Create elections
    Given I have logged in as an admin
    And I have navigated to the "manage_elections" admin page
    When I click on the Create "Election" button
    And I fill out the form fields with election titled: "US 2024 Election" and start date of "11-07-2024" and start time of "1000" and end date of "11-07-2024" and end time of "2000"
    And I submit the form
    When I navigate back to the "manage_elections" admin page
    Then I should see my election titled: "US 2024 Election" with start date and time of "2024-11-07 10:00:00" and end date and time of "2024-11-07 20:00:00"

  Scenario: Create races
    Given I have logged in as an admin
    And I have navigated to the "manage_races" admin page
    When I click on the Create "Race" button
    And I fill out the race form with name: "2024 IA State Local 3"
    And I submit the form
    When I navigate back to the "manage_races" admin page
    Then I should see the content: "2024 IA State Local 3"
    
  Scenario: Manage Precincts
    Given I have logged in as an admin
    And I have navigated to the "manage_precincts" admin page
    When I click on the Create "Precinct" button
    And I fill out the precinct form fields with voting location: "Cedar Rapids Public Library" and election office address: "Cedar Rapids City Hall"
    And I submit the form
    When I navigate back to the "manage_precincts" admin page
    Then I should see the content: "Cedar Rapids Public Library"
    And I should see the content: "Cedar Rapids City Hall"

  Scenario: Assign Manager to Unassigned Precinct
    Given I have logged in as an admin
    And I have navigated to the "manage_precincts" admin page
    And I see a precinct labeled "Cedar Rapids Public Library" with a polling manager named: "Unassigned"
    And I click to update the polling manager for "Cedar Rapids Public Library"
    When I click to assign the polling manager with username "bpoll"
    Then I should see the polling manager "bpoll" assigned to precinct "Cedar Rapids Public Library"

  Scenario: Change Polling Manager for already assigned Precinct
    Given I have logged in as an admin
    And I have navigated to the "manage_precincts" admin page
    And I see a precinct labeled "University Library" with a polling manager named: "bpoll"
    And I click to update the polling manager for "University Library"
    When I click to assign the polling manager with username "bigman"
    Then I should see the polling manager "bigman" assigned to precinct "University Library"

  Scenario: Approve Voters
    Given I have logged in as an admin
    And I have navigated to the "voter_requests" admin page
    And I see a voter needing approval
    When I click to approve the voter
    Then I should see the voter has been approved

  Scenario: Create Zips
    Given I have logged in as an admin
    And I have navigated to the "manage_zips" admin page
    When I click on the Create "Zip" button
    And I fill the form with zip code for location: "52233" with start of "4000" and end of "9000"
    And I submit the form
    When I navigate back to the "manage_zips" admin page
    Then I should see a zip code for location: "52233" with start of "4000" and end of "9000"

  Scenario: Create Poll Managers
    Given I have logged in as an admin
    And I have navigated to the "manage_poll_managers" admin page
    When I click on the Create "Poll Manager" button
    And I fill the poll manager form with username: "jojo", email: "jojo@voterapp.org", and password: "Election01!"
    And I submit the form
    When I navigate back to the "manage_poll_managers" admin page
    Then I should see a poll manager with username: "jojo" in the poll manager list

  Scenario: Search Voters
    Given I have logged in as an admin
    And I have navigated to the "search_voters" admin page
    When I click to search for voters
    And I search for voter with first name "John"
    And I submit the search
    Then I should see the content: "John"

  Scenario: Create Candidate
    Given I have logged in as an admin
    And I have navigated to the "manage_candidates" admin page
    When I click on the Create "Candidate" button
    When I fill out the information for a candidate with first name: "John", last name: "Arbuckle", party: "Garfield", and description: "He's a newspaper comic artist"
    And I submit the form
    When I navigate back to the "manage_candidates" admin page
    Then I should see a candidate in the list with first name: "John", last name: "Arbuckle", party: "Garfield"