package boj_basic.step4;

import java.util.Scanner;

public class Q4344 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int C = sc.nextInt();
		
		for(int i = 0; i<C; i ++) {
			int sum = 0;
			int avg = 0;
			int cnt = 0;
			int N = sc.nextInt();
			int[] arr = new int[N];
			
			for(int j = 0; j<N; j++) {
				arr[j] =  sc.nextInt();
				
				sum += arr[j];
			}
			avg=sum/N;
			for(int k = 0; k<N; k++) {
				if(arr[k] > avg) 
					cnt++;
			}
			System.out.printf("%.3f%%\n",(double)cnt/N*100);
		}

	}

}
