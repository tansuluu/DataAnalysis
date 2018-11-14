import java.util.ArrayList;
import java.util.Arrays;

public class Stack {
    ArrayList<Node> list;

    public Stack(Node node) {
        list = new ArrayList<>();
        list.add(node);
    }

    Stack(){
        this.list=null;
    }

    public int size(){
        return list.size();
    }
    public void push(Node node){
        list.add(node);
    }
    public void append(Node node) {
        ArrayList<Node> temp = new ArrayList<>();
        if(list.size()==0){
            list.add(node);
        }
        else {
            temp.add(node);
            temp.addAll(list);
            list=temp;
        }
    }
    public Node pop(){
        return list.remove(list.size()-1);
    }

    public ArrayList<Node> getList() {
        return list;
    }

    public void setList(ArrayList<Node> list) {
        this.list = list;
    }
}
