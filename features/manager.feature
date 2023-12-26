Feature: Manager Functions

  Scenario: Search Voters
    Given I have logged in as a manager
    And I have navigated to the "search_voters" manager page
    When I click to search for voters
    And I search for voter with first name "John"
    And I submit the search
    Then I should see the content: "John"

  Scenario: Approve Voters
    Given I have logged in as a manager
    And I have navigated to the "voter_requests" manager page
    And I see a voter needing approval
    When As a manager, I click to approve the voter
    Then I should see the voter has been approved
