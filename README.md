# FuelFinder

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
    - [Detailed Explanation](#detailed-explanation)
    - [Simple Explanation](#simple-explanation)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Overview
The project aims to model a fuel supply chain management system where refineries supply fuel to gas stations. The system offers functionalities such as mapping, distance calculations, and order generation to help optimize the supply chain.

### Simple Explanation

#### What Does It Do?
Our project is a tool for managing fuel supply from refineries to gas stations. It helps you find out:

1. How much fuel each place has.
2. How far and long it takes to get fuel from a refinery to a gas station.
3. Which refineries are the best options for each gas station based on distance, time, and fuel needs.

#### How Does It Work?
- You can see all the refineries and gas stations on a map.
- You can select a refinery and a gas station to find out how far apart they are and how long it would take to drive between them.
- You can generate random fuel amounts for each place to simulate a day's supply and demand.
- You can get a list of best-match refineries for each gas station based on their fuel needs.
- You can click on any of these potential orders to see the best route on the map.

The tool uses Google Maps to show locations and calculate routes. It's a great way to make informed decisions about where to send fuel!

## Features

### Detailed Explanation

#### Overview
The project aims to model a fuel supply chain management system where refineries supply fuel to gas stations. The core functionalities include:

1. Displaying a Google Map that shows refineries and gas stations.
2. Calculating the distance and duration between selected refineries and gas stations.
3. Generating fuel amounts for refineries and gas stations.
4. Creating potential orders that match gas stations with nearby refineries based on fuel needs.

#### Functions and Features

1. **initMap**: Initializes Google Maps, sets up `directionsService` and `directionsRenderer` for later use, and populates `refineries` and `gasStations` arrays with coordinate data.
2. **displayDistanceAndDuration**: Uses Google's Distance Matrix API to fetch the distance and duration between two points (a refinery and a gas station) and returns them.
3. **assignRandomPrices**: Randomly assigns gasoline prices to refineries and gas stations based on historical data.
4. **assignFuelAmounts**: Randomly generates fuel amounts for both refineries and gas stations based on some constraints (max capacities).
5. **distributeFuel**: Helper function to distribute a given total fuel amount into three categories—regular, midgrade, and premium.
6. **getGasPricePosition**: Calculates the position of a given gas price within a known range for different types of gas.
7. **updateMapWithRoute**: Given a selected refinery and gas station, it uses Google's Directions API to find and display the driving route on the map.
8. **Event Listeners**: 
    - "Get Distance & Duration" fetches and displays the distance and duration between selected locations.
    - "Get Fuel Amounts" triggers `assignFuelAmounts` to populate random fuel amounts.
    - "Generate Orders" creates a list of potential orders, matching gas stations with nearby refineries based on their fuel needs.
9. **Interactive Table Rows**: The rows in the "Potential Orders" table are clickable. Clicking a row updates the Google Map to show the route between the selected refinery and gas station.

#### Intuition Behind the Logic
- The application uses Google Maps and Directions API to provide geospatial data and directions.
- The application simulates a day's activity in the supply chain by randomizing fuel amounts and prices, aiming to provide insights on optimal supply chain decisions.
- We use Promise-based asynchronous code to handle API calls and ensure the UI remains responsive.
