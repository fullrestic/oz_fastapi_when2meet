# sqids
"""from typing import Sequence

from sqids import sqids


squid = sqids.Sqids()


class Squids:

    @classmethod
    def encode(cls, nums: Sequence[int]) -> str:
        return squid.encode(nums)"""


# sqids vs base62 성능 테스트
# base62가 훨씬 빠르지만 sqids가 제공하는 라이브러리 같은 것이 다양해 사용범위가 더 넗음
"""
def do_squids():
    now = datetime.now()
    return Squids.encode(
            [now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond,
             random.randint(1, 9)]
        )

def do_base62() :
    uu = uuid.uuid4()
    return Base62.encode(uu.int)

if __name__ == '__main__':
    print(timeit.timeit(lambda: do_squids(), number=10000))
    print(timeit.timeit(lambda: do_base62(), number=10000))
"""
