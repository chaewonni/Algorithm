package boj_basic.step3;

import java.util.Scanner;

public class Q2439 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		for(int i = 1; i<=N; i++) {
			for(int j = 0; j<N; j++) {
				if(j<(N-i)) {
					System.out.print(" ");
				}
				else
					System.out.print("*");
			}
			System.out.println();
		}

	}

}
