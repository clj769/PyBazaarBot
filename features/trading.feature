Feature: a bazaar is the marketplace where agents may trade by sending buy and
         sell orders.

    Scenario: a bazaar is a place to trade, so let's trade
        Given a bazaar where two agents trade
        And the seller has 1 Food
        And the seller has 0 Coins
        And the buyer has 0 Food
        And the buyer has 2 Coins
        When the seller wants to sell 1 Food for 2 Coins
        And the buyer wants to buy 1 Food for 2 Coins
        Then the sale succeeds
        And the seller has 2 Coins
        And the buyer has 1 Food

    Scenario: at the end of the day, the trade book is emptied
        Given a bazaar where two agents trade
        And the seller has 1 Food
        And the buyer has 2 Coins
        When the seller wants to sell 1 Food for 1 Coins
        And the buyer wants to buy 2 Food for 2 Coins
        Then the sale succeeds
        And the books are empty
