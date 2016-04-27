import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

class Reader {
    static BufferedReader reader;
    static StringTokenizer tokenizer;

    static void init(InputStream input) {
        reader = new BufferedReader(
                new InputStreamReader(input));
        tokenizer = new StringTokenizer("");
    }

    static String next() throws IOException {
        while (!tokenizer.hasMoreTokens()) {
            tokenizer = new StringTokenizer(
                    reader.readLine());
        }
        return tokenizer.nextToken();
    }

    static int nextInt() throws IOException {
        return Integer.parseInt(next());
    }

    static String nextStr() throws IOException {
        return next();
    }

    static double nextDouble() throws IOException {
        return Double.parseDouble(next());
    }
}


class Item implements Comparable {
    private int value;
    private Item parent;

    public Item(int value_, Item parent_) {
        this.value = value_;
        this.parent = parent_;
    }

    public Item(Item other_, char mode_) {
        switch (mode_) {
            case '1':
                this.value = other_.value + 1;
                this.parent = other_;
                break;
            case '2':
                this.value = other_.value * 2;
                this.parent = other_;
                break;
            case '3':
                this.value = other_.value * 3;
                this.parent = other_;
                break;
            default:
                break;

        }

    }

    public Item(int value_) {
        this.value = value_;
    }

    public void setParent(Item parent_) {
        this.parent = parent_;
    }

    public Item getParent() {
        return this.parent;
    }

    public String getTrack() {
        Item tmp = this;
        StringBuilder str = new StringBuilder(this.value);
        while (tmp != null) {
            str.append(" ");
            str.append(new StringBuilder(String.valueOf(tmp.value)).reverse());
            tmp = tmp.getParent();
        }
        return str.reverse().toString();
    }

    public int getTrackSize() {
        Item tmp = this;
        int count = 0;
        while (tmp != null) {
            count++;
            tmp = tmp.getParent();
        }
        return count - 1;
    }

    public int getValue() {
        return this.value;
    }

    @Override
    public String toString() {
        return "Item{" +
                "value=" + value +
                ", parent=" + parent +
                '}';
    }

    @Override
    public int compareTo(Object other_) {
        Item other_item = (Item) other_;
        return (this.value < other_item.value) ? -1 : ((this.value == other_item.value) ? 0 : 1);
    }

}


class Calculator {

    private Item n;
    private Item[] mass;

    public Calculator(Item n_) {
        this.n = n_;
        this.mass = new Item[n_.getValue() + 1];
    }


    private Item fillIn(Item item_, char mode_,  int[] mass_tmp_K_, List<Item> mass_tmp_V_) {
        Item item_tmp = new Item(item_, mode_);
        if ((item_tmp.compareTo(this.n) < 1) && (mass_tmp_K_[item_tmp.getValue()] == 0)) {
            mass_tmp_K_[item_tmp.getValue()] = item_tmp.getValue();
            mass_tmp_V_.add(item_tmp);
        }
        return item_tmp;
    }

    public Item findMinIter(){
        Item item_tmp = new Item(1);
        int[] mass_tmp_K = new int[this.n.getValue() + 1];
        List<Item> mass_tmp_V = new ArrayList<>();
        mass_tmp_K[1] = item_tmp.getValue();
        mass_tmp_V.add(item_tmp);
        int k = 0;
        while (item_tmp.compareTo(this.n) != 0){
            int length = mass_tmp_V.size();
            for(int i = k; i < length; i++){
                item_tmp = mass_tmp_V.get(i);
                if(fillIn(item_tmp, '1', mass_tmp_K, mass_tmp_V).compareTo(this.n) == 0) break;
                if(fillIn(item_tmp, '2', mass_tmp_K, mass_tmp_V).compareTo(this.n) == 0) break;
                if(fillIn(item_tmp, '3', mass_tmp_K, mass_tmp_V).compareTo(this.n) == 0) break;
            }
            k++;
            item_tmp = mass_tmp_V.get(mass_tmp_V.size() - 1);
        }
        return item_tmp;
    }

}

public class TEST16c {
    public static void main(String[] args) throws IOException {
        Reader.init(System.in);
        Item n = new Item(Reader.nextInt());
        Calculator C = new Calculator(n);
        Item result = C.findMinIter();
        System.out.println(result.getTrackSize());
        System.out.print(result.getTrack());
    }
}
