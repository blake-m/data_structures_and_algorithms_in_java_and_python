package com.blakem.datastructures.stack;

import org.junit.jupiter.api.Test;

import java.util.Iterator;

import static org.junit.jupiter.api.Assertions.*;

class StackTest {

    @Test
    void getSizeTest() {
        Stack<Integer> testStack =  new Stack<Integer>();
        assertEquals(0, testStack.getSize());
        testStack.pushElementOnTop(1);
        testStack.pushElementOnTop(2);
        testStack.pushElementOnTop(3);
        assertEquals(3, testStack.getSize());
    }

    @Test
    void isEmptyTest() {
        Stack<Integer> testStack =  new Stack<Integer>();
        assertTrue(testStack.isEmpty());
    }

    @Test
    void pushElementOnTopTest() {
        Stack<Integer> testStack =  new Stack<Integer>();
        testStack.pushElementOnTop(1);
        assertEquals(1, testStack.peekFirstElement());
    }

    @Test
    void popElementFromTopTest() {
        Stack<Integer> testStack =  new Stack<Integer>();
        testStack.pushElementOnTop(1);
        var returnedElement = testStack.popElementFromTop();
        assertTrue(testStack.isEmpty());
        assertEquals(1, returnedElement);

    }

    @Test
    void popElementFromTopThrowsExceptionTest() {
        Stack<Integer> testStack =  new Stack<Integer>();
        assertThrows(java.util.EmptyStackException.class,
                     testStack::popElementFromTop,
                     "This stack is EMPTY.");
    }

    @Test
    void peekFirstElementTest() {
        Stack<Integer> testStack =  new Stack<Integer>();
        testStack.pushElementOnTop(1);
        assertEquals(1, testStack.peekFirstElement());
    }

    @Test
    void iteratorTest() {
        Stack<Integer> testStack =  new Stack<Integer>();
        testStack.pushElementOnTop(1);
        testStack.pushElementOnTop(2);
        Iterator<Integer> iteratorStack = testStack.iterator();
        assertEquals(1, iteratorStack.next());
        assertEquals(2, iteratorStack.next());
    }
}