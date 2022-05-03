# Architecture Description
---
## Structure

The app's general structure follows a three-layered model.

```mermaid
    classDiagram

        UI --> services
        services --> entities
```
The UI component includes everything related to user interface elements. This part only displays data retrieved from service elements. The service elements implement the App logic, or in the case of this app, the interaction with the API. The task of entities is to model this API data to something more usable from the app's perspective. Eventually, these instances of entities return to the UI, where they are unpacked and displayed to the user.

## User Interface

The user interface consists of views and frames. Views, managed by the UI element, are usually built from a collection of Frames.
```mermaid
    classDiagram

        UI --o LoginView
        UI --o WeatherView
        WeatherView --o NavbarFrame
        WeatherView --o CurrentFrame
        WeatherView --o ForecastFrame
        WeatherView --o GraphFrame
        ForecastFrame --o DetailsFrame
```


In total, the app includes two views; Login- and WeatherView. LoginView is currently used to set the user's API key on the first execution. At the same time, the WeatherView operates as the app's main view. Compared to LoginView, where the view handles all the operations, the Weatherview works more as a manager. It only controls the refreshing of frames and the calls on service methods, leaving the task of displaying graphical elements to Frames.

## Services

---

```mermaid
    classDiagram

        UI --> ConfigService: Check if API key exists
        UI --o LoginView
        LoginView --> ConfigService: Set API key
        WeatherService --> ConfigService: URLs and API key
        IconService --> ConfigService: URL
        ConfigService --> configini: Parse
```

#### ConfigService

The config service is the most global of these three, providing URLs and the API key across the application. It mainly operates with a config.ini file where all necessary information is stored and read on demand. The configuration file system provides excellent flexibility with the service since it's not instance dependent.

---

```mermaid
    sequenceDiagram

    participant WeatherService
    participant Geocoding API
    participant One Call API
    participant One Call API (timemachine)

    WeatherService ->> Geocoding API: City name
    Geocoding API ->> WeatherService: name, latitude, longitude
    WeatherService ->> One Call API: latitude, longitude
    One Call API ->> WeatherService: Weather data
    loop for each day(5)
        WeatherService ->> One Call API (timemachine): latitude, longitude, day
        One Call API (timemachine) ->> WeatherService: Historical data
    end
```

#### WeatherService

The weather service is the one that interacts with the OpenWeather API. In total, the app makes seven calls to three different API endpoints. The first call to Geocoding API converts the city name from user input to latitude and longitude. Using these coordinates, the second call to OpenWeathers One call API endpoint returns the current weather and the forecast for the upcoming days. Finally, the One Call APIs time machine requires five separate calls for each day to get hourly historical data for the past five days. The service passes the data to the Weather entity and returns it.

---

```mermaid
    sequenceDiagram

    participant IconService
    participant OpenWeather API

    IconService ->> OpenWeather API: Icon id
    OpenWeather API ->> IconService: Raw data
    IconService ->> IconService: Open and identify image
    IconService ->> IconService: Turn into Tkinter compatible image
```

#### IconService

The icon service retrieves weather icons from OpenWeather API. The class's only method uses the icon id (passed as an argument) to get icon data. Using Pillow module, the raw data is converted to ImageTk PhotoImage object and returned.

---

## TODO...

#### Class Diagram


```mermaid
    classDiagram
        
        direction LR

        class ConfigService {
            open_weather_url
            geocoding_url
            api_key
            api_key_set
            api_key_is_set()
        }

        class WeatherService {
            weather()
        }

        class IconService {
            get_icon()
        }

        class UI {
            start()
        }

        class LoginView {
            set_api_key
        }

        class WeatherView {
            get_weather()
            update_frames()
        }

        class NavbarFrame {
            navbar()
        }

        class CurrentFrame {
            current()
        }

        class ForecastFrame {
            forecast()
            details()
        }

        class DetailsFrame {
            details()
        }

        class GraphFrame {
            plot_data()
        }
        
        class Weather {
            city
            current
            forecast
            graph
        }
        
        class Current {
        }

        class Forecast {
        }

        class Graph {
        }

        Weather --o Forecast
        Weather --o Current
        Weather --o Graph
        WeatherService --> Weather: use
        WeatherService --> ConfigService: use
        UI --o WeatherView
        UI --o LoginView
        UI --> ConfigService: use
        WeatherView --> WeatherService: use
        WeatherView --o NavbarFrame
        WeatherView --o CurrentFrame
        WeatherView --o ForecastFrame
        WeatherView --o GraphFrame
        ForecastFrame --o DetailsFrame
        CurrentFrame --> IconService: use
        ForecastFrame --> IconService: use
        DetailsFrame --> IconService: use
        LoginView --> ConfigService: implicit
        
```

---

#### Sequence Diagram


```mermaid
    sequenceDiagram

    actor User
    participant UI
    participant WeatherService
    participant ConfigService
    participant Geocoding API
    participant Onecall API
    participant Weather
    participant Current
    participant Forecast
    participant Graph

    User ->> UI: search "Helsinki"
    UI ->> WeatherService: weather("Helsinki")
    ConfigService ->> WeatherService: urls and api key
    WeatherService ->> Geocoding API: "Helsinki"
    Geocoding API ->> WeatherService: longitude, latitude
    WeatherService ->> Onecall API: longitude, latitude
    Onecall API ->> WeatherService: weather data (current and forecast)

    loop for each day(5)
    WeatherService ->> Onecall API: longitude, latitude, day
    Onecall API ->> WeatherService: weather data (historical)
    end

    WeatherService ->> Weather: historical-, current-, and forecast data
    Weather ->> Current: current data
    Current ->> Weather: Current data object

    loop for each day(8)
    Weather ->> Forecast: days data
    Forecast ->> Weather: Forecast data object
    end

    Weather ->> Graph: 120 hours of historical data and 48 hour forecast
    Graph ->> Weather: Dataframe object
    Weather ->> UI: the whole weather object
    UI ->> UI: update_frames()

```