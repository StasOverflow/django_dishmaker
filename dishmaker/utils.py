def many_to_many_igredients_get(obj):
    """
        In case there will be repetitions of ingredients, we need to split procedure into two parts
    :return: List of ingredients for a certain order or dish
    """
    print(obj.dishrecipe.all())
    ing_list = [
        (ing.ingredient_id.name, ing.ingredient_quantity) for ing in obj.dishrecipe.all()
    ]

    ingredients = dict()
    print(ing_list)
    for ing in ing_list:
        if ing[0] not in ingredients:
            value = ing[1]
        else:
            value = ingredients[ing[0]] + ing[1]
        ingredients[ing[0]] = value
    print(ingredients)
    return ingredients
