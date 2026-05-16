namespace LeetCode.CSharp.Algorithms;
public class _0026_RemoveDuplicatesFromSortedArray 
{
    public int RemoveDuplicates(int[] nums)
    {
        if (nums.Length <= 1) return nums.Length;
        int k = 1;
        for (int i = 1; i < nums.Length; i++)
        {
            if (nums[i - 1] != nums[i])
            {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
}
