# CrudOperations
Create a program to read command line arguments on which it will call database interactions like create, update, get or delete functionality. Databases should retain values if something is created. Duplicate data must not be created. Select the database of your choice.

Example :
 python db_interaction.py create_data 1 abc 22
Data created: 1 abc 22

 python db_interaction.py get_data abc
Data found: 1 abc 22

 python db_interaction.py create_data 1 abc 22
Data already exists in database

 python db_interaction.py update_data abc 1 abc 34
Data updated: 1 abc 34

 python db_interaction.py delete_data abc
Data deleted: 1 abc 34

 python db_interaction.py get_data abc
Data Not found.
