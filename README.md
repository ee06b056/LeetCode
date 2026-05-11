# LeetCode

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
dotnet build LeetCode.sln              # build the solution
dotnet run --project LeetCode.CSharp   # run the console entry point
dotnet test                            # run all tests
dotnet restore                         # restore NuGet packages
```

## Layout

```
LeetCode.sln
LeetCode.CSharp/
  LeetCode.CSharp.csproj        # net10.0 console project
  Program.cs                    # entry-point sandbox
  Algorithms/                   # one file per LeetCode problem
    0001_TwoSum.cs
LeetCode.CSharp.Tests/
  LeetCode.CSharp.Tests.csproj  # xUnit test project (net10.0)
  Algorithms/                   # one test file per problem
    _0001_TwoSumTests.cs
```

Each solution lives in `LeetCode.CSharp/Algorithms/` under namespace `LeetCode.CSharp.Algorithms`. Files are named `<ZeroPaddedNumber>_<PascalProblemName>.cs` (e.g. `0001_TwoSum.cs`). The class name mirrors the filename with a leading underscore — `class _0001_TwoSum` — because C# identifiers can't start with a digit.

Tests mirror the source layout under `LeetCode.CSharp.Tests/Algorithms/` (namespace `LeetCode.CSharp.Tests.Algorithms`). Test files are named `_<ZeroPaddedNumber>_<PascalProblemName>Tests.cs` (e.g. `_0001_TwoSumTests.cs`), matching their source class with a `Tests` suffix.
