Feature: Verify that Enter/Tab key works as a substitute for the Log in button.
  Scenario Outline:
    Given on the login page
    And cursor is focused on <element>
    When pressed the 'Enter' key on the keyboard
    Then performing login
    Examples:
      | element          |
      | USERNAME textbox |
      | PASSWORD textbox |
      | LOGIN button     |