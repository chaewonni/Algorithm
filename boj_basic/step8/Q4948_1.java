package boj_basic.step8;

import java.util.Scanner;

public class Q4948_1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			int sum = 0;
			int n = sc.nextInt();
			int[] arr = new int[2*n+1];
			if(n==0)
				break;
			else {
				arr[1]=1;
				for(int num = 2; num<=2*n; num++) {
					if((int)Math.pow(num, 2)>2*n) 
						break;
					else {
						for(int i =(int)Math.pow(num, 2); i<=2*n; i+=num) {
							arr[i]=1;
						}
					}
				}
			}
			for(int i = n+1; i<=2*n; i++) {
				if(arr[i]==0)
					sum+=1;
			}
			System.out.println(sum);
		}

	}

}
