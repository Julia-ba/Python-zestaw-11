import pytest
from singlelist_11_1 import SingleList, Node


@pytest.fixture
def list3():
    sl = SingleList()
    sl.insert_tail(Node(1))
    sl.insert_tail(Node(2))
    sl.insert_tail(Node(3))
    return sl


def test_remove_tail(list3):
    removed = list3.remove_tail()
    assert removed.data == 3
    assert list3.length == 2
    assert list(list3) == [1, 2]
    assert list3.tail.data == 2


def test_remove_tail_single_element():
    sl = SingleList()
    sl.insert_tail(Node(10))
    removed = sl.remove_tail()
    assert removed.data == 10
    assert sl.is_empty()
    assert sl.head is None
    assert sl.tail is None


def test_remove_tail_empty():
    sl = SingleList()
    with pytest.raises(ValueError):
        sl.remove_tail()


def test_join():
    l1 = SingleList()
    l1.insert_tail(Node(1))
    l2 = SingleList()
    l2.insert_tail(Node(2))

    l1.join(l2)
    assert list(l1) == [1, 2]
    assert l1.length == 2
    assert l2.is_empty()
    assert l2.head is None


def test_clear(list3):
    list3.clear()
    assert list3.is_empty()
    assert list3.length == 0
    assert list3.head is None
    assert list3.tail is None