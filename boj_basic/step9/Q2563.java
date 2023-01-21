package boj_basic.step9;

import java.util.Scanner;

public class Q2563 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		int[][] arr = new int[101][101];
		
		for(int i = 0; i<101; i++) {
			for(int j = 0; j<101; j++) {
				arr[i][j] = 0;
			}
		}
		
		
		for(int i = 0; i<N; i++) {
			int num1 = sc.nextInt();
			int num2 = sc.nextInt();
			for(int j = num1; j< num1+10; j++) {
				for(int k = num2; k<num2+10; k++) {
					arr[j][k]=1;
				}
			}
		}
		
		int sum = 0;
		for(int i = 0; i<101; i++) {
			for(int j = 0; j<101; j++) {
				sum += arr[i][j];
			}
		}
		
		System.out.println(sum);
		

	}

}
