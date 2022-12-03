import sys, os.path

DATA_FOLDER_PATH = '../data'
DATA_FOLDER_PATH_EXAMPLE = '../data_example'

def get_raw_data():
    
    if not os.path.exists(DATA_FOLDER_PATH) :
        raise FileNotFoundError(f'data folder does not exist [{DATA_FOLDER_PATH}]')

    day = sys.argv[0].replace('.py', '')

    data_path = f'{DATA_FOLDER_PATH}/data_{day}.txt'
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f'data file does not exist [{data_path}]')
    
    with open(data_path) as file:
        content = []
        for line in file.readlines():
            content.append(line.strip())

    return content

def get_raw_data_example():
    
    if not os.path.exists(DATA_FOLDER_PATH_EXAMPLE) :
        raise FileNotFoundError(f'data folder does not exist [{DATA_FOLDER_PATH_EXAMPLE}]')

    day = sys.argv[0].replace('.py', '')

    data_path = f'{DATA_FOLDER_PATH_EXAMPLE}/data_{day}.txt'
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f'data file does not exist [{data_path}]')
    
    with open(data_path) as file:
        content = []
        for line in file.readlines():
            content.append(line.strip())

    return content
