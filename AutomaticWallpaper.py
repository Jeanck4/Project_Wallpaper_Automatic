import ctypes
import tempfile
from PIL import Image
import win32api, win32con

# Obtém a resolução da tela
def get_screen_resolution():
    width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    return width, height

# Redimensiona a imagem para uma largura e altura específicas
def resize_image(image_path, target_width, target_height):
    image = Image.open(image_path)
    resized_image = image.resize((target_width, target_height))
    return resized_image

# Cria um papel de parede para dois monitores
def create_dual_monitor_wallpaper(image_path):
    # Obtém a resolução da tela total (para dois monitores)
    width, height = get_screen_resolution()
    total_width = width * 2
    total_height = height

    # Abre a imagem original
    image = Image.open(image_path)
    # Redimensiona a imagem para a resolução total da tela
    resized_image = resize_image(image_path, total_width, total_height)

    # Corta a imagem ao meio para cada monitor
    left_image = resized_image.crop((0, 0, width, height))
    right_image = resized_image.crop((width, 0, total_width, height))

    # Salva temporariamente as imagens cortadas
    left_temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    right_temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)

    left_temp_file_path = left_temp_file.name
    right_temp_file_path = right_temp_file.name

    left_image.save(left_temp_file_path)
    right_image.save(right_temp_file_path)

    left_temp_file.close()
    right_temp_file.close()

    return left_temp_file_path, right_temp_file_path

# Define o papel de parede para dois monitores
def change_dual_monitor_wallpaper(left_image_path, right_image_path):
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02

    # Define o papel de parede para o primeiro monitor
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, left_image_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)

    # Define o papel de parede para o segundo monitor
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 1, right_image_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)

if __name__ == "__main__":
    wallpaper_path = r"C:\Users\jean.kuzava\Downloads\fabrizio-conti-k6GpdsPJSZw-unsplash.png"
    left_wallpaper_path, right_wallpaper_path = create_dual_monitor_wallpaper(wallpaper_path)
    change_dual_monitor_wallpaper(left_wallpaper_path, right_wallpaper_path)


#Só jogar no cmd para criar o arquivo executável em seguida colocar ele na pasta
#inicializadores windows para quando pc ligar trocar wallpaper:
#pyinstaller --onefile AutomaticWallpaper.py
#Win + R = shell:startup - comando para abrir inicializar do windows
