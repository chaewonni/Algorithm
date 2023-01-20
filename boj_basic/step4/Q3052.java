package boj_basic.step4;

import java.util.Scanner;

public class Q3052 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] intArray = new int[42];
		
		int num =0;
		for(int i = 0; i<intArray.length; i++) {
			intArray[i]=0;
		}
		for(int i = 0; i<10; i++) {
			
			num = sc.nextInt();
			intArray[num%42] =1;
			
		}
		
		int cnt = 0;
		for(int i = 0; i<intArray.length; i++) {
			if(intArray[i]==1)
				cnt++;
			}
		System.out.println(cnt);
	}

}
