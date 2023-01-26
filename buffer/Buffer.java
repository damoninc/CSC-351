package buffer;

public class Buffer {
    public String reverseItemAtIndex(int n) {
        String[] data = new String[] { "Alice", "Bob", "Charlie", "Daisy", "Ernie", "Frank", "Gob"};
        String x = data[n];
        StringBuilder sb = new StringBuilder(x);
        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        Buffer buffer = new Buffer();

        System.out.println("first item: " + buffer.reverseItemAtIndex(0));
        System.out.println("last item: " + buffer.reverseItemAtIndex(6));
        System.out.println("after data end: " + buffer.reverseItemAtIndex(7));
        System.out.println("after buffer end: " + buffer.reverseItemAtIndex(1024));
        System.out.println("before buffer start: " + buffer.reverseItemAtIndex(-1));

    }
}