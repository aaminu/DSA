#ifndef QUEUE_H_
#define QUEUE_H_

#include <stdlib.h>
#include <stdio.h>

#define QUEUE_SIZE 10

template <class T>
class Queue
{
protected:
    T *qu_array;
    int front;
    int back;
    int _size;
    int _capacity;

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
Queue<T>::Queue(int size) : _capacity(size), front(-1), back(-1), qu_array(new T[size]), _size(0) {}

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
    _size++;
    back++;
    qu_array[back] = item;
}

template <class T>
T *Queue<T>::dequeue()
{
    if (isEmpty())
        return nullptr;

    _size--;
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
    return (back + 1) == _capacity;
}

/*returns total size of queue*/
template <class T>
int Queue<T>::capacity() const
{
    return _capacity;
}

/*returns capacity of queue usuage*/
template <class T>
int Queue<T>::size() const
{
    return _size;
}

//----------------------------- CIRCULAR QUEUE -----------------------------------//
template <class T>
class CircularQueue : public Queue<T>
{
public:
    using Queue<T>::Queue; // Using Queue Constructors

    bool isFull();

    void enqueue(const T &item);
    T *dequeue();
};

template <class T>
bool CircularQueue<T>::isFull()
{
    if ((this->back + 1) == this->_capacity && this->front == 0)
    {
        return true;
    }

    if (this->front == this->back + 1)
    {
        return true;
    }

    return false;
}

template <class T>
void CircularQueue<T>::enqueue(const T &item)
{
    if (isFull())
    {
        fprintf(stderr, "Queue is Full");
        exit(EXIT_FAILURE);
    }

    if (this->isEmpty())
    {
        this->front++;
    }
    this->_size++;
    this->back = (this->back + 1) % this->_capacity;
    this->qu_array[this->back] = item;
}

template <class T>
T *CircularQueue<T>::dequeue()
{
    if (this->isEmpty())
        return nullptr;

    this->_size--;
    if (this->front == this->back)
    {
        int tmp = this->front;
        this->front = -1;
        this->back = -1;
        return &this->qu_array[tmp];
    }
    int tmp = this->front;
    this->front = (this->front + 1) % this->_capacity;
    return &this->qu_array[tmp];
}

#endif