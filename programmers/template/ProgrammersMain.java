// import java.util.*;

class Solution {
    public void print() {
        System.out.println("Hello World!");
    }
}





class ProgrammersMain {
    public static void main(String[] args) {
        testcase1();
    }

    public static void checkAnswer() {
        System.out.println("Hello checkAnswer!");

        if (true) {
            System.out.println("Testcase is Passed!");
        } else {
            System.err.println("@@@@@@@@@@ Testcase is Failed! @@@@@@@@@@");
        }
        System.out.println();

    }

    public static void testcase1() {

        System.out.println("Hello TestCase1!");
        checkAnswer();
    }
}