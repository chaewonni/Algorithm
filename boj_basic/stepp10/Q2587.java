package boj_basic.stepp10;

import java.util.Scanner;

public class Q2587 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] arr = new int[5];
		int sum = 0;
		int mid = 0;
		int tmp = 0;
		
		for(int i = 0; i<5; i++) {
			int N = sc.nextInt();
			arr[i]=N;
		}
		
		for(int i = 1; i<5; i++) {
			for(int j = 0; j<i; j++) {
				if(arr[i-j]<arr[i-j-1]) {
					tmp=arr[i-j-1];
					arr[i-j-1]=arr[i-j];
					arr[i-j]=tmp;
				}
			}
		}
		
		for(int i = 0; i<5; i++) {
			sum+=arr[i];
		}

		System.out.println(sum/5);
		System.out.println(arr[2]);
		
	}

}
