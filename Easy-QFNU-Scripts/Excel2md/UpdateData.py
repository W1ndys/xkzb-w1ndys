import pandas as pd
import os
import re


def parse_markdown_file(content):
    """解析markdown文件内容，返回课程、校区、老师的层级结构"""
    structure = {}
    current_course = None
    current_district = None
    current_teacher = None

    lines = content.split("\n")
    for line in lines:
        if line.startswith("## "):
            current_course = line[3:].strip()
            structure[current_course] = {}
            current_district = None
            current_teacher = None
        elif line.startswith("### "):
            current_district = line[4:].strip()
            if current_course:
                structure[current_course][current_district] = {}
            current_teacher = None
        elif line.startswith("#### "):
            current_teacher = line[5:].strip()
            if current_course and current_district:
                structure[current_course][current_district][current_teacher] = []

    return structure


def find_insertion_point(content, course, district, teacher):
    """找到在文件中插入新内容的位置"""
    lines = content.split("\n")
    course_pattern = f"## {course}"
    district_pattern = f"### {district}"
    teacher_pattern = f"#### {teacher}"

    # 找到课程、校区、老师的位置
    course_found = False
    district_found = False
    teacher_found = False

    for i, line in enumerate(lines):
        if line.startswith(course_pattern):
            course_found = True
        elif course_found and line.startswith(district_pattern):
            district_found = True
        elif district_found and line.startswith(teacher_pattern):
            teacher_found = True
            # 找到教师后，继续往下找到最后一条评论
            for j in range(i + 1, len(lines)):
                if (
                    lines[j].startswith("##")
                    or lines[j].startswith("###")
                    or lines[j].startswith("####")
                ):
                    return j
                if j == len(lines) - 1:
                    return j + 1

    return -1


def process_data(excel_file, markdown_dir):
    # 读取Excel文件
    df = pd.read_excel(excel_file, header=None)
    df.columns = ["course", "teacher", "district", "year", "description", "submitter"]

    rows_to_delete = []
    unmatched_rows = set()

    # 新增：用于记录更新日志和提交者
    update_log = []
    submitters = set()

    # 遍历markdown文件
    for filename in os.listdir(markdown_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(markdown_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 解析文件结构
            structure = parse_markdown_file(content)
            content_modified = False

            # 处理每一行Excel数据
            for index, row in df.iterrows():
                if index in rows_to_delete:  # 跳过已经处理过的行
                    continue

                course = row["course"]
                district = row["district"]
                teacher = row["teacher"]

                # 检查是否存在对应的结构
                if (
                    course in structure
                    and district in structure[course]
                    and teacher in structure[course][district]
                ):

                    # 找到插入点
                    insert_point = find_insertion_point(
                        content, course, district, teacher
                    )
                    if insert_point != -1:
                        # 构建新内容
                        new_content = f"\n{row['description']}\n\n> {row['submitter']}({row['year']}年)\n"

                        # 插入新内容
                        content_lines = content.split("\n")
                        content_lines.insert(insert_point, new_content)
                        content = "\n".join(content_lines)

                        # 标记要删除的行
                        rows_to_delete.append(index)
                        unmatched_rows.discard(index)
                        content_modified = True

                        # 新增：记录更新日志和提交者
                        update_log.append(
                            f"【{course}】-【{district}】-【{teacher}】-【{row['year']}】"
                        )
                        submitters.add(row["submitter"])

                        print(
                            f"✅ 成功添加: 【{course}】-【{district}】-【{teacher}】-【{row['submitter']}】"
                        )
                else:
                    # 只有当这行数据还没有被成功处理时，才标记为未匹配
                    if index not in rows_to_delete:
                        unmatched_rows.add(index)

            # 只有在文件被修改时才写回
            if content_modified:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

    # 打印未匹配的数据
    if unmatched_rows:
        print("\n❌ 以下数据未找到匹配位置：")
        for index in sorted(unmatched_rows):
            row = df.iloc[index]
            print(
                f"- {row['course']} - {row['district']} - {row['teacher']} - {row['submitter']}"
            )

    # 删除已处理的行
    if rows_to_delete:
        df = df.drop(rows_to_delete)
        df.to_excel(excel_file, index=False, header=False)
        print(f"\n📊 统计信息：")
        print(f"- 成功处理：{len(rows_to_delete)} 条数据")
        print(f"- 未能匹配：{len(unmatched_rows)} 条数据")
        print(f"- 总数据量：{len(df) + len(rows_to_delete)} 条数据")

    # 新增：生成更新日志文件
    if update_log:
        with open("update_log.txt", "a", encoding="utf-8") as f:
            f.write("\n".join(update_log) + "\n")

        with open("submitters.txt", "a", encoding="utf-8") as f:
            f.write(", ".join(sorted(submitters)) + "\n")

        print("\n📝 更新日志已生成")
        print(f"- 更新条目：{len(update_log)} 条")
        print(f"- 提交人数：{len(submitters)} 人")


# 使用示例
process_data("data.xlsx", "example")
