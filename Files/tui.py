import csv


def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should consist of the title 'Solar Record Management System' surrounded by dashes.
    The number of dashes before and after the title should be equal to the number of characters in the title 
    i.e. 30 dashes before and after.

    :return: Does not return anything.
    """
    # TODO: Your code here

    #- Using "- * 30" to print the number of dashes, ive chosen this way so the code looks more clean and easy to understand.
    print("\n","-" * 30, 'Solar Record Management System', "-" * 30)


def menu():

    """
    Task 2: Display a menu of options and read the user's response.

    A menu consisting of the following options should be displayed:
    'Load Data', 'Process Data', 'Visualise Data', 'Save Data' and 'Exit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Load Data', 2 for 'Process Data' and so on.

 If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if invalid selection otherwise an integer corresponding to a valid selection
    """
    # TODO: Your code here

    print (" 1.        Load Data")
    print (" 2.        Process Data")
    print (" 3         Visualise Data")
    print (" 4.        Save Data")
    print (" 5.        Exit")

# using python if  statements and exceptions, in this way if the user enters a : "str" or "float"  the except function will  handle the error, also returns none.
    try:
        user_response = int(input("           Input option :"))

        if (user_response <=0) or ( user_response >=6):
            print (" Invalid option!")

            return()
        else:
            if user_response == 1 :
                return user_response
            if user_response == 2 :
                return (user_response)
            if user_response == 3 :
                return  user_response
            if user_response == 4 :
                return user_response
            if user_response == 5 :
                return user_response

#if the user enters anythingh else this will guide the user.
    except:
        print ("Only interger numbers allowed!")
        return()










def started(operation):
    """
    Task 3: Display a message to indicate that an operation has started.

    The function should display a message in the following format:
    '{operation} has started.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being started
    :return: Does not return anything
    """
    # TODO: Your code here

    if operation == 1 :
        operation = " Load Data"
    elif operation == 2 :
        operation = "Process Data"
    elif operation == 3 :
        operation == "Visualise Data"
    elif operation == 4 :
        operation = "Save Data"
    elif operation == 5 :
        operation = " Exit"
    print (f'{operation} has started.')
# this starts both function "started()" and "menu()"



def completed(operation):
    """
    Task 4: Display a message to indicate that an operation has completed.

    The function should display a message in the following format:
    '{operation} has completed.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being completed
    :return: Does not return anything
    """
    # TODO: Your code here

    if operation == 1:
        operation = " Load Data"
    elif operation == 2:
        operation = "Process Data"
    elif operation == 3:
        operation == "Visualise Data"
    elif operation == 4:
        operation = "Save Data"
    elif operation == 5:
        operation = " Exit"
    print(f'{operation} has completed.')



def error(error_msg):
    """
    Task 5: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter passed to this function

    :param error_msg: A string containing an error message
    :return: Does not return anything
    """
    # TODO: Your code here
    print (f'{error_msg} Error')




def source_data_path():
    """
    Task 6: Retrieve a file path to the source data file.

    The function should prompt the user to enter the file path for a data file (e.g. 'data/sol_data.csv').
    If the file path entered by the user does not end in 'csv' then a suitable error message should be displayed
    and the value None should be returned.
    Otherwise, the file path entered by the user should be returned.

    :return: None if the file path does not end in 'csv' otherwise return the file path entered by the user
    """
    # TODO: Your code here
    try:
        #absolute path of the csv file
        filepath = input(" please input filepath of csv file : ")
        with open(filepath, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                print(line)
    except:
        error(".CSV Not found")


def process_type():
    """
    Task 7: Display a menu of options for how the file should be processed. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Retrieve entity', 'Retrieve entity details', 'Categorise entities by type',
        'Categorise entities by gravity', 'Summarise entities by orbit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Retrieve entity', 2 for 'Retrieve entity details' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    print(" 1.        Retrieve entity")
    print(" 2.        Retrieve entity details")
    print(" 3         Categorise entities by type")
    print(" 4.        Categorise entities by gravity")
    print(" 5.        Summarise entities by orbit")

    try:
        user_response = int(input("           Input option :"))
        if user_response == 1:
            return user_response
        if user_response == 2:
            return user_response
        if user_response == 3:
            return user_response
        if user_response == 4:
            return user_response
        if user_response == 5:
            return user_response
    except:
        error("Invalid option")
        return


def entity_name():
    """
    Task 8: Read in the name of an entity and return the name.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should then read in and return the user's response.

    :return: the name of an entity
    """
    # TODO: Your code here
    entity = input("Please enter the name of the Entity : ")
    return entity

