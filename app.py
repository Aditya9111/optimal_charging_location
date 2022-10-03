#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, render_template, request
import pandas as pd
import folium
from folium.plugins import HeatMap, HeatMapWithTime

# Create the application object
app = Flask(__name__)
# run server:app in terminal
first_df = pd.read_csv('csv/charging_station.csv')
malls_df = pd.read_csv('csv/shopping_malls.csv')
fuel_df = pd.read_csv('csv/gas_station.csv')
apartment_df = pd.read_csv('csv/apartment.csv')
parking_df = pd.read_csv('csv/parking.csv')
university_df = pd.read_csv('csv/university.csv')
final_df = pd.read_csv('csv/final.csv')


@app.route('/', methods=["GET", "POST"])
def home_page():
    start_coords = (12.9716, 77.5946)
    folium_map = folium.Map(
        location=start_coords
    )
    folium_map.save('templates/bangalore_map.html')

    # First_MAP
    first_map = folium.Map(location=[12.9716, 77.5946], tiles='stamentoner')
    first_df.latitude = first_df.latitude.astype(float)
    first_df.longitude = first_df.longitude.astype(float)
    heat_df = first_df[["latitude", "longitude"]]
    heat_data = list(zip(first_df.latitude, first_df.longitude))
    HeatMap(heat_data).add_to(first_map)
    sw = first_df[['latitude', 'longitude']].min().values.tolist()
    ne = first_df[['latitude', 'longitude']].max().values.tolist()
    first_map.fit_bounds([sw, ne])
    first_map.save('templates/charging_map.html')

    # shopping Mall
    for indice, row in malls_df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=row['Name'],
            icon=folium.Icon(color="red", icon="tag", prefix='fa')
        ).add_to(first_map)

    sw = malls_df[['latitude', 'longitude']].min().values.tolist()
    ne = malls_df[['latitude', 'longitude']].max().values.tolist()
    first_map.fit_bounds([sw, ne])
    first_map.save('templates/shopping_mall_map.html')

    # gas station
    for indice, row in fuel_df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=row['Name'],
            icon=folium.Icon(color="blue", icon="fire", prefix='fa')
        ).add_to(first_map)

    sw = fuel_df[['latitude', 'longitude']].min().values.tolist()
    ne = fuel_df[['latitude', 'longitude']].max().values.tolist()

    first_map.fit_bounds([sw, ne])
    first_map.save('templates/fuel_map.html')

    # Apartment

    for indice, row in apartment_df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=row['Name'],
            icon=folium.Icon(color="green", icon="home", prefix='fa')
        ).add_to(first_map)

    sw = apartment_df[['latitude', 'longitude']].min().values.tolist()
    ne = apartment_df[['latitude', 'longitude']].max().values.tolist()

    first_map.fit_bounds([sw, ne])
    first_map.save('templates/apartment_map.html')

    # Parking
    for indice, row in parking_df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=row['Name'],
            icon=folium.Icon(
                color="purple", icon="car", prefix='fa')
        ).add_to(first_map)

    sw = parking_df[['latitude', 'longitude']].min().values.tolist()
    ne = parking_df[['latitude', 'longitude']].max().values.tolist()

    first_map.fit_bounds([sw, ne])
    first_map.save('templates/parking_map.html')

    # University

    for indice, row in university_df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=row['Name'],
            icon=folium.Icon(color="black", icon="university", prefix='fa')
        ).add_to(first_map)

    sw = university_df[['latitude', 'longitude']].min().values.tolist()
    ne = university_df[['latitude', 'longitude']].max().values.tolist()

    first_map.fit_bounds([sw, ne])
    first_map.save('templates/university_map.html')

    # Final
    final = folium.Map(location=[12.9716, 77.5946], tiles='stamentoner')

    final_df.latitude = final_df.latitude.astype(float)
    final_df.longitude = final_df.longitude.astype(float)
    heat_df = final_df[["latitude", "longitude"]]
    heat_data = list(zip(final_df.latitude, final_df.longitude))
    HeatMap(heat_data).add_to(final)

    for indice, row in final_df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=row['Name'],
            icon=folium.Icon(color="green", icon="bolt", prefix='fa')
        ).add_to(final)

    sw = final_df[['latitude', 'longitude']].min().values.tolist()
    ne = final_df[['latitude', 'longitude']].max().values.tolist()

    final.fit_bounds([sw, ne])
    final.save('templates/result_map.html')

    return render_template('index.html')


@app.route('/bangalore_map')
def map():
    return render_template('bangalore_map.html')


@app.route('/charging_map')
def charging_map():
    return render_template('charging_map.html')


@app.route('/shopping_map')
def shopping_map():
    return render_template('shopping_mall_map.html')


@app.route('/fuel_map')
def fuel_map():
    return render_template('fuel_map.html')


@app.route('/parking_map')
def parking_map():
    return render_template('parking_map.html')


@app.route('/apartment_map')
def apartment_map():
    return render_template('apartment_map.html')


@app.route('/university_map')
def university_map():
    return render_template('university_map.html')


@app.route('/result_map')
def result_map():
    return render_template('result_map.html')


@app.route('/process', methods=["GET", "POST"])
def process():
    return render_template('process.html')


@app.route('/output', methods=["GET", "POST"])
def output():
    if request.method == 'GET':
        return render_template('output.html')
    else:
        final = folium.Map(location=[12.9716, 77.5946], tiles='stamentoner')
        EVPR = float(request.form['slider1'])
        final_df = pd.read_csv('csv/final.csv')

        final_df = final_df.loc[final_df['Grade'] < int(EVPR)]

        for indice, row in final_df.iterrows():

            folium.Marker(
                location=[row["latitude"], row["longitude"]],
                popup=row['Name'],
                icon=folium.Icon(color="green", icon="bolt", prefix='fa')
            ).add_to(final)

        sw = final_df[['latitude', 'longitude']].min().values.tolist()
        ne = final_df[['latitude', 'longitude']].max().values.tolist()

        final.fit_bounds([sw, ne])

        final.save('templates/output_map.html')
    return render_template("output.html",
                           my_input1=EVPR,
                           tables=[final_df.to_html(classes='table table-bordered table-hover" id = "optimum_table',
                                                    index=False, border=0)],
                           map_html='output_map.html'
                           )

    # return render_template('output.html')


@app.route('/ouputMap', methods=["GET", "POST"])
def outputMap():
    return render_template('output_map.html')


# start the server with the 'run()' method
if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True) #will run locally http://127.0.0.1:5000/
