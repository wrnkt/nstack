import random
import math
import string
from statistics import median

import debug

class Tile:
    def __init__(self, letter: str):
        self.letter = letter

    @property
    def letter(self):
        return self._letter

    @letter.setter
    def letter(self, value):
        self._letter = value

    def set_letter(self, letter: str):
        self.letter = letter

    def __str__(self):
        return self._letter

    def print(self):
        print(self.letter)

class Stack:
    def __init__(self, entry_list: list[str], name: str, reverse = False):
        self.name = name
        self.tiles = []
        for c in entry_list:
            self.tiles.append(Tile(c))

    def __str__(self):
        str_out = ""
        str_out += self.name + "\n"
        for tile in reversed(self.tiles):
            str_out += str(tile) + "\n"

        return str_out
    
    def pop_last_tile(self) -> str:
        last_tile = self.tiles.pop()
        return last_tile

    def add_new_tile(self, new_tile: Tile):
        self.tiles.append(new_tile)

    def get_length(self) -> int:
        return len(self.tiles)

    def get_tile(self, i):
        return self.tiles[i]

    def print(self):
        for tile in self.tiles:
            tile.print()

    def print_name_and_tiles(self):
        print(self.name)
        self.print()

class StackList:
    def __init__(self, stack_list: list[Stack]):
        self.stacks = stack_list

    def print(self):
        PADDING = 18
        # print justified title
        print(f"".join([f"{s.name:<{PADDING}}" for s in self.stacks]))
        # calculate max length of stack to iterate over
        max_length = max([s.get_length() for s in self.stacks])
        for i in reversed(range(0, max_length)):
            row = ""
            placeholder = '#'
            for s in self.stacks:
                try: 
                    row += f"{s.get_tile(i).letter:<{PADDING}}"
                except:
                    row += f"{placeholder:<{PADDING}}"
            print(row)


LOCAL_WORD_FILE = "/usr/share/dict/words"
LOCAL_DICTIONARY_LIST = open(LOCAL_WORD_FILE).read().splitlines()

WORD_LENGTH_RANGE = (2,5)

def create_letter_string(length: int, dictionary: list[str], random_injection = 0):
    # random_injection represents the degree to which random letters are put in
    # between the words. 0 is none, all the letters will be part of a word.
    match random_injection:
        case 0:
            print("GENERATING WITH NO RANDOM INJECTION")
            working_list = random_word_length_filter(WORD_LENGTH_RANGE,
                    math.floor((length/WORD_LENGTH_RANGE[0])), dictionary)
            working_string = "".join(working_list)
            return working_string[:length]
        case range(1,10):
            print("NOT IMPLEMENTED")
        case 10:
            return make_rand_string(length)
        case _:
            print("NOT IMPLEMENTED")

def random_word_length_filter(len_range, n: int, dictionary: list[str]) -> list[str]:
    # return a length n list of words between upper and lower bound
    filtered_dict = []
    output_list = []
    count = 0

    for word in dictionary:
        if (
                not word.istitle() and
                len(word) >= len_range[0] and
                len(word) <= len_range[1]
            ):
                filtered_dict.append(word)

    [output_list.append(random.choice(filtered_dict)) for x in"1"*n]

    return output_list

def make_rand_string(length: int) -> str:
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase)
            for _ in range(length))

def move_top_tile_a_to_b(a: Stack, b: Stack):
    b.add_new_tile(a.pop_last_tile())
    pass    


def print_state(sl: StackList):
    def print_separator(sl: StackList):
        x = max([len(s.name) for s in sl.stacks])
        if x > 18:
            print("-"*x*sl.stacks)
        else:
            print("-"*18*len(sl.stacks))
    print_separator(sl)
    sl.print()
    print_separator(sl)
    
def test():
    stack_test = Stack("abcde", "Test Stack")
    stack_test.print()
    print(f"remove letter: {stack_test.pop_last_tile().get_letter()}")
    nt = Tile("p")
    stack_test.add_new_tile(nt)
    print(f"add tile {nt}")
    stack_test.print()

def get_move(sl: StackList):
    print("From left to right select the number of the source stack:")
    stack_prompt = ""

    for stack in sl.stacks:
        stack_prompt += f"{stack.name}:{sl.stacks.index(stack) + 1:<10}"
    print(stack_prompt)

    dest_stack = ""
    src_stack = ""

    def is_valid_stack(sl: StackList, s: Stack):
        if int(s) > len(sl.stacks) or int(s) < 1:
            print(f"Pick a stack between 1 and {len(sl.stacks)}")
        return int(s) <= (len(sl.stacks)) and int(s) > 0

    while True:
        src_stack = input("Move tile from: ")
        if not is_valid_stack(sl, src_stack):
            continue
        elif dest_stack != src_stack:
            break
        else:
            print(f"Unhandled input error. {src_stack = } | {dest_stack = }")

    while True:
        dest_stack = input("Move tile to: ")
        if not is_valid_stack(sl, dest_stack):
            continue
        elif dest_stack == src_stack:
            print("Source and destination stack can't be the same.")
        elif dest_stack != src_stack:
            break
        else:
            print(f"Unhandled input error. {src_stack = } | {dest_stack = }")

    print(f"{len(sl.stacks) = }")

    print(f"Moving tile from {src_stack} to {dest_stack}")
    move_top_tile_a_to_b(sl.stacks[int(src_stack)-1],
            sl.stacks[int(dest_stack)-1])


def game_test():
    s1 = Stack("weuif", "Stack")
    s2 = Stack("tfuiwd", "Stack")
    s3 = Stack(create_letter_string(9, LOCAL_DICTIONARY_LIST,
        random_injection=0), "Stack")
    user_stack = Stack("", "Play Stack")

    play_stacks = StackList([s1, s3, user_stack]) 
    print_state(play_stacks)

    while True:
        get_move(play_stacks)
        print_state(play_stacks)

    print(s1.tiles[0])

def main():
    game_test()

if __name__ == "__main__":
    main()
