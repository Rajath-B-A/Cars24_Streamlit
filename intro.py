import  streamlit as st


st.title("Cars 24 second hand car price prediction")

st.header("My Calculator")

def square(x):
    return x**2

x = st.number_input("Enter the number")

if st.button("Submit"):
    res = square(x)
    st.write(res)

col1,col2,col3 = st.columns(3)

with col1:
   st.image("https://th.bing.com/th?id=OSK.HERO8XH_s8vodPa3VIQliZrFNwgvD9pQ3xob2vslQY6YQrM&w=312&h=200&c=15&rs=2&o=6&dpr=1.3&pid=SANGAM")

with col2:
   st.image("https://media.gettyimages.com/id/51524404/photo/eddy-hall-feeds-squirrels-in-st-james-park.jpg?b=1&s=594x594&w=0&k=20&c=s-xd06MiDUjrG_BG4xGq4NGcjHuari107vGHOoA3s3c=")

with col3:
   st.image("https://th.bing.com/th/id/OIP.R2XY2ALo4y8gs7kYAJPQzwHaEo?w=294&h=183&c=7&r=0&o=5&dpr=1.3&pid=1.7")


st.image("https://th.bing.com/th/id/OIP.9i-kp1V31HeVHc4n9YBqQQHaEo?w=304&h=189&c=7&r=0&o=5&dpr=1.3&pid=1.7")

from PIL import Image
image = Image.open("wallpaperflare.com_wallpaper.jpg")
st.image(image)

#st.image_open("https://th.bing.com/th/id/OIP.9i-kp1V31HeVHc4n9YBqQQHaEo?w=304&h=189&c=7&r=0&o=5&dpr=1.3&pid=1.7")