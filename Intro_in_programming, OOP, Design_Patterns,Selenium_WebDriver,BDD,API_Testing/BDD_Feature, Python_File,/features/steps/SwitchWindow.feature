Feature:
  As an Automation Tester
  I will test this page
  So that I will show you how

  Scenario Outline:Switch Window Title
    Given the site formy
    When the person click on the Switch Window
    And open a new page
    Then <button1>, <button2>
    Examples:
      | button1      | button2    |
      | Open new tab | Open alert |
      | Open new tab | ok         |