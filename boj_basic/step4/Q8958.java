package boj_basic.step4;

import java.util.Scanner;

public class Q8958 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = Integer.parseInt(sc.next());
		
		String[] stringArray = new String[N];
		
		for(int i = 0; i<N; i++) {
			int cnt = 0, sum = 0;
			stringArray[i] = sc.next();
			
			for(int j = 0; j<stringArray[i].length(); j++) {
				if(stringArray[i].charAt(j)=='O') {
					cnt ++;
				}
				else
					cnt = 0;
				sum += cnt;
			}
			System.out.println(sum);
		}

	}

}
