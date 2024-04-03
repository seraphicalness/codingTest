using System;
using System.Linq;
using System.Text;

namespace baekjoon
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int[] num = new int[n];

            for (int i = 0; i < n; i++)
            {
                num[i] = int.Parse(Console.ReadLine());

            }
            int[] a = num.Distinct().ToArray();
            Array.Sort(a);

            StringBuilder sb = new StringBuilder(string.Join("\n",a));

            Console.WriteLine(sb);


        }
    }
}

