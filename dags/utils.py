import os

def read_config(config_file_path):
    config = {}
    with open(config_file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if '=' in line:
                key, value = line.strip().split('=')
                config[key] = value
    return config