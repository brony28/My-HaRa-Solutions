import java.io.*;
import java.util.*;
import java.util.Scanner;
import java.util.ArrayList;

public class hand{
	public static void main(String[] args) {
		int i,outp;
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		ArrayList<Integer> ans = new ArrayList<Integer>();

		for(i=0;i<t;i++){
			int inp = sc.nextInt();
			
			outp=((((inp-1)*(2+(inp-2)))/2));
			ans.add(outp);
		}
		for (i=0;i<ans.size() ;i++ ) {
			System.out.println(ans.get(i));
		}
	}
}