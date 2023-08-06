import streamlit as st
# st.cache_resource()
st.set_page_config(
        layout = 'wide',
        page_title = 'EDA Shopping',
        page_icon= '📊')
# ______________________________________________________________________________________________________________________________________________________________________________________________________
# Import Libraries
import streamlit as st
import plotly.express as px
import pandas as pd

# with st.container():
About = st.sidebar.checkbox(":blue[Show About EDA & Application Info]")
Planning = st.sidebar.checkbox(":orange[Show About Application Planning]")
About_me = st.sidebar.checkbox(":green[Show About me]")
if About:
    st.sidebar.header(":blue[About EDA & Application Info]")
    st.sidebar.write("""
    * In this EDA Project we have 4 tabels [Customers , Orders , Products , Sales].
    * Merged them into one DataFrame called (Data).👍
    * Did some data modifications on (*data type like date (date fromat , year,month,year*)👍
    * Sepreated the Data and charts to 3 tabs :👍
        * Data Information 💾
        * Categorical 📊
        * Numerical 📈
    * :red[So let us see the insights 👀]
    """)
# ______________________________________________________________________________________________________________________________________________________________________________________________________
if Planning :
    st.sidebar.header(":orange[Application Planning]")
    st.sidebar.write("""
    - Application Planning :
    - 1) Side Bar:
        - About EDA & Application Info
        - Application Planning
        - About me
    - 2) 3 tabs
        - 1) Tab no 1 = Data Information (Describe , info)
        - 2) Tab no 1 = Categorical visuals :
            (Histogram, Bar Plot, Scatter Plot)
        - 3) Tab no 3 = Numerical Visuals
            (Bar plot, Line Plot per mont, Heatmap)
    """)
# ______________________________________________________________________________________________________________________________________________________________________________________________________
if About_me :
    st.sidebar.header(":green[About me]")
    st.sidebar.write("""
    - Osama SAAD
    - Student Data Scaience & Machine Learning @ Epsilon AI
    - Infor ERP Consaltant @ Ibnsina Pharma
    - LinkedIn: 
        https://www.linkedin.com/in/ossama-ahmed-saad-525785b2
    - Github : 
        https://github.com/OsamaSamnudi
    """)
# "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
# Make 3 Tabs (Data Information 💾 , Categorical 📊 , Numerical 📈)

Data_Info , Categorical , Numerical = st.tabs (['Data Information 💾' , 'Categorical 📊' , 'Numerical 📈'])
df = pd.read_csv('data.csv' , index_col=0)

with Data_Info:
    # st.cache_resource()
    with st.container():
        st.header("Data Describe")
        DI_select = st.selectbox('Please select:',['Please select','All Columns' , 'Categorical' , 'Numerical' , 'custom'])
        if DI_select == 'Please select':
            st.write(":red[Please Choise a column from the list:]")
        elif DI_select == 'All Columns':
            st.write(":violet[Describe Table (All Columns):]")
            st.dataframe(data=df.describe().T , use_container_width=True)
        elif DI_select == 'Numerical':
            st.write(":orange[*Describe Table (All Numerical):*]")
            st.dataframe(data=df.describe(exclude = ['object']).T , use_container_width=True)
        elif DI_select == 'Categorical':
            st.write(":orange[*Describe Table (All Categorical):*]")
            st.dataframe(data=df.describe(include = ['object']).T , use_container_width=True)
        else:
            columns = st.selectbox('Please select:',df.columns.tolist())
            st.write(":orange[*Describe Table for :*]",columns)
            st.dataframe(data=df[columns].describe())

    with st.container():
        pd.options.display.float_format = '{:,.0f}'.format
        st.header("Data Information")
        DataInfo = st.checkbox("Show Data Info")
        if DataInfo :
            st.dataframe(data=df.dtypes.reset_index(name='Type'), hide_index=True)
