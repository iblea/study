import java.util.*;

class Rooms {
    List<Room> rooms;

    public Rooms() {
        this.rooms = new ArrayList<>();
        this.rooms.add(new Room());
    }

    public void addRoom(Room room) {
        this.rooms.add(room);
    }

    public int getRoomCount() {
        return this.rooms.size();
    }

    public void addBookTime(BookTime bookTime) {
        for (Room room : this.rooms) {
            int index = room.isAbleToReservation(bookTime);
            if (index >= 0) {
                room.addBookTime(bookTime, index);
                return ;
            }
        }
        Room newRoom = new Room();
        newRoom.addBookTime(bookTime);
        this.rooms.add(newRoom);
    }
}

class Room {
    List<BookTime> bookTimes;

    public Room() {
        this.bookTimes = new ArrayList<>();
    }

    public void addBookTime(BookTime bookTime) {
        this.bookTimes.add(bookTime);
    }

    public void addBookTime(BookTime bookTime, int index) {
        this.bookTimes.add(index, bookTime);
    }

    public int isAbleToReservation(BookTime bookTime) {
        int booktimesLength = this.bookTimes.size();
        if (booktimesLength == 0) {
            return 0;
        }

        if (bookTime.getEnd() <= this.bookTimes.get(0).getStart()) {
            return 0;
        }

        if (this.bookTimes.get(booktimesLength - 1).getEnd() <= bookTime.getStart()) {
            return booktimesLength;
        }

        for (int i = 1; i < booktimesLength; i++) {
            BookTime curBookTime = this.bookTimes.get(i);
            BookTime prevBookTime = this.bookTimes.get(i - 1);
            if (prevBookTime.getEnd() <= bookTime.getStart() &&
                bookTime.getEnd() <= curBookTime.getStart()) {
                return i;
            }
        }
        return -1;
    }
}

class BookTime {
    Integer start;
    Integer end;

    public BookTime(String[] revervationTime) {
        this.start = timeStringtoInt(revervationTime[0]);
        this.end = timeStringtoInt(revervationTime[1]);
        // if (this.end < this.start) {
        //     this.end += 24 * 60;
        // }
        this.end += 10;
    }

    public Integer timeStringtoInt(String time) {
        String[] timeArr = time.split(":");
        return Integer.parseInt(timeArr[0]) * 60 + Integer.parseInt(timeArr[1]);
    }

    public Integer getStart() {
        return this.start;
    }
    public Integer getEnd() {
        return this.end;
    }
}

class Solution {
    public int solution(String[][] book_time) {
        Rooms rooms = new Rooms();

        // Arrays.sort(book_time, new Comparator<String[]>() {
        //     @Override
        //     public int compare(String[] o1, String[] o2) {
        //         return o1[0].compareTo(o2[0]);
        //     }
        // });

        Arrays.sort(book_time, (o1, o2) -> o1[0].compareTo(o2[0]));

        for (String[] revervationTime : book_time) {
            BookTime bookTime = new BookTime(revervationTime);
            rooms.addBookTime(bookTime);
        }
        return rooms.getRoomCount();
    }
}





class Main {
    public static void main(String[] args) {
        testcase1();
        testcase2();
        testcase3();
        testcase4();
        testcase5();
        testcase6();
        testcase7();
        testcase8();
        testcase9();
        testcase10();
        testcase11();
        testcase12();
    }

    public static void checkAnswer(int result, int expected) {
        if (result == expected) {
            // System.out.println("Testcase is Passed!");
        } else {
            System.out.println("result: " + result);
            System.out.println("expected: " + expected);
            System.err.println("@@@@@@@@@@ Testcase is Failed! @@@@@@@@@@");
            System.out.println();
        }
        // System.out.println();

    }

    public static void testcase1() {
        final String[][] bookTime = {{"15:00", "17:00"}, {"16:40", "18:20"}, {"14:20", "15:20"}, {"14:10", "19:20"}, {"18:20", "21:20"}};
        int result = new Solution().solution(bookTime);
        int expected = 3;
        checkAnswer(result, expected);
    }

    public static void testcase2() {
        final String[][] bookTime = {{"09:10", "10:10"}, {"10:20", "12:20"}};
        int result = new Solution().solution(bookTime);
        int expected = 1;
        checkAnswer(result, expected);
    }

    public static void testcase3() {
        final String[][] bookTime = {{"10:20", "12:30"}, {"10:20", "12:30"}, {"10:20", "12:30"}};
        int result = new Solution().solution(bookTime);
        int expected = 3;
        checkAnswer(result, expected);
    }

    public static void testcase4() {
        final String[][] bookTime = {{"08:00", "08:30"}, {"08:00", "13:30"}, {"10:20", "12:30"}};
        int result = new Solution().solution(bookTime);
        int expected = 2;
        checkAnswer(result, expected);
    }

    public static void testcase5() {
        final String[][] bookTime = {{"05:57", "06:02"}, {"04:00", "06:59"}, {"03:56", "07:57"}, {"06:12", "08:55"}, {"07:09", "07:11"}};
        int result = new Solution().solution(bookTime);
        int expected = 3;
        checkAnswer(result, expected);
    }

    public static void testcase6() {
        final String[][] bookTime = {{"08:00", "08:30"}};
        int result = new Solution().solution(bookTime);
        int expected = 1;
        checkAnswer(result, expected);
    }

    public static void testcase7() {
        final String[][] bookTime = {{"08:00", "08:30"}, {"08:00", "13:00"}, {"12:30", "13:30"}};
        int result = new Solution().solution(bookTime);
        int expected = 2;
        checkAnswer(result, expected);
    }

    public static void testcase8() {
        final String[][] bookTime = {{"12:30", "13:20"}, {"09:10", "10:10"}, {"10:20", "12:20"}};
        int result = new Solution().solution(bookTime);
        int expected = 1;
        checkAnswer(result, expected);
    }

    public static void testcase9() {
        final String[][] bookTime = {{"00:30", "00:50"}, {"00:05", "00:15"}, {"00:00", "00:01"}};
        int result = new Solution().solution(bookTime);
        int expected = 2;
        checkAnswer(result, expected);
    }

    public static void testcase10() {
        final String[][] bookTime = {{"02:00", "02:10"}, {"00:00", "00:10"}, {"00:40", "00:50"}, {"00:20", "00:30"}};
        int result = new Solution().solution(bookTime);
        int expected = 1;
        checkAnswer(result, expected);
    }

    public static void testcase11() {
        final String[][] bookTime = {{"09:10", "10:10"}, {"10:19", "12:20"}};
        int result = new Solution().solution(bookTime);
        int expected = 2;
        checkAnswer(result, expected);
    }

    public static void testcase12() {
        final String[][] bookTime = {{"10:00", "10:20"}, {"09:00", "09:20"}, {"09:20", "09:40"}, {"09:40", "10:00"}};
        int result = new Solution().solution(bookTime);
        int expected = 2;
        checkAnswer(result, expected);
    }





}