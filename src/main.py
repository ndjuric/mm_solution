#!/usr/bin/env python
import json


class Result(object):
    def __init__(self):
        self.green = 0
        self.red = 0
        self.white = 0
        self.green_indexes = {}
        self.value_counter = {}

    def increment_value(self, value):
        if value not in self.value_counter:
            self.value_counter[value] = 0
        self.value_counter[value] += 1

    def __dict__(self):
        return {
            'green': self.green,
            'red': self.red,
            'white': self.white,
            'value_counter': self.value_counter,
            'green_indexes': self.green_indexes
        }

    def __str__(self):
        return json.dumps(self.__dict__())


class SolutionTester(object):
    def __init__(self, secret):
        self.secret = secret
        self.result = Result()

        self.secret_map = {}
        for element in secret:
            if element not in self.secret_map:
                self.secret_map[element] = 0
            self.secret_map[element] += 1

        print(self.secret)
        print(self.secret_map)
        print('---')

    def test_green(self, test):
        # prvo vidi jel ima zelenih
        for i in range(len(self.secret)):
            if test[i] != self.secret[i]:
                continue
            self.result.green += 1
            self.result.green_indexes[i] = True
            self.result.increment_value(test[i])

    def test_red(self, test):
        for i in range(len(self.secret)):
            if i in self.result.green_indexes:
                continue  # preskoci jer je zelen
            if test[i] not in self.secret_map:
                continue  # preskoci jer vrednost ne postoji u secretu
            if test[i] not in self.result.value_counter:
                self.result.value_counter[test[i]] = 0
            if self.result.value_counter[test[i]] >= self.secret_map[test[i]]:
                continue
            self.result.red += 1
            self.result.increment_value(test[i])

    def test_white(self):
        self.result.white = len(self.secret) - self.result.green - self.result.red

    def run_test(self, test):
        self.result = Result()
        # 1. zeleno = tacan index/value match
        # 2. crveno = value postoji ali index nije dobar
        # 3. belo = value ne postoji

        self.test_green(test)
        self.test_red(test)
        self.test_white()

        print(test)
        print(self.result)
        print('---')


def main():
    secret = [1, 1, 3, 4]
    tests = [
        # [1, 1, 3, 4],  # Z Z Z Z
        [3, 4, 1, 1],  # C C C C
        [3, 3, 3, 3],  # B B Z B
    ]

    tester = SolutionTester(secret)
    for test in tests:
        tester.run_test(test)


if __name__ == '__main__':
    main()
