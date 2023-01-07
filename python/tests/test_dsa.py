from data_structures.stack import Stack
from data_structures.queue import Queue

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
