package boj_basic.stepp10;

import java.util.Scanner;

public class Q25305 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int k = sc.nextInt();
		int tmp = 0;
		
		int[] arr = new int[N];
		
		for(int i = 0; i<N; i++) {
			int x = sc.nextInt();
			arr[i]=x;
		}
		
		for(int i = 1; i<N; i++) {
			for(int j = 0; j<i; j++) {
				if(arr[i-j]<arr[i-j-1]) {
					tmp=arr[i-j-1];
					arr[i-j-1]=arr[i-j];
					arr[i-j]=tmp;
				}
			}
		}
		
		System.out.println(arr[N-k]);

	}

}
