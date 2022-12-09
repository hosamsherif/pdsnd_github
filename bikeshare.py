import time
import pandas as pd
import numpy as np

"""Dataset description: The dataset consists of three different cities in USA which are new york, chicago and
washington , where each city has a csv file containing its information """

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
        print("Would you like to look for which data Chicago , New York City or Washington")
        city = input("Please enter the name of the city to analyze: \n").lower().strip()
        try:
            pd.read_csv(CITY_DATA[city])
            break
        except:
            print("Invalid city!, Please enter the name of the city as one of the names I mentioned and try again\n") 

    # TO DO: get user input for month (all, january, february, ... , june)
    List_of_months=['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month= input("""Please enter the name of the month from these following months ['January', 'February', 'March', 'April', 'May', 'June'] to filter by, or 'all' to apply no month filter: \n""").lower().strip()
        if month in List_of_months or month=='all':
            break
        else:
           print("Invalid Month!, Please enter the name of the month as one of the names I mentioned and try again\n")  
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    List_of_days=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']
    
    while True:
        day= input("Please enter the name of the day of week from these following days ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday']to filter by, or 'all' to apply day filter: \n").lower().strip()
        if day in List_of_days or day=='all':
            break
        else:
           print("Invalid Day!, Please enter the name of the day as one of the names I mentioned and try again\n")  
        
        
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month    
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
    #df['day_of_week'] = df['Start Time'].dt.dow
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = [i+1 for i,m in enumerate(months) if m==month][0]
        #print(df['month'])
        # filter by month to create the new dataframe
        #print(df.count())
        #df.loc[df['month'] == month]
        df=df[df['month']==month]
        #print(df.count())
    # filter by day of week if applicable
    if day != 'all':
        df=df[df['day_of_week']==day.capitalize()]
        # filter by day of week to create the new dataframe

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel based on the filters determined by the used input."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
   
    # TO DO: display the most common month
 

    print("The most common month is: {}".format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("The most common day of week is: {}".format(df['day_of_week'].mode()[0])) 

    # TO DO: display the most common start hour
    print("The most common Start hour is: {}".format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station    
    print("The most common Start Station used is: {}".format(df['Start Station'].mode()[0]))
    
    # TO DO: display most commonly used end station    
    print("The most common End Station used is: {}".format(df['End Station'].mode()[0]))
    
    # TO DO: display most frequent combination of start station and end station trip
    Start_End_common_station=df.groupby(['Start Station','End Station']).size().idxmax()
    
    Start_End_common_station_str="'{}' , '{}'".format(Start_End_common_station[0],Start_End_common_station[1])
    print("The most common combination of Start Station and End Station trip is: {}".format(Start_End_common_station_str)) 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    print("The total travel time is: {}".format(df['Trip Duration'].sum())) 

    # TO DO: display mean travel time
    print("The average travel time is: {}".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, Is_Washignton):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_types_counts=df['User Type'].value_counts().values
    User_types=df['User Type'].value_counts().index.tolist()       
    for name, count in zip(User_types,User_types_counts):
              print("The count of {} is: {}  ".format(name,count))

    # TO DO: Display counts of gender
    if Is_Washignton==1:
        print("No Gender and Birth Year Data provided for Washignton")
        return
    
    Gender_counts=df['Gender'].value_counts().values
    Genders=df['Gender'].value_counts().index.tolist()
    for name, count in zip(Genders,Gender_counts):
              print("The count of {} is: {}  ".format(name,count))

    # TO DO: Display earliest, most recent, and most common year of birth
    print("The Earliest year of birth is: {}".format(df['Birth Year'].min()))
    print("The most recent year of birth is: {}".format(df['Birth Year'].max()))
    print("The most common year of birth is: {}".format(df['Birth Year'].mode()[0]))
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displaying 5 rows upon the user request"""
    view_data_choice = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no\n").lower().strip()
    index=0
    while(view_data_choice=='yes'):
        if index+5>len(df):
            print(df.iloc[index:])
            print("There are no more data to show\n")
            break
        print(df.iloc[index:index+5])
        index+=5
        view_data_choice=input("Do you want to see the next 5 rows? Enter yes or no\n").lower().strip()
       
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        df.drop(df.columns[0],axis=1,inplace=True)  # as this column has no name and we will not use it in our computations nor filters
      
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if(city=='washington'):
            user_stats(df,1)
        else:
            user_stats(df,0)
        
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
