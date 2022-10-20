# https://blog.csdn.net/QD_Jason/article/details/124097342

# 在ISO国际标准中定义了A0纸张的大小为1189mm×841mm，将A0纸沿长边对折后为A1纸，大小为841mm×594mm，在对着的过程中长度直接取下整(实际裁剪时可能有损耗)。将A1纸沿长边对折后为A2纸，以此类推。
# 输入纸张的名称，请输出纸张的大小。
# 【输入格式】输入一行包含一个字符串表示纸张的名称，该名称一定是A0、A1、A2、A3、A4、A5、A6、A7、A8、A9之一
# 【输出格式】输出两行，每行包含一个整数，依次表示长边和短边的长度。

a0_w = 1189
a0_h = 841
old_w = a0_w
old_h = a0_h
n = int(input())
a_list = [[old_w, old_h]]
while True:
    new_w = old_h
    new_h = old_w // 2
    if new_h == 0:
        break
    a_list.append([new_w, new_h])
    old_w = new_w
    old_h = new_h
    # print(new_w, new_h)

print(a_list[n][0])
print(a_list[n][1])
# print(len(a_list))
