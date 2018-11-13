public class Node {
    private Node leftChild;
    private Node rightChild;
    private int value;

    public Node(Node leftChild, Node rightChild, int value) {
        this.leftChild = leftChild;
        this.rightChild = rightChild;
        this.value = value;
    }

    public Node(int value) {
        this.leftChild = null;
        this.rightChild = null;
        this.value = value;
    }

    public Node getLeftChild() {
        return leftChild;
    }

    public void setLeftChild(Node leftChild) {
        this.leftChild = leftChild;
    }

    public Node getRightChild() {
        return rightChild;
    }

    public void setRightChild(Node rightChild) {
        this.rightChild = rightChild;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return "Node{" +
                "leftChild=" + leftChild +
                ", rightChild=" + rightChild +
                ", value=" + value +
                '}';
    }
}
