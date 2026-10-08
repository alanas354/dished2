from django.contrib import admin

# Register your models here.
from .models import *


# admin.site.register(MealIdea)
# admin.site.register(NewDish)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Link)
admin.site.register(RandomIngredient)
admin.site.register(CommonIngredient)
admin.site.register(SeasoningIngredient)
admin.site.register(LikeRecipe)
admin.site.register(SaveSearch)



