from PyInquirer import prompt


class Schema:
    """Creates a schema for storing database tables"""

    def __init__(self, name="myschema"):
        self.name = name
        self.tables = []

    def __input_table_index(self):
        """ask user to select table and returns index. returns null if there is no table"""
        if self.tables:
            question = {
                'type': 'list',
                'name': 'table_index',
                'message': 'Select an Item to delete',
                'choices': [{'name': table.name, 'value': i}
                            for i, table in self.tables],
            }
            return prompt([question]).table_index

    def add_new_table(self, name):
        """Create a new table in the schema if the table name already doesn't
        exists"""
        for table in self.tables:
            if table.name == 'name':
                print("A table named %s already exisits" % name)
                return
        self.tables.append(Table(name))

    def remove_table(self, name):
        """removes a table if exists"""
        table_index = self.__input_table_index()
        if table_index:
            del self.tables[table_index]

    def modify_table(self):
        """removes a table if exists"""
        table_index = self.__input_table_index()
        if table_index:
            #self.tables[table_index].modify()
            print("Modifying table " + self.tables[table_index].name)

class Table:
    """creates a new table"""

    def __init__(self, name):
        """"creates a new table with this name"""
        self.name = name
