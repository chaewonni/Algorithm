package boj_basic.step7;

import java.util.Scanner;

public class Q2839 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		if(N/5==0)
			System.out.println(-1);
		else if((N%5)%3==0)
			System.out.println(N/5+(N%5)/3);
		else if((N%5)%3>0) {
			if(N%3==0)
				System.out.println(N/3);
			else
				System.out.println(-1);
		}



	}

}
