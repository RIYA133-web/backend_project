
import streamlit as st
import requests

API_URL = "https://backend-project-15sa.onrender.com"

st.set_page_config(
    page_title="User Management",
    page_icon="👥",
    layout="wide"
)

st.title("👥 User Management Dashboard")
st.caption("Manage your users easily")

tab1, tab2, tab3, tab4 = st.tabs(
    ["👤 Users", "➕ Add User", "✏️ Edit User", "🗑️ Delete User"]
)

# -------------------- USERS LIST --------------------
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
        st.error("Could not connect to the API. Please try again.")


# -------------------- ADD USER --------------------
with tab2:
    st.subheader("Add a New User")

    with st.form("add_user_form"):
        name = st.text_input("Full Name")
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
                            error = response.json().get(
                                "error", "Could not create user."
                            )
                        except ValueError:
                            error = "Could not create user."
                        st.error(error)

                except requests.RequestException:
                    st.error("Could not connect to the API.")


# -------------------- EDIT USER --------------------
with tab3:
    st.subheader("Edit an Existing User")

    try:
        response = requests.get(f"{API_URL}/users", timeout=30)

        if response.ok:
            users = response.json()

            if not users:
                st.info("No users available to edit.")
            else:
                user_options = {
                    f"{user['name']} (ID: {user['id']})": user
                    for user in users
                }

                selected_label = st.selectbox(
                    "Select a user",
                    list(user_options.keys()),
                    key="edit_user_select"
                )
                selected_user = user_options[selected_label]

                with st.form("edit_user_form"):
                    new_name = st.text_input(
                        "Name",
                        value=selected_user["name"]
                    )
                    new_age = st.number_input(
                        "Age",
                        min_value=0,
                        max_value=120,
                        value=int(selected_user["age"]),
                        step=1
                    )

                    update_clicked = st.form_submit_button("Save Changes")

                    if update_clicked:
                        if not new_name.strip():
                            st.warning("Please enter a name.")
                        else:
                            update_response = requests.put(
                                f"{API_URL}/users/{selected_user['id']}",
                                json={
                                    "name": new_name.strip(),
                                    "age": int(new_age)
                                },
                                timeout=30
                            )

                            if update_response.ok:
                                st.success("User updated successfully!")
                                st.rerun()
                            else:
                                try:
                                    error = update_response.json().get(
                                        "error", "Could not update user."
                                    )
                                except ValueError:
                                    error = "Could not update user."
                                st.error(error)
        else:
            st.error("Could not load users for editing.")

    except requests.RequestException:
        st.error("Could not connect to the API.")


# -------------------- DELETE USER --------------------
with tab4:
    st.subheader("Delete a User")

    try:
        response = requests.get(f"{API_URL}/users", timeout=30)

        if response.ok:
            users = response.json()

            if not users:
                st.info("No users available to delete.")
            else:
                user_options = {
                    f"{user['name']} (ID: {user['id']})": user
                    for user in users
                }

                selected_label = st.selectbox(
                    "Select a user to delete",
                    list(user_options.keys()),
                    key="delete_user_select"
                )

                selected_user = user_options[selected_label]

                st.warning(
                    f"You are about to delete {selected_user['name']} "
                    f"(ID: {selected_user['id']})."
                )

                confirm = st.checkbox(
                    "I confirm that I want to delete this user.",
                    key="confirm_delete_user"
                )

                if st.button("🗑️ Delete User", type="primary"):
                    if not confirm:
                        st.warning("Please confirm before deleting.")
                    else:
                        delete_response = requests.delete(
                            f"{API_URL}/users/{selected_user['id']}",
                            timeout=30
                        )

                        if delete_response.ok:
                            st.success("User deleted successfully!")
                            st.rerun()
                        else:
                            try:
                                error = delete_response.json().get(
                                    "error", "Could not delete user."
                                )
                            except ValueError:
                                error = "Could not delete user."
                            st.error(error)
        else:
            st.error("Could not load users for deletion.")

    except requests.RequestException:
        st.error("Could not connect to the API.")
