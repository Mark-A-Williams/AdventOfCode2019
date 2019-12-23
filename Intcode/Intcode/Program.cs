using System;

namespace Intcode
{
    class Program
    {
        static void Main(string[] args)
        {
            var intcodeHelper = new IntcodeHelper();
            var program = intcodeHelper.GetIntcodeProgram(2);
            foreach (var command in program)
            {
                Console.Write(command + ',');
            }
        }
    }
}
