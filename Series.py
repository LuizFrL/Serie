import os, time
from glob import glob
from moviepy.editor import VideoFileClip


def run_movie(file):
    if os.path.basename(file).find('@') == -1:
        clip = VideoFileClip(file)
        duration = int(clip.duration) - 20
        os.startfile(file)
        time.sleep(duration)
        os.system('taskkill /im ApplicationFrameHost.exe')
        time.sleep(1)
        rename_file(serie)
    else:
        print('Episódio já visto.')


def rename_file(file):
    name = os.path.basename(file)
    os.rename(file, file.replace(name, '@' + name))


if __name__ == '__main__':
    series = glob(r'E:\Filmes e Series\Series\Supernatural\SuperNatural 2\*.mp4')
    for serie in series:
        print('Rodando filme:', serie, '\n')
        run_movie(serie)
