#!/usr/bin/env python3
import sys
import requests
import json
from datetime import datetime


class NotificationSender:
    def __init__(self):
        self.webhooks = [
            "https://oapi.dingtalk.com/robot/send?access_token=24382be6f3b3cf4474947f5e9450a24116178d57536526ef80450ba62f0afc51",
            "https://oapi.dingtalk.com/robot/send?access_token=6c88b9cc9dd208047f4a604f704ffaa53c564beb00f7082d81ab8f4a638b3942",
        ]

    def send_dingtalk_message(self, message, is_success):
        """发送钉钉通知"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if is_success:
            content = {
                "msgtype": "markdown",
                "markdown": {
                    "title": "网站更新成功通知",
                    "text": (
                        f"### ✅ 网站更新成功\n\n"
                        f"- **时间**：{current_time}\n"
                        f"- **站点**：[easy-qfnu.top](https://easy-qfnu.top)\n"
                        f"- **状态**：部署完成\n\n"
                        "网站已完成更新！"
                    ),
                },
            }
        else:
            content = {
                "msgtype": "markdown",
                "markdown": {
                    "title": "网站更新失败通知",
                    "text": (
                        f"### ❌ 网站更新失败\n\n"
                        f"- **时间**：{current_time}\n"
                        f"- **错误信息**：{message}\n"
                        f"- **站点**：easy-qfnu.top\n\n"
                        "请及时检查并处理！"
                    ),
                },
            }

        headers = {"Content-Type": "application/json"}
        for webhook in self.webhooks:
            try:
                response = requests.post(
                    webhook, data=json.dumps(content), headers=headers
                )
                if response.status_code == 200:
                    response_data = response.json()
                    if response_data.get("errcode") == 0:
                        print(f"通知发送成功 - Webhook: {webhook}")
                    else:
                        print(
                            f"通知发送失败 - Webhook: {webhook}, 错误: {response_data.get('errmsg')}"
                        )
                else:
                    print(
                        f"HTTP错误 - Webhook: {webhook}, 状态码: {response.status_code}"
                    )
            except Exception as e:
                print(f"发送通知时发生错误 - Webhook: {webhook}, 错误: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 notify.py <message> <is_success>")
        sys.exit(1)

    message = sys.argv[1]
    is_success = sys.argv[2].lower() == "true"

    sender = NotificationSender()
    sender.send_dingtalk_message(message, is_success)
