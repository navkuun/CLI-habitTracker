# CLI habit tracker
from cli_tables.cli_tables import * 
import time
import json

# Create new table
def create_new_table():
    time.sleep(0.1)
    print("- You have chosen to create a new table -")
    table_file_name= input("File Name : ")
    new_table = open("/c/Users/navkh/Documents/Habit_tracker/table_file_name.json", "x")
# MAIN

def main():
    print("Hello World")
    print("Let's get started, welcome to the habit tracker")
    time.sleep(0.5)
    want_to_continue = input("Continue [Y/n] ")
    while want_to_continue.lower() != 'n':
        print("Options : ")
        print("View habit tables : 1")
        print("Create a new habit table : 2")
        print("Add a new habit : 3")
        try:
            choice = int(input())
        except:
            print("Error - no choice chosen")

        if choice == 1:
            create_new_table()            
        elif choice == 2:
            print(2)
        elif choice == 3:
           print(3) 



if __name__ == "__main__":
    main()