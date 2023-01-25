package boj_basic.stepp10;

import java.util.Scanner;

public class Q2750 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[] arr = new int[N+1];
		
		for(int i = 0; i<N; i++) {
			int num = sc.nextInt();
			arr[i]=num;
		}
		
		int tmp = 0;
		for(int i = 1; i<N; i++) {
			for(int j = 0; j<i; j++) {
				if(arr[i-j]<arr[i-j-1]) {
					tmp=arr[i-j-1];
					arr[i-j-1]=arr[i-j];
					arr[i-j]=tmp;
				}
			}
		}
		
		for(int i = 0; i<N; i++) {
			System.out.println(arr[i]);
		}
	}

}
