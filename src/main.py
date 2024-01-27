import streamlit as st


def inp():
    '''
        Sets session state of input to empty string
    '''
    st.session_state.input = st.session_state.widget
    st.session_state.widget = ""


def main():
    st.title("Quarter Planner")
    if 'input' not in st.session_state:
        st.session_state.input = ''
    if 'start' not in st.session_state:
        st.session_state.start = 0
    empty = st.empty()
    st.text_area("Search...", key="widget", on_change=inp)
    #  on_change continues the code after user queries again so we do not need while True loop
    query = st.session_state.input
    # print(query)
    
    ### Query contains user input
    ### function(query)
    pass



if __name__ == '__main__':
    main()