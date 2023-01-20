package boj_basic.step7;

import java.util.Scanner;

public class Q2839_1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int x = 0;
		
		while(true) {
			if(n%5==0) {
				System.out.println(n/5+x);
				break;
			}
			else if(n<=0) {
				System.out.println(-1);
				break;
			}
			
			n-=3;
			x++;
		}

	}

}
