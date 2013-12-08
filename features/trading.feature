Feature: a bazaar is the marketplace where agents may trade by sending buy and
         sell orders.

    Scenario: a bazaar is a place to trade, so let's trade
    Given a bazaar where two agents trade
    And the seller has 1 Food
    And the seller has 0 coins
    And the buyer has 0 Food
    And the buyer has 2 coins
    When the seller wants to sell 1 Food for 2 coins
    And the buyer wants to buy 1 Food for 2 coins
    Then the sale succeeds
    And the seller has 2 coins
    And the buyer has 1 Food

    Scenario: remaining bids are kept in the market
    Given a bazaar where two agents trade
    And the seller has 1 Food
    And the buyer has 2 coins
    When the seller wants to sell 1 Food for 1 coins
    And the buyer wants to buy 2 Food for 2 coins
    Then the sale succeeds
    And a bid remains on the bid book