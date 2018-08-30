from typing import List


def length(string: str) -> int:
    pass


def character_code(char: str) -> int:
    pass


def addition(first_number: int, second_number: int) -> int:
    pass


def multiply(first_number: int, second_number: int) -> int:
    pass


def lowercase(string: str) -> str:
    pass


def uppercase(string: str) -> str:
    pass


def remove_first_slice(array: List[int]) -> List[int]:
    pass


def remove_first_pop(array: List[int]) -> List[int]:
    pass


def remove_first_delete(array: List[int]) -> List[int]:
    pass


assert length("Testwords") == 9
assert length("What goes here") == 14
assert character_code("a") == 97
assert character_code("😋") == 128523
assert addition(5, 10) == 15
assert addition(50, 5) == 55
assert multiply(50, 1) == 50
assert multiply(50, 5) == 250
assert lowercase("no idea") == "no idea"
assert lowercase("Tests") == "tests"
assert uppercase("HmmWhatsThis") == "HMMWHATSTHIS"
assert uppercase("words") == "WORDS"
assert remove_first_slice([2, 3, 5, 6]) == [3, 5, 6]
assert remove_first_pop([2, 3, 5, 6]) == [3, 5, 6]
assert remove_first_delete([2, 3, 5, 6]) == [3, 5, 6]

print("All done :)")
