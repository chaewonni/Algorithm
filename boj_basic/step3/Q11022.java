package boj_basic.step3;

import java.util.Scanner;

public class Q11022 {
		
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
			
		int T = sc.nextInt();
		int A=0;
		int B =0;
		int sum = 0;
			
		for(int i = 0; i<T; i ++) {
			A= sc.nextInt();
			B=sc.nextInt();
			sum = A+B;
			System.out.println("Case #" + (i+1) + ": " + A + " + " + B + " = " + sum);
		}
	}

		}
