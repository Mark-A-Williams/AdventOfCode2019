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
    }
}
