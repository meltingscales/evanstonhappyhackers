# function ideas:

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

    pass
    # step 1: ask the user if they want to read in a file, or enter data
    ## step 1.1: If they want to read in a file, load in into a Pandas dataframe
    ## step 1.2: If they want to enter data, repeatedly ask them for data, and load it one-by-one into a pandas dataframe

    # step 2: put all of the data into a Pandas Dataframe

    # step 3: for loop: calculate gross profits for each repair and re-store it in each dataframe row. like an excel spreadsheet

    # step 4: plot the dataframe into a pyplot window

    # step 5: if we didn't load it from a CSV file, we should save our pandas dataframe to a CSV file.