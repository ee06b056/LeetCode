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
- `ImplicitUsings` is **deliberately off** — the user is learning .NET and wants to see every namespace referenced explicitly. Do not enable it.
- Place `using` directives **above** the file-scoped `namespace` declaration (the standard C# convention), as in `Program.cs` and `TwoSum_1.cs`.
- `Program.cs` is currently just a stub `Main`; new problems are written as standalone classes in `Algorithms/` and are not wired into `Main` unless you need to invoke one ad hoc.

## Working style — learning repo

This repository is a personal practice space for the user to learn C# / .NET. **Do not auto-edit code to fix issues you spot.** Instead:

- Explain what you'd change and why, point at the file and line, and let the user apply the change themselves.
- Doc-only updates (CLAUDE.md, README) and read-only investigation are fine to do directly.
- If the user explicitly asks you to make a code change ("go ahead and fix it", "apply that"), then edit — but the default is teach, not do.
