# Reproduction artifacts

Copied from the project repository for the Project 2 report. The repository copies are the working versions; this folder is a snapshot.

Contents:

- `scripts/setup.sh` starts or checks MySQL 8.0.32 and fetches and builds the pinned Troc commit `a6d50e3f596b356137d2f8c3c8b31a61bf7fe2c5` into `.deps/Troc`.
- `scripts/run_all.sh` runs setup and the four reproduction runners.
- `repro/` contains one runner per bug and the WriteCheck #104833 case file.
- `results/` contains captured reference outputs from earlier runs.
- `compose.yaml` defines the MySQL 8.0.32 container (`csi5137-atdm-mysql8032`, host port 3307, root/root).

## Requirements

- Docker, and Git
- On macOS, Docker Desktop or Colima
- Network access to GitHub (Troc clone) and Docker Hub (`mysql:8.0.32`, `maven:3.9.11-eclipse-temurin-17`)

## Run

From this `artifacts/` folder:

```bash
cd artifacts
./scripts/run_all.sh
```

Expected final line:

```text
PASS: 4/4 representative MySQL bugs reproduced on MySQL 8.0.32.
```

Single runners, from `artifacts/`:

```bash
./repro/coddtest_111241.sh
./repro/ddlcheck_114904.sh
./repro/writecheck_104833.sh
./repro/radar_110125.sh
```

The scripts find their root from their own path, so they do not depend on the current directory. They write `.deps/` and `results/*.latest.txt` into this folder. Do not commit `.deps/`.

Status: these copied scripts have not been run from this layout for this report. The Docker reproduction was not rerun when the report was written; the values in the report come from `results/`.

`repro/coddtest_111421.sh` is an exploratory runner. It is not part of `run_all.sh` and does not print a PASS line.
