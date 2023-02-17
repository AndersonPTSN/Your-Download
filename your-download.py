from pytube import YouTube, Playlist
import PySimpleGUI as sg
import threading
import os

def validador_pasta(diretorio):
	lista = list(diretorio)
	caracteres = ['\\','/','|','<','>','*',':','“','?']
	for i in caracteres:
		if(i in lista):
			return -1
	return 0

def download_video(video_url):
	if(validador_pasta(values["pasta"]) == -1):
		sg.popup("Caracteres invalidos pra criação de pasta \n\n \\, /, |, <, >, *, :, “, ?",title="ERRO")
	else:
		sg.popup("Aguarde ate o termino do download \n\nIrá abrir um popup ao terminar",title="AVISO")
		try:
			yt = YouTube(video_url)
		except Exception as e:
			sg.popup("Link: "+values["input"]+"\n\nindisponivel para download ",title="ERRO")
		else:
			video = yt.streams.get_highest_resolution()
			out_file = video.download(output_path=values["pasta"])

			base, ext = os.path.splitext(out_file)
			new_file = base + '.mp3'
			try:
				os.rename(out_file, new_file) # <--- Não é possível criar um arquivo já existente
			except Exception as e:
				sg.popup("Vídeo: \n"+yt.title+"\n\nnão pode ser baixado pois existe um arquivo de mesmo nome",title="ERRO")

			sg.popup("Download finalizado com sucesso!",title="AVISO")

def download_playlist(playlist_url):
	if(validador_pasta(values["pasta"]) == -1):
		sg.popup("Caracteres invalidos pra criação de pasta \n\n \\, /, |, <, >, *, :, “, ?",title="ERRO")
	else:
		playlist = Playlist(playlist_url)
		try:
			a = len(playlist) #IS A PLAYLIST?
		except Exception as e:
			download_video(playlist_url)
		else:
			sg.popup("Aguarde ate o termino do download \n\nIrá abrir um popup ao terminar",title="AVISO")
			for url in playlist:
				try:
					yt = YouTube(url)
				except Exception as e:
					sg.popup("Link: "+values["input"]+"\n\nindisponivel para download ",title="ERRO")
				else:
					video = yt.streams.get_highest_resolution()
					out_file = video.download(output_path=values["pasta"])

					base, ext = os.path.splitext(out_file)
					new_file = base + '.mp3'
					try:
						os.rename(out_file, new_file) # <--- Não é possível criar um arquivo já existente
					except Exception as e:
						sg.popup("Vídeo: \n"+yt.title+"\n\nnão pode ser baixado pois existe um arquivo de mesmo nome",title="ERRO")
			sg.popup("Download finalizado com sucesso!",title="AVISO")

def download_audio(video_url):
	if(validador_pasta(values["pasta"]) == -1):
		sg.popup("Caracteres invalidos pra criação de pasta \n\n \\, /, |, <, >, *, :, “, ?",title="ERRO")
	else:
		sg.popup("Aguarde ate o termino do download \n\nIrá abrir um popup ao terminar",title="AVISO")
		try:
			yt = YouTube(video_url)
		except Exception as e:
			sg.popup("Link: "+values["input"]+"\n\nindisponivel para download ",title="ERRO")
		else:
			try:
				audio = yt.streams.filter(only_audio=True)[0]
			except Exception as e:
				sg.popup("Vídeo: "+yt.title+"\n\ncom restrição de idade ",title="ERRO")
			else:
				out_file = audio.download(output_path=values["pasta"])

				base, ext = os.path.splitext(out_file)
				new_file = base + '.mp3'
				try:
					os.rename(out_file, new_file) # <--- Não é possível criar um arquivo já existente
				except Exception as e:
					sg.popup("Vídeo: \n"+yt.title+"\n\nnão pode ser baixado pois existe um arquivo de mesmo nome",title="ERRO")
			sg.popup("Download finalizado com sucesso!",title="AVISO")


def download_playlist_audio(video_url):
	if(validador_pasta(values["pasta"]) == -1):
		sg.popup("Caracteres invalidos pra criação de pasta \n\n \\, /, |, <, >, *, :, “, ?",title="ERRO")
	else:
		playlist = Playlist(video_url)
		try:
			a = len(playlist) #IS A PLAYLIST?
		except Exception as e:
			download_audio(video_url)
		else:
			sg.popup("Aguarde ate o termino do download \n\nIrá abrir um popup ao terminar",title="AVISO")
			for url in playlist:
				try:
					yt = YouTube(url)
				except Exception as e:
					sg.popup("Link: "+values["input"]+"\n\nindisponivel para download ",title="ERRO")
				else:
					try:
						audio = yt.streams.filter(only_audio=True)[0]
					except Exception as e:
						sg.popup("Vídeo: "+yt.title+"\n\ncom restrição de idade ",title="ERRO")
					else:
						out_file = audio.download(output_path=values["pasta"])
						base, ext = os.path.splitext(out_file)
						new_file = base + '.mp3'
						try:
							os.rename(out_file, new_file) # <--- Não é possível criar um arquivo já existente
						except Exception as e:
							sg.popup("Vídeo: \n"+yt.title+"\n\nnão pode ser baixado pois existe um arquivo de mesmo nome",title="ERRO")
			sg.popup("Download finalizado com sucesso!",title="AVISO")


sg.theme('DefaultNoMoreNagging')   # --------- escolhe um tema para a interface


frame_layout = [
			[sg.Text('Cole o link do Youtube:')],
			[sg.Input(key="input")],
			[sg.Text('Deseja baixar em Vídeo(MP4) ou Áudio(MP3):')],
			[sg.Radio('Vídeo(MP4)', "RADIO1", default=True,key="video"), sg.Radio('Áudio(MP3)', "RADIO1",key="audio")],
			[sg.Text('Deseja baixar um único vídeo/música ou uma playlist:')],
			[sg.Radio('Single', "RADIO2", default=True,key="single"), sg.Radio('Playlist', "RADIO2",key="playlist")],
			[sg.Text('Digite o nome da pasta a ser criada:')],
			[sg.Input('Playlist',key="pasta")],
            [sg.Button('Baixar',key="button"), sg.Button('Cancel',key="close")] 
]

layout = [	

			[sg.Frame('Your-Download', frame_layout, font='Any 12')],
]

window = sg.Window('Your-Download', layout,font=("Helvetica", 12))

while True:
	event, values = window.read()

	if event in (None, 'close'):  
		break
	if event == "button":
		if values["video"] == True:
			if values["single"] == True:
				threading.Thread(download_video(values["input"])).start()
			else:
				threading.Thread(download_playlist(values["input"])).start()
		else:
			if values["single"] == True:
				threading.Thread(download_audio(values["input"])).start()
			else:
				threading.Thread(download_playlist_audio(values["input"])).start()
window.close()
