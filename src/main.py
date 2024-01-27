import streamlit as st
import input_format as inpf
import json

def applications():
    with open('./applications/applications.json') as json_file:
        data = json.load(json_file)

    # Set the option to display images at the same width
    # st.set_option('deprecation.showfileUploaderEncoding', False)

    # Define the size of the images
    image_width = 200

    # Initialize a list to store image elements
    image_elements = []

    # Iterate over each application in the data
    col1, col2, col3 = st.columns(3)
    for index, app in enumerate(data):
        # Add the image to the list of image elements
        if index % 3 == 0:
            with col1:
                st.header(app["name"])
                st.image(app["path"], width=image_width)
        elif index % 3 == 1:
            with col2:
                st.header(app["name"])
                st.image(app["path"], width=image_width)            
        elif index % 3 == 2:
            with col3:
                st.header(app["name"])
                st.image(app["path"], width=image_width)
        else:
            col1, col2, col3 = st.columns(3)

        # image_elements.append(st.image(app["path"], caption=app["name"], width=image_width))

    # Display the images in a row
    # st.write("Applications:")
    # st.write(image_elements)


def inp():
    '''
        Sets session state of input to empty string
    '''
    st.session_state.input = st.session_state.widget
    st.session_state.widget = ""


def main():
    st.title("ZotHub")
    
    # set page to wide
    # st.set_page_config(page_title="ZotHub", layout="wide")

    if 'input' not in st.session_state:
        st.session_state.input = ''
    if 'start' not in st.session_state:
        st.session_state.start = 0
    empty = st.empty()
    # st.text_input("Search...", key="widget", on_change=inp)
    st.text_area("Search...", key="widget", on_change=inp)
    #  on_change continues the code after user queries again so we do not need while True loop
    query = st.session_state.input
    applications()
    # print(query)
    
    # ics-6d 4 2

    ### Query contains user input
    ### function(query)
    pass


if __name__ == '__main__':
    main()