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
        if(root.getValue()<value) {
            if(root.getLeftChild()!=null)
                add(root.getLeftChild(), value);
            root.setLeftChild(new Node(value));
        }
        else if(root.getValue()>=value){
            if (root.getRightChild()!=null)
                add(root.getRightChild(),value);

            root.setRightChild(new Node(value));
        }
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
