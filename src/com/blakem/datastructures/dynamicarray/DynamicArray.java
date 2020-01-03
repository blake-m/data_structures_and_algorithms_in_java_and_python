/*
 * An implementation of dynamic array.
 * Huge thanks to William Fisset who is a great DS & Algorithms teacher.
 */
package com.blakem.datastructures.dynamicarray;

@SuppressWarnings("unchecked")
public class DynamicArray<T> implements Iterable<T> {
    private T[] arr;
    private int len = 0; // Length revealed to users
    private int capacity = 0; // Actual length

    public DynamicArray() {
        this(16);
    }

    public DynamicArray(int capacity) {
        if (capacity < 0) throw new IllegalArgumentException("Capacity can't be lower than 0");
        this.capacity = capacity;
        arr = (T[]) new Object[capacity];
    }

    public int size() {
        return len;
    }

    public boolean isEmpty() {
        return len == 0;
    }

    public T get(int index) {
        return arr[index];
    }

    public void set(int index, T elem) {
        arr[index] = elem;
    }

    public void clear() {
        for (int i = 0; i < len; i++) {
            arr[i] = null;
        }
        len = 0;
    }

    public void add(T elem) {
        // If length + 1 is the same capacity: it's time to resize.
        // I double the size of the static array - it could be anything
        // else that increases the capacity of the array.
        if (capacity == len+1) {
            if (capacity == 0) capacity = 1;
            else capacity *= 2;
            // Create a new static array (twice as big)
            // Copy all elements into it
            T[] doubledArray = (T[]) new Object[capacity];
            for (int i = 0; i < len; i++) {
                doubledArray[i] = arr[i];
            }
            arr = doubledArray;
        }
        arr[len++] = elem;
    }

    public T removeAtIndex(int remove_at) {
        if (remove_at >= len) {
            throw new IndexOutOfBoundsException();
        }
        T elem_to_remove = arr[remove_at];
        T[] changedArray = (T[]) new Object[len-1];
        for (int i = 0, j = 0; i < len; i++, j++) {
            if (i == remove_at) {
                j--;
            } else {
                changedArray[j] = arr[i];
            }
        }
        arr = changedArray;
        capacity = --len;
        return elem_to_remove;
    }

}

// Removes a specified element
// find the index of an element
// check if contains
// Override the iterator
// -> add hasNext
// -> add next
// -> add remove
// toString
