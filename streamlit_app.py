import streamlit as st

products = [
    {"id": 1, "name": "Boots", "price": 10.0, "category": "Footwear"},
    {"id": 2, "name": "Cap", "price": 20.0, "category": "Clothing"},
    {"id": 3, "name": "Shirt", "price": 30.0, "category": "Clothing"},
    {"id": 4, "name": "Jacket", "price": 40.0, "category": "Clothing"},
    {"id": 5, "name": "Socks", "price": 50.0, "category": "Footwear"},
    {"id": 6, "name": "Sweater", "price": 60.0, "category": "Clothing"},
    {"id": 7, "name": "Gloves", "price": 70.0, "category": "Clothing"},
    {"id": 8, "name": "Scarf", "price": 80.0, "category": "Clothing"},
    {"id": 9, "name": "Belt", "price": 90.0, "category": "Clothing"},
    {"id": 10, "name": "Shoes", "price": 100.0, "category": "Footwear"},
    {"id": 11, "name": "Milk", "price": 10.0, "category": "Grocery"},
    {"id": 12, "name": "Bread", "price": 20.0, "category": "Grocery"},
    {"id": 13, "name": "Eggs", "price": 30.0, "category": "Grocery"},
    {"id": 14, "name": "Butter", "price": 40.0, "category": "Grocery"},
    
]

for product in products:
    if 'checked_id_' + str(product['id']) not in st.session_state:
        st.session_state['checked_id_' + str(product['id'])] = False

@st.cache_resource
def update_cart(product_id, value):
    st.session_state['checked_id_' + str(product_id)] = value

users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
]

admins = [
    {"username": "admin1", "password": "password1"},
    {"username": "admin2", "password": "password2"},
]

orders = []
order_items = []
sessions = []


carts = []



st.title("Welcome to the Demo Marketplace")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.header("User Login")

    # write streamlit form
    user_login_form = st.form(key="user_login_form")
    username = user_login_form.text_input("Username")
    password = user_login_form.text_input("Password", type="password")

    # remove this later
    username = 'user1'
    password = 'password1'

    user_submit_button = user_login_form.form_submit_button(
        label="Login"
    )
    st.session_state['logged_in'] = True


if user_submit_button and st.session_state['logged_in']:
    for user in users:
        if user["username"] == username and user["password"] == password:
            # delete login form and all its elements

            st.success("You have successfully logged in.")
            st.header("Products")
            cart_items = []
            for product in products:
                #with st.form(key=("form" + str(product["id"]))):
                st.write(f'name : {product["name"]}')#, f'price : {product["price"]}', f'category : {product["category"]}')
                add_checkbox = st.checkbox(label="Add to Cart", key=("checkbox" + str(product["id"])),
                                           value=st.session_state['checked_id_' + str(product['id'])],
                                           on_change=update_cart, 
                                           args=(product["id"], not st.session_state['checked_id_' + str(product['id'])]))
                if st.session_state['checked_id_' + str(product['id'])]:
                    cart_items.append(product)
                    # st.divider()
                    # if added:
                    #     cart_items.append(product)

            with st.expander("View Cart"):

                if len(cart_items) > 0:
                    st.header("Cart")
                    for item in cart_items:
                        st.write(item["name"], item["price"])
                    with st.form(key="checkout_form"):
                        st.write("Total: ", sum([item["price"] for item in cart_items]))
                        checkout_button = st.form_submit_button(label="Checkout")
                        if checkout_button:
                            orders.append({"user": user, "items": cart_items})
                            st.success("You have successfully checked out.")
                            break
                else:
                    st.warning("Your cart is empty.")
                    break
            break

        else:
            st.error("Invalid username or password")

# write streamlit header


