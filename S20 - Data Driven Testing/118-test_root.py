import pytest
from root import root


@pytest.mark.parametrize(
    ("num", "num_root"),
    (
        (100, 10),
        (36, 6),
        (25, 5),
        (16, 4),
        (9, 3),
        (4, 2),
    )
)
def test_root(num, num_root):
    assert root(num) == num_root