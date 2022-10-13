import os
from zipfile import ZipFile

def zip_all(search_dir, extensions, output_path):
    with ZipFile(output_path, 'w') as output_zip:
        for root, dirs, files in os.walk(search_dir):
            relative_path = os.path.relpath(root, search_dir)
            for file in files:
                name, ext = os.path.splitext(file)
                if ext.lower() in extensions:
                    output_zip.write(os.path.join(root,file),
                    arcname=os.path.join(rel_path,file))
