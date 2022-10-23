import random
import string
import math
from statistics import median

class Tile:
    def __init__(self, letter: str):
        self.letter = letter

    def get_letter(self) -> str:
        return self.letter

    def set_letter(self, letter: str):
        self.letter = letter

    def print(self):
        print(self.letter)

class Stack:
    def __init__(self, entry_list: list[str], name: str, reverse = False):
        self.name = name
        self.tile_list = []
        for c in entry_list:
            self.tile_list.append(Tile(c))
    
    def pop_last_tile(self) -> str:
        last_tile = self.tile_list.pop()
        return last_tile

    def add_new_tile(self, new_tile: Tile):
        self.tile_list.append(new_tile)

    def get_length(self) -> int:
        return len(self.tile_list)

    def get_tile(self, i):
        return self.tile_list[i]

    def print(self):
        for tile in self.tile_list:
            tile.print()

    def print_name_and_tiles(self):
        print(self.name)
        self.print()

class StackList:
    def __init__(self, stack_list: list[Stack]):
        self.stacks = stack_list

    def print(self):
        # print justified title
        print(f"".join([f"{s.name:<18}" for s in self.stacks]))
        # calculate max length of stack to iterate over
        max_length = max([s.get_length() for s in self.stacks])
        for i in reversed(range(0, max_length)):
            row = ""
            placeholder = '#'
            for s in self.stacks:
                try: 
                    row += f"{s.get_tile(i).get_letter():<18}"
                except:
                    row += f"{placeholder:<18}"
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

def test():
    stack_test = Stack("abcde", "Test Stack")
    stack_test.print()
    print(f"remove letter: {stack_test.pop_last_tile().get_letter()}")
    nt = Tile("p")
    stack_test.add_new_tile(nt)
    print(f"add tile {nt}")
    stack_test.print()

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
    

def main():
    s1 = Stack("weuif", "Stack 1")
    s2 = Stack("tfuiwd", "Stack 2")
    s3 = Stack(create_letter_string(9, LOCAL_DICTIONARY_LIST,
        random_injection=0), "Stack 3")
    user_stack = Stack("", "Play stack")

    play_stacks = StackList([s1, s3, user_stack]) 
    print_state(play_stacks)

    move_top_tile_a_to_b(s1, s2)
    print_state(play_stacks)

if __name__ == "__main__":
    main()
    # test()
    # print(make_rand_string(5))
    # print(create_letter_string(36, LOCAL_DICTIONARY_LIST, random_injection=0))
    # print(random_word_length_filter((3,4),3,LOCAL_DICTIONARY_LIST))
