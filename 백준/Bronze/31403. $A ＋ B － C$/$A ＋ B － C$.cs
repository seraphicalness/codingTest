using System;
using System.Linq;
using System.Text;

namespace baekjoon
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int A = int.Parse(Console.ReadLine());
            int B = int.Parse(Console.ReadLine());
            int C = int.Parse(Console.ReadLine());

            Console.WriteLine(A + B - C);
            string result = A.ToString() + B.ToString();
            Console.WriteLine(int.Parse(result) - C);


        }
    }
}

