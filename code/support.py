from csv import reader
from os import walk
import pygame

def import_csv_layout(path):  # give path, return list of lists
    map = []
    with open(path, 'r') as f:
        csv_file = reader(f)
        for row in csv_file: map.append(row)
    return map

def import_folder(path):
    animation_set = []
    for dir in walk(path):
        for picture in dir[2]:
            full_path = dir[0] + picture
            animation_set.append(pygame.image.load(full_path).convert_alpha())

    return animation_set

# import_folder('../graphics/player/down/')
