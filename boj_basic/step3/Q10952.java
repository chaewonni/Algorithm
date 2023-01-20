package boj_basic.step3;

import java.util.Scanner;

public class Q10952 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num1 = 0;
		int num2 = 0;
		
		while(sc.hasNextInt()) {
			num1 = sc.nextInt();
			num2 = sc.nextInt();
			System.out.println(num1+num2);
		}

	}

}
