Feature: production of commodities

Scenario outline: a worker creates commodities
  Given a <worker> with <input_amount> <input_commodity>
  When he works
  Then a farmer has <output_amount> <output_commodity>
  Examples: occupations
  | worker     | input_amount | input_commodity | output_amount | output_commodity |
  | farmer     | 1            | wood            | 2             | food             |
  | miner      | 1            | food            | 2             | ore              |
  | woodcutter | 1            | food            | 1             | wood             |
  | blacksmith | 1            | wood            | 2             | tools            |

Scenario outline: a worker creates more commodities while working with tools
  Given a <worker> with <input_amount> <input_commodity>
  and a <worker> has a tool
  When he works
  Then a <worker> has <output_amount> <output_commodity>
  and a <worker> has 0 <input_commodity>
  Examples: occupations
  | worker     | input_amount | input_commodity | output_amount | output_commodity |
  | farmer     | 1            | wood            | 4             | food             |
  | miner      | 1            | wood            | 4             | ore              |
  | woodcutter | 1            | food            | 2             | wood             |

  Scenario: some workers need commodities and food
    Given a refiner with 4 ore
    And a refiner with 1 food
    When he works
    Then a refiner has 4 metal
    And a refiner has 0 food

  Scenario: a worker receives a fine when he cannot work
    Given a farmer with 0 wood
    And a farmer with 2 coins
    When he works
    Then a farmer has 0 food
    And a farmer has 0 coins