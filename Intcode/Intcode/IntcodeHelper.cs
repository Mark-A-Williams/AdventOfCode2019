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
    }
}
