import java.io.*;
 
class Solution {
    static String solution(int N, int K)
    {
        String res = "";
         
        for (int i = 0; i < K; i++)
            res = res + (char)('a' + i);
        int count = 0;  
        for (int i = 0; i < N - K; i++)
        {
            res = res + (char)('a' + count);
            count++;
             
            if (count == K)
                count = 0;
        }
         
        return res;
    }
     
    // Driver code
    static public void main (String[] args)
    {
     
        int N = 5, K = 2;
         
        System.out.println(findString(n, k));
    }
}