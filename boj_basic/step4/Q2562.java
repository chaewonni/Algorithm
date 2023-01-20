package boj_basic.step4;

import java.util.Scanner;

public class Q2562 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] intArray= new int[9];
		int max = 0;
		int i =0;
		int number = 0;
		
		for(i = 0; i<intArray.length; i++) {
			intArray[i] = sc.nextInt();
			
			if(intArray[i]>max) {
				max = intArray[i];
				number = i;
			}
				
		}
		
		System.out.println(max);
		System.out.println(number+1);
		
		

	}

}
