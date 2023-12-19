import argparse
import random

def merge_and_shuffle(file1_path, file2_path, output_file_path, random_seed=None):
    # Step 1: Read content from both files
    with open(file1_path, 'r', encoding='utf-8') as file1:
        content1 = file1.readlines()

    with open(file2_path, 'r', encoding='utf-8') as file2:
        content2 = file2.readlines()

    # Step 2: Merge the content
    merged_content = content1 + content2

    # Step 3: Shuffle the content with a specific random seed
    random.seed(random_seed)
    random.shuffle(merged_content)

    # Step 4: Write the shuffled content to a new file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(merged_content)

def main():
    parser = argparse.ArgumentParser(description='Merge and shuffle two files.')
    parser.add_argument('file1_path', type=str, help='Path to the first file')
    parser.add_argument('file2_path', type=str, help='Path to the second file')
    parser.add_argument('output_file_path', type=str, help='Path to the output file')
    parser.add_argument('--random_seed', type=int, default=None, help='Random seed for reproducibility')

    args = parser.parse_args()

    merge_and_shuffle(args.file1_path, args.file2_path, args.output_file_path, args.random_seed)

if __name__ == "__main__":
    main()
