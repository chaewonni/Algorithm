package boj_basic.step6;

import java.util.Scanner;

public class Q1157_2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		
		int arr[] = new int[26];
		
		for(int i = 0; i<s.length(); i++) {
			if('A' <= s.charAt(i) && s.charAt(i) <= 'Z')
				arr[s.charAt(i)-'A']++;
			else
				arr[s.charAt(i)-'a']++;
		}
		int max = -1;
		char ch = '?';
		
		for(int i = 0; i<26; i++) {
			if(arr[i]>max) {
				max = arr[i];
				ch = (char) (i + 65);
			}
			else if(arr[i] == max)
				ch = '?';
		}
		System.out.println(ch);

	}

}
