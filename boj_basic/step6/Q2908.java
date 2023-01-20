package boj_basic.step6;

import java.util.Scanner;

public class Q2908 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int A = sc.nextInt();
		int B = sc.nextInt();
		
		int C = (A%100%10)*100+(A%100/10)*10+(A/100);
		int D = (B%100%10)*100+(B%100/10)*10+(B/100);
		
		if(C>D)
			System.out.println(C);
		else
			System.out.println(D);

	}

}
