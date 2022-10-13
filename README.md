# Optimal EV charging location
Optimal EV Charging Location based on density and nearby places algorithm


The fact that the current network of charging stations is still in its infancy is frustrating for many prospective electric vehicle (EV) customers. "Range anxiety" refers to the condition where EV users are concerned about depleting their battery during a trip. Home charging is already available to the majority of EV owners, however it is nearly difficult for those who reside in apartments or complexes. Therefore, expanding the charging network is vital to advance EV sales. Government of India targets 30% electric vehicles by 2030. **Where should they be placed in order to minimise the total social cost is a logical issue to address.**

For municipal planners to select the best placement for future electric vehicle (EV) charging stations in the City of Bangalore, **Optimus** is an optimization and visualisation tool. It enables the user to investigate the best placement of charging stations in various EV charging demand scenarios. The product is deployed as a [Web app](http://optimus.herokuapp.com/). 

## Packages
Please run `pip install -r requirements.txt` on your virtual environment to install the required python packages to run. This project solves the **optimization** problem using algorithm shown below, **visualizes** the final result using Folium, and deploys the **web app** using Flask. 

## Data Source
* Demand for charging: number of trips in Bangalore [link](https://github.com/syedmisbah/Uber-movement-bangalore-dataset)
* Supply for charging: currently existing charging stations + potential future charging stations ( currently existing parking lots) (from Google MAPS API)

## Optimization Model  
* The decision: choosing a subset of parking lots to install chargers. 
* Objective: Minimizing (the cost of installing chargers + electric car drivers' travel cost from the charging station to their travel destination)
* Constraints:  <br>
(1) Each destination should have enough charging stations.<br>
(2) Charging capacity does not exceed each station's limit.

### Model Formulation
![formulation](https://raw.githubusercontent.com/Aditya9111/optimal_charging_location/main/pics/9.png)

## The Web App
This section briefly explains the [web app](http://optimus.herokuapp.com/). On the home page, the user will be prompted to enter one parameters: Electric Vehicle Penetration Ratio ( what percentage of vehicle you want to convert to electric) . 
#### Landing Page and User Input
![Landing Page](https://raw.githubusercontent.com/Aditya9111/optimal_charging_location/main/pics/1.png)
![user-input](https://raw.githubusercontent.com/Aditya9111/optimal_charging_location/main/pics/5.png)
The online app will display a table of parking lots that are ideal sites to install chargers after the user hits the "Find Optimal Locations" button.

#### Explore results on a map
#### Final Result Heatmap with Markers
![Heat Map](https://raw.githubusercontent.com/Aditya9111/optimal_charging_location/main/pics/4.png)
The user had the option of viewing the outcomes on a map.
![existing charging section](https://raw.githubusercontent.com/Aditya9111/optimal_charging_location/main/pics/2.png)

## Quickstart to run this application

First clone the repostiory

```
$ git clone https://github.com/Aditya9111/optimal_charging_location.git
```
Change directory to main directory

```
$ cd optimal_charging_location
```
Create a virtual environment and install dependencies
```
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install --upgrade pip setuptools
$ python -m pip install -r requirements.txt
```

Start the development server
```
$ python app.py or flask run
```
That's it! 

Navigate to `http://127.0.0.1/` and start your new project!

