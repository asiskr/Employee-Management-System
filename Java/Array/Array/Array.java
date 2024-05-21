package Array;

import java.util.Arrays;
import java.util.HashSet;

public class Array {
    public static void main(String[] args) {
        int[] arr = new int[] { 4, 7, 34, 545, 9, 545 };
        int n = arr.length;

        // REVERSE ARRAY BY K STEPS
        int k = 3;
        k = k % n;
        reverse(arr, 0, k - 1);
        reverse(arr, k, n - 1);
        reverse(arr, 0, n - 1);

        // Print the reversed array
        System.out.println("Reversed Array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }

        // Perform binary search
        int[] Barray = new int[] { 4, 7, 9, 34, 545, 545 };
        int target = 7; // Example target value
        int result = binarySearch(Barray, target);
        System.out.println("\nIndex of " + target + " in Barray: " + result);

        // Merge two arrays
        long[] arr1 = new long[] { 4, 7, 9 };
        long[] arr2 = new long[] { 545, 545 };
        int x = arr1.length;
        int m = arr2.length;

        merge(arr1, arr2, x, m);

        // Print the merged arrays
        System.out.println("The merged arrays are:");
        System.out.print("arr1[] = ");
        for (long num : arr1) {
            System.out.print(num + " ");
        }
        System.out.print("\narr2[] = ");
        for (long num : arr2) {
            System.out.print(num + " ");
        }
        System.out.println();

        // REMOVE DUPLICATES
        HashSet<Integer> set = new HashSet<>();
        for (int num : arr) {
            set.add(num);
        }
        System.out.println("Array after removing duplicates: " + set);

        // TRAVERSE AN ARRAY
        System.out.println("Traversing the array:");
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }

        // MAXIMUM ELEMENT
        Arrays.sort(arr);
        int last = arr[n - 1];
        System.out.println("Maximum element: " + last);

        // MAX AND MIN IN LOOP
        int MAX = Integer.MIN_VALUE;
        int MIN = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (arr[i] > MAX) {
                MAX = arr[i];
            }
            if (arr[i] < MIN) {
                MIN = arr[i];
            }
        }
        System.out.println("Maximum element (in loop): " + MAX);
        System.out.println("Minimum element (in loop): " + MIN);

        // REVERSE AN ARRAY
        System.out.println("Reversed array:");
        for (int i = arr.length - 1; i >= 0; i--) {
            System.out.println(arr[i]);
        }
    }

    // REVERSE ARRAY BY K STEPS FUNCTIION
    private static void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }

    // BINARY SEARCH ON SORTED ARRAY FUNCTION
    private static int binarySearch(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }

    public static void merge(long[] arr1, long[] arr2, int n, int m) {

        // Declare 2 pointers:
        int left = n - 1;
        int right = 0;

        // Swap the elements until arr1[left] is
        // smaller than arr2[right]:
        while (left >= 0 && right < m) {
            if (arr1[left] > arr2[right]) {
                long temp = arr1[left];
                arr1[left] = arr2[right];
                arr2[right] = temp;
                left--;
                right++;
            } else {
                break;
            }
        }

        // Sort arr1[] and arr2[] individually:
        Arrays.sort(arr1);
        Arrays.sort(arr2);
    }
    /*
     * int[] myArray = new int[7];
     * 
     * myArray[0]=10;myArray[1]=20;myArray[2]=80;myArray[3]=30;myArray[4]=40;myArray
     * [5]=50;myArray[6]=60;
     * 
     * int index = -1;
     * int count = 0;for(
     * int i:myArray)
     * {
     * if (i == 80) {
     * index = count;
     * break;
     * }
     * count++;
     * }System.out.println(index);
     */
}
