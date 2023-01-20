package boj_basic.step3;

import java.util.Scanner;

public class Q25304 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int X = sc.nextInt();
		int N = sc.nextInt();
		
		int a = 0;
		int b = 0;
		int sum = 0;
		
		for(int i = 0; i <N; i ++) {
			a = sc.nextInt();
			b = sc.nextInt();
			sum += a*b;
		}
		
		if(sum == X)
			System.out.println("Yes");
		else
			System.out.println("No");
		

	}

}
