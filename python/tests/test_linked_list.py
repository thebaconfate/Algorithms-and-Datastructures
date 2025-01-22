import pytest
import ad.linked_list as ll


@pytest.fixture
def setup_list() -> list[int]:
    "Testing list"
    return [1, 2, 3, 4, 5, 6]


def test_empty_list():
    empty_list = ll.empty_list()
    assert isinstance(empty_list, list)
    assert len(empty_list) == 0


def test_create_list(setup_list: list[int]):
    lst = ll.create_list(*setup_list)
    assert lst == setup_list


def test_is_empty(setup_list: list[int]):
    assert ll.is_empty([])
    assert not ll.is_empty(setup_list)


def test_cons(setup_list: list[int]):
    assert ll.cons(0, setup_list) == [0] + setup_list


def test_update(setup_list: list[int]):
    assert ll.update(0, 0, setup_list) == [0] + setup_list[1:]
    with pytest.raises(IndexError):
        ll.update(1, -1, setup_list)


def test_reverse(setup_list):
    assert ll.reverse(setup_list) == setup_list[::-1]


def test_filter_list(setup_list):
    assert ll.filter_list(lambda x: x % 2 == 0, setup_list) == [
        x for x in setup_list if x % 2 == 0
    ]


def test_map_list(setup_list):
    assert ll.map_list(lambda x: x**2, setup_list) == [x**2 for x in setup_list]


def test_for_each(setup_list):
    target = "".join(map(str, setup_list))
    curr = ""

    def update_curr(val):
        nonlocal curr
        curr = curr + str(val)

    assert ll.for_each(lambda x: update_curr(x), setup_list) is None
    assert curr == target


def test_concat(setup_list):
    assert (
        ll.concat(setup_list, ll.reverse(setup_list)) == setup_list + setup_list[::-1]
    )


def test_append(setup_list):
    assert ll.append(7, setup_list) == setup_list + [7]
