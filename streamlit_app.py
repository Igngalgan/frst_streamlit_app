
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.header('Fruityvice fruit advice!')

try:
       fruit_choice = streamlit.text_input('What fuit would you like info about?')
       if not fruit_choice:
                streamlit.error('Please select something')
       else:
                    fruityvice_response = request.get("https://fruityvice.com/api/fruit/"+fruit_choice)
                    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
                    streamlit.dataframe(fruityvice_normalized)
                    
except URLError as e:
        streamlit.error()
        
        
    
    
    
streamlit.stop();

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list ")


my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


my_cur.execute("insert into fruit_load_list values ('from streamlit')");

