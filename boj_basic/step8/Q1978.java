package boj_basic.step8;

import java.util.Scanner;

public class Q1978 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		

		int n = 0;
		for(int i = 0; i<N; i++) {
			int cnt = 0;
			int num = sc.nextInt();
			if(num == 1)
				cnt++;
			for(int j = 2; j<num; j++) {
				if(num%j==0)
					cnt++;
			}
			
			if(cnt==0)
				n++;
			
		}
		System.out.println(n);
		
		
		

	}

}
