package boj_basic.step7;

import java.util.Scanner;

public class Q2775 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		int k  = 0;
		int n = 0;
		int sum = 0;
		
		
		for(int i = 0; i<T; i++) {
			k = sc.nextInt();
			n = sc.nextInt();
			int[] arr = new int[n+1];
			for(int h = 0; h<=n; h++) {
				arr[h]=h;
			}
			for(int j = 1; j<=k; j++) {
				for(int l = 1; l<=n; l++) {
					arr[l]+=arr[l-1];
					sum = arr[l];
				}
				
			}
			System.out.println(sum);
			
		}

	}

}
