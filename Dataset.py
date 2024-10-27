with zipfile.ZipFile(f'{dataset_path}/G1020.zip', 'r') as zip_ref:
    zip_ref.extractall('/content/G1020')
