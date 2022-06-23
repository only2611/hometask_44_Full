from random import shuffle



def random_numbers(n):
    data = list(range(1, 10))
    shuffle(data)
    return data[:n]


class Game():
    secret_numbers = random_numbers(4)

    def __init__(self) -> None:
        self.numbers = None

    def validation(self, numbers_str):
        try:
            numbers = [int(s) for s in numbers_str]
            if len(numbers) != 4:
                return "must be four numbers"
            if len(numbers) != len(set(numbers)):
                return "not unique values"
            for i in numbers:
                if i > 9 or i < 1:
                    return "numbers not in 1-9"
            self.numbers = numbers
        except:
            return "Values must be only numbers"

    def results(self):
        bulls = 0
        cows = 0
        for i in range(len(self.numbers)):
            if self.numbers[i] == self.secret_numbers[i]:
                bulls += 1
            elif self.numbers[i] in self.secret_numbers:
                cows += 1

        if bulls == 4:
            return "the winner"
        elif bulls or cows:
            return f"you have {bulls} bulls and {cows} cows"
        else:
            return "Just looser"