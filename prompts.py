def prompt_for_city():
    """
    Asks user to specify a city to analyze.

    Returns:
        (str) city - name of the city to analyze
    """

    valid_cities = ["chicago", "new york city", "washington"]
    while True:
        city = input("Enter a city to analyze (Chicago, New York City, or Washington): ").lower()
        if city in valid_cities:
            return city
        else:
            print("Invalid city entered.\n")

def prompt_for_month(valid_months):
    """
    Asks user to specify a month to filter on.

    Returns:
        (str) month - month to filter on
    """

    while True:
        month = input("Enter a month to filter on (All, January, February, March, April, May or June): ").lower()
        if month in valid_months:
            return month
        else:
            print("Invalid month entered.\n")

def prompt_for_day():
    """
    Asks user to specify a day to filter on.

    Returns:
        (str) day - day to filter on
    """

    valid_days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    while True:
        day = input("Enter a day to filter on (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday): ").lower()
        if day in valid_days:
            return day
        else:
            print("Invalid day entered.\n")

def prompt_for_raw_data(is_continue=False):
    """
    Prompts the user for whether to display raw data

    Args:
        (bool) is_continue - Whether this is a continuation prompt
    """

    print()

    input_question = ""
    if is_continue:
        input_question = "Would you like to continue? Enter yes or no: "
    else:
         input_question = "Would you like to view the raw data? Enter yes or no: "

    while True:
        user_input = input(input_question).lower()
        if user_input in ["yes", "no"]:
            return user_input
        else:
            print("Invalid entry. Enter yes or no")