#docstring - ashrain Warad - Basketball database application.
#imports
import sqlite3

#contants and variables
DATABASE = "basketball.db"


#funtions
def Print_all_Players():
  '''print all the players'''
  db = sqlite3.connect("basketball.db")
  cursor = db.cursor()
  sql = "SELECT * FROM player;"
  cursor.execute(sql)
  results  = cursor.fetchall()
  #loop through all of the results
  print(f"player_name         player_height  shoe_size     team_id")
  for players in results:
      print(f"{players[1]:<20}{players[2]:<15}{players[3]:<14}{players[4]:<22}")
  #loop finished here
  db.close()

def Print_all_State():
  '''print all the states'''
  db = sqlite3.connect("basketball.db")
  cursor = db.cursor()
  sql = "SELECT * FROM player_state;"
  cursor.execute(sql)
  results  = cursor.fetchall()
  #loop through all of the results
  print(f"country             city            player_id")
  for players in results:
      print(f"{players[1]:<20}{players[2]:<16}{players[3]:<17}")
  #loop finished here
  db.close()

def Print_all_Team():
  '''print all the Team'''
  db = sqlite3.connect("basketball.db")
  cursor = db.cursor()
  sql = "SELECT * FROM Team;"
  cursor.execute(sql)
  results  = cursor.fetchall()
  #loop through all of the results
  print(f"Team_Name              position       losses         win ")
  for players in results:
      print(f"{players[1]:<24}{players[2]:<15}{players[3]:<14}{players[4]:<22}")
  #loop finished here
  db.close()

#main code
while True:
    user_input = input("\nEnter a command.\n1. Print all players.\n2. Print all player states\n3. Print all Teams\n7.Exit\n")
    if user_input == "1":
        Print_all_Players()
    elif user_input == "2":
        Print_all_State()
    elif user_input == "3":
        Print_all_Team()
    elif user_input == "4":
        break    
    else:
        print("Invalid input/n")

