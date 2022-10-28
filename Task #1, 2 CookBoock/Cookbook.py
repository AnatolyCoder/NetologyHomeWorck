import json

file = open('list of recipes', 'r', encoding='utf8')
cook_book = {}

while True:
    dish_ingredients = []
    dish_name = file.readline()
    quant_ingredients = file.readline()
    if dish_name == '':
        break
    for i in range(int(quant_ingredients)):
        ingredient = file.readline()
        ingredient_list = ingredient.split(' | ')
        ingredient_dict = {'ingredient_name': ingredient_list[0], 'quantity': ingredient_list[1], 'measure': ingredient_list[2]}
        dish_ingredients.append(ingredient_dict)
    cook_book.update({dish_name: dish_ingredients})
    empty_line = file.readline()

# print(json.dumps(cook_book, indent=0, ensure_ascii=False))

def get_shop_list_by_dishes(dishes, person_count):
    finish_ingredients_dict = {}
    for dish_name, dish_ingredients_list in cook_book.items():
        if dish_name in dishes:
            for ingredient_dict in dish_ingredients_list:
                for key, value in ingredient_dict.items():
                    if key == 'quantity':
                        ingredient_dict[key] *= person_count
                finish_ingredients_dict.update({ingredient_dict.get('ingredient_name'): {'measure': ingredient_dict.get('measure'), 'quantity': ingredient_dict.get('quantity')}})
    return print(json.dumps(finish_ingredients_dict, indent=0, ensure_ascii=False))

# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)