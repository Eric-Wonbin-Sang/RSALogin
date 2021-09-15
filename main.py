import cv2
import time
import pytesseract

from Classes import Webcam, Display

from General import Constants

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"


def main():

    webcam = Webcam.get_webcam(2)

    with open(Constants.code_txt_path, 'w') as code_txt:
        while webcam is not None:

            if webcam.set_transformed_frame() is None:
                continue

            display = Display.Display(webcam.frame)
            # display.show()

            if None not in display.value_list:
                print("".join(str(v) for v in display.value_list))
                code_txt.seek(0)
                code_txt.write("".join(str(v) for v in display.value_list))
                code_txt.truncate()
                code_txt.flush()
            else:
                for seven_segment in display.seven_segment_list:
                    if seven_segment.value is None:
                        print("Issue with {} - {}".format(seven_segment.idx, seven_segment.color_dict))
                        # seven_segment.show()
            print("--------------------")

            c = cv2.waitKey(1)
            if c == 27:
                break

            time.sleep(1)

    webcam.cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
