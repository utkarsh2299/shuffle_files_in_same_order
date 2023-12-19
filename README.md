# merge_and_shuffle_files

This Python script merges the content of two files and shuffles the lines while maintaining order within each file.

## Overview

The script takes the content of two input files, merges them, and shuffles the lines while preserving the order within each file. This can be useful for creating a shuffled dataset while ensuring that the order of samples within each original dataset is maintained.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/merge_and_shuffle_files.git

2. **Run the Script:**

```bash
python merge_and_shuffle.py file1_path file2_path output_file_path [random_seed]

-file1_path: Path to the first input file.
-file2_path: Path to the second input file.
-output_file_path: Path to the output file where the merged and shuffled content will be saved.
-random_seed (optional): Specify a random seed for reproducibility. If not provided, the shuffle will be random.
