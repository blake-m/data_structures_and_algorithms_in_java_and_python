package com.blakem.datastructures.dynamicarray;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;


class DynamicArrayTest {
    @org.junit.jupiter.api.Test
    void emptyListSizeTest() {
        int testCapacity = 2;
        int testLen = 0;
        DynamicArray<Integer> dA = new DynamicArray<Integer>(testCapacity);
        assertEquals(testLen, dA.size()); // size() gets len, not capacity
    }

    @org.junit.jupiter.api.Test
    void isEmptyWithAnEmptyArrayTest() {
        DynamicArray<Integer> dA = new DynamicArray<Integer>();
        assertTrue(dA.isEmpty());
    }

    @org.junit.jupiter.api.Test
    void isEmptyWithAnArrayWithElementsTest() {
        DynamicArray<Integer> dA = new DynamicArray<Integer>(2);
        dA.add(2);
        dA.add(2);
        assertFalse(dA.isEmpty());
    }

    @org.junit.jupiter.api.Test
    void getTest() {
        int testInteger = 25324;
        DynamicArray<Integer> dA = new DynamicArray<Integer>(2);
        dA.add(testInteger);
        assertEquals(testInteger, dA.get(0));
    }

    @org.junit.jupiter.api.Test
    void addTest() {
        int testInteger = 3252325;
        DynamicArray<Integer> dA = new DynamicArray<Integer>(0);
        dA.add(testInteger);
        assertEquals(testInteger, dA.get(0));
    }

    @org.junit.jupiter.api.Test
    void setTest() {
        int testIndex = 3;
        int testElement = 5325;
        DynamicArray<Integer> dA = new DynamicArray<Integer>(5);
        dA.set(testIndex, testElement);
        assertEquals(testElement, dA.get(testIndex));
    }

    @org.junit.jupiter.api.Test
    void clear() {
        int[] testArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
        DynamicArray<Integer> dA = new DynamicArray<Integer>(5);
        for (int number: testArray) {
            dA.add(number);
        }
        dA.clear();
        assertTrue(dA.isEmpty());
    }

    @org.junit.jupiter.api.Test
    void listWithElementsSizeTest() {
        int testCapacity = 2;
        int testLen = 2;
        DynamicArray<Integer> dA = new DynamicArray<Integer>(testCapacity);
        dA.add(2);
        dA.add(2);
        assertEquals(testLen, dA.size()); // size() gets len, not capacity
    }

    @org.junit.jupiter.api.Test
    void removeAtIndexRemovesTheElementTest() {
        int[] testArray = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        int testIndex = 5;
        DynamicArray<Integer> dA = new DynamicArray<Integer>(5);
        for (int number: testArray) {
            dA.add(number);
        }
        dA.removeAtIndex(testIndex);
        assertNotEquals(testArray[testIndex], dA.get(5));
    }

    @org.junit.jupiter.api.Test
    void removeAtIndexReturnsRemovedElementTest() {
        int[] testArray = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        int testIndex = 5;
        DynamicArray<Integer> dA = new DynamicArray<Integer>(5);
        for (int number: testArray) {
            dA.add(number);
        }
        int removedElement = dA.removeAtIndex(testIndex);
        assertEquals(testArray[testIndex], removedElement);
    }

    @org.junit.jupiter.api.Test
    void removeTest() {
        int[] testArray = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        int testElement = 5;
        DynamicArray<Integer> dA = new DynamicArray<Integer>(5);
        for (int number: testArray) {
            dA.add(number);
        }
        dA.remove(testElement);
        assertNotEquals(testArray[5], dA.get(testElement));
    }

    @org.junit.jupiter.api.Test
    void indexOfReturnsMinusOneIfElementNotInIndexTest() {
        int[] testArray = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        int testElement = 11;
        DynamicArray<Integer> dA = new DynamicArray<Integer>(5);
        for (int number: testArray) {
            dA.add(number);
        }
        int indexElement = dA.indexOf(testElement);
        assertEquals(-1, indexElement);
    }

    @org.junit.jupiter.api.Test
    void indexOfReturnsElementIndexTest() {
        int[] testArray = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        int testElement = 5;
        DynamicArray<Integer> dA = new DynamicArray<Integer>(5);
        for (int number: testArray) {
            dA.add(number);
        }
        int indexElement = dA.indexOf(testElement);
        assertEquals(5, indexElement);
    }

    @org.junit.jupiter.api.Test
    void containsIfContainsTest() {
        int[] testArray = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        int testElement = 5;
        DynamicArray<Integer> dA = new DynamicArray<Integer>(5);
        for (int number: testArray) {
            dA.add(number);
        }
        assertTrue(dA.contains(testElement));
    }

    @org.junit.jupiter.api.Test
    void containsIfNotContainsTest() {
        int[] testArray = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        int testElement = 50;
        DynamicArray<Integer> dA = new DynamicArray<Integer>(5);
        for (int number: testArray) {
            dA.add(number);
        }
        assertFalse(dA.contains(testElement));
    }

    @org.junit.jupiter.api.Test
    void testToStringTest() {
        int[] testArray = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        DynamicArray<Integer> dA = new DynamicArray<Integer>(5);
        for (int number: testArray) {
            dA.add(number);
        }
        String testString = dA.toString();
        assertEquals("[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]", testString);
    }
}