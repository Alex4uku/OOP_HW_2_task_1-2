from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        count_ingredients = int(file.readline())
        data_ingredients = []
        for i in range(count_ingredients):
            emp = file.readline()
            ingredient_name, quantity, measure = emp.strip().split(' | ')
            ingredient = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure,
            }
            data_ingredients.append(ingredient)
        file.readline()
        cook_book[dish] = data_ingredients
    pprint(cook_book, sort_dicts=False, indent=6)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    if isinstance(dishes, list):
        for dish in dishes:
            if dish in cook_book:
                for ingredients in cook_book[dish]:
                    ingredient_name, quantity, measure = ingredients.get('ingredient_name'), \
                            int(ingredients.get('quantity')) * person_count, ingredients.get('measure')
                    shop_list_1 = {
                        'measure': measure,
                        'quantity': quantity
                    }
                    if ingredient_name not in shop_list:
                            shop_list[ingredient_name] = shop_list_1
                    else:
                        a = shop_list[ingredient_name]
                        b = int(a.get('quantity')) + quantity
                        shop_list_1['quantity'] = b
                        shop_list[ingredient_name] = shop_list_1
            else:
                print('Данные введены неверно!')
        pprint(shop_list)

    else:
        if dishes in cook_book:
            for ingredients in cook_book[dishes]:
                ingredient_name, quantity, measure = ingredients.get('ingredient_name'), \
                    int(ingredients.get('quantity')) * person_count, ingredients.get('measure')
                shop_list_1 = {
                    'measure': measure,
                    'quantity': quantity
                }
                shop_list[ingredient_name] = shop_list_1
        else:
            print('Данные введены неверно!')
        pprint(shop_list)
print()
print()
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print()
get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)