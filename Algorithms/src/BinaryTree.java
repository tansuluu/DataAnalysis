public class BinaryTree {

    private Node root;

    public BinaryTree() {

    }

    public BinaryTree(Node root) {
        this.root = root;

    }

    public void add(int value){
        root=add(root,value);

    }
    private Node add(Node root, int value){
        if(root==null){
            return new Node(value);
        }
        if(root.getValue()<value) {
            root.setLeftChild(add(root.getLeftChild(),value));
        }
        if(root.getValue()>=value){
            root.setRightChild(add(root.getRightChild(),value));
        }

        return root;
    }

    public Node getRoot() {
        return root;
    }

    public void setRoot(Node root) {
        this.root = root;
    }

    @Override
    public String toString() {
        return "BinaryTree{" +
                "root=" + root +
                '}';
    }
}
