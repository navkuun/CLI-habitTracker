# CLI habit tracker
from cli_tables.cli_tables import * 
import time
import re
import json
import os

# Create new table
def create_new_table():
    time.sleep(0.1)
    print("- You have chosen to create a new table -")
    table_file_name = input("Table name : ")
    OUTPUT_DIR = os.getcwd()
    f = open(os.path.join(OUTPUT_DIR, f'{table_file_name}.json'), 'w')
    f.close()
    width = int(input("How many days do you want to track use this table ? :"))
    string_habits = input("Please enter a list of habits, seperated by a comma : ")
    list_habits =  string_habits.split(',')
    # habits_store = {}
    # for habit in list_habits:
    #     for i in range(1,width+1):
    #         habits_store[habit][i] = ' '

    fields = ['Habits']
    records = [[]] 
    for habit in list_habits:
        records.append(habit)
    for i in range(1,width+1):
        fields.append(i)

    print_table(fields, records)


    
    

    


# Delete a table
def delete_table():
    time.sleep(0.1)
    print("- You have chosen to delete a table -")
    table_file_name = input("Enter table name, to remove : ")
    path = os.getcwd()
    directories = os.listdir(path) # list of file names

    for file in directories:
        match = re.search("\.json$", file)
        if match:                
            full_path = os.path.join(path, file)
            os.remove(full_path)


# MAIN

def main():
    print("Let's get started, welcome to the habit tracker")
    time.sleep(0.5)
    want_to_continue = input("Start program [Y/n] ")
    while want_to_continue.lower() != 'n':
        print("Options : ")
        print("Create a new habit table : 1")
        print("Delete a table : 2")
        print("View habit tables : 3")
        print("Add a new habit : 4")

        try:
            choice = int(input())
        except:
            print("Error - no 'valid' choice chosen")

        if choice == 1:
            create_new_table()            
        elif choice == 2:
            delete_table()
        elif choice == 3:
           print(3) 

        want_to_continue = input("Continue [Y/n] ")


if __name__ == "__main__":
    main()