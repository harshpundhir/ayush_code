import streamlit as st
import json

def app():
    #products = json.load(open("products.json", "r"))
    #st.session_state['products'] = products

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    st.title("Welcome to the Demo Marketplace")
    st.header("Login Page")

    users = [
        {"username": "user1", "password": "password1"},
        {"username": "user2", "password": "password2"},
    ]

    admins = [
    {"username": "admin1", "password": "password1"},
    {"username": "admin2", "password": "password2"},
    ]

    user_login_form = st.form(key="user_login_form")
    username = user_login_form.text_input("Username")
    password = user_login_form.text_input("Password", type="password")


    

    admin = st.checkbox("Admin Login")
    with st.expander("Login details"):

            st.write("1 sample admin and user login detail:")
            st.divider()
            st.write("Admin Login")
            st.write("Username: admin1")
            st.write("Password: password1")
            st.divider()
            st.write("User Login")
            st.write("Username: user1")
            st.write("Password: password1")


    user_submit_button = user_login_form.form_submit_button(label="Login")


    if user_submit_button:
        if admin:
            for admin in admins:
                if admin["username"] == username and admin["password"] == password:
                    st.success("You have successfully logged in as admin.")
                    st.session_state['logged_in'] = True
                    st.session_state['role'] = 'admin'
                    st.experimental_rerun()
                    break
            else:
                st.error("Invalid admin username or password")
        else:
            for user in users:
                if user["username"] == username and user["password"] == password:
                    st.success("You have successfully logged in.")
                    st.session_state['logged_in'] = True
                    st.session_state['role'] = 'user'
                    st.experimental_rerun()
                    
                    break
                else:
                    st.error("Invalid username or password")


