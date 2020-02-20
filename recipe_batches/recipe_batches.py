#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
      # assign 'ingredients' in recipe dictionary to variable
      recipe_keys = recipe.keys()
      
      batches = float('inf')
      # if ingredient value is not sufficient return 0
      for i in recipe_keys:
            if ingredients.get(i) == None:
                  return 0
                
            recipe_value = recipe.get(i)
            ingredient_value = ingredients.get(i)
          # divide ingredient value by recipe value to get possible number of batches
            ingredient_batch = math.floor(ingredient_value/recipe_value)
          # assign result to batches and return it  
            if ingredient_batch < batches:
                  batches = ingredient_batch
            
      return batches
      
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))