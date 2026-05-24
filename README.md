# LeetCode

Personal collection of LeetCode solutions in C# and Python, used as a hands-on space to learn both .NET and the Python ecosystem. The repo carries parallel implementations as the practice migrates from C# to Python; the same problem can live in both tracks under the same problem number.

## Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download) (10.0.x) — for the C# track
- [Python 3.14](https://www.python.org/downloads/) — for the Python track

Check with:

```
dotnet --version
python3 --version
```

## Build & run

### C#

From the repository root:

```
dotnet build LeetCode.sln              # build the solution
dotnet run --project LeetCode.CSharp   # run the console entry point
dotnet test                            # run all tests
dotnet restore                         # restore NuGet packages
```

### Python

Activate the venv first (per shell, from repo root):

```
source LeetCode.Python/.venv/bin/activate
```

Then from inside `LeetCode.Python/`:

```
pytest -v                                          # run all tests
pytest tests/algorithms/test_p0001_two_sum.py      # run a single file
pytest -k two_sum                                  # filter by name
python program.py                                  # run the scratch file
```

Re-create the venv on a fresh machine:

```
python3 -m venv LeetCode.Python/.venv
source LeetCode.Python/.venv/bin/activate
pip install -r LeetCode.Python/requirements.txt
```

Leave the venv with `deactivate`.

## Layout

```
LeetCode.sln
LeetCode.CSharp/
  LeetCode.CSharp.csproj           # net10.0 console project
  Program.cs                       # entry-point sandbox
  Algorithms/                      # one file per LeetCode problem
    0001_TwoSum.cs
LeetCode.CSharp.Tests/
  LeetCode.CSharp.Tests.csproj     # xUnit test project (net10.0)
  Algorithms/                      # one test file per problem
    _0001_TwoSumTests.cs
LeetCode.Python/
  pyproject.toml                   # pytest config
  requirements.txt                 # pinned deps (pip freeze)
  program.py                       # scratch file (mirrors Program.cs)
  algorithms/                      # one file per LeetCode problem
    p0001_two_sum.py
  tests/algorithms/                # one test file per problem
    test_p0001_two_sum.py
Notes/                             # shared language-comparative reference
  data-structures.md
```

Problems use **four-digit zero-padded numbers** across both languages — the leading number identifies the LeetCode problem regardless of implementation language.

### C#

Solutions live in `LeetCode.CSharp/Algorithms/` under namespace `LeetCode.CSharp.Algorithms`. Files are named `<ZeroPaddedNumber>_<PascalProblemName>.cs` (e.g. `0001_TwoSum.cs`). The class name mirrors the filename with a leading underscore — `class _0001_TwoSum` — because C# identifiers can't start with a digit.

Tests mirror the source layout under `LeetCode.CSharp.Tests/Algorithms/` (namespace `LeetCode.CSharp.Tests.Algorithms`). Test files are named `_<ZeroPaddedNumber>_<PascalProblemName>Tests.cs` (e.g. `_0001_TwoSumTests.cs`), matching their source class with a `Tests` suffix.

### Python

Solutions live in `LeetCode.Python/algorithms/`. Files are named `p<ZeroPaddedNumber>_<snake_case_problem_name>.py` (e.g. `p0001_two_sum.py`). The `p` prefix sidesteps the "identifiers can't start with a digit" constraint while keeping the four-digit number scannable. The solution class is always `class Solution:` with the method signature LeetCode provides — copy-paste portable in either direction.

Tests mirror the source layout under `LeetCode.Python/tests/algorithms/`. Test files are named `test_p<ZeroPaddedNumber>_<snake_case_problem_name>.py` (e.g. `test_p0001_two_sum.py`), using plain `def test_*` functions (pytest style) with `@pytest.mark.parametrize` for the LeetCode example cases.
