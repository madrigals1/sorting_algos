from dataclasses import dataclass
from typing import List


@dataclass
class TestCase:
    input: List[int]
    output: List[int]

    def __str__(self):
        return f"Input: {self.input}, Output: {self.output}"

test_cases = [
    TestCase(input = [12, 4, 5, 6, 7, 3, 1, 15], output = [1, 3, 4, 5, 6, 7, 12, 15]),
    TestCase(input = [1], output = [1]), 
    TestCase(input = [1, 2, 3], output = [1, 2, 3]),
    TestCase(input = [], output = []),
]
