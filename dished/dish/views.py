from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q

from .forms import *
from .models import *


# def home(request):
#    return render(request, 'dish/home.html')
def home(request):
    if request.method == 'POST':
        form = RecipeIdeaForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            cuisine = form.cleaned_data['cuisine']
            time = form.cleaned_data['time']
            meal_category = form.cleaned_data['meal_category']
            vegan = form.cleaned_data['vegan']
            vegetarian = form.cleaned_data['vegetarian']
            few = form.cleaned_data['few']
            search = form.cleaned_data['search']
            user = request.user
            save_search(user, cuisine, time, meal_category, vegan, vegetarian, few, search)
            liked_recipes, unliked_recipes, liked_links, unliked_links = get_recipe(cuisine, time, meal_category,
                                                                                    vegan, vegetarian, few,
                                                                                    search, user)
            context = {'form': form, 'liked_recipes': liked_recipes, 'unliked_recipes': unliked_recipes,
                       'liked_links': liked_links, 'unliked_links': unliked_links}
            return render(request, 'dish/home.html', context)
        elif form.is_valid():
            cuisine = form.cleaned_data['cuisine']
            time = form.cleaned_data['time']
            meal_category = form.cleaned_data['meal_category']
            vegan = form.cleaned_data['vegan']
            vegetarian = form.cleaned_data['vegetarian']
            few = form.cleaned_data['few']
            search = form.cleaned_data['search']
            liked_recipes, unliked_recipes, liked_links, unliked_links = get_recipe(cuisine, time, meal_category,
                                                                                    vegan, vegetarian, few, search)
            context = {'form': form, 'liked_recipes': liked_recipes, 'unliked_recipes': unliked_recipes,
                       'liked_links': liked_links, 'unliked_links': unliked_links}
            return render(request, 'dish/home.html', context)
    elif request.user.is_authenticated and SaveSearch.objects.filter(user=request.user).exists():
        user = request.user
        saved_form = SaveSearch.objects.get(user=user)

        cuisine = getattr(saved_form, 'cuisine')
        meal_category = getattr(saved_form, 'meal_category')
        time = getattr(saved_form, 'time')
        vegan = getattr(saved_form, 'vegan')
        vegetarian = getattr(saved_form, 'vegetarian')
        few = getattr(saved_form, 'few')
        search = getattr(saved_form, 'search')
        form = RecipeIdeaForm(initial={"cuisine": cuisine, "meal_category": meal_category, "time": time, "vegan": vegan,
                                       "vegetarian": vegetarian, "few": few, "search": search})
        save_search(user, cuisine, time, meal_category, vegan, vegetarian, few, search)
        liked_recipes, unliked_recipes, liked_links, unliked_links = get_recipe(cuisine, time, meal_category,
                                                                                vegan, vegetarian, few, search, user)
        context = {'form': form, 'liked_recipes': liked_recipes, 'unliked_recipes': unliked_recipes, 
                   'liked_links': liked_links, 'unliked_links': unliked_links}
        return render(request, 'dish/home.html', context)
    else:
        form = RecipeIdeaForm()
        liked_recipes = Recipe.objects.all()
        unliked_recipes = []
        liked_links = Link.objects.all()
        unliked_links = []
        context = {'form': form, 'liked_recipes': liked_recipes, 'unliked_recipes': unliked_recipes,
                   'liked_links': liked_links, 'unliked_links': unliked_links}
        return render(request, 'dish/home.html', context)


