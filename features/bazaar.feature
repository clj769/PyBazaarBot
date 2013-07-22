Feature: a bazaar is the marketplace where agents may trade by sending buy and
         sell orders.

    Scenario: a bazaar is a place to trade, so let's trade
    Given a bazaar with two agents
    And the seller has 1 food
    And the seller has 0 coins
    And the buyer has 0 food
    And the buyer has 2 coins
    When the seller wants to sell 1 food for 2 coins
    And the buyer wants to buy 1 food for 2 coins
    Then the sale succeeds
    And the seller has 2 coins
    And the buyer has 1 food