#ifndef STACK_H_
#define STACK_H_

#include <stdlib.h>

#define STACK_SIZE 10

template <class T>
class Stack
{
private:
    T *st_array;
    int top;
    int _size;

public:
    Stack(int size = STACK_SIZE);
    ~Stack();

    void push(T item);
    T pop();
    const T *peek();

    bool isEmpty();
    bool isFull();
    int size() const;
    int capacity() const;
};

template <class T>
Stack<T>::Stack(int size)
{
    _size = size;
    st_array = new T[size];
    top = -1;
}

template <class T>
Stack<T>::~Stack()
{
    delete[] st_array;
}

template <class T>
bool Stack<T>::isEmpty()
{
    return top == -1;
}

template <class T>
bool Stack<T>::isFull()
{
    return (top + 1) == _size;
}

/*returns total size of stack*/
template <class T>
int Stack<T>::size() const
{
    return _size;
}

/*returns capacity of stack usuage*/
template <class T>
int Stack<T>::capacity() const
{
    return top + 1;
}

template <class T>
void Stack<T>::push(T item)
{
    if (isFull())
    {
        exit(EXIT_FAILURE);
    }
    top++;
    st_array[top] = item;
}

template <class T>
T Stack<T>::pop()
{
    if (isEmpty())
    {
        exit(EXIT_FAILURE);
    }
    return st_array[top--];
}

template <class T>
const T *Stack<T>::peek()
{
    if (isEmpty())
    {
        exit(EXIT_FAILURE);
    }

    return st_array + top;
}

#endif