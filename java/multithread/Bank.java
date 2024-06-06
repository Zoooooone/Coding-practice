public class Bank {
    private int money;
    private String name;

    public Bank(String name, int money) {
        this.name = name;
        this.money = money;
    }

    public synchronized void deposit(int m) {
        money += m;
    }

    public synchronized boolean withdraw(int m) {
        if (money >= m) {
            money -= m;
            return true;
        } else {
            return false;
        }
    }

    public String getName() {
        return name;
    }

    public static void main(String[] args) {
        Bank bank = new Bank("A", 100);

        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 10; i++) {
                bank.deposit(10);
                System.out.println("deposit: " + 10 + " money: " + bank.money);
                try {
                    Thread.sleep(50);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }, "Thread 1");

        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 10; i++) {
                bank.withdraw(10);
                System.out.println("withdraw: " + 10 + " money: " + bank.money);
                try {
                    Thread.sleep(50);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }, "Thread 2");

        t1.start();
        t2.start();
    }
}
