#ifndef QUEUE_H_
#define QUEUE_H_

#include <stdlib.h>
#include <stdio.h>

#define QUEUE_SIZE 10

template <class T>
class Queue
{
private:
    T *qu_array;
    int front;
    int back;
    int _size;

public:
    Queue(int = QUEUE_SIZE);
    ~Queue();

    void enqueue(const T &item);
    T *dequeue();
    const T *peek();

    bool isEmpty();
    bool isFull();
    int size() const;
    int capacity() const;
};

template <class T>
Queue<T>::Queue(int size) : _size(size), front(-1), back(-1), qu_array(new T[size]) {}

template <class T>
Queue<T>::~Queue()
{
    delete[] qu_array;
}

template <class T>
void Queue<T>::enqueue(const T &item)
{
    if (isFull())
    {
        fprintf(stderr, "Queue is Full");
        exit(EXIT_FAILURE);
    }

    if (isEmpty())
    {
        front++;
    }
    back++;
    qu_array[back] = item;
}

template <class T>
T *Queue<T>::dequeue()
{
    if (isEmpty())
        return nullptr;

    if (front == back)
    {
        int tmp = front;
        front = -1;
        back = -1;
        return &qu_array[tmp];
    }

    return &qu_array[front++];
}

template <class T>
const T *Queue<T>::peek()
{
    if (isEmpty())
    {
        return nullptr;
    }

    return &qu_array[front];
}

template <class T>
bool Queue<T>::isEmpty()
{
    return back == -1;
}

template <class T>
bool Queue<T>::isFull()
{
    return (back + 1) == _size;
}

/*returns total size of queue*/
template <class T>
int Queue<T>::capacity() const
{
    return _size;
}

/*returns capacity of queue usuage*/
template <class T>
int Queue<T>::size() const
{
    if (back == -1)
        return 0;

    if (front == back)
        return 1;

    if (front == 0)
        return back + 1;

    return (back - front + 1);
}

#endif