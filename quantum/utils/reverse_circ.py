def reverse_lines(input_file_path, output_file_path):
    try:
        # 读取输入文件的所有行
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        # 如果文件为空，则无需继续处理
        if not lines:
            print("输入文件是空的！")
            return

        # 去除每行末尾的换行符并反转列表
        lines = [line.rstrip('\n') for line in lines][::-1]

        # 将反转后的行写入输出文件
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            for line in lines:
                outfile.write(line + '\n')

        print(f"已成功将结果写入{output_file_path}")

    except FileNotFoundError:
        print(f"找不到文件: {input_file_path}")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == '__main__':
    # 调用函数，指定输入和输出文件路径
    reverse_lines('input.txt', 'output.txt')