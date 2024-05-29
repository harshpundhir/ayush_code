import streamlit as st
import json

def app():

    st.title("Welcome to the Demo User")
    products = json.load(open("products.json", "r"))
    orders = []

    for product in products:
        if 'checked_id_' + str(product['id']) not in st.session_state:
            st.session_state['checked_id_' + str(product['id'])] = False

    
    cart_items = []
    #with st.form(key="products_form"):
    for product in products:     
        st.write(f'Product : {product["name"]}', f'Price : {product["price"]}', f'Category : {product["category"]}')
        add_checkbox = st.checkbox(label="Add to Cart", key=("checkbox" + str(product["id"])))
        st.divider()
                        
        if add_checkbox:
            st.session_state['checked_id_' + str(product['id'])] = True
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
                tot = sum([item["price"] for item in cart_items])        
                st.write("Total: ", tot)
                checkout_button = st.form_submit_button(label="Checkout")
                payments = st.radio("Payment Method", ("Credit Card", "Debit Card", "COD", "UPI", "Net Banking"))
                if checkout_button and payments:
                    st.write(f"You selected {payments} as your payment method.")
                    orders.append(cart_items)
                    st.success(f"You will be shortly redirected to the portal for Unified Payment Interface to make a payment of Rs. {tot}")
        else:
            st.warning("Your cart is empty.")
                    