# "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
with Categorical:
    with st.container():
        # st.cache_resource()
        st.header('Categorical Describtive Statistics (histogram)')
        cat_columns = ['Please select','age','city','colour','gender','name_day_delivery','name_day_order','product_name','product_type', 'size', 'state']
        col1_select = st.selectbox("Categorical Cloumns List (histogram)" , cat_columns)
        col1, col2, col3 = st.columns([7,1,7])
        with col1 :
            st.subheader('Histogram in month_order')
            if col1_select == 'Please select':
                st.write(":red[Please Choise a column from the list:]")
            else:
                st.write(f"Histogram for ({col1_select}) in month_order")
                fig =px.histogram(df, x = col1_select , y = 'month_order' ,color_discrete_sequence=px.colors.qualitative.Bold, text_auto = True)
                col1.plotly_chart(fig,use_container_width=True)
        with col3 :
            st.subheader('Histogram in month_delivery')
            if col1_select == 'Please select':
                st.write(":red[Please Choise a column from the list:]")
            else:
                st.write(f"Histogram for ({col1_select}) in month_delivery")
                fig =px.histogram(df, x = col1_select , y = 'month_delivery' ,color_discrete_sequence=px.colors.qualitative.Plotly_r, text_auto = True)
                col3.plotly_chart(fig,use_container_width=True)
    with st.container():
        # st.cache_resource()
        st.header('Categorical Describtive Statistics (bar Plot)')
        x = st.selectbox('Select x :' , cat_columns)
        y = st.selectbox('Select y :' , cat_columns)
        col4, col5, col6 = st.columns([7,1,7])
        with col4:
            st.subheader('bar Plot/Count')
            if x == 'Please select' or y == 'Please select' :
                st.write(":red[Please Choise a column from the list:]")
            else:
                if x == y:
                    st.write(":red[Please Choise Diffrent Columns in X & Y]")
                else:
                    msk_1 = df.groupby(x)[[y]].count().sort_values(by=[x],ascending = False).reset_index()
                    fig_col4 = px.bar(msk_1, x = x, y = y , color = x , text_auto=True)
                    col4.plotly_chart(fig_col4,use_container_width=True)
        with col6:
            st.subheader('bar Plot/sum of total_price')
            if x == 'Please select' or y == 'Please select' :
                st.write(":red[Please Choise a column from the list:]")
            else:
                if x == y:
                    st.write(":red[Please Choise Diffrent Columns in X & Y]")
                else:
                    msk_2 = df.groupby([x , y])[['total_price']].sum().sort_values(by=[x],ascending = False).reset_index()
                    fig_col6 = px.bar(msk_2 , x = x, y = y , color = x , text_auto=True)
                    col6.plotly_chart(fig_col6 , use_container_width=True)
# "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
with Numerical:
    with st.container():
        st.header('Numerical Describtive Statistics')
        Numerical_lst = ['Please select','age','colour','gender','name_day_delivery','name_day_order','product_name','product_type', 'size', 'state']
        Numerical_select = st.selectbox("Select One" ,Numerical_lst )
        col1, col2, col3 = st.columns([7,1,7])
        with col1 :
            st.subheader('Bar Plot in Total Price (Mean)')
            if Numerical_select == 'Please select':
                st.write(":red[Please Choise a column from the list:]")
            else:
                st.write(f"bar plot for ({Numerical_select}) in total_price (mean)")
                msk = df.groupby([Numerical_select])[['total_price']].mean().sort_values(by=Numerical_select,ascending = False).reset_index()
                fig = px.bar(msk , x = Numerical_select , y= 'total_price' , color = Numerical_select , text_auto=True)
                col1.plotly_chart(fig,use_container_width=True)

        with col3 :
            st.subheader('Bar Plot in Total Price (sum)')
            if Numerical_select == 'Please select':
                st.write(":red[Please Choise a column from the list:]")
            else:
                st.write(f"bar plot for ({Numerical_select}) in total_price (sum)")
                msk = df.groupby([Numerical_select])[['total_price']].sum().sort_values(by=Numerical_select,ascending = False).reset_index()
                fig = px.bar(msk , x = Numerical_select , y= 'total_price' , color = Numerical_select , text_auto=True)
                col3.plotly_chart(fig,use_container_width=True)
    with st.container():
        st.header('Numerical Describtive Statistics (Line per year)')
        Line_lst = ['Please select','quantity_x' , 'quantity_y' , 'payment' , 'total_price']
        Line_select = st.selectbox("Select One" , Line_lst)
        st.subheader('Line per year')
        if Line_select == 'Please select':
            st.write(":red[Please Choise a column from the list:]")
        else:
            st.write(f"Line over month for ({Line_select})")
            msk_1 = df.groupby('month_order')[[Line_select]].sum().sort_values(by='month_order',ascending = True).reset_index()
            fig_1 = px.line(msk_1 , x = 'month_order' , y = Line_select , color_discrete_sequence=px.colors.qualitative.Light24_r)
            st.plotly_chart(fig_1,use_container_width=True)

    with st.container():
            st.subheader('Heatmap Corrolation')
            corrolation = st.checkbox('Show Corrolations')
            if corrolation :
                cor = df[['customer_id','payment','age','zip_code','sales_id','product_id','price_per_unit','quantity_x','total_price','product_ID','price','quantity_y','month_order','day_order']].corr()
                fig_corr = px.imshow(cor , text_auto=True  , width= 1500 , height= 1500 , color_continuous_scale='rdylbu')
                st.plotly_chart(fig_corr,use_container_width=True,theme="streamlit")
