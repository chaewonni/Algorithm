package boj_basic.step7;

import java.util.Scanner;

public class Q1193 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int X = sc.nextInt();
		int count = 0;
		int i = 1;
		int j = 1;
		
		boolean down = false;
		boolean up = false;
		
		while(X!=count) {
			if(down) {
				if(j-1==0) {
					down = false;
					continue;
				}else {
					i+=1;
					j-=1;
					count++;
					continue;
				}
			}
			if (up) {
                if (i - 1 == 0) {
                    up = false;
                    continue;
                } else {
                    i -= 1;
                    j += 1;
                    count++;
                    continue;
                }
            }

            if (i == 1) {
                j += 1;
                count++;
                down = true;
                continue;
            } else if (j == 1) {
                i += 1;
                count++;
                up = true;
                continue;
            }

        }

        System.out.printf("%d/%d", i, j);
		}

	}


