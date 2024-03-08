import java.util.*;

class Test {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(30);
        list.add(50);

        list.add(1, 20);
        list.add(3, 40);
        System.out.println(list.toString());
        list.add(5, 60);
        list.add(0, 0);

        System.out.println(list.toString());
    }
}