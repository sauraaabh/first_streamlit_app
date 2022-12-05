import streamlit
streamlit.title(" My Parents New Healthy Diner")
streamlit.header(" Breakfast Menu")
streamlit.text(" Poha ")
streamlit.text(" Idli")
streamlit.text("🥑 Avocado on the toast")
streamlit.text("🐔 Egg omellette ")
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥣 Kale, Spinach & Rocket Smoothie')
streamlit.text('🍞 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')   


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# New section to display api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())
# below line flattens json i.e json_normalize()
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# shows dataframe as a table. 
streamlit.dataframe(fruityvice_normalized)
import snowflake.connector;
