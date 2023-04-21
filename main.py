from youtube_dl import YoutubeDL

music_list=[]

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

while True:
    choice = input('Escolha uma das opções abaixo\n1 - Adicionar música\n2 - Ir para dowload\n3 - sair\n')
    if choice == '1':
        music_url = input('Cole aqui a URL da música desejada: ')
        music_list.append(music_url)
        continue
    elif choice == '2':
        if not music_list:
            print('Nenhuma música adicionada.')
            continue

        for music in music_list:
            try:
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([music])
            except Exception as e:
                print(f'Erro ao baixar a música: {music}. Erro: {e}')
                continue

            title = ydl.extract_info(music, download=False).get('title', None)
            if title:
                print(f'{title} baixada com sucesso.')
            else:
                print(f'Erro ao mover a música: {music}.')
        break
    elif choice == '3':
        break
    else:
        print('Opção inválida. Tente novamente.')
        continue
