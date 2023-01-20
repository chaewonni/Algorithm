package boj_basic.step6;

import java.util.Scanner;

public class Q1157 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		
		int[] arr = new int[26];

		for(int i = 0; i<26; i++) {
			for(int j = 0; j<s.length(); j++) {
				if(Character.isUpperCase(s.charAt(j)))
					if(Character.toLowerCase(s.charAt(j))-'a'==i) {
						arr[i]++;
					}
				else if(s.charAt(j)-'a'==i) {
					arr[i]++;
				}
			}
		}
		
		int max = -1;
		for(int i = 0; i<26; i++) {
			if(max < arr[i]) 
				max = i;	
		}
		System.out.println(max);
		System.out.println(Character.toUpperCase((char)(max+97)));
	}

}
