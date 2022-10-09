import PySimpleGUI as sg
from pytube import YouTube
from win10toast import ToastNotifier
import os


def runner(caminho, links):

    video = YouTube(links)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path=f"{caminho}")
    notificacao()
    janela['mensagem'].update('Donwload feito com sucesso')
    print("\nDownload Concluído com Sucesso!\n")

def notificacao():
    toaster = ToastNotifier()

    toaster.show_toast(
        "DownTube",
        "Download finalizado com sucesso!",
        threaded=True,
        icon_path=None,
        duration=5
    )
    return notificacao

if __name__ == '__main__':

    abrirPasta = os.getcwd()

# layout
    sg.theme('Reddit')

# janela
    layout = [
        [sg.Text('Caminho:'), sg.InputText(key='caminho', size=(30, 1)),
         sg.FolderBrowse(initial_folder=abrirPasta)],
        [sg.Text('Link: '), sg.Input(key='link', size=(33, 1))],
        [sg.Text('', key='mensagem')],
        [sg.Button('INICIAR')],
        [sg.Text(
            '© Copyright, todo direitos reservados ao Caio N Gabriel', key='copywriting')],
    ]

    janela = sg.Window('DonwTube', layout)
# ler eventos
    while True:
        eventos, valores = janela.read()

        if eventos == sg.WINDOW_CLOSED:
            break
        if True:
            try:
                caminho = valores['caminho']
                links = valores['link']
                runner(caminho, links)
            except:
                janela['mensagem'].update(
                    'Falha, verifique se o link e o caminho estão corretos! ')