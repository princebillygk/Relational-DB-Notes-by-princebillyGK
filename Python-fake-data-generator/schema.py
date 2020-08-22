from json import load as json_loader

from PyInquirer import prompt

with open('datatypes_faker.json') as datatype_file:
    datatypes = json_loader(datatype_file)


class Schema:
    """Creates a schema for storing database columns"""

    def __init__(self, name="myschema"):
        self.name = name
        self.tables = []

    def __input_table_index(self):
        """Get column index from prompt"""
        if self.tables:
            question = {
                'type': 'list',
                'name': 'table_index',
                'message': 'Select an table from the list',
                'choices': [{'name': table.name, 'value': index}
                            for index, table in enumerate(self.tables)],
            }
            return prompt([question])['table_index']

    def add_new_table(self):
        """Create a new table in the schema"""
        # input table name
        table_name = prompt({
            'type': 'input',
            'name': 'table',
            'message': 'Input table name'
        })['table']
        # check if table name already exists
        for table in self.tables:
            if table.name == table_name:
                print("A table named %s already exists" % table_name)
                return
        # creates a table
        self.tables.append(Table(table_name))

    def remove_table(self):
        """removes a table if exists"""
        table_index = self.__input_table_index()
        if table_index is not None:
            table_name = self.tables.pop(table_index).name
            print(table_name + " is removed")
        else:
            print("No tables to remove")

    def modify_table(self):
        """removes a table if exists"""
        table_index = self.__input_table_index()
        if table_index is not None:
            print("Modifying table " + self.tables[table_index].name)
        else:
            print("No tables to modify")

    def generate(self):
        print("generating fake data")

    def list_tables(self):
        for table in self.tables:
            print(table.name)


class Table:
    """creates a new column"""

    def __init__(self, name):
        """creates a new column with this name"""
        self.name = name
        self.columns = []
        self.open_table_menu()

    def __input_column_index(self):
        """Get column index from prompt"""
        if self.columns:
            question = {
                'type': 'list',
                'name': 'column_index',
                'message': 'Select an column from the list',
                'choices': [{'name': column.name, 'value': index}
                            for index, column in enumerate(self.columns)],
            }
            return prompt([question])['column_index']

    def open_table_menu(self):
        """suggests options for modifying column"""
        while True:
            question = {
                'type': 'list',
                'name': "choice",
                'message': "What do you want to do?",
                'choices': [
                    {
                        'name': 'Add a new column',
                        'value': 'ADD',
                    },
                    {
                        'name': 'remove a column',
                        'value': 'DEL',
                    },
                    {
                        'name': 'edit a column',
                        'value': 'EDIT',
                    },
                    {
                        'name': 'list columns',
                        'value': 'LIST',
                    },
                    {
                        'name': 'back',
                        'value': 'BACK'
                    }
                ]
            }
            user_choice = prompt(question)['choice']
            if user_choice == 'ADD':
                self.add_new_column()
            elif user_choice == 'DEL':
                self.remove_column()
            elif user_choice == 'EDIT':
                self.modify_column()
            elif user_choice == 'LIST':
                self.list_columns()
            else:
                break

    def add_new_column(self):
        """Add a new column to table"""
        column_name = prompt({
            'type': 'input',
            'name': 'column',
            'message': 'Input column name'
        })['column']
        # check if column name already exists
        for column in self.columns:
            if column.name == column_name:
                print("A column named %s already exists" % column_name)
                return
        # creates a column
        self.columns.append(Column(column_name))

    def remove_column(self):
        """removes a column if exists"""
        column_index = self.__input_column_index()
        if column_index is not None:
            column_name = self.columns.pop(column_index).name
            print(column_name + " is removed")
        else:
            print("No columns to remove")

    def modify_column(self):
        """removes a column if exists"""
        column_index = self.__input_column_index()
        if column_index is not None:
            print("Modifying column " + self.columns[column_index].name)
        else:
            print("No columns to modify")

    def list_columns(self):
        for column in self.columns:
            print(column.name)


class Column:
    """Creates a new column"""

    def __init__(self, name):
        self.name = name
        self.type = 'number'
        self.references = []
        self.isUnique = False

    def open_column_menu(self):
        """suggests options for modifying column"""
        while True:
            question = {
                'type': 'list',
                'name': "choice",
                'message': "What do you want to do?",
                'choices': [
                    {
                        'name': 'Edit type',
                        'value': 'EDIT',
                    },
                    {
                        'name': 'Set  unique index',
                        'value': 'UNIQ',
                    } if self.isUnique is False
                    else
                    {
                        'name': 'Remove unique index',
                        'value': 'NOTUNIQ',
                    },
                    {
                        'name': 'Go back',
                        'value': 'BACK'
                    }
                ]
            }

            user_choice = prompt(question)['choice']
            if user_choice == 'EDIT_TYPE':
                self.edit_type()
            elif user_choice == 'UNIQ':
                self.isUnique = True
            elif user_choice == 'NOTUNIQ':
                self.isUnique = False
            else:
                break

    def edit_type(self):
        """Select dataype for the column"""
        self.type = prompt([{
            'name': 'type',
            'type': 'list',
            'message': 'Please select a type from the list',
            'choices': datatypes
        }])['type']


class Reference:
    """Create foreign key"""

    def __init__(self, name, table_index, column_index):
        self.name = name
        self.table_index = table_index
        self.column_index = column_index
