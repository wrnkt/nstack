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
    def __init__(self, letter_list: list[str], reverse = False):
        self.letter_list = []
        for c in letter_list:
            self.letter_list.append(Tile(c))
    
    def pop_last_tile(self) -> str:
        last_tile = self.letter_list.pop()
        last_tile_char = last_tile.get_letter()
        return last_tile_char

    def print(self):
        for tile in self.letter_list:
            tile.print()

class StackList:
    def __init__(self, stack_list: list[Stack]):
        self.stacks = stack_list

    def print(self):
        for stack in self.stacks:
            print(stack)
            stack.print()

def test():
    stack_test = Stack("abcde")
    stack_test.print()
    print(stack_test.pop_last_tile())
    stack_test.print()
    

def main():
    s1 = Stack("weuifvjkdf")
    s2 = Stack("tusdwefiwd")
    play_stacks = StackList([s1, s2]) 
    play_stacks.print()

if __name__ == "__main__":
    main()
