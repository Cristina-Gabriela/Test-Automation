Feature:
  As an Automation Tester
  I will test this page
  So that I will show you how

  Scenario Outline:Modal Title
    Given the site formy
    When the person click on the Modal
    And open a new page
    Then click on the <button>, <OK>, <Close>
    Examples:
      | button | OK | Close |


