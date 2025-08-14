def add(a: int, b: int) -> int:
    return a + b


def mul(a: int, b: int) -> int:
    return a * b


def test_add() -> None:
    # Given
    a, b = 1, 1

    # When
    result = add(a, b)

    # Then
    assert result == 2
