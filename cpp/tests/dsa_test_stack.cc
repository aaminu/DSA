#include "../src/stack_.h"

#include "gtest/gtest.h"

// Fixture
class IntStackTest : public ::testing::Test
{
protected:
    void SetUp() override
    {
        st1.push(1);
        st1.push(2);
        st1.push(3);
        st1.push(5);
        st1.push(4);
    }

    Stack<int> st1 = Stack<int>(5);
    Stack<int> st2 = Stack<int>(2);
};

// Test for Emptiness and Null return
TEST_F(IntStackTest, EmptyNullTest)
{
    // check size
    EXPECT_EQ(st2.size(), 0);

    // check retrun of null if empty and poped
    int *n = st2.pop();
    EXPECT_EQ(n, nullptr);
}

// Check for Capacity
TEST_F(IntStackTest, StackFullTest)
{
    // Check that stack is filled
    EXPECT_EQ(st1.size(), st1.capacity());

    // Check using helper method
    EXPECT_EQ(st1.isFull(), true);
}

TEST_F(IntStackTest, PopWorks)
{
    int *n = st1.pop();
    ASSERT_NE(n, nullptr);
    EXPECT_EQ(*n, 4);
    EXPECT_EQ(*st1.pop(), 5);
}

TEST_F(IntStackTest, PushWorks)
{
    st2.push(1);
    st2.push(2);
    EXPECT_EQ(st2.size(), 2);

    EXPECT_EXIT(st1.push(5), testing::ExitedWithCode(1), "Stack is Full");
}

TEST_F(IntStackTest, PeekWorks)
{
    const int *n = st1.peek();
    ASSERT_NE(n, nullptr);
    EXPECT_EQ(*n, 4);
    EXPECT_EQ(st1.size(), 5);

    const int *m = st2.peek();
    EXPECT_EQ(m, nullptr);
}