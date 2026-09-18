# Restore full Add-in project files

The full `VirastyarWordAddin2010.csproj` and legacy `VirastyarWordAddin.csproj` (targeting **.NET Framework 4.8** with **EmbedInteropTypes**) are stored as base64 chunks because of GitHub API size limits during automated upgrades.

## Restore

From the repository root:

```bash
python3 tools/restore-addin-csproj/restore_addin_csproj.py
```

This overwrites:

- `VirastyarWordAddin/VirastyarWordAddin2010/VirastyarWordAddin.csproj`
- `VirastyarWordAddin/VirastyarWordAddin/VirastyarWordAddin.csproj`

Then commit the restored files:

```bash
git add VirastyarWordAddin/
git commit -m "Restore full Add-in csproj files (.NET 4.8 + Embed Interop)"
git push
```

## What was upgraded

1. All library projects: .NET Framework 3.5/4.0 → **4.8**
2. Office Interop references: **EmbedInteropTypes=True**, SpecificVersion=False
3. Bootstrapper packages for .NET 3.5/4.0 Client set to Install=false
