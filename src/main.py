import streamlit as st
import input_format as inpf
from directedGraph import DirectedGraph
import json

from student_info import InputParser

def applications():
    with open('./applications/applications.json') as json_file:
        data = json.load(json_file)

    # Define the size of the images
    image_width = 125

    st.markdown("""
    <style>
        .sidebar .sidebar-content {
            max-height: 80vh; /* Adjust as needed */
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
    </style>
    """, unsafe_allow_html=True)

    # Iterate over each application in the data
    with st.sidebar:
         st.header("Extra Resources")

    with st.sidebar:
        for app in data:
            st.markdown(f"### [{app['name']}]({app['page_url']})")
            st.image(app["path"], width=image_width)

def curr_inp():
    '''
        Sets session state of input to empty string
    '''
    st.session_state.curr_input = st.session_state.curr_widget
    st.session_state.curr_widget = ""


def prev_inp():
    '''
        Sets session state of input to empty string
    '''
    st.session_state.prev_input = st.session_state.prev_widget
    st.session_state.prev_widget = ""


def main():
    st.title("Quarter Planner")
    
    # set page to wide
    # st.set_page_config(page_title="ZotHub", layout="wide")

    # if 'input' not in st.session_state:
    #     st.session_state.input = ''
    
    if "curr_input" not in st.session_state:
        st.session_state.curr_input = ''
    if "prev_input" not in st.session_state:
        st.session_state.prev_input = ''
    if "num_input" not in st.session_state:
        st.session_state.num_input = ''

    if 'start' not in st.session_state:
        st.session_state.start = 0
    empty = st.empty()
    # st.text_input("Search...", key="widget", on_change=inp)
    st.header("Taken Classes")
    st.text_area("Classes taken...", key="curr_widget", on_change=curr_inp)
    
    st.header("Preferences")
    st.markdown("Please follow the specified format:<br /> \
                [number of cs classes]<br /> \
                [number of GEs]<br /> \
                [start range of units]-[end range of units]<br /> \
                [Undesirable courses (i.e. (I&CS53, COMPSCI161)]", unsafe_allow_html=True)
    st.text_area("Insert Preferences...", key="prev_widget", on_change=prev_inp)

    #  on_change continues the code after user queries again so we do not need while True loop
    taken_class_query = st.session_state.curr_input
    pref_class_query = st.session_state.prev_input
    # num_class_query = st.session_state.num_input

    ### Taken Classes
    if taken_class_query and taken_class_query[-1] != '\n':
        taken_class_query += "\n"
    ip = InputParser(taken_class_query, pref_class_query)
    student_prog, student_pref = ip.parse_input()

    # st.header("Extra Resources")
    applications()
    if taken_class_query:
        st.header("Next Quarter Possible Courses")
        st.write(student_prog)
    print(student_prog)
    print(student_pref)
    
    # ics-6d 4 2

    ### Query contains user input
    ### function(query)
    pass


    g = DirectedGraph()

    potentialClasses = g.getPotentialFutureCourse(student_prog.cats_and_courses)
    finalList = g.getFinalList(potentialClasses, 4)

    print(finalList)
    



if __name__ == '__main__':
    main()