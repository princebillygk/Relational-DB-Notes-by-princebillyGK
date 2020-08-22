from PyInquirer import prompt
from schema import Schema

print("Welcome to database generator")
print("Created by Prince Billy Graham Karmoker")

# init schema
schema_name = prompt([{
    'type': 'input',
    'name': 'schema',
    'message': 'Enter the name of the schema'
}])['schema']

db = Schema(name=schema_name)

while True:
    # get user choice
    question = {
        'type': 'list',
        'name': "choice",
        'message': "What do you want to do?",
        'choices': [
            {
                'name': 'Add a new table',
                'value': 'ADD',
            },
            {
                'name': 'Remove a table',
                'value': 'DEL',
            },
            {
                'name': 'Modify a table',
                'value': 'EDIT',
            },
            {
                'name': 'list tables',
                'value': 'LIST',
            },
            {
                'name': 'Generate fake data',
                'value': 'GEN',
            },
            {
                'name': 'Quit',
                'value': 'QUIT'
            }
        ]
    }
    user_choice = prompt([question])['choice']

    if user_choice == 'GEN':
        db.generate()
    elif user_choice == 'ADD':
        db.add_new_table()
    elif user_choice == 'DEL':
        db.remove_table()
    elif user_choice == 'EDIT':
        db.modify_table()
    elif user_choice == 'LIST':
        db.list_tables()
    else:
        print("Good bye for now. See you again!")
        break
