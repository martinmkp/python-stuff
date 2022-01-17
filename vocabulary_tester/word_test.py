import pandas as pd

def word_test(words):
    """
    The vocabulary tester.
    """
    words = words.sample(frac=1).reset_index(drop=True)
    col_1 = list(words.iloc[:, 0])
    col_2 = list(words.iloc[:, 1])

    points = 0
    max_points = words.shape[0]

    for i in range(max_points):
        word = input(f"Word {i+1}/{max_points}: {col_1[i]}: ")
        if word == col_2[i]:
            print("Correct!")
            points +=1
        else:
            print(f"Incorrect answer. The correct answer is: {col_2[i]}")
    print(f"Results: {points}/{max_points}")
