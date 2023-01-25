package boj_basic.step8;

import java.util.Scanner;

public class Q4948 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			int sum = 0;
			int n = sc.nextInt();
			int[] arr = new int[2*n+1];
			if(n==0)
				break;
			else {
				for(int i = n+1; i<=2*n; i++) {
					if(n==1)
						arr[n]=1;
					else {
						for(int j = 2; j<i; j++) {
							if(i%j==0)
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
