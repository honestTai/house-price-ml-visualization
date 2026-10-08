# -*- coding: utf-8 -*-
import re
import csv

def clean_and_write_data(input_filename, output_filename):
    with open(input_filename, encoding="gbk") as f:
        reader = csv.reader(f)
        context = [line for line in reader]

    with open(output_filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for line in context:
            line = [x.strip() for x in line]
            if line[0] == "id":
                writer.writerow(line)
                continue

            if "别墅" in line:
                line_copy = line[:]
                line[8] = "null"
                line[9] = line_copy[8]
                line[10] = "null"
                line[11] = line_copy[9]
                line[12] = line_copy[10]
                line[13] = line_copy[11]
                line[14] = "null"
                line[15] = "null"
                line[16] = line_copy[13]
            if "商业办公类" in line:
                result = re.match(r"\d{4}-\d{1,2}-\d{1,2}", line[17])
                if result is None:
                    del line[17]
                result = re.match(r"\d{4}-\d{1,2}-\d{1,2}", line[17])
                if result is None:
                    del line[17]
                result = re.match(r"\d{4}-\d{1,2}-\d{1,2}", line[17])
                if result is None:
                    del line[17]
            if "车库" in line:
                line_copy = line[:]
                line[5] = "null"
                line[6] = line_copy[5]
                line[7] = "null"
                line[11] = line_copy[7]

            try:
                float_num = float(line[3])
                line[3] = str(int(float_num))
                line[4] = line[4].split("元")[0]

                if line[7] != "null" and line[7] != "暂无数据":
                    line[7] = line[7].split("㎡")[0]

                if line[9] != "null" and line[9] != "暂无数据":
                    line[9] = line[9].split("㎡")[0]

                writer.writerow(line)
            except Exception as e:
                print("数据项转换失败！该记录未写入")

if __name__ == "__main__":
    input_filename = "data_file\\ershoufang.csv"
    output_filename = "data_cluster/ershoufang-clean-utf8-v1.1.csv"
    clean_and_write_data(input_filename, output_filename)
    print("数据清洗和写入完成。")
