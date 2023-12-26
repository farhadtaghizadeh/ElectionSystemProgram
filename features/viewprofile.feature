# Created by ssankey at 12/8/23
Feature: Login
  # Enter feature description here

  Scenario: Successful login as admin
    Given I navigate to the login page
    And I enter the admin username and password
    When I click Sign In
    Then I should see the admin panel

  Scenario: Successful login as voter
    Given I navigate to the login page
    And I enter the voter username and password
    When I click Sign In
    Then I should see the voter panel

  Scenario: Successful login as manager
    Given I navigate to the login page
    And I enter the manager username and password
    When I click Sign In
    Then I should see the manager panel