# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Personal LeetCode practice in C#. Single console project (`LeetCode/LeetCode.csproj`) targeting `net10.0` with `ImplicitUsings` **disabled** and `Nullable` enabled. The only NuGet dependency is `Newtonsoft.Json`.

## Commands

Run from the repo root:

- Build: `dotnet build LeetCode-CSharp.sln`
- Run the console entry point: `dotnet run --project LeetCode`
- Restore packages: `dotnet restore`

There is no test project yet — `dotnet test` will not run anything until one is added.

## Conventions

- Solutions live in `LeetCode/Algorithms/` under namespace `LeetCode.Algorithms`.
- File and class names follow `<PascalProblemName>_<LeetCodeNumber>.cs` (e.g. `TwoSum_1.cs` for problem 1). Match the class name to the file name.
- Because `ImplicitUsings` is off, every file must declare its own `using` directives explicitly. The existing style places `using` statements **after** the file-scoped `namespace` declaration — keep that style for consistency with `TwoSum_1.cs` and `Program.cs`.
- `Program.cs` is currently just a stub `Main`; new problems are written as standalone classes in `Algorithms/` and are not wired into `Main` unless you need to invoke one ad hoc.
