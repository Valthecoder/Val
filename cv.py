import cv2
from colorama import Fore
import numpy
from ffpyplayer.player import MediaPlayer


print(Fore.GREEN + 'Zuriel Elijah D. Valencia | Assignment #2 in PLD')
print("")

name = input(Fore.BLUE + 'Enter your name: ')
age = input(Fore.BLUE + 'Enter your age: ')
address = input(Fore.BLUE + "Enter your address: ")
print("")

print(Fore.RED + 'Bot has received the following information:')
print("")
print("Name: ", Fore.GREEN + name)
print(Fore.RED + "Age: ", Fore.GREEN + age)
print(Fore.RED + "Address: ", Fore.GREEN + address)

vid = cv2.VideoCapture('c:\\Users\\cora lagtrata\\Val\\Ricky.mp4')

while vid.isOpened():
    ute, frame = vid.read()
    if ute:

        cv2.imshow('Video', frame)

        if cv2.waitKey(25) & 0xFF == ord('u'):
            break

    else:
        break

vid.release()

cv2.destroyAllWindows()