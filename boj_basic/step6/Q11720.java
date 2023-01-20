package boj_basic.step6;

import java.util.Scanner;

public class Q11720 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int sum =0;
		String s = sc.next();
		
		for(int i = 0; i<N; i++) {
			sum += s.charAt(i)-'0';
		}
		System.out.println(sum);

	}

}
