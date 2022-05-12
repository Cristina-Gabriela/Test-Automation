Feature: BDD
  As a lover of chocolate
  I want more chocolate
  So that I will eat

  @Smoke
  Scenario Outline: Title product
    Given The product <name>
    When In the location <x>
    And Buy more <products>
    Then I will enjoy <name>


    Examples:
      | name  | x    | products   |
      | choco | home | chocolates |
      | apple | here | fruits     |
      | juice | town | this       |