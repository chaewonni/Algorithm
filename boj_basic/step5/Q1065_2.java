package boj_basic.step5;

import java.util.Scanner;

public class Q1065_2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int cnt = 0;
		
		for(int i = 1; i<=N; i++) {
			String s = Integer.toString(i);
			int num = 0;
			int cntt = 0;
			for(int j = 0; j<s.length(); j++) {
				if(j+1<s.length() && j-1>=0) {
					if((s.charAt(j+1)-'0')-(s.charAt(j)-'0')==(s.charAt(j)-'0')-(s.charAt(j-1)-'0')); 
						cntt++;
				}
			}
			if(cntt == s.length()-2)
				cnt++;
			else if(s.length()==1||s.length()==2)
				cnt++;
		}
		
		System.out.println(cnt);
		
	}

}


