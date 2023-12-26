Feature: Voter functions
  # Enter feature description here

  Scenario: Vote in an election
    Given I have logged in as a voter
    And I am on the main voter dashboard
    When I click on to view races for the election
    And I click on to view the candidates for the race
    And I click on the candidate I want to vote for
    Then I should see my vote has been submitted
