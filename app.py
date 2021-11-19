import streamlit as st
import requests
import datetime

st.markdown('''
# Streamlit-based Frontend for my NY Taxifare API
## Simple package exploring what is possible using the streamlit package
*by [Malte Berneaud](https://mberneaud.github.io/)*
''')


# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count

## User Inputs
date = st.date_input("Date of trip")
time = st.time_input("Time of trip")
pickup_longitude = st.text_input("Pickup Longitude", 40.7614327)
pickup_latitude = st.text_input("Pickup Latitude", -73.9798156)
dropoff_longitude = pickup_latitude = st.text_input("Dropoff Longitude",
                                                    40.6331166)
dropoff_latitude = st.text_input("Dropoff Latitude", -73.8874078)
passenger_count = st.slider('How many passengers?', 1, 6, 2)

# Calculations
pickup_datetime = datetime.datetime.combine(date, time)

# Implementing a function that handles empty lat and lons

def string_to_float(string_number):
    if string_number:
        return float(string_number)
    return(0.0)



# 2. Let's build a dictionary containing the parameters for our API...

params = dict(
    pickup_datetime = str(pickup_datetime),
    pickup_longitude = string_to_float(pickup_longitude),
    pickup_latitude = string_to_float(pickup_latitude),
    dropoff_longitude = string_to_float(dropoff_longitude),
    dropoff_latitude = string_to_float(dropoff_latitude),
    passenger_count = int(passenger_count)
)

if 0 in params.values():
    st.write('''
    # Please enter values for all fields to get a prediction!
    ''')



# Calling API

"# Predicticted fare price"

url = 'https://taxifare-api-vrzsllpx4a-ew.a.run.app/predict'

response = requests.get(url, params=params)
prediction = response.json().get("prediction", False)

if prediction:
    st.markdown(f"### Your predicted fare is {prediction:.2f} USD")
else:
    st.markdown("### Could not generate a prediction")

'''
## Testing area
'''
st.write(response.json().get("prediction"))


# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
