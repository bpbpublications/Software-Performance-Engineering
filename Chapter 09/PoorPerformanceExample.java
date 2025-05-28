import java.util.ArrayList;
import java.util.List;

public class PoorPerformanceExample {
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        List<Dummy> DummyCollection = new ArrayList();
        
        String result = "";
        for (int i = 0; i < 1000000; i++) {
            result += " " + i; // Inefficient string concatenation
            DummyCollection.add(new Dummy());
        }

        long endTime = System.currentTimeMillis();
        System.out.println("Result: " + result);
        System.out.println("Execution time: " + (endTime - startTime) + " milliseconds");
    }
}
