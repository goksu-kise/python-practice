import os
import time


def build_tree(height):
    tree = []
    for i in range(height):
        spaces = " " * (height - i - 1)
        stars = "*" * (2 * i + 1)
        tree.append(spaces + stars)
    tree.append(" " * (height - 1) + "|")
    return tree

def add_star(tree, height):
    tree[0] = " " * (height - 1) + "★"
    return tree

def add_sequential_lights(tree):
    new_tree = []
    for line in tree:
        new_line = ""
        for i in range(len(line)):
            if line[i] == "*" and i % 2 == 0:
                new_line += "o"
            else:
                new_line += line[i]
        new_tree.append(new_line)
    return new_tree

def is_fibonacci(c):
    a, b = 0, 1
    while b < c:
        a, b = b, a + b
    return b == c or c == 0

def is_prime(c):
    if c < 2: return False
    for i in range(2, int(c**0.5) + 1):
        if c % i == 0: return False
    return True


def sparkle_pattern(tree, magic_word):
    vowels = "aeiouAEIOU"
    tree_str = "\n".join(tree)
    new_tree_str = ""
    light_index = 0
    
    for char in tree_str:
        if char == 'o' and light_index < len(magic_word):
            if magic_word[light_index] in vowels:
                new_tree_str += "@"
            else:
                new_tree_str += "o" 
            light_index += 1
        else:
            new_tree_str += char
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- SPARKLE ANIMATION ---")
    print(new_tree_str)
    time.sleep(2)

def pulse_pattern(tree):
    for _ in range(5): 
        os.system('cls' if os.name == 'nt' else 'clear') 
        for line in tree:
            print(line.replace('o', '@')) 
        time.sleep(0.5) 
        
        os.system('cls' if os.name == 'nt' else 'clear')
        for line in tree:
            print(line) 
        time.sleep(0.5)

def wave_pattern(tree):
    for i in range(len(tree)):
        os.system('cls' if os.name == 'nt' else 'clear')
        for index, line in enumerate(tree):
            if index == i:
                print(line.replace('o', '@'))
            else:
                print(line)
        time.sleep(0.2)

def reverse_wave_pattern(tree):
    for i in range(len(tree) - 1, -1, -1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- REVERSE WAVE ANIMATION ---")
        for index, line in enumerate(tree):
            if index == i:
                print(line.replace('o', '@'))
            else:
                print(line)
        time.sleep(0.3)

height = 10
tree = build_tree(height)
tree = add_star(tree, height)
tree = add_sequential_lights(tree)

for line in tree:
    print(line)

magic_word = input("Enter the magic word: ")
sequence_number = int(input("Enter the sequence number: "))

word_len = len(magic_word)

if word_len % 2 == 0:
    if is_prime(sequence_number):
        sparkle_pattern(tree, magic_word)
    else:
        pulse_pattern(tree)
else:
    if is_fibonacci(sequence_number):
        wave_pattern(tree)
    else:
        reverse_wave_pattern(tree)


