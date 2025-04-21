import java.io.*;
import java.util.*;

public class 치즈 {
    static int N, M;
    static int[][] map;
    static boolean[][] visited;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int time = 0;

        while (true) {
            visited = new boolean[N][M];
            markOutsideAir(); //외부 공기 표시

            List<int []> toMelt = new ArrayList<>();
            
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (map[i][j] == 1 && shouldMelt(i,j)) {
                        toMelt.add(new int[]{i,j});
                    }
                }
            }

            if (toMelt.isEmpty()) break;

            for (int[] pos: toMelt) {
                map[pos[0]][pos[1]] = 0;
            }

            time++;
        }

        System.out.println(time);
    }

    static void markOutsideAir() {
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0,0});
        visited[0][0] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (nr >= 0 && nr < N && nc >= 0 && nc < M) {
                    if (!visited[nr][nc] && map[nr][nc] == 0) {
                        visited[nr][nc] = true;
                        q.add(new int[]{nr, nc});
                    }
                }
            }
        }
    }

    static boolean shouldMelt(int r, int c) {
        int airContact = 0;

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr >= 0 && nr < N && nc >= 0 && nc < M) {
                if (visited[nr][nc] && map[nr][nc] == 0) {
                    airContact++;
                }
            }
        }

        if (airContact >= 2) {
            return true;
        } else {
            return false;
        }
    }
}