Feature:
  As an Automation Tester
  I will test this page
  So that I will show you how

  Scenario Outline:Checkbox Title
    Given the site formy
    When the person click on the Checkbox
    And open a new page
    Then click on each button <Checkbox1>, <Checkbox2>, <Checkbox3>
    Examples:
      | Checkbox1 | Checkbox2 | Checkbox3 |