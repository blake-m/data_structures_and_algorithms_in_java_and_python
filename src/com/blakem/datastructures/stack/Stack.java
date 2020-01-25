/* An implementation of a stack with a doubly linked list. */

package com.blakem.datastructures.stack;

import java.util.Iterator;
import java.util.LinkedList;

public class Stack<T> implements Iterable<T> {

    private LinkedList<T> stackList = new LinkedList<T>();

    public Stack() {}

    public Stack(T initialElement) {
        pushElementOnTop(initialElement);
    }

    public int getSize() {
        return stackList.size();
    }

    public boolean isEmpty() {
        return getSize() == 0;
    }

    public void pushElementOnTop(T element) {
        stackList.addLast(element);
    }

    public T popElementFromTop() {
        if (isEmpty()) throw new java.util.EmptyStackException();
        return stackList.removeLast();
    }

    public T peekFirstElement() {
        if (isEmpty()) throw new java.util.EmptyStackException();
        return stackList.peekLast();
    }

    @Override
    public Iterator<T> iterator() {
        return stackList.iterator();
    }
}
