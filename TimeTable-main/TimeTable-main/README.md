## User Manual for Time-table Automation System

### 1. Overview

The Time-table Automation System is a command-line Python application designed to automate the scheduling of courses for academic sessions at a university. It processes course data, assigns rooms, schedules lectures, tutorials, and labs while avoiding conflicts (e.g., professor and room conflicts), and accounts for break times (morning and lunch breaks). The system generates timetables for each department-semester combination and outputs them to an Excel file (`timetable_all_departments.xlsx`). It also identifies and reports unscheduled courses in `unscheduled_courses.xlsx` and generates faculty schedules in `all_faculty_timetables.xlsx`.

This manual provides instructions for downloading, setting up, and using the system, along with usage scenarios, requirements satisfied, future work, and FAQs.

---

### 2. Instructions for Downloading the Software from GitHub

#### Accessing the Repository

- Visit the GitHub repository: `https://github.com/Darshan7455/Automated-Timetable-.git`
- If the repository is private, request access from the Software Psych team.

#### Cloning the Repository

- Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and run: 
  ```
  git clone https://github.com/Darshan7455/Automated-Timetable-.git
  ```

- This downloads the project files to a `TimeTable` folder on your machine.

#### Downloading as ZIP

- Alternatively, on the GitHub repository page, click the green "Code" button and select "Download ZIP".
- Extract the ZIP file to a folder on your machine.

---

### 3. How to Set Up the Software

#### Prerequisites

