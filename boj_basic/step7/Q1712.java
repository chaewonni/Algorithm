package boj_basic.step7;

import java.util.Scanner;

public class Q1712 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int A = sc.nextInt(); //�������
		int B = sc.nextInt(); //�������
		int C = sc.nextInt(); //��ǰ����
		
		int s = 0;
		int i = 0;
		for(int x = 2^63-1; x>0; x--) {
			if((A+B*x)<C*x) {
				s = x;
			}
			else {
				i = -1;
			}
				
		}
		if(s>0)
			System.out.println(s);
		else
			System.out.println(i);
			
		

	}

}
