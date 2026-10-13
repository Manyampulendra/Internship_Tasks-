# Q1. Frequency of Each Word
def word_frequency(sentence):
    result = {}
    for word in sentence.lower().split():
        result[word] = result.get(word, 0) + 1
    return result

# Q2. Frequency of Each Character
def character_frequency(word):
    result = {}
    for char in word:
        result[char] = result.get(char, 0) + 1
    return result

# Q3. First Non-Repeating Character
def first_non_repeating_character(word):
    counts = character_frequency(word)
    for char in word:
        if counts[char] == 1:
            return char
    return None

# Q4. Check Anagrams (case- and space-insensitive)
def are_anagrams(s1, s2):
    a = "".join(s1.lower().split())
    b = "".join(s2.lower().split())
    return character_frequency(a) == character_frequency(b)

# Q5. First Repeating Character
def first_repeating_character(text):
    seen = set()
    for char in text:
        if char in seen:
            return char
        seen.add(char)
    return None

# Q6. Move All Zeros to the End of a List
def move_zeros_to_end(numbers):
    return [x for x in numbers if x !=0] + [x for x in numbers if x == 0]

# Q7. Find the Second Highest Distinct Number in a List
def second_highest_distinct(numbers):
    unique = []
    for x in numbers:
        if x not in unique:
            unique.append(x)
    if len(unique) < 2:
        return None
    largest = unique[0]
    second = None
    for x in unique[1:]:
        if x > largest:
            second, largest = largest, x
        elif x != largest and (second is None or x > second):
            second = x
    return second

# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(numbers):
    result = []
    seen = set()
    for x in numbers:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result

# Q9. Find the Missing Number from 1 to N
def find_missing_number(numbers, n):
    return n * (n + 1) // 2 - sum(numbers)

# Q10. Find Two Numbers Whose Sum Equals a Target
def first_pair_sum(numbers, target):
    seen_values = []
    for current in numbers:
        needed = target - current
        for earlier in seen_values:
            if earlier == needed:
                return [earlier, current]
        seen_values.append(current)
    return []

# Q11. Find the Number Closest to Zero
def closest_to_zero(numbers):
    if not numbers:
        return None
    closest = numbers[0]
    for x in numbers[1:]:
        if abs(x) < abs(closest) or (abs(x) == abs(closest) and x > closest):
            closest = x
    return closest

# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    set2 = set(list2)
    return [x for x in list1 if x in set2]

# Q13. Rotate a List to the Right by K Positions
def rotate_right(numbers, k):
    if not numbers:
        return []
    k %= len(numbers)
    return numbers[-k:] + numbers[:-k] if k else numbers[:]

# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_sum_of_consecutive(numbers):
    if len(numbers) < 2:
        return None
    max_sum = numbers[0] + numbers[1]
    for i in range(1, len(numbers) - 1):
        current_sum = numbers[i] + numbers[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_pairs_sum(numbers, target):
    pairs = []
    seen = set()
    for current in numbers:
        needed = target - current
        if needed in seen:
            pairs.append((needed, current))
        seen.add(current)
    return pairs
