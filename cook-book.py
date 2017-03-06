def read_cook_book():
    cook_book = {}
    with open('cook-list.txt') as f:
        while True:
            dish_name = f.readline().strip()
            if dish_name:
                cook_book[dish_name] = []
                number_of_dish_items = int(f.readline())
                for i in range(number_of_dish_items):
                    item = f.readline().split(' | ')
                    u = {}
                    u['ingridient_name'] = item[0].strip()
                    u['quantity'] = int(item[1].strip())
                    u['measure'] = item[2].strip()
                    cook_book[dish_name].append(u)
            else:
                break
    return cook_book

cook_book = read_cook_book()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    # for shop_list_item in shop_list.values():
    #    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))
        
def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()

# def main():
#     read_cook_book()


# if __name__ == '__main__':
#   main()