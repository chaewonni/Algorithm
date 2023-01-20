package boj_basic.step5;

public class Q4673_2 {
	
	static int d(int n) {
		String s = Integer.toString(n);
		int num = 0;
		int sum = 0;
		
		for(int i = 0; i<s.length(); i ++) {
			num = s.charAt(i)-'0';
			sum += num;
		}
		return n+sum;
	}

	public static void main(String[] args) {
		
		boolean check[] = new boolean[10001];
		
		for(int i = 1; i<10001; i++) {
			if(d(i)<10001) {
				check[d(i)]=true;
			}
		}
		
		for(int i =1; i<10001; i++) {
			if(check[i]==false) {
				System.out.println(i);
			}
		}

	}

}
