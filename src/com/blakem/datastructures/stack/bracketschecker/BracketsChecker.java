/*
BracketsChecker.java

A simple program which takes a String with a combination of different brackets: [, {, (, <
and returns true if they match.

Example 1:
    Input String:   "([()]){}{[]}"
    Returns:        true

Example 2:
    Input String:   "([]]{)([])("
    Returns:        false

It could have some real life usage (e.g. in IDEs) if it worked with usual characters
in between different brackets. Expanding it to have this functionality would be easy
but the goal of production of this micro-program was to train STACK implementation.
 */

package com.blakem.datastructures.stack.bracketschecker;

import com.blakem.datastructures.stack.Stack;

public class BracketsChecker {
    // I decided to leave these as static in case I wanted to develop this small programme further.
    private static Stack<Character> bracketsStack;
    private static char[] leftBrackets = {'{', '[', '<', '('};

    public static boolean isLeft(char bracket) {
        for (char leftBracket: leftBrackets) {
            if (leftBracket == bracket) {
                return true;
            }
        }
        return false;
    }

    public static char reverseRightBracket(char bracket) throws IllegalArgumentException {
        if (bracket == ')') {
            return '(';
        } else if (bracket == ']') {
            return '[';
        } else if (bracket =='>') {
            return '<';
        } else if (bracket == '}') {
            return '{';
        } else {
            throw new IllegalArgumentException("Argument is not a valid bracket: (, {, <, [");
        }
    }

    public static boolean checkIfMatch(String bracketsSequence) {
        bracketsStack = new Stack<Character>();

        for (int i=0; i<bracketsSequence.length(); i++) {
            char currentBracket = bracketsSequence.charAt(i);

            if (isLeft(currentBracket)) {
                bracketsStack.pushElementOnTop(currentBracket);
            } else if (bracketsStack.isEmpty() || reverseRightBracket(currentBracket) != bracketsStack.popElementFromTop()) {
                return false;
            }
        }
        return true;
    }
}


// For bracket in brackets
//      check if left
//      if is left --> add to stack
//      if is right --> Check if not empty and Compare with first in stack
//          if match --> remove first in stack
//          if not match --> return False
// if empty --> return True
