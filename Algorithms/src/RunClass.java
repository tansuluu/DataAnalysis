public class RunClass {

    public static void main(String[] args) {
        Node n=new Node(7);
        BinaryTree b=new BinaryTree(n);
        b.add(4);
        b.add(9);
        b.add(1);
        b.add(67);
        System.out.println(b);
        System.out.println(dfcFunction(n,67));
        System.out.println(bfcFunction(n,1));
    }

    public static boolean dfcFunction(Node root,int value){
        Stack stack=new Stack(root);
        while (stack.size()>0){
            Node temp=stack.pop();
            if(contains(temp,value))
                return true;
            else {
                if(temp.getRightChild()!=null) stack.push(temp.getRightChild());
                if(temp.getLeftChild()!=null) stack.push(temp.getLeftChild());
            }
        }
        return false;
    }
    public static boolean bfcFunction(Node root,int value){
        Stack stack=new Stack(root);
        while (stack.size()>0){
            Node temp=stack.pop();
            System.out.println(temp.getValue()+" dfc");

            if(contains(temp,value))
                return true;
            else {
                if(temp.getLeftChild()!=null) stack.append(temp.getLeftChild());
                if(temp.getRightChild()!=null) stack.append(temp.getRightChild());

            }
        }
        return false;
    }

    public static boolean contains(Node node,int value){

        if(value==node.getValue())
            return true;
        return false;
    }
}
