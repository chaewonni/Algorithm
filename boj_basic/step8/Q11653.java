package boj_basic.step8;

import java.util.Scanner;

public class Q11653 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		while(true) {
			if(N==1)
				break;
			else {
				for(int i = 2; i<=N; i++) {
					if(N%i==0) {
						N=N/i;
						System.out.println(i);
						break;
					}
					
				}
			}
		}

	}

}
