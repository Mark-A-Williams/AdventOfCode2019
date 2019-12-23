using System;
using System.Collections.Generic;
using System.Text;

namespace Intcode
{
    public interface IIntcodeService
    {
        void ImportIntcodeProgamFromFile(int day);
        void EvaluateOpcode(int position);
    }
}
