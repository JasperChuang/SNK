Feature: Verify that all the fields such as Username, Password has a valid placeholder.
  Scenario Outline: Within the maximum word limit
  	Given on the login page
    When typing '12345678901234567890' into <element> textbox
    Then can type '12345678901234567890' into <element> textbox
    Examples:
      | element  |
      | USERNAME |
      | PASSWORD |

  Scenario Outline: exceed the word limit
    Given on the login page
    When typing '123456789012345678901' into <element> textbox
    Then can only type '12345678901234567890' into <element> textbox
    Examples:
      | element  |
      | USERNAME |
      | PASSWORD |