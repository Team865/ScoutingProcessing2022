import cv2
from pyzbar import pyzbar
import time

spacer = False


def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        # 1
        barcode_info = barcode.data.decode('utf-8')

        if barcode_info[0] == "T":
            barcode_info = barcode_info.split("\r\n")[1]

        if spacer:
            barcode_info += "\r\n"
        else:
            barcode_info += ",\n"

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        # 3
        with open("qrcode.csv", mode='a') as file:
            file.write(barcode_info)
            time.sleep(1.5)
    return frame


def main():
    # 1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    # 2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('QR Scanner', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    # 3
    camera.release()
    cv2.destroyAllWindows()


# 4
if __name__ == '__main__':
    main()
