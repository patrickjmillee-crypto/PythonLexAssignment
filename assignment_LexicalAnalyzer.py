"""
Author: Patrick Miller
BuffID: 1121370
date: 2026-10-06

"""

class Lexer:
    LETTER = "LETTER"
    DIGIT = "DIGIT"
    UNKNOWN = "UNKNOWN"
    EOF = "EOF"

    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.char = ""
        self.char_class = ""
        self.lexeme = ""

        self.get_char() 

    def get_char(self):
        if self.pos < len(self.text):
            self.char = self.text[self.pos]
            self.pos += 1

            if self.char.isalpha():
                self.char_class = self.LETTER
            elif self.char.isdigit():
                self.char_class = self.DIGIT
            else:
                self.char_class = self.UNKNOWN
        else:
            self.char = ""
            self.char_class = self.EOF

    def add_char(self):
        self.lexeme += self.char

    def get_non_blank(self):
        while self.char.isspace() and self.char_class != self.EOF:
            self.get_char()

    def lookup(self, ch: str) -> str:
        lookup_table = {
            '+': 'ADD_OP',
            '-': 'SUB_OP',
            '*': 'MULT_OP',
            '/': 'DIV_OP',
            '(': 'LEFT_PAREN',
            ')': 'RIGHT_PAREN',
            '=': 'ASSIGN_OP'
        }
        return lookup_table.get(ch, 'UNKNOWN_TOKEN')

    def lex(self)-> tuple:
        self.lexeme = ""
        self.get_non_blank()

        if self.char_class == self.EOF:
            self.lexeme = "EOF"
            return(self.lexeme, "EOF")

        if self.char_class == self.LETTER:
            while self.char_class == self.LETTER or self.char_class == self.DIGIT:
                self.add_char()
                self.get_char()
            return (self.lexeme, "ID")

        elif self.char_class == self.DIGIT:
            while self.char_class == self.DIGIT:
                self.add_char()
                self.get_char()
            return (self.lexeme, "INT_CONSTANT")

        elif self.char_class == self.UNKNOWN:
            self.add_char()
            token = self.lookup(self.char)
            self.get_char()
            return(self.lexeme, token)

        else:
            self.add_char()
            token = self.lookup(self.char)
            self.get_char()
            return (self.lexeme, token)

expression = "a = 3 + b * (c -2) / 4"
lexer = Lexer(expression)

print(f"Parsing expression: '{expression}'\n")
print(f"{'lexeme' :<12} | {'Token':<12}")
print("-" * 27)

while True:
    lexeme, token = lexer.lex()
    print(f"{lexeme:<12} | {token:<12}")
    if token == "EOF":
        break