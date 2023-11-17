import cv2
from colorama import Fore

print(Fore.GREEN + 'Zuriel Elijah D. Valencia | Assignment #2 in PLD')
print("")

name = input(Fore.BLUE + 'Enter your name: ')
img = cv2.imread('Hello World.jpg')
cv2.imshow("Hello meme Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

age = input(Fore.BLUE + 'Enter your age: ')
print(Fore.BLUE + "Press U to close the video")
address = input(Fore.BLUE + "Enter your address: ")

img = cv2.imread('PUP.jpeg')
cv2.imshow("PUP Logo Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("")

print(Fore.RED + 'Bot has received the following information:')
print("")
print("Name: ", Fore.GREEN + name)
print(Fore.RED + "Age: ", Fore.GREEN + age)
print(Fore.RED + "Address: ", Fore.GREEN + address)

print(Fore.YELLOW + "Thank you for Watching!")
print(Fore.WHITE + "Never gonna give you up!")

mized = "c:\\Users\\cora lagtrata\\Val\\Ricky.mp4"


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


