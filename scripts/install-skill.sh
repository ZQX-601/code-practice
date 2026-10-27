#!/usr/bin/env bash

set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skill_source="${project_root}/skills/coding-interview-coach"
codex_root="${CODEX_HOME:-${HOME}/.codex}"
skills_root="${codex_root}/skills"
skill_target="${skills_root}/coding-interview-coach"

if [[ ! -f "${skill_source}/SKILL.md" ]]; then
  echo "未找到 Skill 源码：${skill_source}" >&2
  exit 1
fi

mkdir -p "${skills_root}"

if [[ -e "${skill_target}" ]]; then
  timestamp="$(date +%Y%m%d-%H%M%S)"
  backup_target="${skills_root}/coding-interview-coach.backup-${timestamp}"
  mv "${skill_target}" "${backup_target}"
  echo "已备份原 Skill：${backup_target}"
fi

cp -R "${skill_source}" "${skill_target}"
echo "已安装 Skill：${skill_target}"
echo "请使用 Codex 打开项目目录：${project_root}"
