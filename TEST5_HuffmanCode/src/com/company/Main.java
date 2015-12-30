package com.company;

/* package whatever; // don't place package name! */

        import java.util.*;
        import java.lang.*;
        import java.io.*;


class TreeNode {
    private String bite;
    private int frequency;
    private String value;
    private TreeNode parent;

    public TreeNode() {
        this.bite = "";
        this.frequency = 0;
        this.value = "";
        this.parent = null;
    }


    public TreeNode(String bite, int frequency) {
        this.bite = bite;
        this.frequency = frequency;
        this.value = "";
        this.parent = null;
    }

    public TreeNode(TreeNode node_i_, TreeNode node_j_, String value_) {
        this.bite = node_i_.bite + node_j_.bite;
        this.frequency = node_i_.frequency + node_j_.frequency;
        this.value = value_;
        this.parent = null;
    }

    public TreeNode(TreeNode node_i_, TreeNode node_j_) {
        this.bite = node_i_.bite + node_j_.bite;
        this.frequency = node_i_.frequency + node_j_.frequency;
        this.value = "";
        this.parent = null;
    }


    public String getBite() {
        return bite;
    }

    public void setBite(String bite) {
        this.bite = bite;
    }

    public int getFrequency() {
        return frequency;
    }

    public void setFrequency(int frequency) {
        this.frequency = frequency;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public TreeNode getParent() {
        return parent;
    }

    public void setParent(TreeNode parent) {
        this.parent = parent;
    }

    public String getCode_() {
        if (parent != null) {
            return this.value + parent.getCode();
        } else {
            return this.value;
        }

    }

    public String getCode() {
        return new StringBuilder(getCode_()).reverse().toString();
    }

    boolean isLetter(){
        return this.bite.length() == 1;
    }

}


class Tree {
    List<TreeNode> nodes;
    List<TreeNode> leaves;

    public Tree() {
        this.nodes = new ArrayList<>();
        this.leaves = new ArrayList<>();
    }

    public Tree(TreeNode root_) {
        this.nodes = new ArrayList<>();
        this.leaves = new ArrayList<>();
        nodes.add(root_);

    }

    public TreeNode addNode(TreeNode node_) {
        nodes.add(node_);
        if(node_.isLetter()) this.leaves.add(node_);
        return nodes.get(nodes.size() - 1);
    }


    public String getCodes() {
        StringBuilder result = new StringBuilder();
        for (TreeNode node : this.leaves) {
            result.append(node.getBite());
            result.append(": ");
            result.append(node.getCode());
            result.append("\n");
        }
        return  result.toString();
    }
    public int countLeaves() {
        return  leaves.size();
    }

    public String stringCoder(String s_){
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s_.length(); i++) {
            for (TreeNode node : this.leaves) {
                if(node.getBite().equals(String.valueOf(s_.charAt(i)))) result.append(node.getCode());
            }
        }
        return result.toString();
    }
}

class Queue {

    private List<TreeNode> queue;

    public Queue(String s_) {
        queue = new ArrayList<>();
        for (int i = 0; i < s_.length(); i++) Insert(s_.charAt(i));
    }

    public int size() {
        return queue.size();
    }

    public int Insert(TreeNode item_) {
        for (int i = queue.size() - 1; i > -1; i--) {
            TreeNode item_i = queue.get(i);
            if (item_i.getBite().equals(item_.getBite())) {
                item_i.setFrequency(item_i.getFrequency() + item_.getFrequency());
                for (int j = 0; j < i; j++) {
                    TreeNode item_j = queue.get(j);
                    if (item_j.getFrequency() < item_i.getFrequency()) {
                        queue.set(j, item_i);
                        queue.set(i, item_j);
                        return 0;
                    }
                }
                return 0;
            }
        }
        queue.add(item_);
        TreeNode item_i = item_;
        int i = queue.size() - 1;
        for (int j = i - 1; j > -1; j--) {
            TreeNode item_j = queue.get(j);
            if (item_j.getFrequency() < item_i.getFrequency()) {
                queue.set(j, item_i);
                queue.set(j + 1, item_j);
            }
        }
        return 1;
    }

    public int Insert(String s_) {
        TreeNode item = new TreeNode(s_, 1);
        return Insert(item);
    }

