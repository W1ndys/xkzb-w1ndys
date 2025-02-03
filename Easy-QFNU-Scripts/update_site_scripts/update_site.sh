#!/bin/bash

# 定义变量
WORK_DIR="/tmp/easy-temp"
TARGET_DIR="/opt/1panel/apps/openresty/openresty/www/sites/easy-qfnu.top/index"
SSH_REPO_URL="git@github.com:W1ndys/Easy-QFNU.git"
PROXY_URL="https://ghfast.top/https://github.com/W1ndys/Easy-QFNU.git"

# 清理旧的临时目录
rm -rf "$WORK_DIR"
mkdir -p "$WORK_DIR"

# 尝试克隆仓库，优先 SSH，其次代理
echo "正在使用 SSH 克隆..."
if ! git clone --depth 1 --branch gh-pages "$SSH_REPO_URL" "$WORK_DIR" --quiet; then
    echo "SSH 克隆失败，尝试使用代理..."
    if ! git clone --depth 1 --branch gh-pages "$PROXY_URL" "$WORK_DIR" --quiet; then
        echo "所有克隆方式均失败，无法连接到仓库"
        python3 notify.py "克隆失败，无法连接到仓库" false
        exit 1
    fi
    echo "使用代理克隆成功"
else
    echo "使用 SSH 克隆成功"
fi

# 检查克隆是否成功
if [ ! -d "$WORK_DIR" ] || [ -z "$(ls -A $WORK_DIR)" ]; then
    echo "克隆成功但目录为空"
    python3 notify.py "克隆成功但目录为空" false
    exit 1
fi

# 确保目标目录存在
mkdir -p "$TARGET_DIR"

# 复制文件到目标目录
echo "正在更新网站文件..."
cp -r "$WORK_DIR"/* "$TARGET_DIR"/

# 设置权限
echo "正在设置权限..."
chown -R 1000:1000 "$TARGET_DIR"
find "$TARGET_DIR" -type f -exec chmod 644 {} \;
find "$TARGET_DIR" -type d -exec chmod 755 {} \;

# 清理临时文件
rm -rf "$WORK_DIR"

# 发送成功通知
python3 notify.py "更新成功" true

echo "更新完成！" 