
Feature: Test Autocomplete Formy

  @Smoke
  Scenario: Check address field
    Given I go to autocomplete test
    When I type an address
    Then The actual result should be the same as the expected
