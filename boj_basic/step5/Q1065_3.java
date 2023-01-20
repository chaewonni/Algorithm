package boj_basic.step5;

import java.util.Scanner;

public class Q1065_3 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int cnt = 0;
		
		for(int i = 1; i<=N; i++) {
			int num = 0;
			if(i>99) {
				if((i%100/10)-(i/100)==(i%100%10)-(i%100/10)) {
					cnt++;
				}
			}
			else
				cnt++;
		}
		
		System.out.println(cnt);
		
	}

}