def get_recipe(cuisine, time, meal_category, vegan, vegetarian, few, search, user=None):
    recipes = Recipe.objects.all()
    links = Link.objects.all()
    if cuisine != 'Any':
        recipes = recipes.filter(cuisine=cuisine)
        links = links.filter(cuisine=cuisine)
    if time != 'Any':
        recipes = recipes.filter(time=time)
        links = links.filter(time=time)
    if meal_category != 'Any':
        recipes = recipes.filter(meal_category=meal_category)
        links = links.filter(meal_category=meal_category)
    if vegan:
        recipes = recipes.filter(vegan=True)
        links = links.filter(vegan=True)
    if vegetarian:
        recipes = recipes.filter(vegetarian=True)
        links = links.filter(vegetarian=True)
    if few:
        recipes = recipes.filter(few=True)
        links = links.filter(few=True)
    if search:
        # print(recipes)
        recipes = recipes.filter((Q(name__icontains=search) | Q(ingredient__ingredient__icontains=search)))
        recipes = recipes.distinct()
        # recipes = recipes.filter(name__icontains=search)
        # recipes = recipes.filter(ingredient__ingredient__icontains=search)
        # print(recipes)

        links = links.filter((Q(name__icontains=search) | Q(source__icontains=search)))
        links = links.distinct()
    if user:
        liked_recipes = []
        unliked_recipes = []
        for match in recipes:
            liked = LikeRecipe.objects.filter(user=user, recipe=match)
            if liked.exists():
                liked_recipes.append(match)
            else:
                unliked_recipes.append(match)
        liked_links = []
        unliked_links = []
        for match in links:
            liked = LikeLink.objects.filter(user=user, link=match)
            if liked.exists():
                liked_links.append(match)
            else:
                unliked_links.append(match)
        # print(liked_recipe)
        return liked_recipes, unliked_recipes, liked_links, unliked_links
    else:
        liked_recipes = recipes
        unliked_recipes = []
        liked_links = links
        unliked_links = []
        return liked_recipes, unliked_recipes, liked_links, unliked_links


def save_search(user, cuisine, time, meal_category, vegan, vegetarian, few, search2):
    search = SaveSearch(user=user)
    if cuisine != 'Any':
        search.cuisine = cuisine
    if time != 'Any':
        search.time = time
    if meal_category != 'Any':
        search.meal_category = meal_category
    if vegan:
        search.vegan = True
    if vegetarian:
        search.vegetarian = True
    if few:
        search.few = True
    if search:
        search.search = search2
    prev = SaveSearch.objects.filter(user=user)
    if prev.exists():
        prev.delete()
    search.save()


def recipe(request, recipe_id):
    recipe2 = get_object_or_404(Recipe, pk=recipe_id)
    # print(recipe2.step1)
    # num_steps = 0
    # for i in range(1, 11):
    #     step = "step" + str(i)
    #     currstep = locals()[step]
    #     step_val = recipe2.currstep
    #     if step_val != "" and step_val != "None":
    #         num_steps = num_steps + 1
    ingredients = Ingredient.objects.filter(recipe=recipe2)
    if request.user.is_authenticated:
        user = request.user
        liked = LikeRecipe.objects.filter(user=user, recipe=recipe2)
        if liked.exists():
            liked = True
        else:
            liked = False
        context = {'recipe': recipe2, 'ingredients': ingredients, 'liked': liked}
        return render(request, 'dish/recipe.html', context)
    else:
        context = {'recipe': recipe2, 'ingredients': ingredients}
        return render(request, 'dish/recipe.html', context)


def recipe_like(request, recipe_id):
    user = request.user
    like(user, recipe_id)
    return HttpResponseRedirect(reverse('recipe', args=(recipe_id,)))


def home_like(request, recipe_id):
    user = request.user
    like(user, recipe_id)
    # print(user)
    return HttpResponseRedirect(reverse('home'))


def home_like_link(request, link_id):
    user = request.user
    like_link(user, link_id)
    # print(user)`
    return HttpResponseRedirect(reverse('home'))


def profile_like(request, recipe_id):
    user = request.user
    like(user, recipe_id)
    return HttpResponseRedirect(reverse('profile'))

def profile_like_link(request, link_id):
    user = request.user
    like_link(user, link_id)
    return HttpResponseRedirect(reverse('profile'))


def userRecipes_like(request, recipe_id):
    user = request.user
    like(user, recipe_id)
    return HttpResponseRedirect(reverse('userRecipes'))


def like(user, recipe_id):
    liked = LikeRecipe.objects.filter(user=user, recipe=recipe_id)
    recipe2 = get_object_or_404(Recipe, pk=recipe_id)
    like2 = False
    if liked.exists():
        liked.delete()
        like2 = False
    else:
        # recipe2 = get_object_or_404(Recipe, id=request.POST.get('match_id'))
        like_object = LikeRecipe(user=user, recipe=recipe2)
        LikeRecipe.save(like_object)
        context = {'liked': True}
        like2 = True
    return like2

def like_link(user, link_id):
    liked = LikeLink.objects.filter(user=user, link=link_id)
    link2 = get_object_or_404(Link, pk=link_id)
    # like2 = False
    if liked.exists():
        liked.delete()
        like2 = False
    else:
        like_object = LikeLink(user=user, link=link2)
        LikeLink.save(like_object)
        like2 = True
    return like2

