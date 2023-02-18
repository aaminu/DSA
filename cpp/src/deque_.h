#ifndef DEQUE_H_
#define DEQUE_H_

#include <stdlib.h>
#include <stdio.h>

#define QUEUE_SIZE 10

template <class T>
class Deque
{
protected:
    T *qu_array;
    int front;
    int back;
    int _size;
    int _capacity;

public:
    Deque(int = QUEUE_SIZE);
    ~Deque();

    void pushFront(const T &item);
    void pushBack(const T &item);
    T *popFront();
    T *popBack();
    const T *peekFront();
    const T *peekBack();

    bool isEmpty();
    bool isFull();
    int size() const;
    int capacity() const;
};

template <class T>
Deque<T>::Deque(int size) : _capacity(size), front(-1), back(-1), qu_array(new T[size]), _size(0) {}

template <class T>
Deque<T>::~Deque()
{
    delete[] qu_array;
}

template <class T>
void Deque<T>::pushFront(const T &item)
{
    if (isFull())
    {
        fprintf(stderr, "Deque is Full");
        exit(EXIT_FAILURE);
    }

    if (isEmpty())
    {
        _size++;
        front++;
        back++;
        qu_array[front] = item;
        return;
    }
    _size++;
    if (front == 0)
    {
        front = _capacity - 1;
        qu_array[front] = item;
        return;
    }

    qu_array[--front] = item;
}

template <class T>
void Deque<T>::pushBack(const T &item)
{
    if (isFull())
    {
        fprintf(stderr, "Deque is Full");
        exit(EXIT_FAILURE);
    }

    if (isEmpty())
    {
        _size++;
        front++;
        back++;
        qu_array[back] = item;
        return;
    }

    _size++;
    if (back == _capacity - 1)
    {
        back = 0;
        qu_array[back] = item;
        return;
    }

    qu_array[++back] = item;
}

template <class T>
T *Deque<T>::popFront()
{
    if (isEmpty())
        return nullptr;

    if (_size == 1)
    {
        _size--;
        T *tmp = &qu_array[front];
        front = -1;
        back = -1;
        return tmp;
    }

    _size--;
    if (front == _capacity - 1)
    {
        T *tmp = &qu_array[front];
        front = 0;
        return tmp;
    }

    return &qu_array[front++];
}

template <class T>
T *Deque<T>::popBack()
{
    if (isEmpty())
        return nullptr;

    if (_size == 1)
    {
        _size--;
        T *tmp = &qu_array[back];
        front = -1;
        back = -1;
        return tmp;
    }
    _size--;
    if (back == _capacity - 1)
    {
        T *tmp = &qu_array[back];
        back = 0;
        return tmp;
    }

    return &qu_array[back--];
}

template <class T>
const T *Deque<T>::peekFront()
{
    if (isEmpty())
        return nullptr;

    return &qu_array[front];
}

template <class T>
const T *Deque<T>::peekBack()
{
    if (isEmpty())
        return nullptr;

    return &qu_array[back];
}

template <class T>
bool Deque<T>::isEmpty()
{
    return (front == -1) && (_size == 0);
}

template <class T>
bool Deque<T>::isFull()
{
    return ((back + 1) == _capacity && front == 0) || ((back + 1 == front));
}

/*returns total size of deque*/
template <class T>
int Deque<T>::capacity() const
{
    return _capacity;
}

/*returns capacity of deque usuage*/
template <class T>
int Deque<T>::size() const
{
    return _size;
}

#endif