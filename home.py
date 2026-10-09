from home_function import*

while True:
    option=show_menu()
    print('.'*50)
    if option==0:
        print('Exit')
        print('.'*50)
        break
    elif option==1:
        home=add_home()
        print('.'*50)
    elif option==2:
        show_home_list(home_list)
        print('.'*50)
    elif option==3:
        home=search_by_home_number(home_list)
        print('.'*50)
    elif option==4:
        count=home_count(home_list)
        print('home count: ', count)
        print('.'*50)
    else:
        print('INVALID...')
        print('.'*50)
