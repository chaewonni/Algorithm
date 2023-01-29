package boj_basic.step8;

import java.util.Scanner;

public class Q9020 {

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
			int min = n;
			String[] brr = new String[n+1];
			
			for(int j = 1; j<n+1; j++) {
				for(int k = 1; k<n+1; k++) {
					if(arr[j]==0 && arr[k]==0) {
						if(j+k==n) {
							if(j<=k) 
								brr[k-j]=Integer.toString(j)+" "+Integer.toString(k);
						}
					}
				}
			}
			for(int j = 0; j<n+1; j++) {
				if(brr[j]!=null) {
					if(j<min)
						min = j;
				}
			}
			System.out.println(brr[min]);
		}

	}

}
