#!/bin/bash

# 检查当前目录是否为 Git 仓库
if [ ! -d ".git" ]; then
    echo "❌ 当前目录不是一个 Git 仓库。"
    exit 1
fi

# 拉取主仓库的最新更改
echo "🔄 正在拉取主仓库的最新更改..."
git pull

# 遍历所有子模块并切换到 main 分支
echo "🔄 正在更新子模块到 main 分支..."
git submodule foreach '
  echo "🔄 Updating submodule $name to track main branch"
  git checkout main
  git pull origin main
'

# 强制将所有子模块的引用更新到当前的最新 main 分支
echo "🔄 强制更新子模块引用到最新 main 分支..."
git submodule update --remote --merge

echo "✅ 项目及其子模块已成功更新。"
