#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  maximum = 0
  count = 0

  if len(recipe) > len(ingredients):
    print("not enough ingredients for the supllied recipe!")
    return 0
  
  for i in recipe:
    batches = 0

    if ingredients[i] // recipe[i] >= 1:
      batches = (ingredients[i] // recipe[i])
      return batches

    else :
      return 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


# What we know: 
# - we know that we want to return the max amount of batches that can be made using the ingredients available for the recipe given.
# - we know that our function takes in 2 dictionaries one for recipe and one for ingredients.

# Base Case:
# - if the recipe ask for an ingredient that isn't in our ingredients 
# - if the recipe has an ingredient that ask for more than our ingredient supply

# Pseudo Code:
# 1. check the recipe and make sure that we have the exact ingredients
  # if len(recipe) > len(ingredients):
  #   return 0
# 2. next loop through both recipe and ingredients and compare values
  # for i in recipe:
  #   for j in ingredients:
# 3. if recipe ask for more than we have then return 0
      # if ingredients[j] >= recipe[i]:
# 4. divide the recipe ingredient value from the ingredient value
      #   batch = recipe[i] // ingredients[j]
      
      # return 0
# 
# 