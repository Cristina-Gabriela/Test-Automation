Feature:
  As an Automation Tester
  I will test this page
  So that I will show you how

  Scenario Outline:Radio Button Title
    Given the site formy
    When the person click on the Radio Button
    And open a new page
    Then click on <button1>, <button2>, <button3>
    Examples:
      | button1        | button2        | button3        |
      | Radio button 1 | Radio button 2 | Radio button 3 |