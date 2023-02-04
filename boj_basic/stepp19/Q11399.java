package boj_basic.stepp19;

import java.util.Scanner;

public class Q11399 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[] arr = new int[1001];
		int sum = 0;
		int num = 0;
		
		for(int i = 0; i<N; i++) {
			int p = sc.nextInt();
			arr[i] = p;
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
				num += arr[i];
				sum+= num;
		}
		
		System.out.println(sum);

	}

}
