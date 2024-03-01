package boj_basic.stepp19;

import java.util.Scanner;

public class Q11047 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int K = sc.nextInt();
		int[] arr = new int[N+1];
		int num = 0;
		
		for(int i = 1; i<=N; i++) {
			int A = sc.nextInt();
			arr[i]=A;
		}
		
		int sum = 0;
		
		while(K!=0) {
			for(int i = 1; i<=N; i++) {
				if(arr[i]<=K) {
					num = arr[i];
				}
					
			}
			sum += K/num;
			K = K%num;
		}
		System.out.println(sum);

	}

}
