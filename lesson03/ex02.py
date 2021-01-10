def create_user(
    name='John',
    surname='Doe',
    birth_year='1976',
    city='New Jersey',
    email='johndoe@gmail.com',
    phone='12345'):

    user = {
        'name': name,
        'surname': surname,
        'birth_year': birth_year,
        'city': city,
        'email': email,
        'phone': phone
    }

    for value in user.values():
        print(f'{value} ', end='')

    print('\n')
