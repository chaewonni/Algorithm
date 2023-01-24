package boj_basic.step8;

import java.util.Scanner;

public class Q1929_1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int M = sc.nextInt();
		int N = sc.nextInt();
		
		int[] arr = new int[N+1];		
		
		arr[1]=1; //1은 소수 아님. 미리 배열에 1로 저장
		
		for(int num = 2; num<=N; num++) {
			if((int)Math.pow(num,2)>1000000)
				break; //num을 제곱했을 때 범위(100000)를 넘어가면 break
			else {
				for(int i=(int)Math.pow(num, 2); i<=N; i=i+num) {
					arr[i]=1; //num의 배수들은 소수가 아니므로 배열에 1로 저장
				}
			}
		}
		
		for(int i = M; i<=N; i++) {
			if(arr[i]==0) { //소수일 때
				System.out.println(i); //출력
			}
		}

	}

}