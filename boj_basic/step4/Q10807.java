package boj_basic.step4;

import java.util.Scanner;

public class Q10807 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] intArray = new int[n];
		
		for(int i = 0; i<n; i ++) {
			int num = sc.nextInt();
			intArray[i] = num;
		}
		int v = sc.nextInt();
		int cnt = 0;
		for(int i = 0; i<n; i++) {
			if(intArray[i]==v)
				cnt++;
		}
			System.out.println(cnt);
	}


	}


