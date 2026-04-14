import pandas as pd
import os
import shutil

SELECTED_SIGNS = [
    "bird", "fish", "duck", "frog", "alligator", "cat", "dog", "cow",
    "pig", "tiger", "lion", "horse", "wolf", "bee", "owl", "goose",
    "jump", "dance", "blow", "drink", "drop", "find", "give", "make",
    "cry", "read", "cut", "hide", "fall", "ride",
    "yes", "no", "finish", "open", "close", "up", "down", "fast",
    "quiet", "wait", "now", "later", "every", "same", "any",
    "pizza", "boat", "airplane", "rain", "snow"
]

TRAIN_CSV    = r".\asl-signs\train.csv" #path to original train.csv file
LANDMARK_DIR = r".\asl-signs\train_landmark_files" # path to original directory with parquet files (landmark data)
OUTPUT_DIR   = r".\asl-signs-50" # path to output directory where filtered train.csv and corresponding parquet files will be saved

train    = pd.read_csv(TRAIN_CSV) # Load original train.csv
filtered = train[train['sign'].isin(SELECTED_SIGNS)] # Filter to only selected signs

# Save filtered csv
os.makedirs(OUTPUT_DIR, exist_ok=True) # Ensure output directory exists
filtered.to_csv(os.path.join(OUTPUT_DIR, 'train.csv'), index=False) # Save filtered train.csv without index
print(f"Saved filtered train.csv with {len(filtered)} rows") # Print number of rows in filtered train.csv

# Copy only the parquet files we need
copied, missing = 0, 0
for _, row in filtered.iterrows():  # Iterate over filtered rows to copy corresponding parquet files
    src = os.path.join(r".\asl-signs", row['path']) # Construct source path for parquet file based on original directory and path in train.csv
    dst = os.path.join(OUTPUT_DIR, row['path']) # Construct destination path for parquet file in output directory
    os.makedirs(os.path.dirname(dst), exist_ok=True) # Ensure destination directory exists
    if os.path.exists(src):
        shutil.copy2(src, dst)
        copied += 1
    else: # If source parquet file is missing, count it
        missing += 1
    if copied % 500 == 0:
        print(f"  Copied {copied} files...")

print(f"\nDone! Copied {copied} files, {missing} missing")
print(f"Output saved to: {OUTPUT_DIR}")