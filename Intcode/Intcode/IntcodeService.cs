using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace Intcode
{
    public class IntcodeService : IIntcodeService
    {
        public List<string> IntcodeProgram { get; set; }
        public string BasePath { get; set; }

        public IntcodeService()
        {
            var currentDirectory = Directory.GetCurrentDirectory();
            BasePath = currentDirectory.Substring(0, currentDirectory.LastIndexOf("2019") + 5);
        }

        public void ImportIntcodeProgamFromFile(int day)
        {
           
        }

        public void PrintStuff()
        {
            Console.WriteLine("Hello, world!");
            Console.ReadKey();
        }
    }
}
