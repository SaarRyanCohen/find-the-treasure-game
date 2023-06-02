import random

def create_cache_file(filename):
    digits = [str(i) * random.randint(1, 20) for i in range(10)]
    content = ''.join(digits) + 'TREASURE' + ''.join(digits[::-1])

    with open(filename, 'w') as file:
        file.write(content)

def play_game(filename):
    with open(filename, 'r') as file:
        content = file.read()
        treasure_indices = [i for i, char in enumerate(content) if char == 'T']
        current_index = 0
        moves = 0

        while current_index not in treasure_indices:
            print("Where do you want to move? [1- forward 2-backwards]")
            direction = int(input())
            print("How many characters?")
            num_chars = int(input())

            if direction == 1:
                current_index += num_chars
            elif direction == 2:
                current_index -= num_chars

            if current_index < 0:
                current_index = 0
            elif current_index >= len(content):
                current_index = len(content) - 1

            print("You hit '{}'".format(content[current_index]))
            moves += 1

        print("Congratulations! You found the treasure in {} moves.".format(moves))

filename = 'cache.txt'
create_cache_file(filename)
play_game(filename)