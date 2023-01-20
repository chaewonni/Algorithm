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
		
		//BufferedReader로 입력한 값은 전부 String으로 리턴되므로 토큰화하여 가공해야함
		StringTokenizer st;
		
		//String값이 리턴되므로 필요한 형태로 형변환 해줘야한다.
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
