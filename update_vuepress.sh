#!/bin/bash

pnpm dlx vp-update
echo "更新完成，暂停五秒，请手动重启服务"
sleep 5
read -p "按任意键继续..."
