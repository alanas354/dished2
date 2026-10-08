from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import Textarea

from .models import *


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


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
    (0, 'Under 30 minutes'),
    (1, '30-60 minutes'),
    (2, 'over an hour')
]


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
#     labels = {
#         "few": 'Less than 5 ingredients',
#         "step1": "1",


class RecipeIdeaForm(forms.Form):
    cuisine = forms.CharField(label='Cuisine', widget=forms.Select(choices=cuisineChoices))
    meal_category = forms.CharField(label='Meal Category', widget=forms.Select(choices=meal_categoryChoices))
    time = forms.CharField(label='Time Involved', widget=forms.Select(choices=prepTime))
    vegan = forms.BooleanField(required=False)
    vegetarian = forms.BooleanField(required=False)
    few = forms.BooleanField(label='<5 ingredients', required=False)
    search = forms.CharField(required=False)

    # class Meta:
    #     model = Recipe
    #     fields = ["cuisine", "time", "meal_category", "vegan", "vegetarian", "few"]
    #     labels = {"few": 'Less than 5 ingredients'}


class NewDishForm(forms.Form):
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

    name = forms.CharField(label='Recipe Title')
    pic = forms.CharField(label='Image Source')
    cuisine = forms.CharField(label='Cuisine', widget=forms.Select(choices=cuisineChoices))
    meal_category = forms.CharField(label='Meal Category', widget=forms.Select(choices=meal_categoryChoices))
    time = forms.CharField(label='Time Involved', widget=forms.Select(choices=prepTime))
    vegan = forms.BooleanField(required=False)
    vegetarian = forms.BooleanField(required=False)
    few = forms.BooleanField(label='Less than 5 ingredients', required=False)
    challenge = forms.BooleanField(required=False)

    ingredient1 = forms.CharField()
    challenge1 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'bigger'}))
    ingredient2 = forms.CharField(required=False)
    challenge2 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'bigger'}))
    ingredient3 = forms.CharField(required=False)
    challenge3 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'bigger'}))
    ingredient4 = forms.CharField(required=False)
    challenge4 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'bigger'}))
    ingredient5 = forms.CharField(required=False)
    challenge5 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'bigger'}))
    ingredient6 = forms.CharField(required=False)
    challenge6 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'bigger'}))
    ingredient7 = forms.CharField(required=False)
    challenge7 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'bigger'}))
    ingredient8 = forms.CharField(required=False)
    challenge8 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'bigger'}))
    ingredient9 = forms.CharField(required=False)
    challenge9 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'bigger'}))
    ingredient10 = forms.CharField(required=False)
    challenge10 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'bigger'}))

    step1 = forms.CharField(label="1")
    step2 = forms.CharField(label="2")
    step3 = forms.CharField(label="3")
    step4 = forms.CharField(required=False, label="4")
    step5 = forms.CharField(required=False, label="5")
    step6 = forms.CharField(required=False, label="6")
    step7 = forms.CharField(required=False, label="7")
    step8 = forms.CharField(required=False, label="8")
    step9 = forms.CharField(required=False, label="9")
    step10 = forms.CharField(required=False, label="10")

    def clean(self):
        cleaned_data = super().clean()
        cs = [cleaned_data.get("challenge1"), cleaned_data.get("challenge2"),
              cleaned_data.get("challenge3"), cleaned_data.get("challenge4"),
              cleaned_data.get("challenge5"),cleaned_data.get("challenge6"),
              cleaned_data.get("challenge7"), cleaned_data.get("challenge8"),
              cleaned_data.get("challenge9"), cleaned_data.get("challenge10")]

        if sum(bool(x) for x in cs) > 3:
            raise ValidationError("Cannot have more than 3 challenge ingredients")
            # self.add_error('subject', msg)
        return cleaned_data
    # class Meta:
    #     model = Recipe
    #     fields = '__all__'
    #     widgets = {
    #         # 'name': Textarea(attrs={})
    #         'step1': Textarea(attrs={'rows': 2}),
    #         'step2': Textarea(attrs={'rows': 2}),
    #         'step3': Textarea(attrs={'rows': 2}),
    #         'step4': Textarea(attrs={'rows': 2}),
    #         'step5': Textarea(attrs={'rows': 2}),
    #         'step6': Textarea(attrs={'rows': 2}),
    #         'step7': Textarea(attrs={'rows': 2}),
    #         'step8': Textarea(attrs={'rows': 2}),
    #         'step9': Textarea(attrs={'rows': 2})
    #     }
    #     labels = {
    #         "few": 'Less than 5 ingredients',
    #         "step1": "1",
    #         "step2": "2",
    #         "step3": "3",
    #         "step4": "4",
    #         "step5": "5",
    #         "step6": "6",
    #         "step7": "7",
    #         "step8": "8",
    #         "step9": "9",
    #         "ingredient1": "",
    #         "ingredient2": "",
    #         "ingredient3": "",
    #         "ingredient4": "",
    #         "ingredient5": "",
    #         "ingredient6": "",
    #         "ingredient7": "",
    #         "ingredient8": "",
    #         "ingredient9": "",
    #         "ingredient10": ""
    #     }

