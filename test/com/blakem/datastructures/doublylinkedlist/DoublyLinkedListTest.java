package com.blakem.datastructures.doublylinkedlist;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class DoublyLinkedListTest {

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
        var dLL = new DoublyLinkedList<String>();
        dLL.addFirst("element");
        assertFalse(dLL.isEmpty());
    }

    @Test
    void getSizeWithElementsTest() {
        var dLL = new DoublyLinkedList<String>();
        dLL.addFirst("element");
        dLL.addFirst("element");
        dLL.addFirst("element");
        assertEquals(3, dLL.getSize());
    }

    @Test
    void isEmptyWithEmptyListTest() {
        var dLL = new DoublyLinkedList<String>();
        assertEquals(0, dLL.getSize());

    }

    @Test
    void isEmptyWithElementsTest() {
        var dLL = new DoublyLinkedList<String>();
        dLL.addFirst("element");
        assertFalse(dLL.isEmpty());
    }

    @Test
    void addFirstTest() {
        var dLL = new DoublyLinkedList<String>();
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
        var dLL = new DoublyLinkedList<String>();
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
        var dLL = new DoublyLinkedList<String>();
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
        var dLL = new DoublyLinkedList<String>();
        dLL.addFirst("Elem 1");
        assertEquals("Elem 1", dLL.checkFirst());
    }

    @Test
    void checkLastTest() {
        var dLL = new DoublyLinkedList<String>();
        dLL.addLast("Elem 1");
        assertEquals("Elem 1", dLL.checkLast());
    }

    @Test
    void removeFirstTest() {
        var dLL = new DoublyLinkedList<String>();
        int i = 0;
        while (i < 25) {
            dLL.addLast("Elem " + i);
            i++;
        }
        String removedElement = dLL.removeFirst();
        assertEquals("Elem 0", removedElement);
    }

    @Test
    void removeFirstThrowsEmptyListExceptionTest() {
        var dLL = new DoublyLinkedList<String>();
        assertThrows(RuntimeException.class, dLL::removeFirst, "This list is EMPTY.");
    }

    @Test
    void removeLastTest() {
        var dLL = new DoublyLinkedList<String>();
        int i = 0;
        while (i < 25) {
            dLL.addLast("Elem " + i);
            i++;
        }
        String removedElement = dLL.removeLast();
        assertEquals("Elem 24", removedElement);
    }

    @Test
    void removeLastThrowsEmptyListExceptionTest() {
        var dLL = new DoublyLinkedList<String>();
        assertThrows(RuntimeException.class, dLL::removeLast, "This list is EMPTY.");
    }


    @Test
    void removeAtReturnsRemovedDataTest() {
        var dLL = new DoublyLinkedList<String>();
        int i = 0;
        while (i < 25) {
            dLL.addLast("Elem " + i);
            i++;
        }
        assertEquals("Elem 5", dLL.removeAt(5));
    }

    @Test
    void removeAtRemovesElementAtTheEndTest() {
        var dLL = new DoublyLinkedList<String>();
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
        var dLL = new DoublyLinkedList<String>();
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
        var dLL = new DoublyLinkedList<String>();
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
        var dLL = new DoublyLinkedList<String>();
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
        var dLL = new DoublyLinkedList<String>();
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
        var dLL = new DoublyLinkedList<String>();
        int i = 0;
        while (i < 5) {
            dLL.addLast("Elem " + i);
            i++;
        }
        String dLLString = dLL.toString();
        assertEquals("[Elem 0, Elem 1, Elem 2, Elem 3, Elem 4,  ]", dLLString);
    }
}
