# Configuration file for Facial Recognition Attendance System

# Model Configuration
MODEL_CONFIG = {
    'input_size': (224, 224, 3),
    'batch_size': 32,
    'epochs': 50,
    'learning_rate': 0.001,
    'confidence_threshold': 0.7
}

# Face Detection Configuration
FACE_DETECTION_CONFIG = {
    'method': 'mtcnn',  # 'mtcnn' or 'haar'
    'min_confidence': 0.9,
    'min_face_size': (30, 30)
}

# Database Configuration
DATABASE_CONFIG = {
    'db_path': 'attendance.db',
    'backup_interval': 24  # hours
}

# Mobile App Configuration
MOBILE_APP_CONFIG = {
    'window_size': (800, 600),
    'camera_fps': 30,
    'display_fps': 15
}

# Data Collection Configuration
DATA_COLLECTION_CONFIG = {
    'min_images_per_student': 20,
    'max_images_per_student': 100,
    'image_size': (224, 224),
    'augmentation': True
}

# Performance Configuration
PERFORMANCE_CONFIG = {
    'use_gpu': True,
    'max_batch_size': 64,
    'memory_limit': 4096  # MB
}




