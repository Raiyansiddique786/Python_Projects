# Typing Speed Test

import os
import shutil 

import time  
import random 

sentences = ["The quick brown fox jumps over the lazy dog.", "A quick brown fox jumps over the lazy dog.", "The quick brown fox jumps over the lazy dog!"]

# Function to measure accuracy
def measure_accuracy(user_input, test_sentence):
    user_words = user_input.split()
    test_words = test_sentence.split()
    correct_words = sum(1 for u, t in zip(user_words, test_words) if u == t)
    accuracy = (correct_words / len(test_words)) * 100 
    return accuracy 

# Function to conduct the typing test
def typing_test ():
    test_sentence = random.choice(sentences)
    print("Type the following sentence as fast as you can:")
    print(test_sentence)
    input("Press Enter to start...")
    start_time = time.time() 
    user_input = input("\nStart typing: \n")
    end_time = time.time()
    time_taken = end_time - start_time
    time_taken_in_minutes = time_taken / 60
    word_count = len(test_sentence.split())
    wpm = word_count / time_taken_in_minutes

    print("Results:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Word count: {word_count}")
    print(f"Words per minute: {wpm:.2f}")
    accuracy = measure_accuracy(user_input, test_sentence)
    print(f"Accuracy: {accuracy:.2f}%")


typing_test()



