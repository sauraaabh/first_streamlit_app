import streamlit
streamlit.title(" My Parents New Healthy Diner")
streamlit.header(" Breakfast Menu")
streamlit.text(" Poha ")
streamlit.text(" Idli")
streamlit.text("🥑 Avacado on the toast")
streamlit.text("🐔 Egg omellette ")
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥣 Kale, Spinach & Rocket Smoothie')
streamlit.text('🍞 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')   

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# my_fruit_list = my_fruit_list.set_index('Fruit')
