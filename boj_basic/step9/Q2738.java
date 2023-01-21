package boj_basic.step9;

import java.util.Scanner;

public class Q2738 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		int[][] arr = new int[N][M];
		
		for(int i = 0; i<N; i++) {
			for(int j = 0; j<M; j++) {
				arr[i][j] = 0;
			}
		}
		
		for(int n = 0; n<2; n++) {
			for(int i = 0; i<N; i++) {
				for(int j = 0; j<M; j++) {
					arr[i][j] += sc.nextInt();
				}
			}
		}
		
		for(int i = 0; i<N; i++) {
			for(int j = 0; j<M; j++) {
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}

	}

}
