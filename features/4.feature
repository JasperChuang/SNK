Feature: Verify that tab functionality is working properly or not.
  Scenario Outline:
    Given on the login page
    And cursor is focused on <element>
    When press the 'Tab' key on the keyboard
    Then move the focused elements to <next>
    Examples:
      | element          | next             |
      | USERNAME textbox | PASSWORD textbox |
      | PASSWORD textbox | LOGIN button     |