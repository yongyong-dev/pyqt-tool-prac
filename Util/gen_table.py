import random
import string
import time

_DATA_LENGTH = 50000
_LENGTH = 10  # 10자리
string_pool = string.ascii_lowercase  # 소문자


class Util:
    @staticmethod
    def make_random_data_file():
        start = time.time()
        result = []
        with open("../test.csv", "w") as file:
            for _ in range(_DATA_LENGTH):
                name = ""  # 결과 값
                for i in range(_LENGTH):
                    name += random.choice(string_pool)  # 랜덤한 문자열 하나 선택
                file.write(name + ',' + format(random.randint(1, 4294967295), '08X') + ',' + str(random.randint(1, 100))
                           + ',' + str(random.randint(1, 100)) + ',' + str(random.randint(1, 100))
                           + 'msg msg %d msg %d\n')
