package boj_basic.step3;

import java.util.Scanner;

public class Q1110_1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		int i = 0;
		int copy = num;
		
		while(true) {
			num = ((num%10)*10) + ((num/10) + (num%10)) %10;
			i++;
			if(copy == num) {
				break;
			}
		}
		System.out.println(i);

	}

}
