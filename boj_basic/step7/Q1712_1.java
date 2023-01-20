package boj_basic.step7;

import java.util.Scanner;

public class Q1712_1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int A = sc.nextInt(); //고정비용
		int B = sc.nextInt(); //가변비용
		int C = sc.nextInt(); //제품가격
		
		int s = 0;
		if(B>=C)
			System.out.println(-1);
		else {
			s=A/(C-B); //손익분기점 계산법
			System.out.println(s+1);
		}
			

	}

}
