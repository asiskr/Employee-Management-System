package Array;

import java.util.ArrayList;
// import java.util.Iterator;

public class ArrayLists {
    public static void main(String args[]) {
        ArrayList<Integer> nums = new ArrayList<>();
        nums.add(2);
        nums.add(4);
        nums.add(78);
        nums.add(56);
        nums.add(790);
        nums.add(67);
        nums.add(534);
        nums.remove(3);
        for (int ans : nums) {
            System.out.println(ans);
        }
    }

}
