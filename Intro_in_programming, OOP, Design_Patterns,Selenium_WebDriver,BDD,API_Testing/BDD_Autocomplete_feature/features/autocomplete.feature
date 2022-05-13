Feature: Test Autocomplete Formy

  @Smoke
  Scenario Outline: Testing purposes
    Given The site A
    When Go to the first button B
    Then get the C


    Examples:
      | site                                | first        | new address                                     |
      | http://formy-project.herokuapp.com/ | Autocomplete | http://formy-project.herokuapp.com/autocomplete

