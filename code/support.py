from csv import reader
from os import walk
import pygame

def import_csv_layout(path):  # give path, return list of lists
    map = []
    with open(path, 'r') as f:
        csv_file = reader(f)
        for row in csv_file: map.append(row)
    return map
