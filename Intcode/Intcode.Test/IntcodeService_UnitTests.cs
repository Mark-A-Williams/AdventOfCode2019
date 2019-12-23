using System;
using Xunit;
using Intcode;
using System.Linq;
using System.Collections.Generic;

namespace Intcode.Test
{
    public class IntcodeService_UnitTests
    {
        public IntcodeService Sut { get; set; }

        public IntcodeService_UnitTests()
        {
            Sut = new IntcodeService();

        }

        [Fact]
        public void CanImportIntcodeProgramFromFile()
        {
            // Arrange
            var day = 2;

            // Act
            Sut.ImportIntcodeProgamFromFile(day);
            var intcodeProgram = Sut.IntcodeProgram;

            // Assert
            Assert.NotNull(intcodeProgram);
        }

        [Fact]
        public void CanIdentifyOpcodes()
        {
            // Arrange
            Sut.ImportIntcodeProgamFromFile(2);
            var intcodeProgram = Sut.IntcodeProgram;

            // Act
            var opcodeList = new List<string>();
            foreach (var parameter in intcodeProgram.Where((value, index) => index % 4 == 0 && index != intcodeProgram.Count() - 1).ToArray())
            {
                var opcodeName = Enum.GetName(typeof(Opcode), parameter);
                opcodeList.Add(opcodeName);
            }

            // Assert
            foreach (var opcode in opcodeList)
            {
                Assert.NotNull(opcode);
            }
        }

        [Theory]
        [InlineData(new int[] { 1, 3, 6, 2, 0, 7, 5 }, 
                    new int[] { 1, 3, 7, 2, 0, 7, 5 })]
        [InlineData(new int[] { 1, 2, 2, 4, 0 },
                    new int[] { 1, 2, 2, 4, 4 })]
        [InlineData(new int[] { 1, 5, 0, 2, 0, 7, 6 },
                    new int[] { 1, 5, 8, 2, 0, 7, 6 })]
        public void Opcode1AddsInputs(int[] initial, int[] final)
        {
            // Arrange
            Sut.IntcodeProgram = initial;

            // Act
            Sut.EvaluateOpcode(0);

            // Assert
            Assert.Equal(final, Sut.IntcodeProgram);
        }

        [Theory]
        [InlineData(new int[] { 2, 3, 6, 2, 0, 7, 5 },
                    new int[] { 2, 3, 10, 2, 0, 7, 5 })]
        [InlineData(new int[] { 2, 2, 2, 4, 0 },
                    new int[] { 2, 2, 2, 4, 4 })]
        [InlineData(new int[] { 2, 5, 0, 2, 0, 7, 6 },
                    new int[] { 2, 5, 14, 2, 0, 7, 6 })]
        public void Opcode2MultipliesInputs(int[] initial, int[] final)
        {
            // Arrange
            Sut.IntcodeProgram = initial;

            // Act
            Sut.EvaluateOpcode(0);

            // Assert
            Assert.Equal(final, Sut.IntcodeProgram);
        }
    }
}