def challenge(request):
    return render(request, 'dish/challenge.html')

def aboutus(request):
    return render(request, 'dish/aboutus.html')


def profile(request):
    user_id = request.user
    # recipe2 =
    liked = LikeRecipe.objects.filter(user=user_id)
    liked_links = LikeLink.objects.filter(user=user_id)
    recipes = []
    links = []
    for match in liked:
        recipes.append(match.recipe)
    for match in liked_links:
        links.append(match.link)
    return render(request, 'dish/profile.html', {'recipes': recipes, 'links':links})


def userRecipes(request):
    recipes = Recipe.objects.all()
    recipes = recipes.filter(challenge=True)
    if request.user.is_authenticated:
        user = request.user
        liked_recipes = []
        unliked_recipes = []
        for match in recipes:
            liked = LikeRecipe.objects.filter(user=user, recipe=match)
            if liked.exists():
                liked_recipes.append(match)
            else:
                unliked_recipes.append(match)
        # context = {'liked_recipes': liked_recipes, 'unliked_recipes': unliked_recipes}
    else:
        liked_recipes = recipes
        unliked_recipes = []
    context = {'liked_recipes': liked_recipes, 'unliked_recipes': unliked_recipes}
    return render(request, 'dish/userRecipes.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Dished profile has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'dish/register.html', context)


def submitdish(request):
    if request.method == "POST":
        form = NewDishForm(request.POST)
        # title = form.name
        # cuisine = form.cuisine
        if form.is_valid():
            form = form.cleaned_data
            print(form)
            new_recipe = Recipe(challenge=form['challenge'], cuisine=form['cuisine'], time=form['time'],
                                meal_category=form['meal_category'], name=form['name'], pic=form['pic'],
                                vegan=form['vegan'], vegetarian=form['vegetarian'], few=form['few'],
                                step1=form['step1'], step2=form['step2'], step3=form['step3'], step4=form['step4'],
                                step5=form['step5'], step6=form['step6'], step7=form['step7'], step8=form['step8'],
                                step9=form['step9'])
            new_recipe.save()
            # challenge_count = 0
            for i in range(1, 11):
                ing = "ingredient" + str(i)
                ing2 = form[ing]
                if ing2 != "":
                    ch = "challenge" + str(i)
                    ch2 = form[ch]
                    new_ingredient = Ingredient(recipe=new_recipe, ingredient=ing2, challenge=ch2)
                    new_ingredient.save()
            if request.user.is_authenticated:
                LikeRecipe(user=request.user, recipe=new_recipe).save()
            return redirect('home')
        else:
            # form = NewDishForm()
            # print(form.errors)
            return render(request, 'dish/submitdish.html', {'form': form})
    else:
        form = NewDishForm()
        return render(request, 'dish/submitdish.html', {'form': form})


def submitlink(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        # title = form.name
        # cuisine = form.cuisine
        if form.is_valid():
            new_link = form.save()
            if request.user.is_authenticated:
                LikeLink(user=request.user, link=new_link).save()
            return redirect('home')
    else:
        form = LinkForm()
    context = {'form': form}
    return render(request, 'dish/submitlink.html', context)


def randomingredient(request):
    ingredients = RandomIngredient.generate_random()

    # get as list?
    ingredients = str(ingredients).split(",")
    i1 = ingredients[0]
    i2 = ingredients[1]
    i3 = ingredients[2]

    return render(request, "dish/randomingredient.html", {"ingredients": ingredients, "i1": i1, "i2": i2, "i3": i3, })


def commoningredient(request):
    ingredients = CommonIngredient.generate_random()

    # get as list?
    ingredients = str(ingredients).split(",")
    i1 = ingredients[0]
    i2 = ingredients[1]
    i3 = ingredients[2]

    return render(request, "dish/commoningredient.html", {"ingredients": ingredients, "i1": i1, "i2": i2, "i3": i3, })


def seasoningingredient(request):
    ingredients = SeasoningIngredient.generate_random()

    # get as list?
    ingredients = str(ingredients).split(",")
    i1 = ingredients[0]
    i2 = ingredients[1]
    i3 = ingredients[2]

    return render(request, "dish/seasoningingredient.html",
                  {"ingredients": ingredients, "i1": i1, "i2": i2, "i3": i3, })
