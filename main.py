import os
import uuid

from PIL import Image

INPUT_DIR = 'files/input'
OUTPUT_DIR = 'files/output'


def rename_files(path):
    num = 0

    for filename in os.listdir(path):
        _, ext = filename.split('.')
        new_filename = f'{str(num).zfill(4)}.{ext}'
        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
        num += 1

    return os.listdir(path)


def main(output_fname=f'converted-{uuid.uuid4()}', rename=False):
    fnames = (
        rename_files(INPUT_DIR) 
        if rename.lower() in ('y', 'yes') 
        else os.listdir(INPUT_DIR)
    )

    opened = (Image.open(f'{INPUT_DIR}/{fname}') for fname in fnames)
    converted = [file.convert('RGB') for file in opened]

    converted[0].save(
        fr'{OUTPUT_DIR}/{output_fname}.pdf', 
        save_all=True,
        append_images=converted[1:]
    )


if __name__ == '__main__':
    fname = input('Converted PDF file name, or leave blank: ')
    rename = input('Do you wish to rename images? (y/n): ')

    main(output_fname=fname, rename=rename)
