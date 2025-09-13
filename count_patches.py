import json
import argparse

def count_non_empty_patches(jsonl_file_path):
    count = 0
    with open(jsonl_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():  # 跳过空行
                data = json.loads(line)
                if data.get("model_patch", "").strip() != "":
                    count += 1
    return count

if __name__ == "__main__":
    total_count = count_non_empty_patches("output_0_processed.jsonl")
    print(f"Number of entries with non-empty model_patch: {total_count}")
