package com.blakem.datastructures.priorityqueue;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class BinaryHeap<T extends Comparable<T>> {
    private int currentHeapSize = 0;

    private int currentHeapCapacity = 0;

    private List<T> heapElementsList = null;

    public BinaryHeap(int size) {
        heapElementsList = new ArrayList<>(size);
    }

    public BinaryHeap(Collection<T> elements) {
        this(elements.size());
        for (T elem: elements) {
            add(elem);
        }
    }

    public boolean isEmpty() {
        return currentHeapSize == 0;
    }


    public void clear() {
        for (int i = 0; i < currentHeapCapacity; i++) {
            heapElementsList.set(i, null);
        }
        currentHeapSize = 0;
    }

    public int size() {
        return currentHeapSize;
    }

    public T peekAt(int position) {
        if (isEmpty()) {
            return null;
        }
        return heapElementsList.get(position);
    }

    public T peekRoot() {
        return peekAt(0);
    }

    public T poll() {
        return removeAt(0);
    }

    public boolean contains(T elemToCheck) {
        for (T element: heapElementsList) {
            if (elemToCheck.equals(element)) {
                return true;
            }
        }
        return false;
    }

    public int returnIndexOfFirstSuchElement(T elemToFind) {
        for (int index = 0; index < currentHeapSize; index++) {
            if (elemToFind.equals(heapElementsList.get(index))) {
                return index;
            }
        }
        return -1;
    }

    public void add(T elem) throws IllegalArgumentException {
        if (elem == null) {
            throw new IllegalArgumentException();
        }
        if (currentHeapSize < currentHeapCapacity) {
            heapElementsList.set(currentHeapSize, elem);
        } else {
            heapElementsList.add(elem);
            currentHeapCapacity++;
        }

        swimToTop(currentHeapSize);
        currentHeapSize++;
    }


    private boolean
    arg1AssociatedListValueIsSmallerThanArg2ListValue(
            int nodeIndex1, int nodeIndex2) {
        T node1 = heapElementsList.get(nodeIndex1);
        T node2 = heapElementsList.get(nodeIndex2);
        return node1.compareTo(node2) <= 0;
    }

    private void swimToTop(int nodePosition) {
        int nextParentNodePosition = (nodePosition-1)/2;
        int rootPosition = 0;

        while (nodePosition > rootPosition
                && arg1AssociatedListValueIsSmallerThanArg2ListValue(
                        nodePosition, nextParentNodePosition)) {
            swap(nextParentNodePosition, nodePosition);
            nodePosition = nextParentNodePosition;

            nextParentNodePosition = (nodePosition-1)/2;
        }
    }

    private void topToDownSink(int nodePosition) {
        while (true) {
            int leftChildNodePosition = nodePosition*2+1;
            int rightChildNodePosition = leftChildNodePosition+1;
            int smallestChildNodePosition = Math.min(leftChildNodePosition,
                                                     rightChildNodePosition);

            // break if can't sink further
            if (smallestChildNodePosition <= currentHeapSize
                || arg1AssociatedListValueIsSmallerThanArg2ListValue(
                    nodePosition, smallestChildNodePosition)) {
                break;
            }

            swap(smallestChildNodePosition, nodePosition);
            nodePosition = smallestChildNodePosition;

        }
    }

    private void swap(int nodePosition1, int nodePosition2) {
        T element1 = heapElementsList.get(nodePosition1);
        T element2 = heapElementsList.get(nodePosition2);

        heapElementsList.set(nodePosition1, element2);
        heapElementsList.set(nodePosition2, element1);
    }

    public boolean remove(T elementToRemove) {
        if (elementToRemove == null) return false;
        int positionTracker = 0;
        for (T element: heapElementsList) {
            if (elementToRemove.equals(element)) {
                removeAt(positionTracker);
                return true;
            }
            positionTracker++;
        }
        return false;
    }

    public T removeAt(int nodePosition) {
        currentHeapSize--;
        T removedElement = heapElementsList.get(nodePosition);
        swap(nodePosition, currentHeapSize);

        heapElementsList.set(currentHeapSize, null);

        if (nodePosition == currentHeapSize) {
            return removedElement;
        }
        T elementSwappedWithRemovedElement = heapElementsList.get(nodePosition);

        // Try either swimming up or sinking
        topToDownSink(nodePosition);
        swimToTop(nodePosition);

        return removedElement;
    }

    // 0 should be passed to start at the root
    public boolean isMinHeap(int currentPosition) {
        // If we are outside the bounds of the heap return true
        int leftChildNodePosition = currentPosition*2+1;
        int rightChildNodePosition = leftChildNodePosition+1;


        if (leftChildNodePosition < currentHeapSize
            && !arg1AssociatedListValueIsSmallerThanArg2ListValue(
                    currentPosition, leftChildNodePosition
        )) {
            return false;
        }

        if (rightChildNodePosition < currentHeapSize
                && !arg1AssociatedListValueIsSmallerThanArg2ListValue(
                currentPosition, rightChildNodePosition
        )) {
            return false;
        }

        return isMinHeap(leftChildNodePosition)
                && isMinHeap(rightChildNodePosition);
    }

    @Override
    public String toString() {
        return heapElementsList.toString();
    }
}
