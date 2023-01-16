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
        st1.push(4);
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