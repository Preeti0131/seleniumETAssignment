
@tag
Feature: Purchase either Moisturizer or Sunscreen
  I want to use this template for my feature file

  @tag1
  Scenario: Shop sunscreen or moisturizer based on temperature information
    Given Launch Weather Shopper website
    When Identify the temperature
    And Choose to buy Moisturizer or Sun screen
    Then Choose the product
    And Read the instruction of product
    And Add the product to cart
    And Verify the cart value and initiate a payment
    And make payment


