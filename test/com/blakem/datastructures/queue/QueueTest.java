package com.blakem.datastructures.queue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Iterator;

class QueueTestEmptyList {

    private Queue<Integer> queue;

    @BeforeEach
    public void setUp() {
        queue = new Queue<Integer>();
    }

    @Test
    void getSizeTest() {
        assertEquals(0, queue.getSize());
    }

    @Test
    void isEmptyTest() {
        assertTrue(queue.isEmpty());
    }

    @Test
    void peekElementFrontTest() {
        assertThrows(RuntimeException.class,
                queue::peekElementFront,
                "This Queue is Empty.");
    }

    @Test
    void peekElementBackTest() {
        assertThrows(RuntimeException.class,
                queue::peekElementBack,
                "This Queue is Empty.");
    }

    @Test
    void dequeueFrontTest() {
        assertThrows(RuntimeException.class,
                queue::dequeueFront,
                "This Queue is Empty.");
    }

    @Test
    void enqueueTest() {
        queue.enqueue(1);
        assertEquals(1, queue.getSize());
        assertEquals(1, queue.peekElementFront());
        assertEquals(1, queue.peekElementBack());
    }

    @Test
    void iteratorTest() {
        Iterator<Integer> queueIterator = queue.iterator();
        assertFalse(queueIterator.hasNext());
    }
}

class QueueTestWithElements {

    private Queue<Integer> queue;

    @BeforeEach
    public void setUp() {
        queue = new Queue<Integer>();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
    }

    @Test
    void getSizeTest() {
        assertEquals(3, queue.getSize());
    }

    @Test
    void isEmptyTest() {
        assertFalse(queue.isEmpty());
    }

    @Test
    void peekElementFrontTest() {
        assertEquals(1, queue.peekElementFront());
    }

    @Test
    void peekElementBackTest() {
        assertEquals(3, queue.peekElementBack());
    }

    @Test
    void dequeueFrontDecreasesSizeTest() {
        queue.dequeueFront();
        assertEquals(2, queue.getSize());
    }

    @Test
    void dequeueFrontRemovesElementTest() {
        assertEquals(1, queue.dequeueFront());
    }

    @Test
    void enqueueIncreasesSizeTest() {
        queue.enqueue(4);
        assertEquals(4, queue.getSize());
    }

    @Test
    void enqueueAddsElementTest() {
        queue.enqueue(4);
        assertEquals(4, queue.peekElementBack());
    }

    @Test
    void iteratorTest() {
        Iterator<Integer> queueIterator = queue.iterator();
    }
}