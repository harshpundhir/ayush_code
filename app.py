import streamlit as st
import admin
import user
import login

# Initialize session state variables if they don't exist
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'role' not in st.session_state:
    st.session_state['role'] = None

def main():
    if st.session_state['logged_in']:
        if st.session_state['role'] == 'admin':
            admin.app()
        elif st.session_state['role'] == 'user':
            user.app()
    else:
        login.app()

if __name__ == "__main__":
    main()
