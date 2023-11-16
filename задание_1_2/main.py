import pprint
cook_book = {}
with open('recipes.txt', encoding="utf-8") as f:
    line_1 = f.readlines()
    count_1 = len(line_1)


with open('recipes.txt', encoding="utf-8") as f:
    
    for i in range(count_1):
        line = f.readline().strip('\n')
        if not line:
            continue
        count = int(f.readline().strip('\n'))
        items = [f.readline().strip('\n').strip('|')for m in range(count)]
        cook_book[line] = []
        for item in items:
            item = item.split('|')
            cook_book[line].append({
                'ingredient_name':item[0],
                'quantity':item[1],
                'measure':item[2]
                
            })


def get_shop_list_by_dishes(dishes, person_count):
    ingridient = {}
    for i in dishes:
        if i in cook_book:
            dish = cook_book[i]
            for vim in dish:
                dish_1 = vim['ingredient_name']
                count = int(vim['quantity'])
                count_1 = vim['measure']
                if dish_1 in cook_book:
                    ingridient[dish_1] += {'measure' : count_1,
                                     'quantity':count * person_count +'\n'
                }

                else:
                     ingridient[dish_1] = {'measure': count_1,
                                     'quantity':count * person_count

                }
    return ingridient


print(get_shop_list_by_dishes(['Запеченный картофель', 'Утка по-пекински'], 2))