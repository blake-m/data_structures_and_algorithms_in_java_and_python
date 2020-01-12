package com.blakem.datastructures.doublylinkedlist;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.fail;

class DoublyLinkedListTest {
    private DoublyLinkedList<String> dLL;

    @BeforeEach
    void setUp() {
        dLL = new DoublyLinkedList<String>();
    }

    @Test
    void initializeEmptyListTest() {
        var emptyLinkedList = new DoublyLinkedList<String>();
        assertEquals(0, emptyLinkedList.getSize());
    }

    @Test
    void initializeWithOneElementTest() {
        var linkedList = new DoublyLinkedList<String>("Element");
        assertEquals(linkedList.checkFirst(), "Element");
    }


    @Test
    void getSizeWithEmptyListTest() {
        dLL.addFirst("element");
        assertFalse(dLL.isEmpty());
    }

    @Test
    void getSizeWithElementsTest() {
        dLL.addFirst("element");
        dLL.addFirst("element");
        dLL.addFirst("element");
        assertEquals(3, dLL.getSize());
    }

    @Test
    void isEmptyWithEmptyListTest() {
        assertEquals(0, dLL.getSize());

    }

    @Test
    void isEmptyWithElementsTest() {
        dLL.addFirst("element");
        assertFalse(dLL.isEmpty());
    }

    @Test
    void addFirstTest() {
        dLL.addFirst("Elem 1");
        assertEquals("Elem 1", dLL.checkFirst());
        dLL.addFirst("Elem 2");
        assertEquals("Elem 2", dLL.checkFirst());
        dLL.addFirst("Elem 3");
        assertEquals("Elem 3", dLL.checkFirst());
        assertNotEquals("Elem 1", dLL.checkFirst());
    }

    @Test
    void addLastTest() {
        dLL.addLast("Elem 1");
        assertEquals("Elem 1", dLL.checkLast());
        dLL.addLast("Elem 2");
        assertEquals("Elem 2", dLL.checkLast());
        dLL.addLast("Elem 3");
        assertEquals("Elem 3", dLL.checkLast());
        assertNotEquals("Elem 1", dLL.checkLast());
    }

    @Test
    void clearTest() {
        int i = 0;
        while (i < 25) {
            dLL.addLast("Elem " + i);
            i++;
        }
        dLL.clear();
        assertEquals(0, dLL.getSize());
    }

    @Test
    void checkFirstTest() {
        dLL.addFirst("Elem 1");
        assertEquals("Elem 1", dLL.checkFirst());
    }

    @Test
    void checkLastTest() {
        dLL.addLast("Elem 1");
        assertEquals("Elem 1", dLL.checkLast());
    }

    @Test
    void removeFirstTest() {
        int i = 0;
        while (i < 25) {
            dLL.addLast("Elem " + i);
            i++;
        }
        String removedElement = dLL.removeFirst();
        assertEquals("Elem 0", removedElement);
    }

    // Learning purposes comment: 1st way of checking for exceptions
    @Test
    void removeFirstThrowsEmptyListExceptionTest() {
        try {
            dLL.removeFirst();
            fail("Exception wasn't thrown");
        } catch (RuntimeException exception) {
            assertEquals("This list is EMPTY.", exception.getMessage());
        }

    }

    @Test
    void removeLastTest() {
        int i = 0;
        while (i < 25) {
            dLL.addLast("Elem " + i);
            i++;
        }
        String removedElement = dLL.removeLast();
        assertEquals("Elem 24", removedElement);
    }

    // Learning purposes comment: 2nd way of checking for exceptions
    @Test
    void removeLastThrowsEmptyListExceptionTest() {
        assertThrows(RuntimeException.class, dLL::removeLast);
    }


    @Test
    void removeAtReturnsRemovedDataTest() {
        int i = 0;
        while (i < 25) {
            dLL.addLast("Elem " + i);
            i++;
        }
        assertEquals("Elem 5", dLL.removeAt(5));
    }

    @Test
    void removeAtRemovesElementAtTheEndTest() {
        int i = 0;
        while (i < 25) {
            dLL.addLast("Elem " + i);
            i++;
        }
        dLL.removeAt(24);
        assertEquals(24, dLL.getSize());
        assertEquals("Elem 23", dLL.checkLast());
    }

    @Test
    void removeAtRemovesElementInTheMiddleTest() {
        int i = 0;
        while (i < 25) {
            dLL.addLast("Elem " + i);
            i++;
        }
        dLL.removeAt(5);
        assertEquals(24, dLL.getSize());
        assertEquals("Elem 6", dLL.checkAt(5));
    }

    @Test
    void removeAtRemovesElementAtTheBeginningTest() {
        int i = 0;
        while (i < 25) {
            dLL.addLast("Elem " + i);
            i++;
        }
        dLL.removeAt(0);
        assertEquals(24, dLL.getSize());
        assertEquals("Elem 1", dLL.checkFirst());
    }

    @Test
    void insertObjectAtInsertInTheMiddleTest() {
        int i = 0;
        while (i < 25) {
            dLL.addLast("Elem " + i);
            i++;
        }
        dLL.insertObjectAt(10, "Elem 1");
        assertEquals("Elem 1", dLL.checkAt(10));
        dLL.insertObjectAt(8, "Elem 2");
        assertEquals("Elem 2", dLL.checkAt(8));
        dLL.insertObjectAt(3, "Elem 3");
        assertEquals("Elem 3", dLL.checkAt(3));
    }

    @Test
    void insertObjectAtInsertAtTheBeginningTest() {
        dLL.insertObjectAt(0, "Elem 1");
        assertEquals("Elem 1", dLL.checkFirst());
        dLL.insertObjectAt(0, "Elem 2");
        assertEquals("Elem 2", dLL.checkFirst());
        dLL.insertObjectAt(0, "Elem 3");
        assertEquals("Elem 3", dLL.checkFirst());
        assertNotEquals("Elem 1", dLL.checkFirst());
    }

    @Test
    void testToStringTest() {
        int i = 0;
        while (i < 5) {
            dLL.addLast("Elem " + i);
            i++;
        }
        String dLLString = dLL.toString();
        assertEquals("[Elem 0, Elem 1, Elem 2, Elem 3, Elem 4,  ]", dLLString);
    }
}
