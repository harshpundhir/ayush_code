import streamlit as st
import json
import pandas as pd
import time

def app():
    st.title("Welcome to the Admin Marketplace")
    products = json.load(open("products.json", "r"))
    if 'products' not in st.session_state:
        st.session_state['products'] = products


    def view_data(products):
        products_df = pd.DataFrame(products, index = [i for i in range(1, len(products)+1)])
        st.write("View Data")
        st.dataframe(pd.DataFrame(products_df))
    
    
    with st.expander("View Products"):
        view_data(st.session_state['products'])

    with st.expander("Add Product"):
        add_product_form = st.form(key="add_product_form", clear_on_submit=True)
        id = add_product_form.number_input("ID",value=None, step=1)
        name = add_product_form.text_input("Name")
        price = add_product_form.number_input("Price", value=None)
        category = add_product_form.text_input("Category")
        add_product_button = add_product_form.form_submit_button(label="Add Product")
        if add_product_button: 
            if id not in [product["id"] for product in st.session_state['products']] and id != None:
                st.session_state['products'].append({"id": id, "name": name, "price": price, "category": category})
                st.toast("Yay! Product added successfully.")
                time.sleep(1.5)
                st.rerun()
            else:
                st.toast(" !!! Product not added. Please check if the ID is unique and not empty.")
    
    with st.expander("Delete Product"):
        delete_product_form = st.form(key="delete_product_form", clear_on_submit=True)
        id = delete_product_form.number_input("ID", value=None, step=1)
        delete_product_button = delete_product_form.form_submit_button(label="Delete Product")
        if delete_product_button:
            if id in [product["id"] for product in st.session_state['products']]:
                st.toast("Product found.")
                for product in st.session_state['products']:
                    if product["id"] == id:
                        st.session_state['products'].remove(product)
                        st.toast("Product deleted successfully.")
                        time.sleep(1.5)
                        st.rerun()        
            else:
                st.toast("Product not found.")
    
    with st.expander("Update Product"):
        # name2 = None
        # price2 = None
        # category2 = None
        update = False
        update_product_form = st.form(key="update_product_form", clear_on_submit=True)
        id = update_product_form.number_input("ID",value=None, step=1)
        if id in [product["id"] for product in st.session_state['products']]:
            st.toast(f"Product with id {id} found.")
            found = True

            for product in st.session_state['products']:
                if product["id"] == id:
                    st.write(f"Name check")
                    name2 = update_product_form.text_input("Name", value=product["name"])
                    price2 = update_product_form.number_input("Price", value=product["price"])
                    category2 = update_product_form.text_input("Category", value=product["category"])
                    if name2 != product["name"] or price2 != product["price"] or category2 != product["category"]:
                        update = True
                    break
        
        else:
            found = False
        update_product_button = update_product_form.form_submit_button(label="Update Product")
        if update_product_button and update:
            if found:
                product["name"] = name2
                product["price"] = price2
                product["category"] = category2
                st.toast("Product updated successfully.")
                time.sleep(1.5)
                st.rerun()
            else:
                st.toast("Product not found.")
                time.sleep(1.5)
                st.rerun()
    
    if st.button("Save Changes"):
        with open("products.json", "w") as f:
            json.dump(st.session_state['products'], f)
        st.success("Changes saved successfully.")
        time.sleep(1.5)
        st.rerun()
        
        
        
            