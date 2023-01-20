package boj_basic.step4;

import java.util.Scanner;

public class Q10818 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int max = -1000000;
		int min = 1000000;
		
		int[] intArray = new int[N];
		for(int i = 0; i <N; i++) {
			intArray[i] = sc.nextInt();
			
			if(intArray[i] > max)
				max = intArray[i];
			
			if(intArray[i] < min)
				min = intArray[i];
			
		}
		
	
		System.out.println(min + " " + max);
	}

}
