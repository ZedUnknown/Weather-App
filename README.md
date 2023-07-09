# WeatherApp

<a href="#">
<img align="right" width="100px" src="https://github.com/ZedUnknown/Weather-App/blob/main/Resources/assets/WeatherTypes/sunny.png" alt="Image"/>
</a>
WeatherApp is a Python-based application that provides users with real-time weather information for a given location. It utilizes the OpenWeatherMap API to fetch accurate weather data and presents it in a user-friendly manner.


## Features

- **Current Weather**: Get up-to-date information on temperature, humidity, wind speed, and weather conditions for a specific location.
- **Location Search**: Enter the name of a city or town to retrieve weather information for that area.
- **Weather Descriptions**: View detailed descriptions of various weather conditions such as clear sky, few clouds, rain, snow, thunderstorm, and more.
- **Dynamic Weather Images**: Show weather-specific images to visually represent the current weather condition.
- **Responsive GUI**: Enjoy a user-friendly and intuitive graphical user interface for seamless interaction with the app.
- **Unit Conversion** (coming soon): Convert temperature between Celsius and Fahrenheit.
- **Timezone Conversion** (coming soon): Adjust the displayed time to the local timezone of the selected location.

## Prerequisites

- Python 3.x
- OpenWeatherMap API Key

## Installation

1. Clone the repository or download the project files.
2. Install the required Python modules by running the following command:
```
python installer.py
```
This command will automatically install the necessary dependencies.

## Configuration

1. Create an account on [OpenWeatherMap](https://openweathermap.org/) and generate an API key.
2. Open the `API.env` file and add the following line, replacing `API_KEY_HERE` with the API key you obtained:
```API="API_KEY_HERE"```


## Usage

1. Run the main script using the following command:
```
python WeatherApp.py
```
2. The application window will open, displaying a search bar.
3. Enter the name of a city or town in the search bar and press Enter or click the search button.
4. The application will retrieve and display the current weather information for the specified location.
5. Explore the app's features, including temperature display, weather description, humidity, wind speed, and more.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The WeatherApp uses the [OpenWeatherMap API](https://openweathermap.org/) to retrieve weather data.
- It incorporates various Python libraries such as `customtkinter`, `os`, `datetime`, `pytz`, `dotenv`, `geopy`, and `PIL`.

## Feedback and Suggestions

Your feedback and suggestions are valuable to us! If you encounter any problems, have ideas for improvement, or would like to suggest additional options, please feel free to:

- Open an issue in this repository to report a problem or bug.
- Submit a pull request if you have a solution or enhancement to contribute.
- Reach out to us through the contact information provided in the repository.

We appreciate your input and look forward to hearing from you! Together, we can make this project even better.

---

Enjoy using the WeatherApp and explore the beauty of weather in different parts of the world!
