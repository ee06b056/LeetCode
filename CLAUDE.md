# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Personal LeetCode practice. The repo carries two parallel implementations as the user migrates from C# to Python:

- **C#** — `LeetCode.CSharp/`, `LeetCode.CSharp.Tests/`, `LeetCode.sln`. Original track, both projects target `net10.0` with `ImplicitUsings` **disabled** and `Nullable` enabled. `LeetCode.CSharp` is a console project with no NuGet deps; `LeetCode.CSharp.Tests` uses xUnit (`xunit`, `xunit.runner.visualstudio`, `Microsoft.NET.Test.Sdk`, `coverlet.collector`).
- **Python** — `LeetCode.Python/`. Newer track from 2026-05-23. Python 3.14 via Homebrew, isolated in a venv at `LeetCode.Python/.venv/`. pytest for tests, no other deps.

Shared `Notes/` (e.g. `Notes/data-structures.md`) contains language-comparative reference material that grows alongside both tracks.

## Commands

### C#

Run from the repo root:

- Build: `dotnet build LeetCode.sln`
- Run the console entry point: `dotnet run --project LeetCode.CSharp`
- Run tests: `dotnet test`
- Run a single problem's tests: `dotnet test --filter "FullyQualifiedName~_0001_TwoSum"`
- Restore packages: `dotnet restore`

### Python

Activate the venv first (per shell, from repo root):

```bash
source LeetCode.Python/.venv/bin/activate
```

Then from inside `LeetCode.Python/`:

- Run all tests: `pytest -v`
- Run a single file: `pytest tests/algorithms/test_p0001_two_sum.py`
- Filter by name: `pytest -k two_sum`
- Install a new package: `pip install <name>` then `pip freeze > requirements.txt`
- Re-create the env on a fresh machine: `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
- Run `program.py` (scratch file) ad hoc: `python program.py`

Leave the venv with `deactivate`.

## Conventions

Problems use **four-digit zero-padded numbers** across both languages — the leading number identifies the LeetCode problem regardless of language. The same problem solved in both languages keeps the same number.

### C#

- Solutions live in `LeetCode.CSharp/Algorithms/` under namespace `LeetCode.CSharp.Algorithms`.
- Files are named `<ZeroPaddedNumber>_<PascalProblemName>.cs` (4-digit number, e.g. `0001_TwoSum.cs`). The class name mirrors the filename with a leading underscore — `class _0001_TwoSum` — because C# identifiers can't start with a digit.
- `ImplicitUsings` is **deliberately off** in both projects — the user is learning .NET and wants to see every namespace referenced explicitly. Do not enable it.
- Place `using` directives **above** the file-scoped `namespace` declaration (the standard C# convention), as in `Program.cs` and `0001_TwoSum.cs`.
- `Program.cs` is currently just a stub `Main`; new problems are written as standalone classes in `Algorithms/` and are not wired into `Main` unless you need to invoke one ad hoc.
- Tests live in `LeetCode.CSharp.Tests/Algorithms/` under namespace `LeetCode.CSharp.Tests.Algorithms`, mirroring the source layout. One file per problem, named `_<ZeroPaddedNumber>_<PascalProblemName>Tests.cs` (e.g. `_0001_TwoSumTests.cs`); the class follows the same `_<Number>_<Name>Tests` pattern. Prefer `[Theory] + [InlineData]` for the LeetCode example cases and `[Fact]` for single scenarios like exception-throwing.

### Python

- Solutions live in `LeetCode.Python/algorithms/`.
- Files are named `p<ZeroPaddedNumber>_<snake_case_problem_name>.py` (e.g. `p0001_two_sum.py`). The `p` prefix sidesteps the "identifiers can't start with a digit" constraint while keeping the four-digit number scannable; a leading underscore is avoided because it carries "private by convention" meaning in Python.
- The solution class is always `class Solution:` with the method signature LeetCode provides (e.g. `def two_sum(self, nums: list[int], target: int) -> list[int]:`). This matches what gets pasted into LeetCode's submission box, so solutions are copy-paste portable in either direction.
- Type hints are encouraged on solution signatures (matches LeetCode's stub style and documents intent) but optional inside method bodies.
- `program.py` at the Python project root is a scratch file for chunk-by-chunk language exploration — mirrors `LeetCode.CSharp/Program.cs`. Not wired into anything; run with `python program.py`.
- Tests live in `LeetCode.Python/tests/algorithms/`, mirroring the source layout. One file per problem, named `test_p<ZeroPaddedNumber>_<snake_case_problem_name>.py` (e.g. `test_p0001_two_sum.py`). Use plain `def test_*` functions (pytest style, not `unittest.TestCase` classes). Prefer `@pytest.mark.parametrize` for the LeetCode example cases.
- `__init__.py` files mark `algorithms/`, `tests/`, and `tests/algorithms/` as packages — intentionally empty, presence-only.
- Dependencies are pinned in `LeetCode.Python/requirements.txt` via `pip freeze`. `LeetCode.Python/pyproject.toml` carries pytest config (test discovery paths) — no build-system or package metadata beyond the minimum.

## Working style — learning repo

This repository is a personal practice space for the user to learn the languages it uses. **Do not auto-edit code to fix issues you spot.** Instead:

- Explain what you'd change and why, point at the file and line, and let the user apply the change themselves.
- Doc-only updates (CLAUDE.md, README) and read-only investigation are fine to do directly.
- If the user explicitly asks you to make a code change ("go ahead and fix it", "apply that"), then edit — but the default is teach, not do.

## Reviewing solutions

Only review a solution when the user names it explicitly (e.g. "review 0009" or "look at PalindromeNumber"). Do not proactively review every file in the repo, batch-review recent commits, or volunteer reviews of solutions the user didn't ask about. When asked, give a structured read without auto-editing:

- **Correctness** — walk the algorithm, call out edge cases that pass and any that look suspicious (overflow, empty input, duplicates, negatives, off-by-one).
- **Idiomatic language usage** — comment on language-specific patterns. This repo is partly about learning the languages, so call these out even when the algorithm is fine.
  - **C# / .NET**: collection expressions, `TryGetValue` vs indexer, LINQ vs loops, nullable annotations, `Span<T>` opportunities.
  - **Python**: comprehensions vs explicit loops, `dict.get(k, default)` vs `if k in d`, `enumerate` / `zip` over manual indexing, the `collections` module (`Counter`, `defaultdict`, `deque`), `heapq`, `bisect`, walrus `:=` where it genuinely simplifies, f-strings, unpacking.
- **Complexity** — state time/space and whether a more standard approach (two-pointer, sliding window, hash map, DP, etc.) would be expected for the problem.
- **Dead code / warnings** — flag unused locals or dead branches. The C# project sets `TreatWarningsAsErrors` with `CS0168;CS0219` exempted, so these compile but are still worth pointing out. Python doesn't enforce this at the compiler level — call out lint-style issues directly.

## Follow-up suggestions

After a review, suggest 2–4 concrete next problems (number + title) that build on what was just practiced — e.g. another hash-map problem after Two Sum, another digit-manipulation problem after Palindrome Number. Keep the list short so the user can pick one and continue.
