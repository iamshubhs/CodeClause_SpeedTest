
import tkinter as tk


window = tk.Tk()
window.title("Speed Typing Test")


import time

from accuracy import calculate_accuracy
from speed import calculate_speed


def speed_typing_test(text1):
    print("Type the following text:")
    print(text1)
    print("Press Enter when you're done.")

    input("Press Enter to start...")
    start_time = time.time()

    user_input = input()

    end_time = time.time()
    elapsed_time = end_time - start_time

    words = text1.split()
    num_words = len(words)
    num_characters = len(text1)

    user_words = user_input.split()
    num_user_words = len(user_words)
    num_user_characters = len(user_input)

    accuracy = calculate_accuracy(text1, user_input)
    speed = calculate_speed(num_user_words, elapsed_time)

    print("Test Result:")
    print("Time taken:", round(elapsed_time, 2), "seconds")
    print("Number of words:", num_words)
    print("Number of characters:", num_characters)
    print("Number of user words:", num_user_words)
    print("Number of user characters:", num_user_characters)
    print("Accuracy:", accuracy, "%")
    print("Typing speed:", speed, "words per minute")



text1 = "The quick brown fox jumps over the lazy dog."

speed_typing_test(text1)

w = tk.Button(window,text="Start Typing Test",command=speed_typing_test)
w.pack(side="top")

window.mainloop()
