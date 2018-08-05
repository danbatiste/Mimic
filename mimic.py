# mimic.py
import random

def get_all_next_to(value, vs):
    indices = []
    for i in range(len(vs) - 1):
        if vs[i] == value:
            indices.append(i + 1)
    return [vs[i] for i in indices]
    
class Word():
    def __init__(self, value, options):
        self.value = value
        self.options = options

    def __str__(self):
        return "Word( '{}' , {} )".format(self.value, self.options)

    def __repr__(self):
        return self.__str__()


class Chain():
    def __init__(self, text = None, file = None):
        self.text = ''
        if file and not text:
            with open(file, 'r') as f:
                for line in f:
                    self.text += line
        elif not file and text:
            self.text = text
        self.words = []
        for word in self.text.split(' '):
            self.words.append(''.join([c for c in word if c.isalnum()]))
        self.current_node = Word(self.words[0], get_all_next_to(self.words[0], self.words))

    def change_node(self, node):
        self.current_node = Word(node, get_all_next_to(node, self.words))

    def restart(self):
        self.change_node(self.words[0])

    def read(self):
        return self.current_node.value
        
    def next(self):
        choices = get_all_next_to(self.current_node.value, self.words)
        if choices:
            choice = random.choice(choices)
            self.change_node(choice)
        else:
            self.restart()


def chain(filepath, n):
    chain = Chain(file = filepath)
    for i in range(n):
        yield chain.read()
        chain.next()

def main():
    arg = input("Enter text: ")
    if arg[0] == '!':
        chain = Chain(file = arg[1:])
    else:
        chain = Chain(text = arg)
    while not input() in ['exit', 'q', 'quit']:
        chain.read()
        chain.next()


if __name__ == "__main__":
    main()

        