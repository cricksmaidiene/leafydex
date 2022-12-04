"""
# Compress Images 🗜

This utlility notebook takes all high-res plant leaves photos from the source directory, 
compresses them and then writes them to a new directory. 
Both source and destination directory have the exact same paths and filenames. 
Any compression setting can be used to write a new directory of compressed images. 
"""

from pyprojroot import here
import os
import pathlib
import shutil

from PIL import Image

from concurrent.futures import ThreadPoolExecutor

from tqdm.autonotebook import tqdm

tqdm.pandas()

"""
Set configurations
"""

HD_IMG_DIR: str = "Plants_2"
CMP_IMG_DIR: str = "Plants_2_compressed"
COMPRESS_SIZE: tuple[int, int] = (200, 200)

# store the filepath address of the current file
__file__: str = os.path.abspath("")

ROOT_DIR_PATH: str = here()
HD_IMG_DIR_PATH: str = os.path.join(ROOT_DIR_PATH, "data", "raw", HD_IMG_DIR)
CMP_IMG_DIR_PATH: str = os.path.join(ROOT_DIR_PATH, "data", "raw", CMP_IMG_DIR)

"""
Create clone directory
"""
# delete compressed root directory if exists
if os.path.exists(CMP_IMG_DIR_PATH) and os.path.isdir(CMP_IMG_DIR_PATH):
    shutil.rmtree(CMP_IMG_DIR_PATH)

os.makedirs(CMP_IMG_DIR_PATH)

"""
Create a hashmap of source directory files to destination directory files. 
Create all required destination directories
"""
image_compress_map: dict[str, str] = {}

# do a depth-first-search based walk through the directory tree
for path, directories, files in os.walk(HD_IMG_DIR_PATH):

    # if leaf nodes are detected
    if files:

        # iterate through each file
        for img_file in files:

            # get hd and compressed file paths
            hd_file_abs_path: str = os.path.join(path, img_file)
            cmp_file_abs_path: str = hd_file_abs_path.replace(HD_IMG_DIR, CMP_IMG_DIR)

            # create directory path
            cmp_folder_abs_path: str = os.path.dirname(cmp_file_abs_path)
            # create compressed subdirectory (idempotent)
            os.makedirs(cmp_folder_abs_path, exist_ok=True)

            # add hd to compressed file mapping
            image_compress_map[hd_file_abs_path] = cmp_file_abs_path

"""
Concurrently write multiple images after compressing to destination
"""
# create a tuple version of image compress mapping dictionary for function argument passing
image_compress_map_tuples: list[tuple[str, str]] = [
    (k, v) for k, v in image_compress_map.items()
]

# create a progress bar to track progress across threads
progress_bar = tqdm(total=len(image_compress_map.keys()), position=0, leave=True)

# thread-safe function
def compress_image(source_path: str, destination_path: str):
    hd_img: Image.Image = Image.open(source_path)
    cmp_img: Image.Image = hd_img.resize(COMPRESS_SIZE)
    cmp_img.save(destination_path, "JPEG", quality=100)
    progress_bar.update(1)


# concurrently compress multiple images and save them
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(
        lambda path_tuple: compress_image(*path_tuple), image_compress_map_tuples
    )
