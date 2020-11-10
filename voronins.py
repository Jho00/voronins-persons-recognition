import face_recognition
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware


kostik = face_recognition.load_image_file("samples/kostik.jpg")
kostik_encoding = face_recognition.face_encodings(kostik)[0]


vera = face_recognition.load_image_file("samples/vera.jpg")
vera_encoding = face_recognition.face_encodings(vera)[0]


ded = face_recognition.load_image_file("samples/nikolay.jpg")
ded_encoding = face_recognition.face_encodings(ded)[0]


galia = face_recognition.load_image_file("samples/galia.jpg")
galia_encoding = face_recognition.face_encodings(galia)[0]

lenia = face_recognition.load_image_file("samples/lenia.jpg")
lenia_encoding = face_recognition.face_encodings(lenia)[0]

nastya = face_recognition.load_image_file("samples/nastya.jpeg")
nastya_encoding = face_recognition.face_encodings(nastya)[0]

masha = face_recognition.load_image_file("samples/masha.jpg")
masha_encoding = face_recognition.face_encodings(masha)[0]


# unknown_image = face_recognition.load_image_file("samples/test.jpeg")


def start_comparing(encoding):
	compare_result = face_recognition.compare_faces([kostik_encoding], encoding)
	if compare_result[0]:
		return "Костик"

	else:
		return compare_vera(encoding)

def compare_vera(encoding):
	compare_result = face_recognition.compare_faces([vera_encoding], encoding)
	if compare_result[0]:
		return "Вера"

	else:
		return compare_ded(encoding)


def compare_ded(encoding):
	compare_result = face_recognition.compare_faces([ded_encoding], encoding)
	if compare_result[0]:
		return "Николай Петрович"

	else:
		return compare_galia(encoding)

def compare_galia(encoding):
	compare_result = face_recognition.compare_faces([galia_encoding], encoding)
	if compare_result[0]:
		return "ГАЛЯ"

	else:
		return compare_lenia(encoding)

def compare_lenia(encoding):
	compare_result = face_recognition.compare_faces([lenia_encoding], encoding)
	if compare_result[0]:
		return "Леня"

	else:
		return compare_nastya(encoding)

def compare_nastya(encoding):
	compare_result = face_recognition.compare_faces([nastya_encoding], encoding)
	if compare_result[0]:
		return "Настя"

	else:
		return compare_masha(encoding)

def compare_masha(encoding):
	compare_result = face_recognition.compare_faces([masha_encoding], encoding)
	if compare_result[0]:
		return "Маша"

	else:
		return "Это не Воронин"


# try:
# 	unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
# 	start_comparing(unknown_encoding)	
# except Exception as e:
# 	print("Тут нет лица")
# else:
# 	pass
# finally:
# 	pass


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import shutil

@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.post("/recognize/")
def create_file(file: UploadFile = File(...)):
	with open("samples/test.jpeg", "wb") as buffer:
	    shutil.copyfileobj(file.file, buffer)

	unknown_image = face_recognition.load_image_file("samples/test.jpeg")
	# unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
	# result = start_comparing(unknown_encoding)	
	try:
		unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
		result = start_comparing(unknown_encoding)	
	except Exception as e:
		result = "Тут нет лица"
	else:
		pass
	finally:
		pass


	return {"filename": file.filename, "result": result}					



