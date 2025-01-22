from typing import Any, Callable, Never


def empty_list() -> list[Never]:
    """Returns an empty list"""
    return []


def create_list(*args: Any) -> list[Any]:
    return list(args)


def is_empty(lst: list[Any]) -> bool:
    """Checks if the list is empty, returns a boolean"""
    return len(lst) == 0


def cons(element: Any, lst: list[Any]) -> list[Any]:
    """Adds an element in front of the list"""
    return [element] + lst


def update(new_value: Any, index: int, lst: list[Any]) -> list[Any]:
    """Updates the list at a given non-negative index with a given value"""
    if index < 0:
        raise IndexError("The index must be positive")
    else:
        return [new_value if i == index else x for i, x in enumerate(lst)]


def reverse(lst: list[Any]) -> list[Any]:
    """Reverses the list"""
    return lst[::-1]


def filter_list(predicate: Callable[[Any], bool], lst: list[Any]) -> list[Any]:
    """Returns a list with all elements that meet a certain predicate"""
    return [x for x in lst if predicate(x)]


def map_list(function: Callable[[Any], Any], lst: list[Any]) -> list[Any]:
    """Returns a list where a function has been applied to all elements"""
    return [function(x) for x in lst]


def for_each(function: Callable[[Any], Any], lst: list[Any]) -> None:
    """Applies a function to a all elements of a list"""
    for el in lst:
        function(el)


def concat(lst1: list[Any], lst2: list[Any]) -> list[Any]:
    """Concatenates two lists together"""
    return lst1 + lst2


def append(element: Any, lst: list[Any]) -> list[Any]:
    """Appends an element to the list"""
    return lst + [element]
