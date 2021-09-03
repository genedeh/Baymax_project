class BaymaxCalculate:
    def add(self, text: str) -> int():
        split_text = text.split()
        try:
            if split_text[1] == '+':
                return int(float(split_text[0]) + float(split_text[-1]))
            else:
                return 'this is not addition'
        except ValueError:
            print('All values most be int or float compatible'.upper())

    def subtract(self, text: str) -> int():
        split_text = text.split()
        try:
            if split_text[1] == '-':
                return int(float(split_text[0]) - float(split_text[-1]))
            else:
                return 'this is not minus'
        except ValueError:
            print('All values most be int or float compatible'.upper())

    def multiplication(self, text: str) -> int():
        split_text = text.split()
        try:
            if split_text[1] == '*':
                return int(float(split_text[0]) * float(split_text[-1]))
            else:
                return 'this is not times'
        except ValueError:
            print('All values most be int or float compatible'.upper())

    def divide(self, text: str) -> int():
        split_text = text.split()
        try:
            if split_text[1] == '/':
                return int(float(split_text[0]) / float(split_text[-1]))
            else:
                return 'this is not division'
        except ValueError:
            print('All values most be int or float compatible'.upper())


