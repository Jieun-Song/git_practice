# 191

# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]

# for i in data:
#     for j in i:
#         print(j*1.00014)

# 192

# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]

# for i in data:
#     for j in i:
#         print(j*1.00014)
#     print("----")

# 193

# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []

# for i in data:
#     for j in i:
#         result.append(j*1.00014)

# print(result)

# 194

# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []

# for i in data:
#     list = []
#     for j in i:

#         list.append(j*1.00014)
#     result.append(list)
# print(result)

# 195

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]

# for i in ohlc:
#     print(i[3])

# 196

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]

# for i in ohlc[1:]:
#     if i[3] > 150:
#         print(i[3])

# 197

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]

# for i in ohlc[1::]:
#     if i[0] <= i[3]:
#         print(i[3])

# 198

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# volarility = []

# for i in ohlc[1::]:
#     volarility.append(i[1]-i[2])

# print(volarility)

# 199

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]

# for i in ohlc[1::]:
#     if i[3] > i[0]:
#         print(i[1]-i[2])

# 200

# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# a = 0

# for i in ohlc[1::]:
#     a += (i[3]-i[0])

# print(a)
