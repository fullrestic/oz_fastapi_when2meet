"""
# 제품 코드
def add(a: int, b: int) -> int:
    return a + b

# 테스트 코드 -- 테스트 함수는 반환값이 없음
def test_add() -> None :
    # Given : 재료를 준비
    a, b = 1, 1

    # When : 테스트 대장이 되는 함수를 호출
    result = add(a, b)

    # Then :
    assert result == 2
        # if not result == 2 : raise AssertionError
"""

"""
실전 문제 -- 택배가 언제 도착할지, 예상 배송일을 계산하는 단위 테스트 직상

- 택배는 2영업일 이후에 도착합니다. 월요일부터 토요일까지가 영업일입니다.
- 단순화를 위해 “도서산간지역”은 고려하지 않습니다.
- 단순화를 위해 설날, 추석 등의 공휴일은 고려하지 않습니다.
"""

from datetime import datetime, timedelta  # noqa

# literal 쓰지 않고 상수를 쓰는 이유
# 2라는 숫자가 무엇을 뜻하는지 정보를 모르는 사람도 알 수 있게
# magic number를 쓰지 말자 : 설명이 없는 값
DELIVERY_DAYS = 2


def _is_holiday(day: datetime) -> bool:
    return day.weekday() > 5


def get_eta(purchase_date: datetime) -> datetime:
    current_date = purchase_date
    remaining_days = DELIVERY_DAYS

    while remaining_days > 0:
        current_date += timedelta(days=1)
        if not _is_holiday(current_date):
            remaining_days -= 1

    return current_date


# 테스트 코드
def test_get_eta_2023_12_01() -> None:
    result = get_eta(datetime(2023, 12, 1))
    assert result == datetime(2023, 12, 4)


def test_get_eta_2024_12_31() -> None:
    result = get_eta(datetime(2024, 12, 31))
    assert result == datetime(2025, 1, 2)


def teset_get_eta_2024_02_28() -> None:
    result = get_eta(datetime(2024, 2, 28))
    assert result == datetime(2024, 3, 1)


def test_get_eta_20223_02_28() -> None:
    result = get_eta(datetime(2023, 2, 28))
    assert result == datetime(2023, 3, 2)
