#include "../src/queue_.h"

#include "gtest/gtest.h"

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
