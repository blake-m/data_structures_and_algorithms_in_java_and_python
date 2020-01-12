package com.blakem.datastructures.stack;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Iterator;

import static org.junit.jupiter.api.Assertions.*;

class StackTest {
    private Stack<Integer> testStack;

    @BeforeEach
    void setUp() {
        testStack = new Stack<Integer>();
    }

    @Test
    void getSizeEmptyStackTest() {
        assertEquals(0, testStack.getSize());
    }

    @Test
    void getSizeStackWithElementsTest() {
        testStack.pushElementOnTop(1);
        testStack.pushElementOnTop(2);
        testStack.pushElementOnTop(3);
        assertEquals(3, testStack.getSize());
    }

    @Test
    void isEmptyTest() {
        assertTrue(testStack.isEmpty());
    }

    @Test
    void isEmptyWithElementsTest() {
        testStack.pushElementOnTop(1);
        assertFalse(testStack.isEmpty());
    }

    @Test
    void pushElementOnTopTest() {
        testStack.pushElementOnTop(1);
        assertEquals(1, testStack.peekFirstElement());
    }

    @Test
    void popElementFromTopTest() {
        testStack.pushElementOnTop(1);
        var returnedElement = testStack.popElementFromTop();
        assertTrue(testStack.isEmpty());
        assertEquals(1, returnedElement);
    }

    @Test
    void popElementFromTopThrowsExceptionTest() {
        assertThrows(java.util.EmptyStackException.class,
                     testStack::popElementFromTop,
                     "This stack is EMPTY.");
    }

    @Test
    void peekFirstElementTest() {
        testStack.pushElementOnTop(1);
        assertEquals(1, testStack.peekFirstElement());
    }

    @Test
    void iteratorTest() {
        testStack.pushElementOnTop(1);
        testStack.pushElementOnTop(2);
        Iterator<Integer> iteratorStack = testStack.iterator();
        assertEquals(1, iteratorStack.next());
        assertEquals(2, iteratorStack.next());
    }
}