import pandas as pd
import numpy as np
import prompts

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

valid_months = ["all", "january", "february", "march", "april", "may", "june"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = prompts.prompt_for_city()
    month = prompts.prompt_for_month(valid_months)
    day = prompts.prompt_for_day()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
    df["hour"] = df["Start Time"].dt.hour
    df["Trip"] = df["Start Station"] + " to " + df["End Station"]

    # filter by month if applicable
    if month != "all":
        # use the index of the months list to get the corresponding int
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df["month"] == month]

    # filter by day of week if applicable
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # Display the most common month
    month_int = df["month"].mode()[0]
    most_common_month = valid_months[month_int].title()
    print("The most common month is " + str(most_common_month))

    # Display the most common day of week
    most_common_day = df["day_of_week"].mode()[0]
    print("The most common day is " + str(most_common_day))

    # Display the most common start hour
    most_common_hour = df["hour"].mode()[0]
    print("The most common hour is " + str(most_common_hour))

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    # Display most commonly used start station
    most_common_start_station = df["Start Station"].mode().values[0]
    print("The most common start station is " + str(most_common_start_station))

    # Display most commonly used end station
    most_common_end_station = df["End Station"].mode().values[0]
    print("The most end station is " + str(most_common_end_station))

    # Display most frequent combination of start station and end station trip
    most_common_trip = df["Trip"].mode().values[0]
    print("The most common trip is " + str(most_common_trip))

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    # Display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time is " + str(total_travel_time))

    # Display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean travel time is " + str(mean_travel_time))

    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    # Display counts of user types
    print("User Type Counts:")
    print(df["User Type"].value_counts())
    print()

    # Washington doesn't have gender or birth year data
    if city != "washington":
        # Display counts of gender
        print("Gender Counts:")
        print(df["Gender"].value_counts())
        print()

        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = df["Birth Year"].min()
        print("The earliest birth year is " + str(earliest_birth_year))

        latest_birth_year = df["Birth Year"].max()
        print("The most recent birth year is " + str(latest_birth_year))

        most_common_birth_year = df["Birth Year"].mode().values[0]
        print("The most common birth year is " + str(most_common_birth_year))

    print('-'*40)


def display_raw_data(df):
    """
    Prompts the user for whether to display raw data and displays the
    raw data 5 lines at a time if the user says yes

    Args:
        (pandas.DataFrame) df - The raw data to display
    """

    user_input = prompts.prompt_for_raw_data()

    start_index = 0
    end_index = 5

    num_rows = df.shape[0]

    while user_input == "yes":
        print(df.iloc[start_index:end_index])
        start_index += 5
        end_index += 5

        if start_index > num_rows:
            print("We have reached the end of the raw data!")
            break

        user_input = prompts.prompt_for_raw_data(True)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no: ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
