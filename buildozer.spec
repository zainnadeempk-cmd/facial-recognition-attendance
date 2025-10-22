[app]
title = Facial Recognition Attendance
package.name = facialattendance
package.domain = com.facialattendance
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,h5,pkl
source.include_patterns = data/*
version = 1.0
requirements = python3,kivy,kivymd,plyer,opencv-python,numpy,pandas,matplotlib,seaborn,scikit-learn,Pillow,tensorflow,mtcnn

[buildozer]
log_level = 2
warn_on_root = 1

[android]
permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE