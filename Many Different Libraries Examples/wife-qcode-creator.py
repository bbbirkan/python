import wifi_qrcode_generator as qr
from PIL import Image
a=qr.wifi_qrcode('birkan', False, 'WPA', '12343df')
a.show()

print('\n'.join(line.split(":",1)[0] for line in open("/etc/passwd")))

