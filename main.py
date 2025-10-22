#!/usr/bin/env python3
"""
Facial Recognition Attendance System
Main application entry point
"""

import os
import sys
import argparse
from datetime import datetime

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def main():
    parser = argparse.ArgumentParser(description='Facial Recognition Attendance System')
    parser.add_argument('--mode', choices=['collect', 'train', 'app', 'test'], 
                       default='app', help='Mode to run the application')
    parser.add_argument('--epochs', type=int, default=50, 
                       help='Number of training epochs')
    parser.add_argument('--batch-size', type=int, default=32, 
                       help='Batch size for training')
    
    args = parser.parse_args()
    
    print("=== Facial Recognition Attendance System ===")
    print(f"Mode: {args.mode}")
    print(f"Timestamp: {datetime.now()}")
    print("=" * 50)
    
    if args.mode == 'collect':
        from data_collection import DataCollector
        collector = DataCollector()
        collector.collect_student_data()
        
    elif args.mode == 'train':
        from train_model import ModelTrainer
        trainer = ModelTrainer()
        trainer.train_model(epochs=args.epochs, batch_size=args.batch_size)
        
    elif args.mode == 'test':
        from train_model import ModelTrainer
        trainer = ModelTrainer()
        trainer.test_model()
        
    elif args.mode == 'app':
        from mobile_app.attendance_app import AttendanceApp
        app = AttendanceApp()
        app.run()

if __name__ == "__main__":
    main()




