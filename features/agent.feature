Feature: basic economic agent
    In order to start the economic simulation,
    As a simulator
    I want to have a economic agent that will be the basis for the simulation

    Scenario: Agent owns things
    Given the Agent
    When given 5 Tools
    Then the Agent owns 5 Tools

    Scenario: Agent has inventory space
    Given the Agent has 100 inventory space
    When given 5 Tools
    And given 1 Food
    Then the Agent has 94 inventory space left

    Scenario: Some things can weigh nothing
    Given the Agent has 1 inventory space
    When given 100 Coins
    Then the Agent has 1 inventory space left
