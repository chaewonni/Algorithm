package boj_basic.step7;

import java.util.Scanner;

public class Q1712_1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int A = sc.nextInt(); //�������
		int B = sc.nextInt(); //�������
		int C = sc.nextInt(); //��ǰ����
		
		int s = 0;
		if(B>=C)
			System.out.println(-1);
		else {
			s=A/(C-B); //���ͺб��� ����
			System.out.println(s+1);
		}
			

	}

}
