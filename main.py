# imports
from cli_tables.cli_tables import * 
import time
import re
import csv 
import os

# Create new table
def create_new_table():
    time.sleep(0.1)
    print("- You have chosen to create a new table -")
    table_file_name = input("Table name : ")
    OUTPUT_DIR = os.getcwd()
    f_path = open(os.path.join(OUTPUT_DIR, f'{table_file_name}.csv'), 'w')
    f_path.close()
    width = int(input("How many days do you want to track use this table ? :"))
    string_habits = input("Please enter a list of habits, seperated by a comma : ")
    list_habits =  string_habits.split(',')

    # creating the header - can be thought of as the fields 
    header = ['Habits']
    for i in range(1, width):
        header.append(f"Day {i}")

    # creating records
    data = []
    for habit in list_habits: 
        data.append([habit])

    for i in range(len(list_habits)):
        for j in range(width):
            data[i].append(' ')

    # writing data and header to path 
    string_full_path = os.path.join(OUTPUT_DIR, f'{table_file_name}.csv')
    with open(string_full_path, 'w') as work:
        z = csv.writer(work)
        z.writerow(header)
        z.writerows(data)

    print(f"- creation of the {table_file_name} table successful-")
    

    
# Delete a table
def delete_table():
    time.sleep(0.1)
    print("- You have chosen to delete a table -")
    table_file_name = input("Enter table name, to remove : ")
    path = os.getcwd()
    directories = os.listdir(path) # list of file names

    for file in directories:
        match = re.search("\.csv$", file)
        if match:                
            full_path = os.path.join(path, file)
            os.remove(full_path)

def display_table():
    print("- you have chosen to display a table -") 
    table_name = input("Please enter your table name : ")

    print("You have choose multiple views :") 
    print("For GUI(pretty) view select: 1")
    print("For CLI(normal) view select: 2")
    choice = int(input())
    if choice == 1: 
        pass  # to do 
    else:
        try:
            file_csv = open(f"{table_name}.csv")
        except:
            print("error - no table of that name found ")
            pass

        data_csv = csv.reader(file_csv)
        list_csv = list(data_csv)
        print(list_csv)

    

# main 
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
            display_table()
        want_to_continue = input("Continue [Y/n] ")


if __name__ == "__main__":
    main()
