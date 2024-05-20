import cv2
from simple_facerec import SimpleFacerec

from source_people import recognition

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images")

# Load Camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# cellini = ["eta' = 17", "classe = 4 INF"]
# licciardino = ["eta' = 18", "classe = 4 INF"]
# prof = ["Docente indirizzo informatico"]
# rizzolo = ["eta' = 17", "classe = 4 INF"]
# vallosio = ["eta' = 17", "classe = 3 INF", "soprannome = Nick"]
# canale = ["eta' = 17", "classe = 4 INF", "soprannome = John"]
# linus = ["Inventore del kernel Linux"]
# gioele = ["eta' = 17", "classe = 4 INF"]
# ape = ["eta' = 18", "classe = 4 INF"]

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 200, 0), 2)

        recognition(name, frame)

        # if name == "Cellini_Marco" :
        #     cv2.putText(frame, cellini[0],(10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        #     cv2.putText(frame, cellini[1],(10, 60), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        
        # if name == "Licciardino_Matteo" :
        #     cv2.putText(frame, licciardino[0],(10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        #     cv2.putText(frame, licciardino[1],(10, 60), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)

        # if name == "prof_Mancuso" :
        #     cv2.putText(frame, prof[0],(10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)

        # if name == "Rizzolo_Lorenzo" :
        #     cv2.putText(frame, rizzolo[0],(10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        #     cv2.putText(frame, rizzolo[1],(10, 60), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)

        # if name == "Canale_Andrea" :
        #     cv2.putText(frame, canale[0],(10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        #     cv2.putText(frame, canale[1],(10, 60), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        #     cv2.putText(frame, canale[2],(10, 90), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)

        # if name == "Vallosio_Gariele" :
        #     cv2.putText(frame, vallosio[0],(10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        #     cv2.putText(frame, vallosio[1],(10, 60), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        #     cv2.putText(frame, vallosio[2],(10, 90), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)

        # if name == "Linus_Torvalds" :
        #     cv2.putText(frame, linus[0],(10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)

        # if name == "Gioele_Mari" :
        #     cv2.putText(frame, gioele[0],(10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        #     cv2.putText(frame, gioele[1],(10, 60), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)

        # if name == "Apetroaie_Antonio" :
        #     cv2.putText(frame, ape[0],(10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
        #     cv2.putText(frame, ape[1],(10, 60), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()