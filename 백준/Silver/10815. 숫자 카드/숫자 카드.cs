using System;
using System.Collections.Generic;
using System.Linq;

namespace baekjoon
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int a = int.Parse(Console.ReadLine());
            string[] acard = Console.ReadLine().Split();

            int b = int.Parse(Console.ReadLine());
            string[] bcard = Console.ReadLine().Split();

            // acard 배열을 HashSet으로 변환
            HashSet<string> acardSet = new HashSet<string>(acard);

            for (int i = 0; i < bcard.Length; i++)
            {
                // acardSet에 bcard[i]가 있는지 확인
                if (acardSet.Contains(bcard[i]))
                {
                    bcard[i] = "1";
                }
                else
                {
                    bcard[i] = "0";
                }
            }

            Console.WriteLine(string.Join(" ", bcard));
        }
    }
}
