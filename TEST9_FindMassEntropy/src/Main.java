import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Scanner;

final class FastMath {
    private FastMath() {
    }
    public static int Signum(int par_) {
        if (par_ >= 0) return 1;
        return -1;
    }
}

class Item implements Comparable{
    private int value = 0;
    private int disorder;


    public Item(int value_) {
        this.value = value_;
        this.disorder = 0;
    }

    public int getDisorder() {
        return disorder;
    }

    public void setDisorder(int disorder_) {
        this.disorder = disorder_;
    }

    @Override
    public int compareTo(Object o) {
        if(this.value < ((Item) o).value) return -1;
        if(this.value > ((Item) o).value) return 1;
        return 0;
    }

    @Override
    public String toString() {
        return String.valueOf(this.value);
    }
}

class Mass {
    private Item[] mass;
    private int length;
    private int begin;
    private int end;
    private int entropy;

    public Mass(InputStream in_) {
        Scanner stdin = new Scanner(in_);
        this.length = stdin.nextInt();
        this.mass = new Item[this.length];
        for (int i = 0; i < this.length; i++) {
            Item item =  new Item(stdin.nextInt());
            this.mass[i] = item;
            if (i > 0) {
                for (int j = i - 1; j > -1; j--) {
                    if (item.compareTo(this.mass[j]) == -1) {
                        item.setDisorder(item.getDisorder() + 1);
                    } else {
                        break;
                    }
                }
            }
            entropy += item.getDisorder();
        }
        this.begin = 0;
        this.end = this.length;
    }

    public Item getItem(int i_) {
        return this.mass[this.begin + i_];
    }

    public int getLength() {
        return this.end - this.begin;
    }

    public void subMass(int begin_, int end_) {
        this.begin = (begin_ >= 0) ? begin_ : 0;
        this.end = (this.length >= end_) ? end_ : this.length;
    }

    public int getEntropy() {
        return entropy;
    }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < getLength(); i++) {
            result.append(getItem(i));
            result.append(" ");
        }
        return result.toString();
    }

}

public class Main {

    public static void main(String[] args) {
        Mass M = new Mass(System.in);
        System.out.print(M.getEntropy());
    }
}
