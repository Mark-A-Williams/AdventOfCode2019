using System;
using Xunit;
using Intcode;

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
    }
}
