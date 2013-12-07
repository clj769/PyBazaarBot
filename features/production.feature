Feature: production of commodities

Scenario Outline: a worker creates commodities
    Given a <worker> with <input_amount> <input_commodity>
    When he works
    Then a farmer has <output_amount> <output_commodity>

    Examples: occupations
    | worker     | input_amount | input_commodity | output_amount | output_commodity |
    | farmer     | 1            | Wood            | 2             | Food             |
    | miner      | 1            | Food            | 2             | Ore              |
    | woodcutter | 1            | Food            | 1             | Wood             |
    | blacksmith | 1            | Wood            | 2             | Tools            |

Scenario Outline: a worker creates more commodities while working with tools
    Given a <worker> with <input_amount> <input_commodity>
    and a <worker> has a tool
    When he works
    Then a <worker> has <output_amount> <output_commodity>
    and a <worker> has 0 <input_commodity>

    Examples: occupations
    | worker     | input_amount | input_commodity | output_amount | output_commodity |
    | farmer     | 1            | Wood            | 4             | Food             |
    | miner      | 1            | Wood            | 4             | Ore              |
    | woodcutter | 1            | Food            | 2             | Wood             |

Scenario: some workers need commodities and food
    Given a refiner with 4 Ore
    And a refiner with 1 Food
    When he works
    Then a refiner has 4 Metal
    And a refiner has 0 Food

Scenario: a worker receives a fine when he cannot work
    Given a farmer with 0 Wood
    And a farmer with 2 Coins
    When he works
    Then a farmer has 0 Food
    And a farmer has 0 Coins