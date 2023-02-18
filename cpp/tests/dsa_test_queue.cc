#include "../src/queue_.h"
#include "../src/deque_.h"

#include "gtest/gtest.h"

/*  Queue Tests*/
class QueueTest : public ::testing::Test
{
protected:
    void SetUp() override
    {
        // q0_ remains empty
        q1_.enqueue(1);
        q2_.enqueue(2);
        q2_.enqueue(3);
    }

    // void TearDown() override {}

    Queue<int> q0_;
    Queue<int> q1_ = Queue<int>(4);
    Queue<int> q2_ = Queue<int>(3);
};

TEST_F(QueueTest, IsEmptyInitially)
{
    EXPECT_EQ(q0_.size(), 0);
}

TEST_F(QueueTest, QueueCapacity)
{
    EXPECT_EQ(q0_.capacity(), 10);
}

TEST_F(QueueTest, DequeueWorks)
{
    EXPECT_EQ(q0_.dequeue(), nullptr);

    int *n = q1_.dequeue();
    ASSERT_NE(n, nullptr);
    EXPECT_EQ(*n, 1);
    EXPECT_EQ(q1_.size(), 0);

    n = q2_.dequeue();
    ASSERT_NE(n, nullptr);
    EXPECT_EQ(*n, 2);
    EXPECT_EQ(q2_.size(), 1);
}

TEST_F(QueueTest, EnqueueWorks)
{

    q0_.enqueue(2);
    q0_.enqueue(3);
    EXPECT_EQ(q0_.size(), 2);

    q1_.enqueue(2);
    q1_.enqueue(3);
    EXPECT_EQ(q1_.size(), 3);
}

TEST_F(QueueTest, PeekWorks)
{

    const int *n = q1_.peek();
    ASSERT_NE(n, nullptr);
    EXPECT_EQ(*n, 1);
    EXPECT_EQ(q1_.size(), 1);

    q2_.dequeue();
    const int *m = q2_.peek();
    ASSERT_NE(m, nullptr);
    EXPECT_EQ(*m, 3);
    EXPECT_EQ(q2_.size(), 1);
}

TEST_F(QueueTest, IsFullWorks)
{

    q2_.enqueue(3);
    EXPECT_EQ(q2_.isFull(), true);
    EXPECT_EQ(q2_.size(), 3);
}

/* Circular Queue Tests*/
class CircularQueueTest : public ::testing::Test
{
protected:
    void SetUp() override
    {
        // q0_ remains empty
        q1_.enqueue(1);
        q2_.enqueue(2);
        q2_.enqueue(3);
        q2_.enqueue(4);
        q2_.enqueue(5);
    }

    // void TearDown() override {}

    CircularQueue<int> q0_;
    CircularQueue<int> q1_ = CircularQueue<int>(4);
    CircularQueue<int> q2_ = CircularQueue<int>(5);
};

TEST_F(CircularQueueTest, IsEmptyInitially)
{
    EXPECT_EQ(q0_.size(), 0);
}

TEST_F(CircularQueueTest, QueueCapacity)
{
    EXPECT_EQ(q0_.capacity(), 10);
}

TEST_F(CircularQueueTest, DequeueWorks)
{
    EXPECT_EQ(q0_.dequeue(), nullptr);

    int *n = q1_.dequeue();
    ASSERT_NE(n, nullptr);
    EXPECT_EQ(*n, 1);
    EXPECT_EQ(q1_.size(), 0);

    n = q2_.dequeue();
    ASSERT_NE(n, nullptr);
    EXPECT_EQ(*n, 2);
    EXPECT_EQ(q2_.size(), 3);
}

TEST_F(CircularQueueTest, EnqueueWorks)
{

    q0_.enqueue(2);
    q0_.enqueue(3);
    EXPECT_EQ(q0_.size(), 2);

    q1_.enqueue(2);
    q1_.enqueue(3);
    EXPECT_EQ(q1_.size(), 3);
}

TEST_F(CircularQueueTest, PeekWorks)
{

    const int *n = q1_.peek();
    ASSERT_NE(n, nullptr);
    EXPECT_EQ(*n, 1);
    EXPECT_EQ(q1_.size(), 1);

    q2_.dequeue();
    const int *m = q2_.peek();
    ASSERT_NE(m, nullptr);
    EXPECT_EQ(*m, 3);
    EXPECT_EQ(q2_.size(), 3);
}

TEST_F(CircularQueueTest, IsFullWorks)
{
    q2_.enqueue(3);
    EXPECT_EQ(q2_.isFull(), true);
    EXPECT_EQ(q2_.size(), 5);
    EXPECT_EXIT(q2_.enqueue(5), testing::ExitedWithCode(1), "Queue is Full");
}

TEST_F(CircularQueueTest, CircularWorks)
{
    q2_.enqueue(3); // Queue Full here
    q2_.dequeue();  // Remove two items
    q2_.dequeue();
    q2_.enqueue(1); // Add two Items back at the removed placed
    q2_.enqueue(2);
    EXPECT_EQ(q2_.isFull(), true);
    EXPECT_EQ(q2_.size(), 5);
    EXPECT_EXIT(q2_.enqueue(5), testing::ExitedWithCode(1), "Queue is Full");
}

/* Deque Tests*/
class DequeTest : public ::testing::Test
{
protected:
    void SetUp() override
    {
        // q0_ remains empty
        q1_.pushFront(1);
        q2_.pushFront(2);
        q2_.pushBack(3);
        q2_.pushFront(4);
        q2_.pushFront(5);
    }

    // void TearDown() override {}

    Deque<int> q0_;
    Deque<int> q1_ = Deque<int>(4);
    Deque<int> q2_ = Deque<int>(5);
};

TEST_F(DequeTest, IsEmptyInitially)
{
    EXPECT_EQ(q0_.size(), 0);
}

TEST_F(DequeTest, QueueCapacity)
{
    EXPECT_EQ(q0_.capacity(), 10);
}

TEST_F(DequeTest, PopWorks)
{
    EXPECT_EQ(q0_.popBack(), nullptr);

    int *n = q1_.popBack();
    ASSERT_NE(n, nullptr);
    EXPECT_EQ(*n, 1);
    EXPECT_EQ(q1_.size(), 0);
    n = q1_.popFront();
    EXPECT_EQ(n, nullptr);

    n = q2_.popBack();
    ASSERT_NE(n, nullptr);
    EXPECT_EQ(*n, 3);
    EXPECT_EQ(q2_.size(), 3);
    q2_.popFront();
    n = q2_.popFront();
    ASSERT_NE(n, nullptr);
    EXPECT_EQ(*n, 4);
    EXPECT_EQ(q2_.size(), 1);
}

TEST_F(DequeTest, PushPeekWorks)
{
    q0_.pushFront(2);
    q0_.pushFront(3);
    q0_.pushFront(4);
    EXPECT_EQ(q0_.size(), 3);
    EXPECT_EQ(*q0_.peekFront(), 4);
    EXPECT_EQ(*q0_.peekBack(), 2);

    q1_.pushBack(2);
    q1_.pushBack(3);
    EXPECT_EQ(q1_.size(), 3);
    EXPECT_EQ(*q1_.peekFront(), 1);
    EXPECT_EQ(*q1_.peekBack(), 3);
}

TEST_F(DequeTest, IsFullWorks)
{
    q2_.pushBack(3);
    EXPECT_EQ(q2_.isFull(), true);
    EXPECT_EQ(q2_.size(), 5);
    EXPECT_EXIT(q2_.pushFront(5), testing::ExitedWithCode(1), "Deque is Full");
}
