from tests import test_cases
from algos import quick_sort

for test_case in test_cases:
    assert quick_sort(test_case.input) == test_case.output, f"Failed on {test_case}"
