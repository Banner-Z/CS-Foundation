//���ѡ��
//http://lx.lanqiao.cn/problem.page?gpid=T14

import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Vector;

public class ALGO4 {
	public static Vector<Vector<Integer>> v = new Vector<>();
	public static int[][] dp;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		dp = new int[n][2];
		for(int i=0;i<n;i++) {
			dp[i][1] = sc.nextInt();
			v.add(new Vector<Integer>());
		}
		for(int i=0;i<n-1;i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			v.get(a-1).add(b-1);
			v.get(b-1).add(a-1);	//��Ϊ��ȷ�����ӹ�ϵ�����Լ�����
		}
		bfs(0,-1);
		System.out.println(Math.max(dp[0][0], dp[0][1]));	//��Ϊ�����ѣ�����0���
	}

	private static void bfs(int root, int pre) {
		Vector<Integer> son = v.get(root);
		for(int i=0;i<son.size();i++) {
			if(son.get(i)!=pre) {	//ֻҪ�������߼��ɣ����ⲻ���ж�visit
				bfs(son.get(i), root);
				dp[root][1] += dp[son.get(i)][0];
				dp[root][0] += Math.max(dp[son.get(i)][0], dp[son.get(i)][1]);
				
			}
		}
		
	}
	
}
