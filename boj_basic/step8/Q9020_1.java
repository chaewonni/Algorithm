package boj_basic.step8;

import java.util.Scanner;

public class Q9020_1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		
		for(int i = 0; i<T; i++) {
			int n = sc.nextInt();
			int[] arr = new int[n+1];
			arr[1]=1;
			for(int j = 2; j<n; j++) {
				if((int)Math.pow(j, 2)>n)
					break;
				else {
					for(int k = (int)Math.pow(j, 2); k<n; k+=j)
						arr[k]=1;
				}
					
			}
			int num = n/2;
			int num2 = n/2;
			
			while(true) {
				if(arr[num]==0 && arr[num2]==0) {
					System.out.println(num+" " + num2);
					break;
				}
				else
					num--; num2++;
			}
		}

	}

}
