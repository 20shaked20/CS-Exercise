package Threads_Java;

import java.io.*;
import java.util.*;


/**
 * This is another option to create a sample thread by using runnable,
 * it's the same as extend, but used in various sceneries depends on your needs.
 * The difference is mainly:
 * When we extend Thread class, each of our thread creates unique object and associate with it.
 * When we implement Runnable, it shares the same object to multiple threads.
 */
public class implement_runnable implements Runnable {
    // method to start Thread
    public void run() {
        System.out.println("Thread is Running Successfully");
    }

    public static void main(String[] args) {
        implement_runnable g1 = new implement_runnable();
        // initializing Thread Object
        Thread t1 = new Thread(g1, "My New Thread");
        t1.start(); // can do run also

        String t_name = t1.getName();
        System.out.println("Thread name =>" + t_name);
    }
}