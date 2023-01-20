package boj_basic.step4;

import java.util.Scanner;

public class Q8958_1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = Integer.parseInt(sc.next());
		
		for(int i = 0; i<N; i++) {
			int cnt = 0;
			int sum = 0;
			String s = sc.next();
			for(int j = 0; j<s.length(); j++) {
				if(s.charAt(j)=='O')
					cnt++;
				else 
					cnt = 0;
				sum += cnt;
			}
			System.out.println(sum);
		}
		

	}

}
