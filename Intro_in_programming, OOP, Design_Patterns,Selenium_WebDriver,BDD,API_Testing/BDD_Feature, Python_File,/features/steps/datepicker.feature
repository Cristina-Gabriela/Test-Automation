Feature:
  As an Automation Tester
  I will test this page
  So that I will show you how

  Scenario Outline:Date picker Title
    Given the site formy
    When the person click on the Date picker
    And open a new page
    Then fill the <date>
    Examples:
      | date      |
      | 5.02.2000 |
      | 7.08.2010 |
      | 5.10.2020 |
      | 4.02.2022 |
      | 1.01.1999 |