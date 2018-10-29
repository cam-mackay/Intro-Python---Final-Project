#campbell_finalProject_draft
#author <Campbell Mackay>
#latest revision date <28 October 2018>
#Weather Data by Location Application
#for Intro Python Course

#uses the requests library to request data from the webservice
#will need to install the module
#import requests

#----------Functions----------#

#displays a welcome message to the user upon initial startup of the application
def welcome_user():
    print("Welcome to the Weather Data by Location Application")
    print("")

#gets the search parameter from the user to be used in the webservice query
def get_search_parameter():
    searchParameter = ""
    while searchParameter != "zip" and searchParameter != "city":
        print("-----------------------------------------------------------")
        print("Would you like to search by zip code or city? (zip or city)")
        searchParameter = input("")
    if searchParameter == "zip":
        return 1
    elif searchParameter == "city":
        return 2

#gets the zip code from the user after zip is chosen as search parameter
#need to implement data validation in final draft; need to figure out the format the API requires
def get_user_zip():
    zipCode = input("Enter a zip code to search: ")
    return zipCode

#gets the city name from the user after city is chosen as search parameter
#need to implement data validation in final draft; need to figure out the format the API requires
def get_user_city():
    cityName = input("Enter a city name to search: ")
    return cityName

#attempts to connect to API and search using a zip code
#will build for final draft after better understanding of API over coming weeks
def connect_api_zip(searchZip):
    print("Requesting connection to http://openweathermap.org... ")

#attempts to connect to API and search using a city name
#will build for final draft after better understanding of API over coming weeks
def connect_api_city(searchCity):
    print("Requesting connection to http://openweathermap.org... ")

#converts whatever file format (JSON/CSV) the API returns to readable text for the user
#will build for final draft
def display_search_results():
    print("Displaying search results... ")
    print("")

#prompts the user if they want to search again using a different parameter
def search_again():
    searchAgain = ""
    while searchAgain != "yes" and searchAgain != "no":
        print("-----------------------------------------------------------")
        print("Would you like to search again? (yes or no)")
        searchAgain = input("")
    if searchAgain == "yes":
        print("New search...")
        print("")
        return 1
    elif searchAgain == "no":
        print("Closing program...")
        print("")
        return 0




#-------------Main-------------#
    
welcome_user()

searchLoop = 1
while searchLoop == 1:

    connectionGood = "unknown"
    locationParameter = get_search_parameter()

    if locationParameter == 1:
        userZip = get_user_zip()
        try:
            connect_api_zip(userZip)
            connectionGood = "yes"
        except:
            print("An error has occurred while trying to connect to API")
        
    elif locationParameter == 2:
        userCity = get_user_city()
        try:
            connect_api_city(userCity)
            connectionGood = "yes"
        except:
            print("An error has occurred while trying to connect to API")

    if connectionGood == "yes":
        display_search_results()

    searchLoop = search_again()
