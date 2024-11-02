const cityElem = document.getElementById('city');
const countryElem = document.getElementById('country');
const temperatureElem = document.getElementById('temperature');
const descriptionElem = document.getElementById('description');
const weatherIconElem = document.getElementById('weather-icon');
const searchBtn = document.getElementById('search-btn');
const cityInput = document.getElementById('city-input');

// Fetch weather data from Flask API
async function fetchWeatherFromAPI(cityName) {
    const apiUrl = `http://127.0.0.1:8000/weatherfetch?city=${cityName}`;
    
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        if (response.ok) {
            updateWeatherUI(data);
        } else {
            alert(data.error || 'City not found! Please try another city.');
        }
    } catch (error) {
        console.error('Error fetching weather data:', error);
        alert('Failed to retrieve data. Please check your connection.');
    }
}

// Update the UI with fetched weather data
function updateWeatherUI(data) {
    cityElem.textContent = data.name;  // Use .name from OpenWeatherMap
    countryElem.textContent = data.sys.country;  // Country from the response
    temperatureElem.textContent = `${Math.round(data.main.temp)}°C`;  // Temperature
    descriptionElem.textContent = capitalizeWords(data.weather[0].description);  // Weather description
    weatherIconElem.src = `https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`;
    console.log(data.weather[0].icon);
      // Weather icon
}

// Capitalize weather description
function capitalizeWords(str) {
    return str.replace(/\b\w/g, char => char.toUpperCase());
}

// Search event
searchBtn.addEventListener('click', () => {
    const cityName = cityInput.value.trim();
    if (cityName) {
        fetchWeatherFromAPI(cityName);
        cityInput.value = '';  // Clear the input field after search
    } else {
        alert('Please enter a valid city name.');
    }
});

// Initial weather for a default city
fetchWeatherFromAPI('Noida');  // Optionally fetch weather for a default city on load
