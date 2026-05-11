# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Personal LeetCode practice in C#. Single console project (`LeetCode.CSharp/LeetCode.CSharp.csproj`) targeting `net10.0` with `ImplicitUsings` **disabled** and `Nullable` enabled. No NuGet dependencies.

## Commands

Run from the repo root:

- Build: `dotnet build LeetCode.sln`
- Run the console entry point: `dotnet run --project LeetCode.CSharp`
- Restore packages: `dotnet restore`

There is no test project yet — `dotnet test` will not run anything until one is added.

## Conventions

- Solutions live in `LeetCode.CSharp/Algorithms/` under namespace `LeetCode.CSharp.Algorithms`.
- Files are named `<ZeroPaddedNumber>_<PascalProblemName>.cs` (4-digit number, e.g. `0001_TwoSum.cs`). The class name mirrors the filename with a leading underscore — `class _0001_TwoSum` — because C# identifiers can't start with a digit.
- `ImplicitUsings` is **deliberately off** — the user is learning .NET and wants to see every namespace referenced explicitly. Do not enable it.
- Place `using` directives **above** the file-scoped `namespace` declaration (the standard C# convention), as in `Program.cs` and `0001_TwoSum.cs`.
- `Program.cs` is currently just a stub `Main`; new problems are written as standalone classes in `Algorithms/` and are not wired into `Main` unless you need to invoke one ad hoc.

## Working style — learning repo

This repository is a personal practice space for the user to learn C# / .NET. **Do not auto-edit code to fix issues you spot.** Instead:

- Explain what you'd change and why, point at the file and line, and let the user apply the change themselves.
- Doc-only updates (CLAUDE.md, README) and read-only investigation are fine to do directly.
- If the user explicitly asks you to make a code change ("go ahead and fix it", "apply that"), then edit — but the default is teach, not do.

## Reviewing solutions

When the user finishes a problem or asks for a review, give a structured read without auto-editing:

- **Correctness** — walk the algorithm, call out edge cases that pass and any that look suspicious (overflow, empty input, duplicates, negatives, off-by-one).
- **Idiomatic C# / .NET** — comment on language usage (collection expressions, `TryGetValue` vs indexer, LINQ vs loops, nullable annotations, `Span<T>` opportunities). This repo is partly about learning the language, so call these out even when the algorithm is fine.
- **Complexity** — state time/space and whether a more standard approach (two-pointer, sliding window, hash map, DP, etc.) would be expected for the problem.
- **Dead code / warnings** — flag unused locals or dead branches. The project sets `TreatWarningsAsErrors` with `CS0168;CS0219` exempted, so these compile but are still worth pointing out.

## Follow-up suggestions

After a review, suggest 2–4 concrete next problems (number + title) that build on what was just practiced — e.g. another hash-map problem after Two Sum, another digit-manipulation problem after Palindrome Number. Keep the list short so the user can pick one and continue.
