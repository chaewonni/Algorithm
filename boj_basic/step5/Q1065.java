package boj_basic.step5;

import java.util.Scanner;

public class Q1065 {
	
	static int han(int n) {
		String s = Integer.toString(n);
		int num = 0;
		int cnt = 0;
		for(int i = 0; i<s.length(); i++) {
			if(i+1<s.length() && i-1>0) {
				if((s.charAt(i+1)-'0')-(s.charAt(i)-'0')==(s.charAt(i)-'0')-(s.charAt(i-1)-'0')); 
					cnt++;
			}
		}
		if(cnt == s.length()-1)
			num = n;
		System.out.println(n);
		return n;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int cnt = 0;
		boolean[] b = new boolean[N+1];
		for(int i = 1; i<=N; i++) {
			if(han(i)<=N)
				b[han(i)]=true;
		}
		
		
		for(int i = 1; i<=N; i++) {
			if(b[han(i)]==true) {
				cnt++;
			}
		}
		
		System.out.println(cnt);
		
	}

}


