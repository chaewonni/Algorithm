package boj_basic.step3;

import java.util.Scanner;

public class Q1110 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		int NUM = 0;
		int i = 0;
		NUM = (num%10)*10 + ((num/10 + num%10)%10);
		
		while(true) {
			if(NUM!=num) {
				NUM = (NUM%10)*10 + ((NUM/10 + NUM%10)%10);
				i++;
			}
			else {
				if(NUM == num);
				break;
			}
		}
		System.out.println(i+1);

	}

}
