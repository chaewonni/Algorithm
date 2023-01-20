package boj_basic.step5;

public class Q4673 {
	
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
		
		int[] array = new int[10001];
		for(int i = 1; i<10001; i++) {
			array[i]=0;
		}
			for(int i = 1; i<10001; i++) {
				if(d(i)<10001)
					array[d(i)]=1;
			}
			for(int j = 1; j<10001; j++) {
				if(array[j]==0) 
					System.out.println(j);
			}

	}

}
