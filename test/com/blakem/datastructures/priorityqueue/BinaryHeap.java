package com.blakem.datastructures.priorityqueue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertThrows;



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
    void addThrowsErrorWithIllegalArgument() {
        assertThrows(IllegalArgumentException.class, () -> {
                bH.add(null);
            }
        );
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
    }

    @Test
    void initializeBinaryHeapWithSpecifiedSize() {
        int i;
    }

    @Test
    void toStringReturnsStringRepresentation() {
        // Works for elements up to 4 chars long
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        for (int n: arr) {
            int sol = (int)Math.pow(2, n) - 1;
            System.out.println(sol);
        }
    }
}
//_____________________nnnn_____________________
//                    /    \
//          ______nnnn_    _nnnn______
//              /    \     /    \
//            nnnn__nnnn__nnnn__nnnn
//
//nnnn__nnnn__nnnn__nnnn__nnnn__nnnn__nnnn__nnnn