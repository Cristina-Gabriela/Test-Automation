Feature: BDD
  As an expert Software Developer
  I am able to update all the software applications automatically
  So that I don't work hardly

  @Smoke
  Scenario Outline:Title Update macOs
    Given A new version of application is available
    When Today at 13:02
    And Before, the user must charge the device
    Then He/she must prepare the macOs for this update
    And After this he/she must reopen the device
    Then Try to use normally
    And If something went wrong
    Then Call the tech team at the number displayed on the <site1>

    Examples:
      | site1                                    |
      | https://support.apple.com/en-us/HT201541 |

  @Smoke
  Scenario:Title Update iPhone,iPod,iPad
    Given This three devices : iPhone,iPod,iPad updated by the software developers
    When The Santa Claus was coming
    And The pricing was falling
    Then A lot of people was buying

  @Regression
  Scenario:Title Update Microsoft
    Given My PC was updated with Microsoft
    When All the system in this enterprise was updated
    And Right now the system run easier
    Then All my projects turns quickly