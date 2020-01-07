/**
 * An implementation of doubly linked list.
 * Comments here are not necessary - just for learning purpose
 * and further reference.
 */

package com.blakem.datastructures.doublylinkedlist;

public class DoublyLinkedList<T> implements Iterable<T> {
    private int size = 0;
    private Node<T> head = null;
    private Node<T> tail = null;

    private static class Node<T> {
        private T data;
        private Node<T> prev, next;

        public Node(T data, Node<T> prev, Node<T> next) {
            this.data = data;
            this.prev = prev;
            this.next = next;
        }

        @Override
        public String toString() {
            return data.toString();
        }
    }

    // Constructor: Empty list
    DoublyLinkedList() {}

    // Constructor: 1 element
    DoublyLinkedList(T firstElement) {
        addFirst(firstElement);
    }

    DoublyLinkedList(T[] listOfElements) {
        for (T element: listOfElements) {
            addLast(element);
        };
    }

    // O(1)
    public int getSize() {
        return size;
    }

    // O(1)
    public boolean isEmpty() {
        return getSize() == 0;
    }

    // O(1)
    public void addFirst(T elem) {
        if (this.isEmpty()) {
            this.head = this.tail = new Node<T>(elem, null, null);
        } else {
            Node<T> next = this.head;
            this.head = new Node<T>(elem, null, null);
            next.prev = this.head;
            this.head.next = next;

            // Could be simplified to
                // head.prev = new Node<T>(elem, null, head);
                // head = head.prev;
        }
        size++;
    }

    // O(1)
    public void addLast(T elem) {
        if (this.isEmpty()) {
            this.head = this.tail = new Node<T>(elem, null, null);
        } else {
            this.tail.next = new Node<T>(elem, this.tail, null);
            this.tail = this.tail.next;
        }
        size++;
    }

    // Empty this linked list, O(n)
    public void clear() {
        while (this.head.next != null) {
            Node<T> next = this.head.next;
            this.head.next = null;
            this.head.data = null;
            next.prev = null;
            this.head = next;
        }
        this.tail = this.head = null;
        size = 0;
    }

    // O(1)
    public T checkFirst() {
        if (isEmpty()) throw new RuntimeException("This list is EMPTY.");
        return head.data;
    }

    // O(1)
    public T checkLast() {
        if (isEmpty()) throw new RuntimeException("This list is EMPTY.");
        return tail.data;
    }

    public T checkAt(int index) {
        if (isEmpty()) throw new RuntimeException("This list is EMPTY.");
        T dataAtIndex = getNodeAtIndex(index).data;
        return dataAtIndex;
    }

    // Remove the first value at the head of the linked list, O(1)
    public T removeFirst() {
        if (isEmpty()) throw new RuntimeException("This list is EMPTY.");

        T removedElement = this.head.data;
        this.head = this.head.next;

        this.size--;

        if (isEmpty()) this.tail = null;
        else this.head.prev = null;

        return removedElement;
    }

    // (1)
    public T removeLast() {
        if (isEmpty()) throw new RuntimeException("This list is EMPTY.");

        T removedElement = this.tail.data;
        this.tail = this.tail.prev;

        this.size--;

        if (isEmpty()) this.head = null;
        else this.tail.next = null;

        return removedElement;
    }

    boolean checkIfIndexIsCorrect(int index) {
        if (index >= size) throw new IllegalArgumentException("Index out of scope.");
        if (index < 0) throw new IllegalArgumentException("Index smaller than 0.");
        return true;
    }

    private Node<T> getNodeAtIndex(int index) {
        checkIfIndexIsCorrect(index);
        Node<T> finalNode = this.head;
        for (int i = 0; i < index; i++) {
            finalNode = finalNode.next;
        }
        return finalNode;
    }

    // O(n)
    // TO DO: Check this one - it's wrong
    public T removeAt(int index) {
        Node<T> nodeToRemove = getNodeAtIndex(index);

        if (nodeToRemove.prev != null) {
            Node<T> previousNode = nodeToRemove.prev;
            previousNode.next = nodeToRemove.next;
        } else {
            this.head = nodeToRemove.next;
            Node<T> previousNode = null;
        }

        if (nodeToRemove.next != null) {
            Node<T> nextNode = nodeToRemove.next;
            nextNode.prev = nodeToRemove.prev;
        } else {
            this.tail = nodeToRemove.prev;
            this.tail.next = null;
        }

        T removedData = nodeToRemove.data;
        nodeToRemove.data = null;
        nodeToRemove.prev = nodeToRemove.next = null;

        this.size--;

        return removedData;
    }

    public void insertObjectAt(int index, T object) {
        getNodeAtIndex(index);
    }

    @Override
    public java.util.Iterator<T> iterator() {
        return new java.util.Iterator<T>() {
            private Node<T> trav = head;

            @Override
            public boolean hasNext() {
                return trav != null;
            }

            @Override
            public T next() {
                T data = trav.data;
                trav = trav.next;
                return data;
            }

            @Override
            public void remove() {
                throw new UnsupportedOperationException();
            }
        };
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        Node<T> trav = head;
        while (trav != null) {
            sb.append(trav.data).append(", ");
            trav = trav.next;
        }
        sb.append(" ]");
        return sb.toString();
    }

}