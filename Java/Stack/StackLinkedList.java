package Stack;

public class StackLinkedList {
    static class Node {
        int data;
        Node next;

        public Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    public static class Stack {
        private Node top;

        public Stack() {
            this.top = null;
        }

        public void push(int data) {
            Node newNode = new Node(data);
            if (isEmpty()) {
                top = newNode;
            } else {
                newNode.next = top;
                top = newNode;
            }
        }

        public int pop() {
            if (isEmpty()) {
                System.out.println("Stack is empty. Cannot pop element.");
                return -1; // Return -1 as an indication of empty stack
            }
            int poppedValue = top.data;
            top = top.next;
            return poppedValue;
        }

        public int peek() {
            if (isEmpty()) {
                System.out.println("Stack is empty. Cannot peek element.");
                return -1; // Return -1 as an indication of empty stack
            }
            return top.data;
        }

        public boolean isEmpty() {
            return top == null;
        }

        public static void main(String[] args) {
            Stack stack = new Stack();

            stack.push(1);
            stack.push(2);
            stack.push(3);
            System.out.println("Peek: " + stack.peek()); // Output: 3
            System.out.println("Pop: " + stack.pop()); // Output: 3
            System.out.println("Peek: " + stack.peek()); // Output: 2
        }
    }
}
