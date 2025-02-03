import pandas as pd
from pypinyin import pinyin, Style
from datetime import datetime


def pinyin_sort(items):
    """按照汉语拼音排序"""
    return sorted(
        items, key=lambda x: "".join([i[0] for i in pinyin(str(x), style=Style.NORMAL)])
    )


def campus_sort(campuses):
    """自定义校区排序，确保曲阜在日照前面"""
    campus_priority = {"曲阜": 1, "日照": 2}
    return sorted(campuses, key=lambda x: campus_priority.get(x, 999))


def normalize_teacher_name(name):
    """标准化教师名称，处理可能的同音字或错别字"""
    name_mapping = {
        "名字1": "名字2",  # 把名字1换成名字2
        "名字3": "名字4",  # 把名字3换成名字4
        # 可以添加更多的映射关系
    }
    return name_mapping.get(name, name)


def generate_markdown(data_file):
    # 读取Excel文件，不使用第一行作为表头
    df = pd.read_excel(data_file, header=None)

    # 为列指定名称
    df.columns = ["课程名称", "任课老师", "校区", "年份", "老师描述", "提交者昵称"]

    # 标准化教师名称
    df["任课老师"] = df["任课老师"].apply(normalize_teacher_name)

    # 按照拼音对课程名称进行排序
    df = df.sort_values(
        by=["课程名称"],
        key=lambda x: [
            "".join([i[0] for i in pinyin(str(item), style=Style.NORMAL)]) for item in x
        ],
    )

    # 创建更新日志
    update_log = f"## {datetime.now().strftime('%Y-%m-%d')} 更新日志\n\n"

    # 收集所有提交者
    all_submitters = df["提交者昵称"].tolist()

    # 生成markdown文本
    markdown = ""

    # 遍历每一行数据
    for _, row in df.iterrows():
        # 添加到更新日志
        update_log += f"[{row['课程名称']}]-[{row['校区']}]-[{row['任课老师']}]-[{row['提交者昵称']}]-[{row['年份']}年]\n"

        # 生成主要内容
        markdown += f"## {row['课程名称']}\n\n"
        markdown += f"### {row['校区']}\n\n"
        markdown += f"#### {row['任课老师']}\n\n"
        markdown += f"{row['老师描述']}\n\n"
        markdown += f"> {row['提交者昵称']}({row['年份']}年)\n\n"

    update_log += "\n---\n"

    return markdown, update_log, all_submitters


# 使用示例
markdown_output, update_log, submitters = generate_markdown("data.xlsx")

# 将主要输出写入文件
with open("output.md", "w", encoding="utf-8") as f:
    f.write(markdown_output)

# 将更新日志写入文件
with open("update_log.md", "w", encoding="utf-8") as f:
    f.write(update_log)

# 将提交者列表写入文件
with open("submitters.txt", "w", encoding="utf-8") as f:
    f.write("，".join(submitters))
