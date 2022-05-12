Feature:BDD
  As a Founder and Tester of Applications
  I will Test Twitter Application and Verify their code on Github
  So that I follow some scenarios

  Scenario Outline: Title Test Twitter App
    Given  The website <website>
    When Click on this site
    And Press Enter
    Then Open a new file with the name of this app
    And Try to login
    And Enter your <e-mail>
    Then Press click

    Examples:
      | website             | e-mail           |
      | https://twitter.com | twitter@user.com |

  @Regression
  Scenario Outline: Title Verify if the code on Github exists
    Given The page <website>
    When The founder find the search bar
    And Press enter on this
    Then He/she enter Twitter on the search bar
    And click enter

    Examples:
      | website            |
      | https://github.com |
