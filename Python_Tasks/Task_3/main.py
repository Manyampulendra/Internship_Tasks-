from solutions import *

def main():
    print("-" * 45)
    print("Welcome to the Python Solutions for Task 3!")
    print("-" * 45)
    print("This program demonstrates various functions for word frequency, character frequency, anagrams, and more.")
print("-" * 45)

print("Q1 Word Frequency:", word_frequency("python is easy and python is powerful"))
print("Q2 Character Frequency:", character_frequency("banana"))
print("Q3 First Non-Repeating Character:", first_non_repeating_character("swiss"))
print("Q4 Anagrams:", are_anagrams("listen", "silent"))
print("Q5 First Repeating Character:", first_repeating_character("programming"))
print("Q6 Move Zeros:", move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))
print("Q7 Second Highest:", second_highest_distinct([10, 20, 40, 30, 40, 20]))
print("Q8 Remove Duplicates:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q9 Missing Number:", find_missing_number([1, 2, 4, 5, 6], 6))
print("Q10 First Pair Sum:", first_pair_sum([2, 7, 11, 15], 9))
print("Q11 Closest to Zero:", closest_to_zero([-8, -3, 2, 5, -2]))
print("Q12 Common Elements:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q13 Rotate Right:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q14 Maximum Consecutive Pair Sum:", max_sum_of_consecutive([4, 7, 2, 9, 5]))
print("Q15 All Unique Pairs Sum:", all_pairs_sum([2, 4, 3, 5, 7, 8, 1], 9))

if __name__ == "__main__":
    main()