package boj_basic.step8;

import java.util.Scanner;

public class Q2581 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int M = sc.nextInt();
		int N = sc.nextInt();
		int num = 0;
		int[] arr = new int[10001];
		int sum = 0;
		
		for(num = M; num<=N; num++) {
			if(num == 1)
				arr[num]=1;
			else if (num >=2) {
				for(int i = 2; i<num; i++) {
					if(num % i == 0)
						arr[num]=1;
				}
			}
			
		}
		
		int min = 10000;
		
		for(int i = M; i<=N; i++) {
			if(arr[i]==0)
				sum += i;
		}
		
		if(sum == 0)
			System.out.println("-1");
		else {
			System.out.println(sum);
			for(int i = M; i<=N; i++) {
				if(arr[i]==0) {
					if(min > i)
						min = i;
				}
			}
			System.out.println(min);
		}
		
		

	}

}
