package boj_basic.step6;

import java.util.Scanner;

public class Q1316 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		String s = null;
		int cnt = 0;
		
		for(int i = 0; i<N; i++) {
			s = sc.next();
			
			for(int j = 0; j<s.length(); j++) {
				if(j<s.length()-2) {
					if(s.charAt(j)!=s.charAt(j+1)) {
						for(int k = j+2; k<s.length(); k++) {
							if(s.charAt(k)==s.charAt(j))
								break;
							else
								cnt++;
						}
					}
					else
						continue;
				}
				else
					cnt++;
			}
		}
		System.out.println(cnt);
		

	}

}
