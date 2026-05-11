using System;
using System.Linq;
using LeetCode.CSharp.Algorithms;
using Xunit;

namespace LeetCode.CSharp.Tests.Algorithms;

public class _0001_TwoSumTests
{
    [Theory]
    [InlineData(new[] {2, 7, 11, 15}, 9, new[] {0, 1})]
    public void TwoSum_ShouldReturnCorrectIndices(int[] nums, int target, int[] expected)
    {
        // Arrange
        var sut = new _0001_TwoSum();

        // Act
        var result = sut.TwoSum(nums, target);

        // Assert
        Assert.Equal(expected.OrderBy(x => x), result.OrderBy(x => x));
    }

    [Fact]
    public void TwoSum_ShouldThrowException_WhenNoSolutionExists()
    {
        // Arrange
        var sut = new _0001_TwoSum();
        var nums = new[] {1, 2, 3};
        var target = 7;

        // Act & Assert
        Assert.Throws<InvalidOperationException>(() => sut.TwoSum(nums, target));
    }
}
