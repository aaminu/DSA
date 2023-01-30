from data_structures.stack import Stack
from data_structures.queue import Queue, Deque

########################## Stack #########################


def test_stack_1():
    # Gather
    st = Stack(int, 5)
    st.push(5)
    st.push(7)
    st.push(8)
    st.push(1)

    # Act
    response1 = st.pop()
    response2 = st.pop()
    response3 = st.peek()
    response4 = st.pop()

    # Asset
    assert response1 == 1
    assert response2 == 8
    assert response3 == response4


def test_stack_2():

    # Gather
    st = Stack(float, 3)

    # Act
    try:
        st.push(1.0)
        st.push(2.567)
        st.push(1)
    except TypeError as t:
        response1 = str(t)

    try:
        st.push(5.0)
        st.push(3.5)
    except ValueError as v:
        response2 = str(v)

    # Asset
    assert response1 == "Item should be of type <class 'float'>"
    assert response2 == "Stack is Full"


########################## Queue #########################
def test_queue_1():
    # Gather
    qu = Queue(int, 5)
    qu.enqueue(5)
    qu.enqueue(7)
    qu.enqueue(8)
    qu.enqueue(1)

    # Act
    response1 = qu.dequeue()
    response2 = qu.dequeue()
    response3 = qu.peek()
    response4 = qu.dequeue()

    # Asset
    assert response1 == 5
    assert response2 == 7
    assert response3 == response4


def test_queue_2():

    # Gather
    qu = Queue(float, 3)

    # Act
    try:
        qu.enqueue(1.0)
        qu.enqueue(2.567)
        qu.enqueue(1)
    except TypeError as t:
        response1 = str(t)

    try:
        qu.enqueue(5.0)
        qu.enqueue(3.5)
    except ValueError as v:
        response2 = str(v)

    # Asset
    assert response1 == "Item should be of type <class 'float'>"
    assert response2 == "Queue is Full"

######################### Deque #########################


def test_deque_1():
    # Gather
    dqu = Deque(int, 10)
    dqu.add_front(5)
    dqu.add_front(7)
    dqu.add_back(8)
    dqu.add_back(1)
    dqu.enqueue(3)  # Same as add_back

    # Act
    response1 = dqu.size()
    response2 = dqu.pop_front()
    response3 = dqu.pop_back()
    response4 = dqu.peek()
    response5 = dqu.pop_front()

    # Asset
    assert response1 == 5
    assert response2 == 7
    assert response3 == 3
    assert response4 == response5


def test_deque_2():

    # Gather
    qu = Deque(float, 3)

    # Act
    try:
        qu.add_back(1.0)
        qu.add_back(2.567)
        qu.add_back(1)
    except TypeError as t:
        response1 = str(t)

    try:
        qu.enqueue(5.0)
        qu.enqueue(3.5)
    except ValueError as v:
        response2 = str(v)

    # Asset
    assert response1 == "Item should be of type <class 'float'>"
    assert response2 == "Deque is Full"
