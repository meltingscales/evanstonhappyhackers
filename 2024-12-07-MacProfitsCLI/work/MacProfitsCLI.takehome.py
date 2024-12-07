# function ideas:
import numpy as np
import pandas as pd

# get_string(message)->string: Ask the user for a message from stdout

# read_csv(path)->DataFrame: Get a file from a path and return a Pandas dataframe.

# unit_tests()->None: Run unit tests on above functions to test them.

if __name__ == "__main__":

    # data we care about:
    # a list of:
    # 1. "macbook_cost" - macbook cost
    # 2. "harvested_part_value" - how much the parts I can harvest from this macbook are worth
    # 3. "resale_value" - how much I can resell the macbook for
    # 4. "overhead" - monthly/weekly, how much overhead


    # step 1: ask the user if they want to read in a file, or enter data

    print("Welcome to our macbook repair profit calc.")
    print("1 - Open a CSV file")
    print("2 - Enter data")

    myvar = input(" > ")

    print(myvar)

    if myvar == '1':
        print("TODO")
        exit(1)
        # load a CSV file into a pandas dataframe
    elif myvar == '2':
        # enter data manually

        # ask them how many macbooks they're going to repair
        numMacbooks = input("Number of macbooks to repair > ")
        numMacbooks = int(numMacbooks)


        my_data = []

        for macbook_id in range(0, numMacbooks):
            # loop over 3 (ex) times

            print("You're now entering data for macbook "+str(macbook_id))
            macbook_cost = input("macbook_cost > ")
            harvested_part_value = input("harvested_part_value > ")
            resale_value = input("resale_value > ")

            # single row, i.e. in an excel spreadsheet
            single_data = [
                macbook_id,
                macbook_cost,
                harvested_part_value,
                resale_value,
            ]

            # add our row to all our rows
            my_data.append(single_data)

        # outside of the for loop, we need to put it into a pandas dataframe
        # print(numMacbooks)
        from pprint import pprint
        pprint(my_data)

        data = np.array(my_data)

        # Create a DataFrame from the array
        df = pd.DataFrame(data, columns=['macbook_id', 'macbook_cost', 'harvested_part_value', 'resale_value'])

        print(df)

        # step 3: for loop: calculate gross profits for each repair and re-store it in each dataframe row. like an excel spreadsheet

        


    else:
        print("Invalid choice")

    ## step 1.1: If they want to read in a file, load in into a Pandas dataframe
    ## step 1.2: If they want to enter data, repeatedly ask them for data, and load it one-by-one into a pandas dataframe

    # step 2: put all of the data into a Pandas Dataframe

    # step 3: for loop: calculate gross profits for each repair and re-store it in each dataframe row. like an excel spreadsheet

    # step 4: plot the dataframe into a pyplot window

    # step 5: if we didn't load it from a CSV file, we should save our pandas dataframe to a CSV file.