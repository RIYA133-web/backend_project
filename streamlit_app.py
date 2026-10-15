
import streamlit as st
import requests

API_URL = "https://backend-project-15sa.onrender.com"

st.set_page_config(
    page_title="User Management",
    page_icon="👥",
    layout="wide"
)

st.title("👥 User Management Dashboard")
st.caption("Manage users easily with your Flask API")

tab1, tab2 = st.tabs(["👤 Users", "➕ Add User"])

with tab1:
    st.subheader("All Users")

    if st.button("🔄 Refresh Users"):
        st.rerun()

    try:
        response = requests.get(f"{API_URL}/users", timeout=30)

        if response.ok:
            users = response.json()

            if users:
                st.dataframe(users, use_container_width=True)
            else:
                st.info("No users found. Add your first user!")
        else:
            st.error(f"Could not load users: {response.status_code}")

    except requests.RequestException:
        st.error("API se connect nahi ho pa raha. Thodi der baad try karo.")

with tab2:
    st.subheader("Add a New User")

    with st.form("add_user_form"):
        name = st.text_input("Full Name", placeholder="Enter user's name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)

        submitted = st.form_submit_button("Create User")

        if submitted:
            if not name.strip():
                st.warning("Please enter a name.")
            else:
                try:
                    response = requests.post(
                        f"{API_URL}/users",
                        json={"name": name.strip(), "age": int(age)},
                        timeout=30
                    )

                    if response.ok:
                        st.success("User created successfully!")
                        st.json(response.json())
                    else:
                        try:
                            error = response.json().get("error", "Could not create user.")
                        except ValueError:
                            error = "Could not create user."
                        st.error(error)

                except requests.RequestException:
                    st.error("API se connect nahi ho pa raha. Thodi der baad try karo.")