- **Python 3.9 or later**: Download from [python.org](https://www.python.org/downloads/).
- **Git**: Download from [git-scm.com](https://git-scm.com/downloads) (optional, for cloning).
- **pip**: Python's package manager (included with Python).

#### Setup Steps

1. **Navigate to the Project Directory**:

- Open a terminal and navigate to the project folder:
  ```
  cd timetable-automation
  ```

2. **Create a Virtual Environment**:

- Create a virtual environment to manage dependencies:
  ```
  python -m venv venv
  ```
- Activate the virtual environment:
  - On Windows:
    ```
    venv\Scripts\activate
    ```
  - On macOS/Linux:
    ```
    source venv/bin/activate
    ```

3. **Install Dependencies**:

- The system requires the following Python libraries:
  - `pandas`: Data manipulation and analysis
  - `openpyxl`: Reading/writing Excel files
  - `datetime`: Date and time manipulation
  - `random`: Random number generation
  - `collections`: Special container datatypes (e.g., defaultdict)
  - `csv`: CSV file reading/writing
  - `json`: JSON data manipulation
  - `os`: Operating system interfaces
  - `traceback`: Stack trace extraction for error reporting

- Install the main dependencies using:
  ```
  pip install pandas openpyxl
  ```
- The other packages (`datetime`, `random`, `collections`, `csv`, `json`, `os`, `traceback`) are part of Python's standard library and don't need separate installation.

- Alternatively, if a `requirements.txt` file is provided, run:
  ```
  pip install -r requirements.txt
  ```

4. **Place Configuration Files**:

- Ensure the required input files (`combined.csv` and `rooms.csv`) are in the project directory (see Section 4 for details).

5. **Run the Application**:

- Run the script to generate timetables:
  ```
  python TT_gen.py
  ```
- The script will generate:
  - `timetable_all_departments.xlsx` - The main timetable file with all department schedules
  - `unscheduled_courses.xlsx` - Report of courses that couldn't be fully scheduled
  - `all_faculty_timetables.xlsx` - Individual schedules for all faculty members
- **Screenshot Placeholder**: [Insert screenshot of the terminal showing the `python TT_gen.py` command and the output messages]

---

### 4. Setting Up Configuration Files

The system requires two input files to operate: `combined.csv` and `rooms.csv`. These files must be placed in the project directory.

#### Required Configuration Files

1. **combined.csv**:

- **Purpose**: Contains course data for scheduling.
- **Format** (example):
  ```
  Course Code,Course Name,Department,Semester,Faculty,L,T,P,S,C,Schedule,total_students
  CS301,Software Engineering,CSE,5,Dr. Smith,3,1,0,0,4,Yes,60
  EC201,Circuits,ECE,3,Dr. Jones,2,1,2,0,4,Yes,45
  ```
- **Fields**:
  - `Course Code`: Unique course identifier (e.g., CS301, or basket courses like B1(CS101/CS102)).
  - `Course Name`: Name of the course.
  - `Department`: Department (e.g., CSE, ECE, DSAI).
  - `Semester`: Semester number (e.g., 1 to 8).
  - `Faculty`: Instructor name (can include multiple options separated by '/' or multiple instructors).
  - `L,T,P,S`: Lecture, Tutorial, Practical, Self-study hours (integers).
  - `C`: Total credits for the course.
  - `Schedule`: Yes/No, indicating if the course should be scheduled (optional).
  - `total_students`: Number of students registered for the course (used for room allocation).

2. **rooms.csv**:

- **Purpose**: Contains room data for scheduling.
- **Format** (example):
  ```
  id,roomNumber,type,capacity
  1,A101,LECTURE_ROOM,60
  2,Lab1,COMPUTER_LAB,35
  3,Room201,SEATER_120,120
  ```
- **Fields**:
  - `id`: Unique identifier for the room.
  - `roomNumber`: Room identifier (e.g., A101, Lab1).
  - `type`: Room type (LECTURE_ROOM, COMPUTER_LAB, HARDWARE_LAB, SEATER_120, SEATER_240).
  - `capacity`: Maximum number of students the room can accommodate.

#### Steps to Configure

1. Place `combined.csv` and `rooms.csv` in the project directory (same folder as the script).
2. Edit the files using Excel or a text editor to match your institution's data.

- **Screenshot Placeholder**: [Insert screenshot of the project directory showing `combined.csv` and `rooms.csv`]

---

### 5. Usage Scenarios

Since the system is a command-line application, usage involves running the script and viewing the output Excel files.

#### Scenario 1: Generate Timetables for All Departments and Semesters

1. **Prepare Input Files**:

- Ensure `combined.csv` and `rooms.csv` are in the project directory with the correct data.
- **Screenshot Placeholder**: [Insert screenshot of the project directory with the input files]

2. **Run the Script**:

- Open a terminal, navigate to the project directory, and run:
  ```
  python TT_gen.py
  ```
- The script will:
  - Read course and room data.
  - Schedule lectures, tutorials, and labs while avoiding conflicts.
  - Allocate break times (morning break: 10:30-10:45; lunch break: dynamically staggered between 12:30-14:00).
  - Generate `timetable_all_departments.xlsx` with separate sheets for each department-semester combination (e.g., `CSE_5`, `ECE_3`).
- **Screenshot Placeholder**: [Insert screenshot of the terminal showing the script execution and completion message]

3. **View the Timetable**:

- Open `timetable_all_departments.xlsx` in Excel.
- The "Overview" sheet contains links to all department-semester timetables.
- Each department-semester sheet shows a timetable with:
  - Days (Monday to Friday) as rows.
  - Time slots (9:00 to 18:30, in 30-minute intervals) as columns.
  - Course details (code, type, faculty, room) in each slot.
  - A legend at the bottom listing courses, faculty, and LTPS details.
  - Self-study only courses and unscheduled components (if any).
- **Screenshot Placeholder**: [Insert screenshot of a timetable sheet in `timetable_all_departments.xlsx`]

4. **Check for Unscheduled Courses**:

- The script generates `unscheduled_courses.xlsx` with details of courses that couldn't be fully scheduled according to their LTPS requirements.
- Open this file to view details of unscheduled courses (code, name, faculty, required vs. scheduled LTPS hours, and possible reasons).
- **Screenshot Placeholder**: [Insert screenshot of `unscheduled_courses.xlsx`]

5. **View Faculty Timetables**:

- Open `all_faculty_timetables.xlsx` to view individual schedules for all faculty members.
- The "Overview" sheet contains links to each faculty member's schedule.
- Each faculty sheet shows their complete teaching schedule across all departments and courses.
- **Screenshot Placeholder**: [Insert screenshot of a faculty timetable in `all_faculty_timetables.xlsx`]

---

### 6. Requirements Satisfied by the Current Version

The current version satisfies the following requirements:

- **REQ-02-Config**: The system reads course data and room assignments from `combined.csv` and `rooms.csv`.
- **REQ-03**: Courses are scheduled in classrooms with sufficient capacity, with students split into sections if needed.
- **REQ-04-CONFLICTS**: The system distributes course components over the week and avoids scheduling multiple components on the same day.
- **REQ-05**: Courses with the same code from different departments are scheduled separately.
- **REQ-06**: Scheduling adheres to the LTPS structure (e.g., 1.5 hours lecture = 3 slots, 2 hours lab = 4 slots, 1 hour tutorial = 2 slots).
- **REQ-07**: Elective courses are grouped into baskets (B1, B2, etc.) and scheduled to avoid conflicts.
- **REQ-08**: Lab sessions are allocated based on lab room capacity, with multiple batches if needed.
- **REQ-09-BREAKS**: Morning break (15 minutes) and inter-class breaks (5 minutes) are included in the schedule.
- **REQ-10-FACULTY**: The system tries to maintain at least 3 hours between a faculty member's classes on the same day.
- **REQ-14-VIEW**: Timetables are exported to Excel for viewing by coordinators, faculty, and students.
- **REQ-18-LUNCH**: Lunch breaks are scheduled in a staggered fashion to avoid overcrowding.

---

### 7. Future Work

The following features are planned for future versions:

- **UI Development**: Add a user interface (e.g., Flask web app or Tkinter desktop app) to allow coordinators, faculty, and students to interact with the system directly.
- **Exam Scheduling (REQ-15-EXAM)**: Implement exam timetable scheduling with seating arrangements and minimize exam days.
- **Analytics Reports (REQ-16-ANALYTICS)**: Enhance reports on room usage, instructor effort, and student effort.
- **Faculty Preferences (REQ-11-FACULTY)**: Improve incorporation of faculty scheduling preferences (e.g., preferred days/times).
- **Reserved Time Slots (REQ-12-COORD)**: Add capability for coordinators to reserve specific time slots.
- **Google Calendar Integration (REQ-13-GCALENDER)**: Allow faculty and students to sync timetables with Google Calendar.
- **Dynamic Modifications (REQ-01)**: Enhance support for modifying existing timetables with minimal changes.
- **Teaching Assistant Allocation (REQ-17-ASSIST)**: Improve allocation of teaching/lab assistants for large courses.

---

### 8. FAQs

**Q: What should I do if the script fails to run?**

- A: Ensure `combined.csv` and `rooms.csv` are in the project directory with the correct format. Check that all dependencies (`pandas`, `openpyxl`) are installed. Review the terminal error message for details.

**Q: What if some courses are unscheduled?**

- A: The script generates `unscheduled_courses.xlsx` with details of unscheduled courses. You can adjust the input data (e.g., reduce conflicts, add more rooms) and rerun the script.

**Q: Can I customize the time slots or break times?**

- A: Yes, but you'll need to modify the constants in the code (`START_TIME`, `END_TIME`, `LECTURE_DURATION`, etc.). A future version will include a configuration file for these settings.

**Q: How do I view the timetable for a specific department?**

- A: Open `timetable_all_departments.xlsx` in Excel. The "Overview" sheet contains links to each department-semester timetable.

**Q: How can a faculty member view their schedule?**

- A: Open `all_faculty_timetables.xlsx` in Excel. The "Overview" sheet contains links to each faculty member's schedule.

**Q: How does the system handle basket courses (electives)?**

- A: Basket courses (e.g., B1, B2) are scheduled in parallel time slots to avoid conflicts for students who need to choose one course from each basket.

**Q: What happens if a room type is missing in `rooms.csv`?**

- A: The script will print a warning (e.g., "No LECTURE_ROOM type rooms found") and try to continue with available rooms. Ensure all required room types are included in `rooms.csv`.

**Q: How do I add more faculty or courses?**

- A: Simply add new entries to the `combined.csv` file following the same format as existing entries.

---

### 9. Conclusion

This user manual provides a guide to setting up and using the Time-table Automation System developed by the Software Psych team. The system automates the generation of academic timetables with conflict avoidance, proper room allocation, and staggered break times. It outputs comprehensive timetables for all departments and faculty members in Excel format. Future versions will add more features and enhance scheduling constraints. For support, contact the Software Psych development team.
