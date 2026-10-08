from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Link(models.Model):
    cuisineChoices = [
        ('Chinese', 'Chinese'),
        ('Mexican', 'Mexican'),
        ('Thai', 'Thai'),
        ('Indian', 'Indian'),
        ('American', 'American')
    ]

    meal_category_Choices = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack')
    ]

    prepTime = [
        (0, 'Under 30 minutes'),
        (1, '30-60 minutes'),
        (2, 'over an hour')
    ]

    # name = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=200, choices=cuisineChoices, default="American")
    time = models.IntegerField(choices=prepTime, default=2)
    meal_category = models.CharField(max_length=200, choices=meal_category_Choices, default="Dinner")

    name = models.CharField(max_length=75)
    source = models.CharField(max_length=75)
    pic = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    few = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    cuisineChoices = [
        ('Chinese', 'Chinese'),
        ('Mexican', 'Mexican'),
        ('Thai', 'Thai'),
        ('Indian', 'Indian'),
        ('American', 'American')
    ]

    meal_categoryChoices = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack')
    ]

    prepTime = [
        (0, 'Under 30 minutes'),
        (1, '30-60 minutes'),
        (2, 'over an hour')
    ]

    challenge = models.BooleanField(default=False)

    cuisine = models.CharField(max_length=200, choices=cuisineChoices, default="American")
    time = models.IntegerField(choices=prepTime, default=2)
    meal_category = models.CharField(max_length=200, choices=meal_categoryChoices, default="Dinner")

    name = models.CharField(max_length=75)
    pic = models.CharField(max_length=200)

    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    few = models.BooleanField(default=False)

    step1 = models.CharField(max_length=200)
    step2 = models.CharField(max_length=200)
    step3 = models.CharField(max_length=200)
    step4 = models.CharField(max_length=200, blank=True)
    step5 = models.CharField(max_length=200, blank=True)
    step6 = models.CharField(max_length=200, blank=True)
    step7 = models.CharField(max_length=200, blank=True)
    step8 = models.CharField(max_length=200, blank=True)
    step9 = models.CharField(max_length=200, blank=True)
    step10 = models.CharField(max_length=200, blank=True)

    # users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=75)
    challenge = models.BooleanField(max_length=75)

# class UserLikes(models.Model):
#     recipes = models.ManyToManyField(Recipe)
#     users = models.ManyToManyField(User)


class LikeRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class LikeLink(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SaveSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    cuisineChoices = [
        ('Any', 'Any'),
        ('Chinese', 'Chinese'),
        ('Mexican', 'Mexican'),
        ('Thai', 'Thai'),
        ('Indian', 'Indian'),
        ('American', 'American')
    ]

    meal_categoryChoices = [
        ('Any', 'Any'),
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack')
    ]

    prepTime = [
        ('Any', 'Any'),
        ('Under 30 minutes', 'Under 30 minutes'),
        ('30-60 minutes', '30-60 minutes'),
        ('over an hour', 'over an hour')
    ]

    cuisine = models.CharField(max_length=200, choices=cuisineChoices, default="Any")
    time = models.CharField(max_length=30, choices=prepTime, default="Any")
    meal_category = models.CharField(max_length=200, choices=meal_categoryChoices, default="Any")

    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    few = models.BooleanField(default=False)

    search = models.CharField(max_length=200, default="")


import openai

import string
from string import punctuation


class RandomIngredient(models.Model):
    name = models.CharField(max_length=255)

    @staticmethod
    def generate_random():
        # initialize the OpenAI API
        openai.api_key = ""
        prompt = "Generate 3 random food ingredients not necessarily found together often as a list delimited by commas"
        model = "text-davinci-002"
        response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=100)

        # remove punctuation, remove extra spaces, etc
        random_ingredient = response.choices[0].text.strip().strip(punctuation)


        # create a new Ingredient object with the generated name
        ingredients = RandomIngredient(name=random_ingredient)
        # ingredient.save()
        return ingredients

    def __str__(self):
        return self.name


class CommonIngredient(models.Model):
    name = models.CharField(max_length=255)

    @staticmethod
    def generate_random():
        # initialize the OpenAI API
        openai.api_key = ""
        prompt = "Generate 3 random common food ingredients that are often found together as a list delimited by commas"
        model = "text-davinci-002"
        response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=100)

        # remove punctuation, remove extra spaces, etc
        random_ingredient = response.choices[0].text.strip().strip(punctuation)


        # create a new Ingredient object with the generated name
        ingredients = CommonIngredient(name=random_ingredient)
        # ingredient.save()
        return ingredients

    def __str__(self):
        return self.name


class SeasoningIngredient(models.Model):
    name = models.CharField(max_length=255)

    @staticmethod
    def generate_random():
        # initialize the OpenAI API
        openai.api_key = ""
        prompt = "Generate 3 random food seasonings excluding salt as a list delimited by commas"
        model = "text-davinci-002"
        response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=100)

        # remove punctuation, remove extra spaces, etc
        random_ingredient = response.choices[0].text.strip().strip(punctuation)


        # create a new Ingredient object with the generated name
        ingredients = SeasoningIngredient(name=random_ingredient)
        # ingredient.save()
        return ingredients

    def __str__(self):
        return self.name
