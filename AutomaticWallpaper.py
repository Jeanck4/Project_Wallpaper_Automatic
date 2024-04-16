import ctypes # pip install ctypes

def change_wallpaper(path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)

if __name__ == "__main__":
    wallpaper_path = r"C:\Users\jean.kuzava\Downloads\5499149.png"
    change_wallpaper(wallpaper_path)

#Só jogar no cmd para criar o arquivo executável em seguida colocar ele na pasta
#inicializadores windows para quando pc ligar trocar wallpaper:
#pyinstaller --onefile AutomaticWallpaper.py
#Win + R = shell:startup - comando para abrir inicializar do windows
