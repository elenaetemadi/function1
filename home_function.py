home_list = []


def show_menu():
    print('1)Add Home information')
    print('2)Home list')
    print('3)Search by Home list')
    print('4)Home count')
    print('0)Exit')
    print('.' * 50)
    option = int(input('Enter your option: '))
    return option


def add_home():
    home_number = int(input('Home number: '))
    owner = input('Owner: ')
    number_of_rooms = int(input('Number of rooms: '))
    parking = input('Does the home have parking? (yes/no) ?')
    if parking == 'yes':
        parking = True
    elif parking == 'no':
        parking = False
    else:
        print('INVALID')
    home = {'home_number': home_number, 'owner': owner, 'number_of_rooms': number_of_rooms, 'parking': parking}
    home_list.append(home)
    return home


def show_home_list(home_list):
    print('Home list\n')
    print(f"{'home_number':15}{'owner':10}{'number_of_rooms':15}{'parking':10}")
    for home in home_list:
        print('{:^15}{:^10}{:^15}{:^10}'.format(home['home_number'], home['owner'], home['number_of_rooms'],
                                                home['parking']))


def search_by_home_number(home_list):
    user_home_number = int(input('Enter your home number: '))
    for home in home_list:
        if home['home_number'] == user_home_number:
            print('found...')
            print('Home found: ', home)
            return home
    else:
        print('not found...')


def home_count(home_list):
    count = len(home_list)
    return count
