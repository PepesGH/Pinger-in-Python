import os
import time
green = '\033[1;32m'
def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    cls()
    arte = '''       _                       
      (_)                      
 _ __  _ _ __   __ _  ___ _ __ 
| '_ \| | '_ \ / _` |/ _ \ '__|
| |_) | | | | | (_| |  __/ |   
| .__/|_|_| |_|\__, |\___|_|   
| |             __/ |          
|_|            |___/           '''
    print(green+arte)
    ip_check = input("What IP did you fucked up? > ")
    os.system("ping -n 50 {}". format(ip_check))
    
    restart = input("Want to restart? y/n > ")
    if restart == "y":
        main()
    elif restart == "n":
        print("Thanks for using the script.")
        time.sleep(4)
        quit()
    else:
        quit()
        
if __name__ == '__main__':
	main()
