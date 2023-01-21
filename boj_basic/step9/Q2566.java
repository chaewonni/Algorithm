package boj_basic.step9;

import java.util.Scanner;

public class Q2566 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] arr = new int[9][9];
		
		for(int i = 0; i<9; i++) {
			for(int j = 0; j<9; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		
		int max = 0;
		int num1 =0;
		int num2 = 0;
		for(int i = 0; i<9; i++) {
			for(int j = 0; j<9; j++) {
				if(max < arr[i][j]) {
					max = arr[i][j];
					num1 = i;
					num2 = j;
				}
			}
		}
		
		System.out.println(max);
		System.out.println((num1+1) +" " + (num2+1));
		
	}

}
