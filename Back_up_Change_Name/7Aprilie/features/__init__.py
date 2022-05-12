# Example

Feature:Passing parameters to step

  Scenario: step parameters

    Given I have a new "DVD" in my cart
    And I have a new "BOOK" in my cart
    And I have a new "CAR" in my cart
    When I click on "Next"
    And I click on "Finish"
    Then I should see "success"


