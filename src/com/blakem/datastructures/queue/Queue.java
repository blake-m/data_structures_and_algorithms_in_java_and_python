/* An implementation of a queue with a doubly linked list. */

package com.blakem.datastructures.queue;
import java.util.Iterator;
import java.util.LinkedList;

public class Queue<T> implements Iterable<T> {

    private LinkedList<T> baseList = new LinkedList<T>();

    public Queue() {}

    public Queue(T firstElement) {
        enqueue(firstElement);
    }

    public int getSize() {
        return baseList.size();
    }

    // Check if the queue is empty (returns true for empty queue)
    public boolean isEmpty() {
        return getSize() == 0;
    }

    private void throwRuntimeErrorIfEmpty() throws RuntimeException {
        if (isEmpty()) {
            throw new RuntimeException("This Queue is Empty.");
        }
    }

    // Peek the first (at the front) element in the queue
    // Throw an error with an empty queue
    // Returns the element
    public T peekElementFront() throws RuntimeException {
        throwRuntimeErrorIfEmpty();
        return baseList.peekFirst();
    }

    // Peek the last (at the back) element in the queue
    // Throw an error with an empty queue
    // Returns the element
    public T peekElementBack() throws RuntimeException {
        throwRuntimeErrorIfEmpty();
        return baseList.peekLast();
    }

    // Remove an element at the front of the queue (following the FIFO - first in, first out)
    // Throw an error with an empty queue
    public T dequeueFront() throws RuntimeException {
        throwRuntimeErrorIfEmpty();
        return baseList.removeFirst();
    }

    // Add an element to the back of the queue
    public void enqueue(T element) {
        baseList.addLast(element);
    }

    // Return an iterator
    @Override
    public Iterator<T> iterator() {
        return baseList.iterator();
    }
}
