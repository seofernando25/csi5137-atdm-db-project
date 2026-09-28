#!/usr/bin/env bash
set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TROC_COMMIT="a6d50e3f596b356137d2f8c3c8b31a61bf7fe2c5"
TROC_DIR="$ROOT/.deps/Troc"
MYSQL_CONTAINER="db-paper-mysql8032"

need() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Missing required command: $1" >&2
    exit 1
  }
}

need docker
need git

if ! docker info >/dev/null 2>&1; then
  if command -v colima >/dev/null 2>&1; then
    echo "Docker daemon is not running; starting Colima..."
    colima start
  else
    echo "Docker daemon is not running. Start Docker and retry." >&2
    exit 1
  fi
fi

if docker inspect "$MYSQL_CONTAINER" >/dev/null 2>&1; then
  docker start "$MYSQL_CONTAINER" >/dev/null 2>&1 || true
else
  docker compose -f "$ROOT/compose.yaml" up -d mysql
fi

echo "Waiting for MySQL 8.0.32..."
for _ in $(seq 1 60); do
  if docker exec "$MYSQL_CONTAINER" mysqladmin ping -h127.0.0.1 -uroot -proot --silent >/dev/null 2>&1; then
    break
  fi
  sleep 2
done

VERSION="$(docker exec "$MYSQL_CONTAINER" mysql -h127.0.0.1 -uroot -proot -Nse 'SELECT VERSION();' 2>/dev/null)"
case "$VERSION" in
  8.0.32*) ;;
  *)
    echo "Expected MySQL 8.0.32, got: $VERSION" >&2
    exit 1
    ;;
esac
echo "MySQL ready: $VERSION"

mkdir -p "$ROOT/.deps"
if [ ! -d "$TROC_DIR/.git" ]; then
  mkdir -p "$TROC_DIR"
  git -C "$TROC_DIR" init -q
  git -C "$TROC_DIR" remote add origin https://github.com/criszy/Troc.git
fi

CURRENT="$(git -C "$TROC_DIR" rev-parse HEAD 2>/dev/null || true)"
if [ "$CURRENT" != "$TROC_COMMIT" ]; then
  echo "Fetching pinned Troc commit $TROC_COMMIT..."
  git -C "$TROC_DIR" fetch -q --depth 1 origin "$TROC_COMMIT"
  git -C "$TROC_DIR" checkout -q --detach FETCH_HEAD
fi

if [ ! -f "$TROC_DIR/target/troc-1.0-SNAPSHOT.jar" ] || [ "${FORCE_BUILD:-0}" = "1" ]; then
  echo "Building pinned Troc artifact..."
  docker run --rm     -v "$TROC_DIR:/work"     -w /work     maven:3.9.11-eclipse-temurin-17     mvn -q package -Dmaven.test.skip=true
fi

echo "Setup complete."
