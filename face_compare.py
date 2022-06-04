import face_recognition
import json
import numpy as np


def cmp_photo():
    with open('sample.json') as json_file:
        data = json.load(json_file)

    known_face_encodings = [np.asarray(i['encode']) for i in data]
    known_face_names = [f"{i['dir']} -> {i['name']}" for i in data]

    try:
        test_image = face_recognition.load_image_file("new_photos/student.jfif")
        encoded_test = face_recognition.face_encodings(test_image)[0]
        for encode in known_face_encodings:
            face_distance = face_recognition.face_distance([encode], encoded_test)
            face_cmp = face_recognition.compare_faces([encode], encoded_test)
            if face_cmp == [True]:
                if face_distance[0] < 0.4:
                    result = np.where(known_face_encodings == encode)[0]
                    index = result[0]
                    return known_face_names[index]
        return "Kechirasiz, kiritilgan shaxs astrum o'quvchisi emas!"

    except IndexError:
        return "Rasmda shaxs aniqlanmadi. Iltimos rasmni tekshirib ko'ring!"


cmp_photo()
