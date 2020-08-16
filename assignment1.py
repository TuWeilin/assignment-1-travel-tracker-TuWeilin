"""
Name:Tu Weilin
Date started:30-07-2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-1-travel-tracker-TuWeilin
"""


def count_places():
    file_read = open('places.csv','r')
    lines = file_read.readlines()
    count = 0
    for line in lines:
        count += 1
    file_read.close()
    return count

def visited_mark_change(n):
    file_lin = open('places.csv', 'r')
    lines = file_lin.readlines()
    count = 0
    for line in lines:
        count += 1
    for i in range(0, count):
        lines[i] = lines[i].split(sep = ",")
    print(lines)
    print(lines[1])
    lines[n-1][3] = 'v\n'
    print(lines)
    for x in range(0, count):
        lines[x] = ','.join(lines[x])
    print(lines)
    file_lin.close()
    file_rewrite = open('places.csv','w')
    file_rewrite.writelines(lines)
    file_rewrite.close()




def marked_visit():
    print("Enter the number of a place to mark as visited")
    count = 0
    Dic_places = dict()
    file_lin = open('places.csv', 'r')
    lines = file_lin.readlines()
    Dic_places = dict()
    for line in lines:
        count += 1
    for i in range(1, count + 1):
        Dic_places.update({i: lines[i - 1]})
    file_lin.close()
    try:
        choice_mark = int(input(">>>"))
    except ValueError:
        print("Invalid input; enter a valid number")
        marked_visit()
    else:
        if choice_mark < 0:
            print("Number must be > 0")
            marked_visit()
        elif choice_mark > count:
            print('Invalid place number')
        marked_choice = Dic_places.get(choice_mark)
        if 'v' in marked_choice:
            print('That place is already visited')
            main()
        if 'n' in marked_choice:
            visited_mark_change(choice_mark)
            places_menu()
            marked_visit()



def places_menu():
    read_file = open('places.csv','r')
    Lines = read_file.readlines()
    count = 0
    visit_mark = 0
    for I in Lines:
        count += 1
        I = I.split(sep=",")
        if 'v' in I[3]:
            I[3] = ''
            visit_mark += 1
        else:
            I[3] = "*"
        print("{:1}{:5}.{:10}  in {:12}  priority {:5}".format(I[3], count, I[0], I[1], I[2]))
    still_places = count - visit_mark
    if still_places > 0 :
        print('{} places. You still want to visit {} places'.format(count, still_places))
    elif still_places == 0 :
        print('{} places. No places left to visit. Why not add a new place?'.format(count))
        main()


def write_file(city_name, country_name, priority_get):
    new_text = open('places.csv', 'a+')
    new_text.writelines('{},{},{},n\n'.format(city_name, country_name, priority_get))
    new_text.close()

def new_places_city():
    city_name = str(input("Name: "))
    if city_name.isspace() or city_name == '':
        print("Input can not be blank")
        new_places_city()
    return city_name

def new_places_country():
    country_name = str(input('country: '))
    if country_name.isspace() or country_name == '':
        print("Input can not be blank")
        new_places_country()
    return country_name

def new_places_priority():
    try:
        priority_get = int(input("priority: "))
        if priority_get <= 0:
            print("Number must be > 0")
            new_places_priority()
    except ValueError:
        print('Invalid input; enter a valid number')
        new_places_priority()
    else:
        return priority_get


def new_places(city_name, country_name, priority_get):
    print('{} in {} (priority {}) added to Travel Tracker'.format(city_name, country_name, priority_get))
    write_file(city_name, country_name, priority_get)




def program_menu():
    '''Show the menu'''
    print('Menu:')
    print('L - List places')
    print('A - Add new place')
    print('M - Mark a places as visited')
    print('Q - Quit')
    menu_choice = str(input('>>>'))
    return menu_choice


print("Travel Tracker 1.0 - by TuWeilin")
print('3 places loaded from places.csv')

def main():
    """Track places visited"""
    choice_menu = ['l', 'L', 'A', 'a', 'M', 'm', 'Q', 'q']
    menu_choice = program_menu()
    while menu_choice not in choice_menu:
        print('invalid menu choice')
        main()
    if menu_choice == 'l' or menu_choice == 'L':
        places_menu()
        main()
    elif menu_choice == 'a' or menu_choice == 'A':
        new_places(new_places_city(), new_places_country(), new_places_priority())
        main()
    elif menu_choice == 'm' or menu_choice == 'M':
        places_menu()
        marked_visit()
    elif menu_choice == 'q' or menu_choice == 'Q':
        count = count_places()
        print('{} places saved to places.csv'.format(count))
        print('Have a nice day :)')
    return



if __name__ == '__main__':
    main()