    public int Insert(char char_) {
        return Insert(String.valueOf(char_));
    }

    public TreeNode popUpMax() {
        TreeNode item = null;
        if (size() != 0) {
            item = queue.get(queue.size() - 1);
            queue.remove(queue.size() - 1);
        }
        return item;
    }


    public Tree makeTree() {
        Tree tree = new Tree();
        //Switcher sw = new Switcher(false);
        while (size() > 1) {
            TreeNode node_i = popUpMax();
            TreeNode node_j = popUpMax();
            node_i.setValue("1");
            node_j.setValue("0");
            TreeNode node = new TreeNode(node_i, node_j);
            node_i.setParent(node);
            node_j.setParent(node);
            tree.addNode(node_i);
            tree.addNode(node_j);
            Insert(node);
        }
        TreeNode root = popUpMax();
        if (root.isLetter()) root.setValue("0");
        tree.addNode(root);
        return tree;
    }

    //public void codesMaker(String s) {
    //    for (int i = 0; i < s.length(); i++) Insert(s.charAt(i));
    //    List<Item> queue_tmp = new ArrayList<>();
    //    for (int i = queue.size(); i > -1 ; i++) queue_tmp.add(queue.get(i));
    //    int index = 0;
    //    while(queue_tmp.size() > 1) {
    //        queue_tmp.get(index);
    //        queue_tmp.get(index);
    //    }
    //
    //
    //    Switcher switcher = new Switcher(false);
    //    StringBuilder code = new StringBuilder();
    //
    //    if (queue.size() == 1) code.append(switcher.pR());
    //    for(int i = 0; i < queue.size() - 1; i++){
    //        queue.get(i).setCode(code.toString() + switcher.p());
    //        code.append(switcher.pR());
    //    }
    //    queue.get(queue.size() - 1).setCode(code.toString());
    //    this.code = code.toString();
    //}


    //public void printCodes() {
    //    for (int i = 0; i < queue.size(); i++) {
    //        Item item = queue.get(i);
    //        System.out.print(item.getItem() + ": " + item.getCode() + "\n");
    //    }
    //}


    //public String getCode(char letter_) {
    //    for (int i = 0; i < queue.size(); i++) {
    //        Item item = queue.get(i);
    //        if(item.getItem().equals(String.valueOf(letter_)))  return item.getCode();
    //    }
    //    return "";
    //}


    //public String CodeString(String s) {
    //    StringBuilder code_s = new StringBuilder();
    //    for (int i = 0; i < s.length(); i++) {
    //        code_s.append(getCode(s.charAt(i)));
    //    }
    //    System.out.print(queue.size() + " " + code_s.length() + "\n");
    //    printCodes();
    //    System.out.print(code_s.toString() + "\n");
    //    return code_s.toString();
    //}

    //public String DeCodeString(String code_s_) {
    //    StringBuilder code_s = new StringBuilder(code_s_);
    //    StringBuilder s = new StringBuilder();
    //    while (code_s.length() > 0){
    //        for(int i = 0; i < code_s.length(); i++){
    //            for(int j = 0; j < queue.size(); j++){
    //                if (code_s.substring(0, i + 1).equals(queue.get(j).getCode())) {
    //                    s.append(queue.get(j).getItem());
    //                    code_s.delete(0, i + 1);
    //                    break;
    //                }
    //            }
    //        }
    //
    //    }
    //    System.out.print(s.toString()  + "\n");
    //    return s.toString();
    //}


}

public class Main {
    public static void main(String[] args) throws java.lang.Exception {

        Scanner input = new Scanner(System.in);
        String s = input.nextLine();
        Queue H = new Queue(s);
        Tree tree = H.makeTree();
        String s_code = tree.stringCoder(s);
        System.out.print(tree.countLeaves() + " " + s_code.length() + "\n");
        System.out.print(tree.getCodes());
        System.out.print(s_code);
        //String code_s = H.CodeString(s);
        //s = H.DeCodeString(code_s);

        //TreeNode root  = new TreeNode("0");
        //Tree tree = new Tree(root);
        //TreeNode n3 = tree.addNode(tree.addNode(tree.addNode(root, "1"), "3"), "4");
        //n3.printBench();
        //root.printBench();
    }
}
