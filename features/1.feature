Feature: Verify that page elements are displayed correctly.
  Scenario Outline: display
    When on the login page
    Then display the <element>
    Examples:
      | element           |
      | SNK favicon       |
      | BRAND layout      |
      | LOGIN layout      |
      | CONTACT layout    |
      | END layout        |
      | SNK logo          |
      | MEMBER label      |
      | MESSAGE label     |
      | USERNAME label    |
      | USERNAME inputbox |
      | PASSWORD label    |
      | PASSWORD inputbox |
      | LOGIN button      |
      | EMAIL icon        |
      | EMAIL textlink    |
      | CALL icon         |
      | CALL textlink     |

  Scenario Outline: correctly
    When on the login page
    Then the <element> is displayed correctly
    Examples:
      | element           |
      | Website title     |
      | SNK favicon       |
      | SNK logo          |
      | MEMBER label      |
      | MESSAGE label     |
      | USERNAME label    |
      | USERNAME inputbox |
      | PASSWORD label    |
      | PASSWORD inputbox |
      | LOGIN button      |
      | EMAIL icon        |
      | EMAIL textlink    |
      | CALL icon         |
      | CALL textlink     |