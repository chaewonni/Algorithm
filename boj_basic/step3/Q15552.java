package boj_basic.step3;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Q15552 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		//BufferedReader�� �Է��� ���� ���� String���� ���ϵǹǷ� ��ūȭ�Ͽ� �����ؾ���
		StringTokenizer st;
		
		//String���� ���ϵǹǷ� �ʿ��� ���·� ����ȯ ������Ѵ�.
		int T = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < T; i ++) {
			st = new StringTokenizer(br.readLine());
			
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			
			int result = A+B;
			
			bw.write(result+"\n");
		}
		
		bw.flush();
		

	}

}
