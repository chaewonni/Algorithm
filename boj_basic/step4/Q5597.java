package boj_basic.step4;

import java.util.Scanner;

public class Q5597 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] intArray = new int[31];
		
		for(int i = 1; i<intArray.length; i++) {
			intArray[i] = 0;
		}
		int num = 0;
		for(int i = 0; i<28; i++) {
			num = sc.nextInt();
			intArray[num] =1;
		}
		
		for(int i = 1; i<intArray.length; i++) {
			if(intArray[i]==0)
				System.out.println(i);
		}

	}

}
