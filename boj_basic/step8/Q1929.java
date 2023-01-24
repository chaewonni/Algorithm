package boj_basic.step8;

import java.util.Scanner;

public class Q1929 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int M = sc.nextInt();
		int N = sc.nextInt();
		
		int[] arr = new int[N+1];		
		int num = 0;
		for(num = M; num<=N; num++) {
			if(num ==1)
				arr[num]=1;
			for(int i = 2; i<num; i++) {
				if(num%i==0)
					arr[num]=1;
			}
		}
		
		for(int i = M; i<=N; i++) {
			if(arr[i]==0) {
				System.out.println(i);
			}
		}

	}

}
