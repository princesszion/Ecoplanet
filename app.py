import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="data.xlsx",
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
    "Select the Farm Name:",
    options=df["Farm"].unique(),
    default=df["Farm"].unique()
)

activity = st.sidebar.multiselect(
    "Select the Activity:",
    options=df["Activity"].unique(),
    default=df["Activity"].unique(),
)


df_selection = df.query(
    "Farm == @farm & Activity ==@activity"
)

# ---- MAINPAGE ----
st.title(":bar_chart:  Dashboard")
st.markdown("##")

# TOP KPI's
total_cost = int(df_selection["Total"].sum())
average_md = round(df_selection["Avg. Md/Ha"].mean(), 1)
star_rating = ":star:" * int(round(average_md, 0))
average_cost_ha = round(df_selection["Cost per Ha (USD)"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Cost:")
    st.subheader(f"US $ {total_cost:,}")
with middle_column:
    st.subheader("Average MD:")
    st.subheader(f"{average_md} {star_rating}")
with right_column:
    st.subheader("Average Cost/ha:")
    st.subheader(f"US $ {average_cost_ha}")

st.markdown("""---""")

# SALES BY PRODUCT LINE [BAR CHART]
cost_activity = (
    df_selection.groupby(by=["Activity"]).sum()[["Total"]].sort_values(by="Total")
)
fig_cost_activity = px.bar(
    cost_activity,
    x="Total",
    y=cost_activity.index,
    orientation="h",
    title="<b>Cost/Activity</b>",
    color_discrete_sequence=["#0083B8"] * len(cost_activity),
    template="plotly_white",
)
fig_cost_activity.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# SALES BY HOUR [BAR CHART]
cost_md = df_selection.groupby(by=["Activity"]).sum()[["Total"]]
fig_cost_md = px.bar(
    cost_md,
    x=cost_md.index,
    y="Total",
    title="<b>Cost /Md</b>",
    color_discrete_sequence=["#0083B8"] * len(cost_md),
    template="plotly_white",
)
fig_cost_md.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_cost_md, use_container_width=True)
right_column.plotly_chart(fig_cost_activity, use_container_width=True)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)