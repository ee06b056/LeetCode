# LeetCode-CSharp

Personal collection of LeetCode solutions written in C#, used as a hands-on space to learn .NET.

## Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download) (10.0.x)

Check with:

```
dotnet --version
```

## Build & run

From the repository root:

```
dotnet build LeetCode-CSharp.sln       # build the solution
dotnet run --project LeetCode          # run the console entry point
dotnet restore                         # restore NuGet packages
```

## Layout

```
LeetCode-CSharp.sln
LeetCode/
  LeetCode.csproj      # net10.0 console project
  Program.cs           # entry-point sandbox
  Algorithms/          # one file per LeetCode problem
    0001_TwoSum.cs
```

Each solution lives in `LeetCode/Algorithms/` under namespace `LeetCode.Algorithms`. Files are named `<ZeroPaddedNumber>_<PascalProblemName>.cs` (e.g. `0001_TwoSum.cs`). The class name mirrors the filename with a leading underscore — `class _0001_TwoSum` — because C# identifiers can't start with a digit.
