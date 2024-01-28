# UCI Quarter Planner

### Synopsis</br>
The Quarter Planner project is to help UCI students (currently only for __only__ ICS students but in Beta Phase ...may display inaccurate information...) recommend classes one quarter ahead based on the current courses they have already taken.

## How to get started
1) Clone the repository on Github
2) Run ```pip install -r requirements/requirements.txt ``` from the root directory of your working project to install all dependencies
3) Run ```streamlit run src/main.py``` from the root directory of working project to run the program
4) There is a list of ___Extra Resources___ links on the sidebar for additional applications students may find useful
5) There are two text boxes.</br>
    I. Taken Classes : Insert taken classes student has taken for previous quarters at UCI and press ```CTRL + ENTER``` or ```CMD + ENTER``` depending on Windows or Mac. Example down below.

    <blockquote> 
    I&CSCI31 </br>
    I&CSCI32 </br>
    I&CSCI33 <br>
    </blockquote>
    II. Preferences : Insert Preferences for courses.</br>
        * Please follow specified format and enter
        <blockquote>
        [number of cs classes] </br>
        [number of GEs] </br>
        [start range of units]-[end range of units] </br>
        [Undesirable courses (i.e. (I&CS53, COMPSCI161))] </br> 
        </blockquote>

Wait for program to run...Users should be able to scroll down and see the 
1) <u>Completed Courses and Progress</u> : Indicating what GEs the classes account for
2) <u>Course Preferences</u> : Lists the course preferences user typed in
3) <u>Course Recommendations</u> : Lists the recommended courses for next quarter
