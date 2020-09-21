from json import load as json_loader

from PyInquirer import prompt

with open('datatypes_faker.json') as datatype_file:
    datatypes = json_loader(datatype_file)


class DBItems:
    def input_unique_obj_index(self, ls_name):
        """Get column index from prompt"""
        if getattr(self, ls_name):
            question = {
                'type': 'list',
                'name': 'table_index',
                'message': 'Select an %s from the list' % ls_name[:-1],
                'choices': [{'name': obj.name, 'value': index}
                            for index, obj in enumerate(getattr(self, ls_name))],
            }
            return prompt([question])['table_index']

    def check_duplicate_name_item(self, ls_name, name):
        for item in getattr(self, ls_name):
            if item.name == name:
                print("A table named %s already exists" % name)
                return True
        return False


class Schema(DBItems):
    """Creates a schema for storing database columns"""

    def __init__(self, name="myschema"):
        super().__init__()
        self.name = name
        self.tables = []
        self.references = []

    def open_schema_menu(self):
        """Access to db functions from this menu"""
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
                        'name': 'Add a new reference',
                        'value': 'ADDR',
                    },
                    {
                        'name': 'Remove a reference',
                        'value': 'DELR',
                    },
                    {
                        'name': 'List Reference',
                        'value': 'LISTR',
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
                self.generate()
            elif user_choice == 'ADD':
                self.add_new_table()
            elif user_choice == 'DEL':
                self.remove_table()
            elif user_choice == 'EDIT':
                self.modify_table()
            elif user_choice == 'LIST':
                self.list_tables()
            elif user_choice == 'LISTR':
                self.list_reference()
            else:
                print("Good bye for now. See you again!")
                break

    def add_new_table(self):
        """Create a new table in the schema"""
        # input table name
        answer = prompt([
            {
                'type': 'input',
                'name': 'table',
                'message': 'Input table name'
            },
            {
                'type': 'confirm',
                'name': 'is_id_included',
                'message': 'Do you want to include an id field?'
            }]
        )

        table_name = answer['table']
        # check if table name already exists
        if self.check_duplicate_name_item('tables', table_name):
            print("Table already exists with this name")
            return
        # creates a table
        self.tables.append(Table(table_name, answer['is_id_included']))

    def remove_table(self):
        """removes a table if exists"""
        table_index = self.input_unique_obj_index('tables')
        if table_index is not None:
            table_name = self.tables.pop(table_index).name
            print(table_name + " is removed")
        else:
            print("No tables to remove")

    def modify_table(self):
        """modify a table if exists"""
        table_index = self.input_unique_obj_index('tables')
        if table_index is not None:
            print("Modifying table " + self.tables[table_index].name)
        else:
            print("No tables to modify")

    def add_new_reference(self):
        """Create a new  reference in the schema"""
        # input reference name
        reference_name = prompt({
            'type': 'input',
            'name': 'reference',
            'message': 'Input reference name'
        })['reference']
        # check if reference name already exists
        if self.check_duplicate_name_item('references', reference_name):
            print("Reference already exists with this name")
            return
        # creates a reference
        print("Source")
        src_tbl_idx = self.input_unique_obj_index('tables')
        src_col_idx = self.tables[src_tbl_idx].input_unique_obj_index('columns')
        print("Reference")
        ref_tbl_idx = self.input_unique_obj_index('tables')
        ref_col_idx = self.tables[ref_tbl_idx].input_unique_obj_index('columns')

        self.references.append(Reference(
            reference_name,
            src_tbl_idx,
            src_col_idx,
            ref_tbl_idx,
            ref_col_idx
        ))

    def remove_reference(self):
        """removes a reference if exists"""
        reference_index = self.input_unique_obj_index('references')
        if reference_index is not None:
            reference_name = self.references.pop(reference_index).name
            print(reference_name + " is removed")
        else:
            print("No references to remove")

    def generate(self):
        print("generating fake data")

    def list_tables(self):
        for table in self.tables:
            table.describe()

    def list_reference(self):
        for ref in self.references:
            ref.describe()


class Table(DBItems):
    """creates a new column"""

    def __init__(self, name, is_id_included):
        super().__init__()
        self.name = name
        self.columns = []
        self.is_id = is_id_included
        self.open_table_menu()

    def describe(self):
        print(self.name + " id: " + str(self.is_id) +
              " columns: " + len(self.columns))

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
        if self.check_duplicate_name_item('columns', column_name):
            print("Column already exists with this name")
            return
        # creates a column
        self.columns.append(Column(column_name))

    def remove_column(self):
        """removes a column if exists"""
        column_index = self.input_unique_obj_index('columns')
        if column_index is not None:
            column_name = self.columns.pop(column_index).name
            print(column_name + " is removed")
        else:
            print("No columns to remove")

    def modify_column(self):
        """modify a column if exists"""
        column_index = self.input_unique_obj_index('columns')
        if column_index is not None:
            print("Modifying column " + self.columns[column_index].name)
        else:
            print("No columns to modify")

    def list_columns(self):
        for column in self.columns:
            print(column.name)


class Column:
    """Creates a new column"""
    type: str

    def __init__(self, name):
        self.name = name
        self.isUnique = False
        self.edit_type()

    def describe(self):
        """describe a column"""
        print(self.name +
              " unique: " + str(self.isUnique) +
              " type: " +
              [dtype.name for dtype in datatypes
               if dtype.value == self.type][0])

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
        """Select datatype for the column"""
        self.type = prompt([{
            'name': 'type',
            'type': 'list',
            'message': 'Please select a type from the list',
            'choices': datatypes
        }])['type']


class Reference:
    """Create foreign key"""

    def __init__(self, name,
                 src_tbl_idx, src_col_idx,
                 ref_tbl_idx, ref_col_idx):
        self.name = name
        self.src_tbl_idx = src_tbl_idx
        self.src_col_idx = src_col_idx
        self.ref_tbl_idx = ref_tbl_idx
        self.ref_col_idx = ref_col_idx

    def describe(self):
        """describe a reference"""
        print(self.name +
              "%s.%s => %s.%s" % self.src_tbl_idx % self.src_col_idx
              % self.ref_tbl_idx % self.ref_col_idx)
