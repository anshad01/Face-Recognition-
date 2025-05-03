import face_recognition

# Load known face images (Use raw string to avoid path issues)
image_of_person1 = face_recognition.load_image_file(r"C:\Users\USER\Desktop\img\image\anshad_img.jpg")
image_of_person2 = face_recognition.load_image_file(r"C:\Users\USER\Desktop\img\image\aravind.jpg")  # New person
image_of_person3 = face_recognition.load_image_file(r"C:\Users\USER\Desktop\img\image\arya.jpg")
image_of_person4 = face_recognition.load_image_file(r"C:\Users\USER\Desktop\img\image\ravitha.jpg")

# Print image dimensions (Optional)
print("Image 1 Shape:", image_of_person1.shape)
print("Image 2 Shape:", image_of_person2.shape)
print("Image 3 Shape:", image_of_person3.shape)
print("Image 4 Shape:", image_of_person4.shape)

# Encode faces (Avoid crash if no face found)
encodings1 = face_recognition.face_encodings(image_of_person1)
encodings2 = face_recognition.face_encodings(image_of_person2)
encodings3 = face_recognition.face_encodings(image_of_person3)
encodings4 = face_recognition.face_encodings(image_of_person4)

if encodings1 and encodings2 and encodings3 and encodings4:
    person1_encoding = encodings1[0]
    person2_encoding = encodings2[0]
    person3_encoding = encodings3[0]
    person4_encoding = encodings4[0]
else:
    print("❌ Error: One or more faces could not be encoded.")
    exit()

# Store face encodings and names
known_face_encodings = [person1_encoding, person2_encoding,person3_encoding,person4_encoding]
known_face_names = ["Anshad", "Aravind","Arya","Ravitha"]

print("✅ Face encoding completed successfully!")
