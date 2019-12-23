using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Linq;

namespace Intcode
{
    public class IntcodeService : IIntcodeService
    {
        public int[] IntcodeProgram { get; set; }
        public string BasePath { get; set; }

        public IntcodeService()
        {
            var currentDirectory = Directory.GetCurrentDirectory();
            BasePath = currentDirectory.Substring(0, currentDirectory.LastIndexOf("2019") + 5);
        }

        public void ImportIntcodeProgamFromFile(int day)
        {
            var filePath = BasePath + $@"Inputs\day{day}input.txt";
            var text = File.ReadAllText(filePath).Trim();
            var intcodeProgramAsStrings = text.Split(',');
            IntcodeProgram = Array.ConvertAll(intcodeProgramAsStrings, s => int.Parse(s));
        }

        public void RunIntcodeProgram()
        {
            for (int i = 0; i < IntcodeProgram.Count(); i += 4)
            {
                EvaluateOpcode(i);
            }
        }

        public void EvaluateOpcode(int position)
        {
            var opcode = IntcodeProgram[position];
            switch (opcode)
            {
                case (int)Opcode.Add:
                    EvaluateOpcode1(position);
                    break;

                case (int)Opcode.Multiply:
                    EvaluateOpcode2(position);
                    break;
            }
        }

        public void EvaluateOpcode1(int position)
        {
            var inputPosition1 = IntcodeProgram[position + 1];
            var inputPosition2 = IntcodeProgram[position + 2];
            var outputPosition = IntcodeProgram[position + 3];

            IntcodeProgram[outputPosition] = IntcodeProgram[inputPosition1] + IntcodeProgram[inputPosition2];
        }

        public void EvaluateOpcode2(int position)
        {
            var inputPosition1 = IntcodeProgram[position + 1];
            var inputPosition2 = IntcodeProgram[position + 2];
            var outputPosition = IntcodeProgram[position + 3];

            IntcodeProgram[outputPosition] = IntcodeProgram[inputPosition1] * IntcodeProgram[inputPosition2];
        }
    }
}
