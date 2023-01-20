package boj_basic.step2;

import java.util.Scanner;

public class Q2525 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();
		
		if(B+C<60)
			System.out.println(A + " " + (B+C));
		else {
			int i = (B+C)/60;
			int l = (B+C)%60;
			if((A+i)>=24) {
				System.out.println((A+i)%24 + " " +  l);
			}
			else
				System.out.println((A+i) + " " + l);
		}
		

	}

}
