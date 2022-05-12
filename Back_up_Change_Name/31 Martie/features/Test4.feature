Feature: BDD
  As an IT person
  I want to know many things
  So that I will try to read and do exercises

  @Smoke
  Scenario Outline: Open Google
    Given The browser Google will be open
    When The internet is connected
    And The person will be in the front of a computer
    Then He will search on <site1> <word1>
    And Enter
    Then He will search another <site2> on <word2>
    And Enter

    Examples:
      | site1  | word2      |
      | google | Automation |

    Examples:
      | site1  | word2    |
      | ecosia | Selenium |

  @Smoke
  Scenario: Open Facebook
    Given The user open the application
    When He has the connection on internet
    And He puts username and password
    Then He visit the news

  @Smoke
  Scenario: Open Messenger
    Given A new version of Messenger is on the market
    When Today, 31 March 2022
    And The testers must be very attentive with the product
    Then It will be an economic boom for the firm

  @Smoke
  Scenario: Open FitPro
    Given A new application for smartwatches
    When Yesterday
    And The Automation Testers must write the scripts for testing
    Then A lot of people will buy this product

  @Regression
  Scenario: Open WhatsApp
    Given WhatsApp was recently installed on the smartphones
    When Before the customers buys the smartphones
    And This application was tested by a lot of qualified employees
    Then This application was verified by manager