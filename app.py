
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from datetime import date

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Personal Expense Tracker")
st.write("Track your expenses, manage your budget, and understand your spending habits.")

# ---------------- DATABASE CONNECTION ----------------

conn = sqlite3.connect("expenses.db", check_same_thread=False)

conn.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    expense_date TEXT NOT NULL,
    payment_method TEXT NOT NULL
)
""")

conn.commit()

# ---------------- DATABASE HELPER ----------------

def get_expenses():
    return pd.read_sql_query(
        "SELECT * FROM expenses ORDER BY expense_date DESC",
        conn
    )


# ---------------- SIDEBAR ----------------

st.sidebar.title("💰 Expense Tracker")

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Dashboard",
        "Add Expense",
        "View Expenses",
        "Update Expense",
        "Delete Expense",
        "Analytics"
    ]
)

# ---------------- CATEGORIES ----------------

categories = [
    "Food",
    "Shopping",
    "Transportation",
    "Entertainment",
    "Bills",
    "Healthcare",
    "Education",
    "Travel",
    "Other"
]

payment_methods = [
    "Cash",
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking"
]


# ---------------- DASHBOARD ----------------

if menu == "Dashboard":

    st.header("📊 Expense Dashboard")

    df = get_expenses()

    if not df.empty:

        today = date.today()
        current_month = today.strftime("%Y-%m")

        monthly_df = df[
            df["expense_date"].str.startswith(current_month)
        ]

        total_expenses = df["amount"].sum()
        monthly_expenses = monthly_df["amount"].sum()
        total_transactions = len(df)

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Expenses",
            f"₹{total_expenses:,.2f}"
        )

        col2.metric(
            "This Month",
            f"₹{monthly_expenses:,.2f}"
        )

        col3.metric(
            "Total Transactions",
            total_transactions
        )

        st.divider()

        st.subheader("Recent Transactions")

        st.dataframe(
            df.head(10),
            use_container_width=True,
            hide_index=True
        )

        st.subheader("Spending by Category")

        category_data = df.groupby(
            "category"
        )["amount"].sum().reset_index()

        fig = px.pie(
            category_data,
            names="category",
            values="amount",
            hole=0.4,
            title="Expense Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    else:

        st.info("No expenses recorded yet. Start by adding your first expense.")


# ---------------- ADD EXPENSE ----------------

elif menu == "Add Expense":

    st.header("➕ Add New Expense")

    with st.form("add_expense_form"):

        amount = st.number_input(
            "Expense Amount (₹)",
            min_value=0.0,
            step=100.0
        )

        category = st.selectbox(
            "Expense Category",
            categories
        )

        description = st.text_input(
            "Description",
            placeholder="Example: Grocery shopping"
        )

        expense_date = st.date_input(
            "Expense Date",
            value=date.today()
        )

        payment_method = st.selectbox(
            "Payment Method",
            payment_methods
        )

        submit = st.form_submit_button("Add Expense")

        if submit:

            if amount <= 0:
                st.error("Amount must be greater than zero.")

            else:

                conn.execute("""
                    INSERT INTO expenses
                    (amount, category, description,
                     expense_date, payment_method)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    amount,
                    category,
                    description.strip(),
                    expense_date.isoformat(),
                    payment_method
                ))

                conn.commit()

                st.success("Expense added successfully!")

                st.rerun()


# ---------------- VIEW EXPENSES ----------------

