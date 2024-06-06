public class sleep {
    public static void main(String[] args) {
        System.out.print("1");
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
        }
    }
}
