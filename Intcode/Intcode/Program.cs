using System;

namespace Intcode
{
    class Program
    {
        static void Main(string[] args)
        {
            var intcodeHelper = new IntcodeHelper();
            var result = intcodeHelper.Day2Part2();
            Console.WriteLine(result);
        }
    }
}
