package boj_basic.step6;

import java.util.Scanner;

public class Q10809 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		
		int[] arr = new int[26];
		for(int i = 0; i<arr.length; i++) {
			arr[i]=-1;
		}
		
		for(int i =s.length()-1; i>=0; i--) {
			arr[s.charAt(i)-97]=i;
		}
		
		for(int i = 0; i<26; i++) {
			System.out.print(arr[i] + " ");
		}

	}

}


/* String alpabet = scanner.next();
 * 
 * for(char i = 'a'; i<='z'; i++){
 * 	System.out.print(alpabet.indexOf(i) + " ");
 * }
 */
