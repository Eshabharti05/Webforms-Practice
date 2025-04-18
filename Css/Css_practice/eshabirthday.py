import time
import os

def birthday_banner():
    """Displays a grand birthday banner with ASCII art."""
    print(r"""
        🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
        🎂      H A P P Y   B I R T H D A Y!      🎂
        🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
        """)
    print(r"""      
          
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⢀⣀⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀
               ⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
             ⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀
            ⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀
    ⠀⠀     ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
           ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
           ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
           ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
           ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀             
           |~~~~~~|
           |                  |
           |     🍒🍒🍒     |
        _|     🍫🍫🍫     |_
     _|         🎂            |_
  _|        🎂🎂🎂🎂🎂         |_
 |~~~***~~~|
 |                              |
 |     🎉  MAKE A WISH!  🎉    |
 |                              |
 |~~~~~~~~~~|
            """)
    time.sleep(1)


def countdown(seconds):
    """A countdown to make it exciting."""
    print("\n🎊 Countdown to the birthday surprise! 🎊\n")
    for i in range(seconds, 0, -1):
        print(f"🎉🎈 {i} 🎈🎉")
        time.sleep(1)
    print("🎉 It's time for the birthday celebration! 🎉\n")


def birthday_wishes(name):
    """Displays a grand birthday message."""
    os.system('cls' if os.name == 'nt' else 'clear')
    birthday_banner()
    time.sleep(2)

    print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
    print(f"🌟🌟 Dear {name.upper()}, 🌟🌟")
    print("Wishing you a day filled with magic, laughter, and happiness!")
    print("May this year bring you endless joy and success!")
    print("🎁🌈 You're not just special—you’re legendary! 🌈🎁")
    print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨\n")
    time.sleep(2)

    print("🎶🎵 Let’s raise a toast to your amazing journey ahead! 🥂🎶🎵")
    print("🎉🎂 Happy Birthday to you, now and forever! 🎂🎉\n")


if __name__ == "_main_":
    name = input("Enter the name of the birthday person: ")
    countdown(5)
    birthday_wishes(name)
