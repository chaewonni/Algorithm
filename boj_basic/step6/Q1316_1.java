package boj_basic.step6;

import java.util.Scanner;

public class Q1316_1 {
	static Scanner sc = new Scanner(System.in);
	
	public static boolean check() {
		boolean[] check = new boolean[26];
		int prev = 0;
		String s = sc.next();
		
		for(int i = 0; i<s.length(); i++) {
			int now=s.charAt(i);
			
			if(prev != now) {
				if(check[now-'a']==false) {
					check[now-'a']=true;
					prev = now;
				}
				else
					return false;
			}
			else
				continue;
		}
		return true;
	}

	public static void main(String[] args) {
		
		int cnt = 0;
		int N = sc.nextInt();
		
		for(int i = 0; i<N; i++) {
			if(check()==true) {
				cnt++;
			}
		}
		System.out.println(cnt);

	}

}
