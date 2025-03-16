import subprocess

def print_lemon_stand():
    ascii_art = """
    ██      ███████  ███    ███  ██████   ██████   ███    ██      
    ██      ██       ████  ████ ██    ██ ██    ██  ████   ██      
    ██      █████    ██ ████ ██ ██    ██ ██    ██  ██ ██  ██      
    ██      ██       ██  ██  ██ ██    ██ ██    ██  ██  ██ ██      
    ███████ ███████  ██      ██  ██████   ██████   ██   ████      
    -------------------------------------------------------      
               L  E  M  O  N     S  T  A  N  D                  
    -------------------------------------------------------      

                 by le_combi
    """
    print(ascii_art)

print_lemon_stand()
start = input("Do you want to start the game? (y/n): ")

if start == "y":
    subprocess.run(["python", "Game.py"])
elif start == "n":
    print("Goodbye!")
    exit(0)
