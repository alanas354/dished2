from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from dish import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('home/<int:recipe_id>/like/', user_views.home_like, name='home_like'),
    path('home/<int:link_id>/likelink/', user_views.home_like_link, name='home_like_link'),
    # path('home/<int:user_id>', user_views.home, name='home'),
    path('challenge/', user_views.challenge, name='challenge'),
    path('aboutus/', user_views.aboutus, name='aboutus'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/<int:link_id>/likelink/', user_views.profile_like_link, name='profile_like_link'),
    path('register/', user_views.register, name='register'),
    path('userRecipes/', user_views.userRecipes, name='userRecipes'),
    path('userRecipes/<int:recipe_id>/like/', user_views.userRecipes_like, name='userRecipes_like'),
    path('submitdish/', user_views.submitdish, name='submitdish'),
    path('submitlink/', user_views.submitlink, name='submitlink'),
    path('randomingredient/', user_views.randomingredient, name='randomingredient'),
    path('commoningredient/', user_views.commoningredient, name='commoningredient'),
    path('seasoningingredient/', user_views.seasoningingredient, name='seasoningingredient'),

    path('login/', auth_views.LoginView.as_view(template_name='dish/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='dish/logout.html'), name='logout'),
    # path('meal_idea/<int:mealidea_id>', user_views.meal_idea, name='meal_idea'),
    path('<int:recipe_id>', user_views.recipe, name='recipe'),
    path('profile/<int:recipe_id>', user_views.profile_like, name='profile_like'),
    path('<int:recipe_id>/like', user_views.recipe_like, name='recipe_like')
    # path('like/<int:match_id>', user_views.like, name='like'),
    # path('meal_idea/<int:mealidea_id>/<int:match_id>', user_views.meal_idea_recipe, name='meal_idea_recipe'),
    # path('meal_idea/<int:mealidea_id>/<int:match_id>', user_views.meal_idea_link, name='meal_idea_link')
]
