using System;
using System.Collections.Generic;
using System.Text;

namespace Intcode
{
    public interface IIntcodeService
    {
        void ImportIntcodeProgamFromFile(int day);
        void RunIntcodeProgram();
        void EvaluateOpcode(int position);
        void EvaluateOpcode1(int position);
        void EvaluateOpcode2(int position);
    }
}
