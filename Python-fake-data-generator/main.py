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
db.open_schema_menu()

