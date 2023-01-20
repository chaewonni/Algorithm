package boj_basic.step7;

import java.util.Scanner;

public class Q10757 {
	

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next();
		String ss = sc.next();
		
		int num = 0;
		if(s.length()>ss.length())
			num = s.length();
		else
			num = ss.length();
		
		int[] arr = new int[num+1];
		int[] arr2 = new int[num +1];
		
		for(int i = 0; i<s.length(); i++) {
			arr[i] = s.charAt(s.length()-1-i)-'0';
		}
		
		for(int i = 0; i<ss.length(); i++) {
			arr2[i] = ss.charAt(ss.length()-1-i)-'0';
		}
		
		for(int i = 0; i<num; i++) {
			if(arr[i]+arr2[i]>=10) {
				arr[i]=(arr[i]+arr2[i])%10;
				arr[i+1]++;
			}else
				arr[i]=arr[i]+arr2[i];
		}
		if(arr[num]>0)
			System.out.print(arr[num]);
		for(int i = num-1; i>=0; i--) {
			System.out.print(arr[i]);
		}
		

	}

}
