using System;

namespace Intcode
{
    class Program
    {
        static void Main(string[] args)
        {
            var intcodeHelper = new IntcodeHelper();
            Console.WriteLine(intcodeHelper.GetInputFileUri());
        }
    }
}