elif menu == "View Expenses":

    st.header("📋 All Expense Records")

    df = get_expenses()

    if not df.empty:

        search = st.text_input(
            "Search by description"
        )

        selected_category = st.selectbox(
            "Filter by Category",
            ["All"] + categories
        )

        filtered_df = df.copy()

        if search:
            filtered_df = filtered_df[
                filtered_df["description"].str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        if selected_category != "All":
            filtered_df = filtered_df[
                filtered_df["category"] == selected_category
            ]

        st.dataframe(
            filtered_df,
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            "⬇️ Download Expense Report",
            filtered_df.to_csv(index=False).encode("utf-8"),
            file_name="expense_report.csv",
            mime="text/csv"
        )

    else:

        st.info("No expense records available.")


# ---------------- UPDATE EXPENSE ----------------

elif menu == "Update Expense":

    st.header("✏️ Update Expense Details")

    df = get_expenses()

    if not df.empty:

        expense_id = st.selectbox(
            "Select Expense ID",
            df["expense_id"].tolist()
        )

        expense = df[
            df["expense_id"] == expense_id
        ].iloc[0]

        with st.form("update_expense_form"):

            amount = st.number_input(
                "Amount (₹)",
                min_value=0.0,
                value=float(expense["amount"]),
                step=100.0
            )

            category = st.selectbox(
                "Category",
                categories,
                index=categories.index(expense["category"])
            )

            description = st.text_input(
                "Description",
                value=expense["description"] or ""
            )

            expense_date = st.date_input(
                "Expense Date",
                value=date.fromisoformat(expense["expense_date"])
            )

            payment_method = st.selectbox(
                "Payment Method",
                payment_methods,
                index=payment_methods.index(
                    expense["payment_method"]
                )
            )

            update = st.form_submit_button(
                "Update Expense"
            )

            if update:

                if amount <= 0:
                    st.error("Amount must be greater than zero.")

                else:

                    conn.execute("""
                        UPDATE expenses
                        SET amount=?, category=?, description=?,
                            expense_date=?, payment_method=?
                        WHERE expense_id=?
                    """, (
                        amount,
                        category,
                        description.strip(),
                        expense_date.isoformat(),
                        payment_method,
                        expense_id
                    ))

                    conn.commit()

                    st.success("Expense updated successfully!")

                    st.rerun()

    else:

        st.info("No expenses available to update.")


# ---------------- DELETE EXPENSE ----------------

elif menu == "Delete Expense":

    st.header("🗑️ Delete Expense Record")

    df = get_expenses()

    if not df.empty:

        expense_id = st.selectbox(
            "Select Expense ID",
            df["expense_id"].tolist()
        )

        expense = df[
            df["expense_id"] == expense_id
        ].iloc[0]

        st.write("Amount:", f"₹{expense['amount']:,.2f}")
        st.write("Category:", expense["category"])
        st.write("Description:", expense["description"])

        confirm = st.checkbox(
            "I confirm that I want to delete this expense."
        )

        if st.button("Delete Expense", type="primary"):

            if confirm:

                conn.execute(
                    "DELETE FROM expenses WHERE expense_id=?",
                    (expense_id,)
                )

                conn.commit()

                st.success("Expense deleted successfully!")

                st.rerun()

            else:

                st.warning("Please confirm before deleting.")

    else:

        st.info("No expense records available.")


# ---------------- ANALYTICS ----------------

elif menu == "Analytics":

    st.header("📈 Expense Analytics")

    df = get_expenses()

    if not df.empty:

        # Category-wise spending

        st.subheader("Category-wise Expense Analysis")

        category_data = df.groupby(
            "category"
        )["amount"].sum().reset_index()

        fig1 = px.bar(
            category_data,
            x="category",
            y="amount",
            color="category",
            title="Expenses by Category",
            labels={
                "category": "Category",
                "amount": "Amount (₹)"
            }
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

        # Monthly spending

        st.subheader("Monthly Expense Analysis")

        df["month"] = pd.to_datetime(
            df["expense_date"]
        ).dt.to_period("M").astype(str)

        monthly_data = df.groupby(
            "month"
        )["amount"].sum().reset_index()

        fig2 = px.line(
            monthly_data,
            x="month",
            y="amount",
            markers=True,
            title="Monthly Spending Trend",
            labels={
                "month": "Month",
                "amount": "Amount (₹)"
            }
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        # Payment method analysis

        st.subheader("Payment Method Analysis")

        payment_data = df.groupby(
            "payment_method"
        )["amount"].sum().reset_index()

        fig3 = px.pie(
            payment_data,
            names="payment_method",
            values="amount",
            title="Expenses by Payment Method"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    else:

        st.info("Add expenses to view analytics.")


# ---------------- FOOTER ----------------

st.sidebar.divider()

st.sidebar.caption(
    "Personal Expense Tracker | Built with Python & Streamlit"
)

conn.close()
