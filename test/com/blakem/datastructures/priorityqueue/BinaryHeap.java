package com.blakem.datastructures.priorityqueue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.mock;


class BinaryHeapEmptyTest {
    private BinaryHeap<Integer> bH;

    @BeforeEach
    void setUp() {
        bH = new BinaryHeap<Integer>(16);
    }

    @Test
    void initializeBinaryHeapWithSpecifiedSize() {
        bH = new BinaryHeap<Integer>(16);
    }

    @Test
    void isEmptyReturnsTrueWhenEmpty() {
        assertTrue(bH.isEmpty());
    }

    @Test
    void sizeReturns0WhenEmpty() {
        assertEquals(0, bH.size());
    }

    @Test
    void peekRootReturnsNullWhenEmpty() {
        assertNull(bH.peekRoot());
    }

    @Test
    void pollThrowsErrorWhenEmpty() {
        assertThrows(IndexOutOfBoundsException.class, bH::poll);
    }

    @Test
    void returnIndexOfFirstSuchElementReturnsMinusOneWhenElementNotPresent() {
        assertEquals(-1, bH.returnIndexOfFirstSuchElement(12));
    }

    @Test
    void containsReturnsFalseWhenElementNotPresent() {
        assertFalse(bH.contains(12));
    }

    @Test
    void addThrowsErrorWithIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
                bH.add(null);
            }
        );
    }

    @Test
    void addIncreasesHeapSize() {
        assertEquals(0, bH.size());
        bH.add(5);
        assertEquals(1, bH.size());
    }

    @Test
    void addFirstElementHasIndexZero() {
        bH.add(3);
        assertEquals(0, bH.returnIndexOfFirstSuchElement(3));
    }

    @Test
    void addingElementsGivesThemProperIndices() {
        for (int i = 0; i < 150; i++) {
           bH.add(i);
           assertEquals(i, bH.returnIndexOfFirstSuchElement(i));
        }
    }

    @Test
    void toStringTest() {
        // Works for elements up to 4 chars long
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        for (int n: arr) {
            int sol = (int)Math.pow(2, n) - 1;
            System.out.println(sol);
        }
    }
}

class BinaryHeapWith15ElementsTest {
    private BinaryHeap<Integer> bH;

    @BeforeEach
    void setUp() {
        bH = new BinaryHeap<Integer>(16);
        int[] arr = {5, 63, 1, 5, 8, 9, 124, 21, 412, 1, 3, 53, 12, 75, 2};
        for (int i: arr) {
            bH.add(i);
        }
    }

    @Test
    void isEmpty() {
        assertFalse(bH.isEmpty());
    }

    @Test
    void clearRemovesAllElements() {
        bH.clear();
        assertTrue(bH.isEmpty());
    }

    @Test
    void peekAtReturnsProperValue() {
        assertEquals(1, bH.peekAt(0));
        assertEquals(1, bH.peekAt(1));
        assertEquals(2, bH.peekAt(2));
        assertEquals(21, bH.peekAt(3));
        assertEquals(3, bH.peekAt(4));
        assertEquals(9, bH.peekAt(5));
        assertEquals(5, bH.peekAt(6));
        assertEquals(63, bH.peekAt(7));
        assertEquals(412, bH.peekAt(8));
        assertEquals(8, bH.peekAt(9));
        assertEquals(5, bH.peekAt(10));
        assertEquals(53, bH.peekAt(11));
        assertEquals(12, bH.peekAt(12));
        assertEquals(124, bH.peekAt(13));
        assertEquals(75, bH.peekAt(14));
    }

    @Test
    void peekRootReturnsProperValue() {
        assertEquals(1, bH.peekRoot());
    }

    @Test
    void containsReturnsTrueWhenElementPresent() {
        assertTrue(bH.contains(412));
    }

    @Test
    void containsReturnsFalseWhenElementNotPresent() {
        assertFalse(bH.contains(4122));
    }

    @Test
    void toStringReturnsStringRepresentation() {
        assertEquals("[1, 1, 2, 21, 3, 9, 5, 63, 412, 8, 5, 53, 12, 124, 75]",
                bH.toString());
    }
}