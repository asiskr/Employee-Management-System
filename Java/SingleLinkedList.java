class Node {
    int val;
    Node next;

    Node(int val) {
        this.val = val;
        this.next = null;
    }
}

public class SingleLinkedList {
    private Node head;
    private Node tail;

    public void Creation(int nodeVal) {
        Node node = new Node(nodeVal);
        if (head == null) {
            head = node;
            tail = node;
        } else {
            tail.next = node;
            tail = node;
        }
    }

    public static void main(String[] args) {
        SingleLinkedList sll = new SingleLinkedList();
        sll.Creation(5);
        System.out.println(sll.head.val);
    }

}
