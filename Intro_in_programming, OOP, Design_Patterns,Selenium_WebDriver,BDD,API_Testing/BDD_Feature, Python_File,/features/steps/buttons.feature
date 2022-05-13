Feature:
  As an Automation Tester
  I will test this page
  So that I will show you how

  Scenario Outline:Buttons Title
    Given the site <formy>
    When the person click on the Buttons
    And click on each button
    Then go back

    Examples:
      | formy                               | Primary | Success | Info | Warning | Danger | Link | Left | Middle | Right | 1 | 2 | Dropdown |
      | http://formy-project.herokuapp.com/ |         |         |      |         |        |      |      |        |       |   |   |          |


#    Examples:
#      | Primary | Success | Info | Warning | Danger | Link | Left | Middle | Right | 1 | 2 | Dropdown        |
#      |         |         |      |         |        |      |      |        |       |   |   | Dropdown link 1 |
#      |         |         |      |         |        |      |      |        |       |   |   | Dropdown link 2 |



