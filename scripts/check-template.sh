#!/bin/sh
# Generate a project from this template and run its full verification, the way a user would.
# Answers can be overridden through the environment: PROJECT_NAME, PYTHON_VERSION.
set -eu

template_root="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
project_name="${PROJECT_NAME:-Demo Notes}"
python_version="${PYTHON_VERSION:-3.12}"
slug="$(printf '%s' "$project_name" | tr '[:upper:] ' '[:lower:]-')"
output_root="$template_root/.generated"
output="$output_root/$slug"

rm -rf "$output"
mkdir -p "$output_root"
docker build --quiet --tag copier-runner "$template_root/scripts/copier" >/dev/null
# Run as the calling user, so the generated files belong to it on a Linux host too.
docker run --rm \
  --user "$(id -u):$(id -g)" \
  --env HOME=/tmp \
  --env GIT_CONFIG_COUNT=1 --env GIT_CONFIG_KEY_0=safe.directory --env GIT_CONFIG_VALUE_0='*' \
  --volume "$template_root:/template:ro" \
  --volume "$output_root:/output" \
  copier-runner \
  copier copy --defaults --vcs-ref HEAD \
    --data project_name="$project_name" \
    --data python_version="$python_version" \
    --data description="Template self-check" \
    /template "/output/$slug"

cd "$output"
git init --quiet --initial-branch main
git add --all
docker compose build --quiet
make verify
