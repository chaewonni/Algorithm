package boj_basic.step6;

import java.util.Scanner;

public class Q2941 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		
		int cnt = 0;
		for(int i = 0; i<s.length(); i++) {
			switch(s.charAt(i)) {
			case '=': case '-': 
				break;
			case 'j':
				if(i>0) {
					if(s.charAt(i-1)=='l' || s.charAt(i-1)=='n')
						break;
					else
						cnt++;
				}
				else
					cnt++;
				break;
			case 'z':
				if(i<s.length()-1 && i>0) {
					if(s.charAt(i-1)=='d' && s.charAt(i+1)=='=')
						break;
					else
						cnt++;
				}
				else
					cnt++;
				break;
			default:
				cnt++;
				break;
			
			}
		}
		System.out.println(cnt);

	}

}
