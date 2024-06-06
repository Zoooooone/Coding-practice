public class multithread {
    public static void main(String[] args) {
        MyThread myThread = new MyThread();
        myThread.start();
        for (int i = 0; i < 100; i++) {
            System.out.print("1");
        }
    }

    public static class MyThread extends Thread {
        public void run() {
            for (int i = 0; i < 100; i++) {
                System.out.print("2");
            }
        }
    }
}

