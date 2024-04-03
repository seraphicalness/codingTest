using System;
using System.Text;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            // 시간 초과
            //string s = Console.ReadLine();
            //int n = int.Parse(s);
            //for (int i = 1; i <= n; i++)
            //{
            //    Console.WriteLine(i);
            //}

            int n = int.Parse(Console.ReadLine());
            StringBuilder allNum = new StringBuilder();

            for (int i = 1; i <= n; i++)
            {
                allNum.AppendLine(i.ToString());
            }

            Console.WriteLine(allNum);
        }
    }
    //Console.WriteLine("숫자를 입력하세요:");
    //string numString = Console.ReadLine();

    //if (int.TryParse(numString, out int num))
    //{
    //    for (int i = 1; i <= num; i++)
    //    {
    //        Console.WriteLine(i);
    //    }
}
 