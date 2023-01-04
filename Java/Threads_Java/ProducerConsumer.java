package Java.Threads_Java;

/**
 * This is an example for typical producer - consumer.
 * here we can see the great use of synchronized methods and why we need them!
 * if we try to disable the sync from Put or Get, the threads will enter a state where its overrun by
 * "demanding too much but cannot produce enough"
 */
public class ProducerConsumer {

    public static void main(String[] args) {
        Buffer buf = new Buffer();


        Thread prod = new Producer(100, buf);
        Thread cons = new Consumer(100, buf);


        prod.start();
        cons.start();

        // Wait for the threads to finish
//    try {
//    	prod.join();
//    	cons.join();
//    } catch (InterruptedException e) {return;}
    }

}

class Buffer {
    private int contents;
    private boolean empty = true;

    //producer put//
    public synchronized void put(int i) throws InterruptedException {
        while (!empty) {    //wait till the buffer becomes empty
            try {
                wait();
            } catch (InterruptedException e) {
                throw e;
            }
        }
        contents = i;
        empty = false;
        System.out.println("Producer: put..." + i);
        notify();
    }

    //consumer get//
    public synchronized int get() throws InterruptedException {
        while (empty) {    //wait till something appears in the buffer
            try {
                wait();
            } catch (InterruptedException e) {
                throw e;
            }
        }
        empty = true;
        notify();
        int val = contents;
        System.out.println("Consumer: got..." + val);
        return val;
    }
}

class Producer extends Thread {
    private final int n;
    private final Buffer prodBuf;

    public Producer(int m, Buffer buf) {
        n = m;
        prodBuf = buf;
    }

    public void run() {
        for (int i = 0; i < n; i++) {
            try {
                Thread.sleep(500); // sleep for a randomly chosen time
            } catch (InterruptedException e) {
                return;
            }

            try {
                prodBuf.put(i + 1); //starting from 1, not 0
            } catch (InterruptedException e) {
                return;
            }

        }
    }
}

class Consumer extends Thread {
    private final int n;
    private final Buffer consBuf;

    public Consumer(int m, Buffer buf) {
        n = m;
        consBuf = buf;
    }

    public void run() {
        int value;
        for (int i = 0; i < n; i++) {
            try {
                value = consBuf.get();
            } catch (InterruptedException e) {
                return;
            }
            try {
                Thread.sleep(500); // sleep for a randomly chosen time
            } catch (InterruptedException e) {
                return;
            }

        }
    }
}