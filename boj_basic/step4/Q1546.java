package boj_basic.step4;

import java.util.Scanner;

public class Q1546 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		double[] Array = new double[num];
		
		for(int i = 0; i <Array.length; i++) {
			Array[i] =sc.nextInt();
		}
		
		double max = 0; 
		for(int i = 0; i<Array.length; i ++) {
			if(max < Array[i])
				max = Array[i];
		}
		
		double sum = 0;
		for(int i = 0; i<Array.length; i ++) {
			Array[i] = Array[i]/max*100;
			sum += Array[i];
		}
		
		System.out.println((double)sum/num);

	}

}
