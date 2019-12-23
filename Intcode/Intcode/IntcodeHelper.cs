using System;
using System.Collections.Generic;
using System.Text;

namespace Intcode
{
    public class IntcodeHelper
    {
        private readonly IntcodeService _intcodeService;

        public IntcodeHelper()
        {
            _intcodeService = new IntcodeService();
        }

        public int[] GetIntcodeProgram(int day)
        {
            _intcodeService.ImportIntcodeProgamFromFile(day);
            return _intcodeService.IntcodeProgram;
        }

        public int Day2Part1()
        {
            _intcodeService.ImportIntcodeProgamFromFile(2);
            _intcodeService.IntcodeProgram[1] = 12;
            _intcodeService.IntcodeProgram[2] = 2;
            _intcodeService.RunIntcodeProgram();
            return _intcodeService.IntcodeProgram[0];
        }

        public int Day2Part2()
        {
            var desiredOutput = 19690720;
            _intcodeService.ImportIntcodeProgamFromFile(2);
            var initialState = _intcodeService.IntcodeProgram;

            var acceptableRange = _intcodeService.IntcodeProgram.Length;

            for (int noun = 0; noun < acceptableRange; noun++)
            {
                for (int verb = 0; verb < acceptableRange; verb++)
                {
                    _intcodeService.IntcodeProgram[1] = noun;
                    _intcodeService.IntcodeProgram[2] = verb;
                    _intcodeService.RunIntcodeProgram();
                    
                    if (_intcodeService.IntcodeProgram[0] == desiredOutput)
                    {
                        return 100 * noun + verb;
                    }

                    _intcodeService.IntcodeProgram = initialState;
                }
            }

            return 0;
        }
    }
}
