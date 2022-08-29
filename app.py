
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit


st.set_page_config(page_title="Data Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
#Load,and Visualize Data from the Ghana Dataset

@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="Data.xlsx",
        engine="openpyxl",
        sheet_name="Philipines",
        usecols="B:J",
        nrows=1000,
    )
    return df

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
farm2 = st.sidebar.multiselect(
    "Select the Farm:",
    options=df["Farm"].unique(),
    default=df["Farm"].unique()
)

activity2 = st.sidebar.multiselect(
    "Select the Activity :",
    options=df["Activity"].unique(),
    default=df["Activity"].unique(),
)


df_selection = df.query(
    "Farm == @farm2 & Activity ==@activity2"
)

# ---- MAINPAGE ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPI's
total_cost = int(df_selection["Total"].sum())
average_md = round(df_selection["Avg. Md/Ha"].mean(), 1)
star_rating = ":star:" * int(round(average_md, 0))
average_cost = round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Costs:")
    st.subheader(f"US $ {total_cost:,}")
with middle_column:
    st.subheader("Average MD:")
    st.subheader(f"{average_md} {star_rating}")
with right_column:
    st.subheader("Average Cost:")
    st.subheader(f"US $ {average_cost}")

st.markdown("""---""")

# COST PER ACTIVITY [BAR CHART]
cost_per_activity = (
    df_selection.groupby(by=["Activity"]).sum()[["Total"]].sort_values(by="Total")
)
fig_cost_per_activity = px.bar(
    cost_per_activity,
    x="Total",
    y=cost_per_activity.index,
    orientation="h",
    title="<b>Cost Per Activity</b>",
    color_discrete_sequence=["#0083B8"] * len(cost_per_activity),
    template="plotly_white",
)
fig_cost_per_activity.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# MD PER ACTIVITY [BAR CHART]
md_per_activity = df_selection.groupby(by=["Activity"]).sum()[["Avg. Md/Ha"]]
fig_md_per_activity = px.bar(
    md_per_activity,
    x=md_per_activity.index,
    y="Avg. Md/Ha",
    title="<b>MD/ACTIVITY</b>",
    color_discrete_sequence=["#0083B8"] * len(md_per_activity),
    template="plotly_white",
)
fig_md_per_activity.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_md_per_activity, use_container_width=True)
right_column.plotly_chart(fig_cost_per_activity, use_container_width=True)


#Load and visualize data from the Philipines Dataset
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="Data.xlsx",
        engine="openpyxl",
        sheet_name="Ghana",
        usecols="B:J",
        nrows=1000,
    )
    return df

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
farm = st.sidebar.multiselect(
    "Select the Farm:",
    options=df["Farm"].unique(),
    default=df["Farm"].unique()
)

activity = st.sidebar.multiselect(
    "Select the Activity :",
    options=df["Activity"].unique(),
    default=df["Activity"].unique(),
)


df_selection = df.query(
    "Farm == @farm & Activity ==@activity"
)

# ---- MAINPAGE ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPI's
total_cost = int(df_selection["Total"].sum())
average_md = round(df_selection["Avg. Md/Ha"].mean(), 1)
star_rating = ":star:" * int(round(average_md, 0))
average_cost = round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Costs:")
    st.subheader(f"US $ {total_cost:,}")
with middle_column:
    st.subheader("Average MD:")
    st.subheader(f"{average_md} {star_rating}")
with right_column:
    st.subheader("Average Cost:")
    st.subheader(f"US $ {average_cost}")

st.markdown("""---""")

# COST PER ACTIVITY [BAR CHART]
cost_per_activity = (
    df_selection.groupby(by=["Activity"]).sum()[["Total"]].sort_values(by="Total")
)
fig_cost_per_activity = px.bar(
    cost_per_activity,
    x="Total",
    y=cost_per_activity.index,
    orientation="h",
    title="<b>Cost Per Activity</b>",
    color_discrete_sequence=["#0083B8"] * len(cost_per_activity),
    template="plotly_white",
)
fig_cost_per_activity.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# MD PER ACTIVITY [BAR CHART]
md_per_activity = df_selection.groupby(by=["Activity"]).sum()[["Avg. Md/Ha"]]
fig_md_per_activity = px.bar(
    md_per_activity,
    x=md_per_activity.index,
    y="Avg. Md/Ha",
    title="<b>MD/ACTIVITY</b>",
    color_discrete_sequence=["#0083B8"] * len(md_per_activity),
    template="plotly_white",
)
fig_md_per_activity.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_md_per_activity, use_container_width=True)
right_column.plotly_chart(fig_cost_per_activity, use_container_width=True)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
