import random
import datetime
import requests

#This function is to print the menu
def menu():
  print("1. Play Game")
  print("2. Date and Time")
  print("3. Weather ")
  print("4. Define")
  print("5. Calculate")
  print("6. Exit")

#This function is to show the menu as well as to get the command from user
def show_menu():
   while True:
    menu()
    print("ZORO: Waiting For Your Command....")
    Command = input("ZORO: Ente Your command:\n").lower()
    if Command == '1' or Command == 'Game':
      print('ZORO: Please Choose the Game')
      choose_game()
      break
    elif Command == '2' or Command == 'Date' or Command == 'Time':
      date_time()
      
    elif Command == '3' or Command == 'Weather':
      weather()
      get_werather_again()
      break
    elif Command == '4' or Command == 'Define':
      definition()
      get_definition_again()
      break
    elif Command == '5' or Command == 'Calculate':
      calculation()
      calculate_again()
      break
    elif Command == '6' or Command == 'Exit' or Command == 'Quit' or Command =='Bye':
      exit()
      break
    else:
      print('ZORO: Oops! Your Entered the Invalid Option')

#This function is used to exit the code
def exit():
  print('ZORO: Bye! It was nice talking with you.')
  print('ZORO: See You Soon!')

#This function ask user to choose the game
def choose_game():
  while True:
    print('1. Number Game')
    print('2. Word Game')
    print('3. Go Back To the Menu')
    command = input("ZORO: Ente the Command:\n")
    if command == '1':
      number_game()
      break
    elif command == '2':
      word_game()
      break
    elif command == '3':
      show_menu()
      break
    else:
      print("ZORO: Oops! Your Entered the Invalid Option")

#This function plays the number game
def number_game():
  print('ZORO: Welcome To the Number Game')
  print('ZORO: I have Hidden the Treasure in the Vault.')
  print('ZORO: You Must Enter the Code to Open the Vault')
  vault_key = random. randint(1,10)
  print(f'{vault_key}')
  
  while True:
    command = input("ZORO: Enter the Code:\n")
    if command.lower() == 'exit':
      print("ZORO: Lets Play Again Soon")
      break
    elif command.isdigit():
      command = int(command)
      if command == vault_key:
        print("ZORO: Hurray!! You're Treasure is Here\n")
        play_again_number_game()
        break
      else: 
        print('ZORO: Oops! Wrong Code')
    else:
      print("ZORO: Oops! Invalid Input")

#This function ask the user to if they want to play number game again?
def play_again_number_game():
  print("ZORO: Do You Want to Play Again?")
  print("1. Play Again")
  print('2. Go Back to Menu')
  print('3. Go Back to the Game Choose Menu')
  print('4. Exit')
  command = input("ZORO: Please Enter Your Command:\n")
  while True:
    if command == '1':
      number_game()
    elif command == '2':
      show_menu()
    elif command == '3':
      choose_game()
    elif command == '4':
      exit()
      break
    else:
      print("ZORO: Please Enter the Valid Input")

#Thsi funciton plays the word game
def word_game():
  print("ZORO: Welcome to The Word Game")
  print("ZORO: I have Hidden the Fruit. If You Guess the Name of it, I Will Give it To You")
  fruits = ['apple', 'mango', 'banana', 'kiwi', 'orange', 'gauva', 'pineapple']
  secret = random.choice(fruits)
  print(f'{secret}')

  while True:
    choice = input('ZORO: Enter the Fruit Name:\n').lower()
    if choice == secret:
      print("ZORO: Hurray! Here's Your Fruit\n")
      play_again_word_game()
      break
    elif choice == 'exit':
      exit()
      break
    else:
      print('ZORO: Oops! Wrong Guess')

#This function ask the user to if they want to play word game again?
def play_again_word_game():
  print("ZORO: Do You Want to Play Again?")
  print("1. Play Again")
  print('2. Go Back to Menu')
  print('3. Go Back to the Game Choose Menu')
  print('4. Exit')
  command = input("ZORO: Please Enter Your Command:\n")
  while True:
    if command == '1':
      word_game()
    elif command == '2':
      show_menu()
    elif command == '3':
      choose_game()
    elif command == '4':
      exit()
      break
    else:
      print("ZORO: Please Enter the Valid Input")

#This function show the date and time
def date_time():
  date = datetime.datetime.now().strftime("%Y-%m-%d")
  time = datetime.datetime.now().strftime("%H:%M:%S")
  print(f"ZORO: The Date is {date} ")
  print(f'ZORO: The Time is {time}')

#This function gets the weather conditions
def weather():
  print("ZORO: Welcome to the Weather Station")
  city = input("ZORO: Enter the Name of the City.\n")
  api_key = '2cb21eb61a9e8f1f5075c68964a50642'
  url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    weather_description = data.get('weather',[{}])[0].get('description')
    temperature = data.get('main',{}).get('temp')
    if weather_description and temperature:
      print(f"ZORO: The weather in {city.title()} is {weather_description} ")
      print(f"ZORO: The Temperature is {temperature}C")
    else:
      print('ZORO: Weather Information Not Available')
  else:
    print('ZORO: Weather Information Not Available')

#This function ask the user if they want to view weather again?
def get_werather_again():
  print("ZORO: Do You Want to Get Weather of any other City?")
  print("1. Get Weather Again")
  print('2. Go Back to Menu')
  print('3. Exit')
  command = input("ZORO: Please Enter Your Command:\n")
  while True:
    if command == '1':
      weather()
    elif command == '2':
      show_menu()
    elif command == '3':
      exit()
      break
    else:
      print("ZORO: Please Enter the Valid Input")

#This function gets the definition
def definition():
    word = input("ZORO: Enter the Word to Define:\n")
    api_key = '26a45656-9811-4444-858b-61564660d041'
    url = f'https://www.dictionaryapi.com/api/v3/references/sd3/json/{word}?key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and data:
            definition = data[0].get('shortdef')
            if definition:
                print(f"ZORO: The definition of '{word}' is: {definition[0]}")
            else:
                print("ZORO: Definition not found.")
        else:
            print("ZORO: Word not found in the dictionary.")
    else:
        print("ZORO: Sorry, I couldn't retrieve the definition.")

#This function ask the user if they want to det definition again?
def get_definition_again():
  print("ZORO: Do You Want to Get Defintion of any other Word?")
  print("1. Get Definition Again")
  print('2. Go Back to Menu')
  print('3. Exit')
  command = input("ZORO: Please Enter Your Command:\n")
  while True:
    if command == '1':
      definition()
    elif command == '2':
      show_menu()
    elif command == '3':
      exit()
      break
    else:
      print("ZORO: Please Enter the Valid Input")

#This function does the calculation
def calculation():
  expression = input("ZORO: Enter the Expression:\n")
  result = eval(expression)
  print(f'ZORO: The result is {result}')

#This function ask if the user want to do more calculation?
def calculate_again():
  print("ZORO: Do You Want to Calculate again?")
  print("1. Do Calculation")
  print('2. Go Back to Menu')
  print('3. Exit')
  command = input("ZORO: Please Enter Your Command:\n")
  while True:
    if command == '1':
      calculation()
    elif command == '2':
      show_menu()
    elif command == '3':
      exit()
      break
    else:
      print("ZORO: Please Enter the Valid Input")


show_menu()

  
  

