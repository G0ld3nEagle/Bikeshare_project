import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city= input('plz enter Chicago, Nerw York City or Washington :').lower()
        if city.title() in ['Chicago', 'New York City', 'Washington'] :
           break
        else: print('plz enter the city name correctly!')
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month= input('plz enter desired month (either all or from January to June (nums and abbrevations not accepted) :').lower()
        if month.title() in ['All'] :
           break
        elif month.title() in ['January','February','March','April','May','June'] :
             break
        else: print('plz enter the month name correctly!')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('plz enter desired day of the week (either all or from monday to sunday (nums and abbrevations not accepted) :').lower()
        if day.title() in ['All'] :
           break
        elif day.title() in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] :
             break
        else: print('plz enter the Day of the week  correctly!')

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) +1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('The most common month: ', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week: ', popular_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start to End']= 'from '+ df['Start Station'] + ' to ' + df['End Station']
    popular_Start_to_End = df['Start to End'].mode()[0]
    print('Most frequent combination of start and end station trip: \n', popular_Start_to_End)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time = df['Trip Duration'].sum()
    print('Total travel time in seconds: ', tot_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time in seconds: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types: \n', user_types)

    # TO DO: Display counts of gender
    try:
        gender_count= df['Gender'].value_counts()
        print('Counts of gender: \n', gender_count)
    except:
        print('no Gender in this city file')
    # TO DO: Display earliest, most recent, and most common year of birth
    try :
        earliest_YOB= int(df['Birth Year'].max())
        most_rescent_YOB= int(df['Birth Year'].min())
        most_common_YOB= int(df['Birth Year'].mode()[0])
        print('earliest year of birth: ', earliest_YOB)
        print('most recent year of birth: ', most_rescent_YOB)
        print('most common year of birth: ', most_common_YOB)
    except :
        print('no Birth year in this city file ')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def Raw_data(city):
    """Displays raw data on bikeshare users."""
    print('\n displaying raw data...\n')
    for chunk in pd.read_csv(CITY_DATA[city], chunksize=5) :
        print(chunk)
        Raw_data = input('\nWould you like to see 5 rows of the raw data? Enter yes or no.\n')
        if Raw_data.lower() != 'yes':
           break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        Raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
