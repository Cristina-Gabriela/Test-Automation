Feature:
  As an Automation Tester
  I will test this page
  So that I will show you how

  Scenario Outline:Key And Mouse Press Title
    Given the site formy
    When the person click on the Key And Mouse Press
    And open a new page
    Then <fill>, <Button>
    Examples:
      | fill | Button |
      | abcd | Button |
      | oood | Button |
      | erty | Button |
      | ytre | Button |
      | hgfd | Button |
      | oipr | Button |