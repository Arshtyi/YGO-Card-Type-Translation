#!/usr/bin/env python3
import json
import os

# 打印当前工作目录，用于调试
print(f"Current working directory: {os.getcwd()}")
print(f"Checking if cards.json exists: {os.path.exists('cards.json')}")

# 读取cards.json文件
try:
    with open('cards.json', 'r', encoding='utf-8') as file:
        print("Reading cards.json...")
        cards_data = json.load(file)
        print(f"Successfully loaded cards.json. Total cards: {len(cards_data.get('data', []))}")
except Exception as e:
    print(f"Error loading cards.json: {e}")
    exit(1)

# 用于存储所有typeline字符串的集合（自动去重）
typeline_strings = set()
cards_with_typeline = 0

# 遍历所有卡牌
for card in cards_data.get('data', []):
    # 检查卡牌是否有typeline字段
    if 'typeline' in card:
        cards_with_typeline += 1
        # typeline是一个字符串列表，将每个字符串添加到集合中
        for type_str in card['typeline']:
            typeline_strings.add(type_str)

print(f"Found {cards_with_typeline} cards with typeline field")
print(f"Collected {len(typeline_strings)} unique typeline strings")

if len(typeline_strings) == 0:
    print("Warning: No typeline strings found in any card!")

# 将所有收集到的typeline字符串按行写入translation.conf文件
try:
    with open('translation.conf', 'w', encoding='utf-8') as output_file:
        # 将集合转换为排序列表，以确保输出的顺序一致
        sorted_typelines = sorted(list(typeline_strings))
        for type_str in sorted_typelines:
            output_file.write(f"{type_str}\n")
    
    print(f"Successfully extracted {len(typeline_strings)} unique typeline strings to translation.conf")
    print(f"Output file location: {os.path.abspath('translation.conf')}")
except Exception as e:
    print(f"Error writing to translation.conf: {e}")
