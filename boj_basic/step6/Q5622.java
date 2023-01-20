package boj_basic.step6;

import java.util.Scanner;

public class Q5622 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		int cnt = 0;
		for(int i = 0; i<s.length(); i++) {
			switch(s.charAt(i)) {
			case 'A': case 'B': case 'C':
				cnt= cnt + 3;
				break;
			case 'D': case 'E': case 'F':
				cnt = cnt + 4;
				break;
			case 'G': case 'H': case 'I':
				cnt = cnt + 5;
				break;
			case 'J': case 'K': case 'L':
				cnt = cnt + 6;
				break;
			case 'M': case 'N': case 'O':
				cnt = cnt + 7;
				break;
			case 'P': case 'Q': case 'R': case 'S':
				cnt = cnt + 8;
				break;
			case 'T': case 'U': case 'V': 
				cnt = cnt + 9;
				break;
			case 'W': case 'X': case 'Y': case 'Z':
				cnt = cnt + 10;
				break;
			}
			
		}
		System.out.println(cnt);

	}

}
