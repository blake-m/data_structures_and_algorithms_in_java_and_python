package com.blakem.datastructures.stack.bracketschecker;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static com.blakem.datastructures.stack.bracketschecker.BracketsChecker.checkIfMatch;
import static com.blakem.datastructures.stack.bracketschecker.BracketsChecker.reverseRightBracket;
import static org.junit.jupiter.api.Assertions.*;


class BracketsCheckerTest {
    @Test
    void checkIsLeftWithLeftBracketsTest() {
        char[] leftBrackets = {'{', '[', '<', '('};
        for (char bracket: leftBrackets) {
            assertTrue(BracketsChecker.isLeft(bracket));
        }
    }

    @Test
    void checkIsLeftWithRightBracketsTest() {
        char[] rightBrackets = {'}', ']', '>', ')'};
        for (char bracket: rightBrackets) {
            assertFalse(BracketsChecker.isLeft(bracket));
        }
    }

    @Test
    void reverseRightBracketWithBracketsTest() {
        assertEquals('(', reverseRightBracket(')'));
        assertEquals('<', reverseRightBracket('>'));
        assertEquals('[', reverseRightBracket(']'));
        assertEquals('{', reverseRightBracket('}'));
        assertNotEquals('(', '>');
    }

    @Test
    void reverseRightBracketThrowsAnExceptionForNonBracketInputTest() {
        assertThrows(IllegalArgumentException.class, () -> {
            BracketsChecker.reverseRightBracket('c');
        });
    }

    @Test
    void checkIfMatchWithEmptyStringTest() {
        String emptyString = "";
        assertTrue(checkIfMatch(emptyString));
    }

    @Test
    void checkIfMatchWithShortCorrectStringTest() {
        String correctShortString = "()";
        assertTrue(checkIfMatch(correctShortString));
    }

    @Test
    void checkIfMatchWithLongCorrectStringTest() {
        String correctLongString = "([()]){}{[]}";
        assertTrue(checkIfMatch(correctLongString));
    }

    @Test
    void checkIfMatchWithIncorrectStringTest() {
        String incorrectString = "([]]{)([])(";
        assertFalse(checkIfMatch(incorrectString));
    }


}