#Level 1 - Task 19 - Capstone Project 2 - Files
from datetime import date

username = input("Enter your username: ")
password = input("Enter your password: ")
# Read the user data text file and store the username and password in user_list
user_list = []
with open('user.txt', 'r') as f:
    for line in f.readlines():
        info = line.strip().split(", ")
        user_list.append(info)

# Stack overflow helped me figure out how to store the data into a dictionary
# The user details in position 0 will be paired with the user details in position 1 from the user_list
# This will be saved in the database dictionary
database = {}
for user_details in user_list:
    database[user_details[0]] = user_details[1]

logged_in = False
# daniweb.com helped me figure out how to structure my while loop
# Only users saved in the database with verified usernames and passwords can log in 
while(username != database.keys() and password != database.get(username)):
    print("Sorry, username and/or password is incorrect. Try again")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
   
else:
    print(f"\nWelcome {username}\n")
    logged_in = True 
# If you have logged in as an admin, your menu will include a statistics option
# You will also be able to register new users
# If the user is not admin your menu will not show statistics and won't let you register a new user
while logged_in == True:
    if username == 'admin':
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
s - View statistics
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user (Admin Only)
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()
         
    # If the user selects 'r' from the menu, as an admin you will be able to register a new user
    if menu == 'r':
        if username == 'admin':
            # Enter the username and password of the new user
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            #confirm the password again
            password_confirm = input("Enter your password again: ")
            #if the password matches write the new user's details into the 'user.txt' file
            if new_password == password_confirm:
                with open('user.txt', 'a') as f1:
                    f1.write(f"\n{new_username}, {new_password}")
                print(f"\n{new_username} has been registered successfully!\n")        
            else:
                # Error message displayed if password does not match
                print("\nYour password does not match. Try again\n")
        else:
             # non admin users will get error message
            print("\nYou are not Admin. You cannot register a user!\n")

    # If the user selects 'a' they will be asked to provide details for the task to be added to 'tasks. txt'
    elif menu == 'a':
        # The username can only be stored if it is already in the database 
        username = input("Enter username of task owner: ")
        while username not in database.keys():
            print(" \nThat username is not registered. Try again\n")
            username = input("Enter username of task owner: ")
        # Additional information will be request once the username is verified
        else:
            title = input("Enter the title of the task: ")
            description = input("Describe the task: ")
            due_date = input("Enter the task due date(d m Y): ")
            current_date = date.today().strftime("%d %b %Y")
            task_complete = 'No'
            with open('tasks.txt', 'a') as f2:
                f2.write(f"\n{username}, {title}, {description}, {current_date}, {due_date}, {task_complete}")

    # All tasks saved in 'tasks.txt' will be displayed to the user when 'va' is selected
    # The data(info) is split according to the heading in the table
    elif menu == 'va':
  
        with open('tasks.txt', 'r') as f3:
           for line in f3.readlines():
               info1 = line.strip().split(", ")
               print(f'''
   ________________________________________________________________________________________

    Task:               {info1[1]}
    Assigned to:        {info1[0]}
    Date assigned:      {info1[3]}
    Due date:           {info1[4]}
    Task Complete?      {info1[5]}
    Task description:
    {info1[2]}
        ''')
    # Only the tasks saved in 'tasks.txt' for the username provided will be displayed
    # The data(info) is split according to the heading in the table
    elif menu == 'vm':
        
        with open('tasks.txt', 'r') as f4:
            for line in f4.readlines():
                info2 = line.strip().split(", ")
                if username == info2[0]:
                    print(f'''
   ____________________________________________________________________________________

    Task:               {info2[1]}
    Assigned to:        {info2[0]}
    Date assigned:      {info2[3]}
    Due date:           {info2[4]}
    Task Complete?      {info2[5]}
    Task description:
    {info2[2]}
        ''')
    # On the admin menu statistics for number of tasks and users will be displayed                 
    elif menu == 's':
        user_count = len(database)
        with open("tasks.txt", 'r') as f5:
            task_count = len(f5.readlines())
                
            print(f'''
  ______________________________________________
    Total number of users:     {user_count}
    Total number of tasks:     {task_count}
  ______________________________________________\n
  ''')
    # To exit the program select 'e' on the menu                      
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    # Selection not shown on the menu will receive an error message
    else:
        print("\nYou have made a wrong choice, Please Try again\n")
