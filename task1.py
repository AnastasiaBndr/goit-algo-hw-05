from wonderwords import RandomWord
import random
r = RandomWord()

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True
    
    def delete(self,key):
        key_hash=self.hash_function(key)
        if self.table[key_hash] is not None:
            i=0
            for pair in self.table[key_hash]:
                if pair[0]==key:
                    del self.table[key_hash][i]
                    return pair
                i=i+1

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    sentense = " ".join(args)
    return cmd, sentense

def main():
    size=10
    H = HashTable(size)
    for i in range(0,size):
        word=r.word()
        number=random.randint(1,99)
        H.insert(word,number)
    print(H.table)

    while True:
        print(f'{bcolors.OKGREEN}command to find:{bcolors.ENDC} find "word"\n{bcolors.OKGREEN}command to delete:{bcolors.ENDC} delete "word"')
        command, *args = parse_input(input())

        if command in ['break', 'stop', 'exit']:
            break
        if command in ['find']:
            print(H.get(args[0]))
        if command in ['delete']:
            print(H.delete(args[0]))
            print(H.table)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

