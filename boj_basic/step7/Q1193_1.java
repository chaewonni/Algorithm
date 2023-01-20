package boj_basic.step7;

import java.util.Scanner;

public class Q1193_1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int X = sc.nextInt();
		
		int line = 0;
		int cnt = 0;
		while(cnt < X) {
			line++;
			cnt = line*(line+1)/2; //등차수열 공식
		}
		
		if(line % 2 != 0) {
			int top = 1+(cnt-X);
			int bottom = line-(cnt-X);
			System.out.println(top+"/"+bottom);
		}
		else {
			int top = line - (cnt - X);
			int bottom = 1+(cnt - X);
			System.out.println(top+"/"+bottom);
		}

	}

}
