package boj_basic.step4;

import java.util.Scanner;

public class Q10781 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int X = sc.nextInt();
		
		int[] intArray = new int[N];
		
		for(int i = 0; i<N; i++) {
			intArray[i] = sc.nextInt();
			if(intArray[i]<X)
				System.out.print(intArray[i] + " ");
		}
		
//		for(int i = 0; i<N; i ++)
//			if(intArray[i]<X)
//				System.out.print(intArray[i] + " ");

	}

}