def entity_details():
    """
    Task 9: Read in the name of an entity and column indexes. Return a list containing the name and indexes.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should also ask the user to enter a list of integer column indexes e.g. 0,1,5,7
    The function should return a list containing the name of the entity and the list of column
    indexes e.g. ['Earth', [0,1,5,7]]

    :return: A list containing the name of an entity and a list of column indexes
    """
    # TODO: Your code here
    entity = input("Please enter the name of an entity : ")
    column = input("Please enter a list of integer colum indexes : ")
    return [entity,column]

def list_entity(entity, cols=[]):
    """
    Task 10: Display an entity. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the entity will be displayed.

    The entity is a list of values corresponding to particular Solar System space entity
    E.g. ['Earth', TRUE, 9.8].
    The function should only display those values from the entity list that correspond to the column
    indexes provided as part of cols.
    E.g. if cols is [0, 2] then for the entity ['Earth', TRUE, 9.8] the following will be displayed
    ['Earth', 9.8]
    E.g. if cols is an empty list then all the values will be displayed i.e. ['Earth', TRUE, 9.8]

    :param entity: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: does not return anything
    """
    # TODO: Your code here
    if cols is None:
        cols = []
    if len(cols) == 0:
        print(entity)
    else:
        display = []
        for col in cols:
            display.append(entity[col])
            print(display)



def list_entities(entities, cols = None):


    # TODO: Your code here
    if cols is None:
        cols =[]
    for entity in entities:
        list_entity(entity,cols)


def list_categories(categories: dict):
    """
    Task 12: Display the contents of the dictionary categories.

    The function should take a single parameter categories which is a dictionary containing category names
    and a list of entities that belong to the category.

    You will need to add the parameter categories to the function definition.

    :param categories: A dictionary containing category names and a list of entities that are part of that category
    :return: Does not return anything
    """
    # TODO: Your code here

    for name,entities in categories.items():
        print(name)
        list_entities(entities)



def gravity_range():
    """
    Task 13: Ask the user for the lower and upper limits for gravity and return a tuple containing the limits.

    The function should prompt the user to enter the lower and upper limit for a range of values related to gravity.
    The values will be floats e.g. 5.1 for lower limit and 9.8 for upper limit.
    The function should return a tuple containing the lower and upper limits

    :return: a tuple with the lower and upper limits
    """
    # TODO: Your code here

    lower = float(input("Please enter the lower limits for the gravity : "))
    upper = float(input("Please enter the lower limits for the gravity : "))

    return lower,upper




def orbits():
    """
    Task 14: Ask the user for a list of entity names and return the list.

    The function should prompt the user to enter a list of entity names e.g. Jupiter,Earth,Mars
    The list represents the entities that should be orbited.
    The user may enter as many entity names as they desire.
    The function should return a list of the entity names entered by the user.

    :return: a list of entity names
    """
    # TODO: Your code here
    #list =input("Pease enter a list of entity names e.g. Jupiter,Earth,Mars : ").split(",")
    #print (list)
    return input("Pease enter a list of entity names e.g. Jupiter,Earth,Mars : ").split(",")



def visualise():
    """
    Task 15: Display a menu of options for how the data should be visualised. Return the user's response.

    A menu should be displayed that contains the following options:
        'Entities by type', 'Entities by gravity', 'Summary of orbits', 'Animate gravities'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Entities by type', 2 for 'Entities by gravity' and so on.

    If the user enters an invalid option, then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here


    print(" 1.        Entities by type'")
    print(" 2.        Entities by gravity")
    print(" 3         Summary of orbits")
    print(" 4.        Animate gravities")

    try:

        user_response = int(input("           Input option :"))
        if user_response == 1:
            return user_response
        if user_response == 2:
            return user_response
        if user_response == 3:
            return user_response
        if user_response == 4:
            return user_response
        if user_response != 1 or 2 or 3 or 4:
            error("Invalid option")

    except: # if user enters a letter or symbol this will handle the error guiding the user.

        error("Invalid option")
        return ()




def save():

    """
    Task 16: Display a menu of options for how the data should be saved. Return the user's response.

    A menu should be displayed that contains the following option:
         'Export as JSON'

    The user's response should be read in and returned as an integer corresponding to the selected option.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here

    print(" 1.        Export as JSON")
    try:
        user_response = int(input("           Select how the data should be saved : ")).strip()
        if user_response == 1:
            return user_response

        if user_response != 1:
            print("Invalid option")
            return ()

    except:
        error("Invalid option")  # calling the function from task 5
        return ()



