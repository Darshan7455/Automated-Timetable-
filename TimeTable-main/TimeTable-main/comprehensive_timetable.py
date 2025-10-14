import pandas as pd
import random
from datetime import datetime, time, timedelta
from openpyxl import Workbook, load_workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Font
from openpyxl.utils import get_column_letter
import csv
import glob
import os
import json

def load_config():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            return config['duration_constants']
    except:
        return {
            'hour_slots': 2,
            'lecture_duration': 3,
            'lab_duration': 4,
            'tutorial_duration': 2,
            'self_study_duration': 2, 
            'break_duration': 1
        }

durations = load_config()
HOUR_SLOTS = durations['hour_slots']
LECTURE_DURATION = durations['lecture_duration']
LAB_DURATION = durations['lab_duration']
TUTORIAL_DURATION = durations['tutorial_duration']
SELF_STUDY_DURATION = durations['self_study_duration']
BREAK_DURATION = durations['break_duration']

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
START_TIME = time(9, 0)
END_TIME = time(18, 30)

LUNCH_WINDOW_START = time(12, 30)
LUNCH_WINDOW_END = time(14, 0)
LUNCH_DURATION = 60

TIME_SLOTS = []
lunch_breaks = {}

def calculate_lunch_breaks(semesters):
    global lunch_breaks
    lunch_breaks = {}
    total_semesters = len(semesters)
    if total_semesters == 0:
        return lunch_breaks
    total_window_minutes = (
        LUNCH_WINDOW_END.hour * 60 + LUNCH_WINDOW_END.minute -
        LUNCH_WINDOW_START.hour * 60 - LUNCH_WINDOW_START.minute
    )
    stagger_interval = (total_window_minutes - LUNCH_DURATION) / (total_semesters - 1) if total_semesters > 1 else 0
    sorted_semesters = sorted(semesters)
    for i, semester in enumerate(sorted_semesters):
        start_minutes = (LUNCH_WINDOW_START.hour * 60 + LUNCH_WINDOW_START.minute + int(i * stagger_interval))
        start_hour = start_minutes // 60
        start_min = start_minutes % 60
        end_minutes = start_minutes + LUNCH_DURATION
        end_hour = end_minutes // 60
        end_min = end_minutes % 60
        lunch_breaks[semester] = (
            time(start_hour, start_min),
            time(end_hour, end_min)
        )
    return lunch_breaks

def initialize_time_slots():
    global TIME_SLOTS
    TIME_SLOTS = generate_time_slots()

def generate_time_slots():
    slots = []
    current_time = datetime.combine(datetime.today(), START_TIME)
    end_time = datetime.combine(datetime.today(), END_TIME)
    while current_time < end_time:
        current = current_time.time()
        next_time = current_time + timedelta(minutes=30)
        slots.append((current, next_time.time()))
        current_time = next_time
    return slots

def load_rooms():
    rooms = {}
    try:
        with open('rooms.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rooms[row['id']] = {
                    'capacity': int(row['capacity']),
                    'type': row['type'],
                    'roomNumber': row['roomNumber'],
                    'schedule': {day: set() for day in range(len(DAYS))}
                }
    except FileNotFoundError:
        print("Warning: rooms.csv not found, using default room allocation")
        return None
    return rooms

def load_batch_data():
    batch_info = {}
    try:
        df = pd.read_csv('combined.csv')
        grouped = df.groupby(['Department', 'Semester'])
        for (dept, sem), group in grouped:
            if 'total_students' in group.columns and not group['total_students'].isna().all():
                total_students = int(group['total_students'].max())
                max_batch_size = 70
                num_sections = (total_students + max_batch_size - 1) // max_batch_size
                section_size = (total_students + num_sections - 1) // num_sections
                batch_info[(dept, sem)] = {
                    'total': total_students,
                    'num_sections': num_sections,
                    'section_size': section_size
                }
        basket_courses = df[df['Course Code'].astype(str).str.contains('^B[0-9]')]
        for _, course in basket_courses.iterrows():
            code = str(course['Course Code'])
            if 'total_students' in df.columns and pd.notna(course['total_students']):
                total_students = int(course['total_students'])
            else:
                total_students = 35
            batch_info[('ELECTIVE', code)] = {
                'total': total_students,
                'num_sections': 1,
                'section_size': total_students
            }
    except FileNotFoundError:
        print("Warning: combined.csv not found, using default batch sizes")
    except Exception as e:
        print(f"Warning: Error processing batch sizes from combined.csv: {e}")
    return batch_info

def find_adjacent_lab_room(room_id, rooms):
    if not room_id:
        return None
    current_num = int(''.join(filter(str.isdigit, rooms[room_id]['roomNumber'])))
    current_floor = current_num // 100
    for rid, room in rooms.items():
        if rid != room_id and room['type'] == rooms[room_id]['type']:
            room_num = int(''.join(filter(str.isdigit, room['roomNumber'])))
            if room_num // 100 == current_floor and abs(room_num - current_num) == 1:
                return rid
    return None

def find_suitable_room(course_type, department, semester, day, start_slot, duration, rooms, batch_info, timetable, course_code="", used_rooms=None):
    pass

def try_room_allocation(rooms, course_type, required_capacity, day, start_slot, duration, used_room_ids):
     pass

def get_required_room_type(course):
      pass

def is_basket_course(code):
      pass

def get_basket_group(code):
      pass

def get_basket_group_slots(timetable, day, basket_group):
    pass

def is_break_time(slot, semester=None):
      pass

def is_lecture_scheduled(timetable, day, start_slot, end_slot):
       pass

def calculate_required_slots(course):
      pass

def select_faculty(faculty_str):
    pass

def check_faculty_daily_components(professor_schedule, faculty, day, department, semester, section, timetable, course_code=None, activity_type=None):
    pass

def check_faculty_course_gap(professor_schedule, timetable, faculty, course_code, day, start_slot):
       pass

def load_reserved_slots():
    pass

def is_slot_reserved(slot, day, semester, department, reserved_slots):
      pass

def load_faculty_preferences():
       pass

def is_preferred_slot(faculty, day, time_slot, faculty_preferences):
       pass

def get_course_priority(course):
       pass

def get_best_slots(timetable, professor_schedule, faculty, day, duration, reserved_slots, semester, department, faculty_preferences):
      pass

class UnscheduledComponent:
      pass

def unscheduled_reason(course, department, semester, professor_schedule, rooms, component_type, check_attempts):
       pass

def generate_all_timetables():
    pass

if __name__ == "__main__":
    generate_all_timetables()
