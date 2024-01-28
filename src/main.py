import streamlit as st
import input_format as inpf
from directedGraph import DirectedGraph
import json

from student_info import InputParser

def applications():
    with open('./applications/applications.json') as json_file:
        data = json.load(json_file)

    # Set the option to display images at the same width
    # st.set_option('deprecation.showfileUploaderEncoding', False)

    # Define the size of the images
    image_width = 100

    # Initialize a list to store image elements
    image_elements = []

    # Iterate over each application in the data
    col1, col2, col3 = st.columns(3)
    for index, app in enumerate(data):
        # Add the image to the list of image elements
        if index % 3 == 0:
            with col1:
                # st.markdown(f"[![{app['name']}]({app['path']})]({app['page_url']})")
                st.markdown(f"### [{app['name']}]({app['page_url']})")
                # st.header(app["name"])
                st.image(app["path"], width=image_width)
        elif index % 3 == 1:
            with col2:
                st.markdown(f"### [{app['name']}]({app['page_url']})")
                # st.header(app["name"])
                st.image(app["path"], width=image_width)            
        elif index % 3 == 2:
            with col3:
                st.markdown(f"### [{app['name']}]({app['page_url']})")
                # st.header(app["name"])
                st.image(app["path"], width=image_width)
        else:
            col1, col2, col3 = st.columns(3)
        # st.markdown(f"[![{app['name']}]({app['path']})]({app['page_url']})")
        # image_elements.append(st.image(app["path"], caption=app["name"], width=image_width))
    # Display the images in a row
    # st.write("Applications:")
    # st.write(image_elements)


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


def num_inp():
    '''
        Sets session state of input to empty string
    '''
    st.session_state.num_input = st.session_state.num_widget
    st.session_state.num_widget = ""


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
    st.text_area("Search...", key="curr_widget", on_change=curr_inp)
    
    st.header("Preferences")
    st.text_area("Search...", key="prev_widget", on_change=prev_inp)

    # st.header("# CS Classes")
    # st.text_area("Search...", key="num_widget", on_change=num_inp)

    #  on_change continues the code after user queries again so we do not need while True loop
    taken_class_query = st.session_state.curr_input
    pref_class_query = st.session_state.prev_input
    # num_class_query = st.session_state.num_input

    ### Taken Classes
    if taken_class_query and taken_class_query[-1] != '\n':
        taken_class_query += "\n"
    ip = InputParser(taken_class_query, pref_class_query)
    student_prog, student_pref = ip.parse_input()

    st.header("Extra Resources")
    applications()
    
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