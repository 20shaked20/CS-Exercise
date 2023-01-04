package Java.Threads_Java;

/**
 * By Extending Thread Class:
 * We can run Threads in Java by using Thread Class,
 * which provides constructors and methods for creating and performing operations on a Thread,
 * which extends a Thread class that can implement Runnable Interface.
 * We use the following constructors for creating the Thread:
 */
public class extend_thread extends Thread {
    // initiated run method for Thread
    public void run() {
        System.out.println("Thread Started Running...");
    }

    public static void main(String[] args) {
        extend_thread g1 = new extend_thread();
        // invoking Thread
        g1.start(); // can also do g1.run();
    }
}