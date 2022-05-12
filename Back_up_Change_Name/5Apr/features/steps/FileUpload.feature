Feature:
  As an Automation Tester
  I will test this page
  So that I will show you how

  Scenario Outline:File Upload Title
    Given the site formy
    When the person click on the File Upload
    And open a new page
    Then click on <button1>, <fill the box>, click on <button2>
    Examples:
      | button1 | fill the box | button2 |
      | Choose  |              | Reset   |