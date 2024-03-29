class Weather {
  constructor(city) {
    this.apiKey = "8099b2335ffe9ad93c23ec909cab5473";
    this.city = city;
    //this.state = state;
  }
  //Fetch weather from API
  async getWeather() {
    const response = await fetch(
      `https://api.openweathermap.org/data/2.5/weather?q=${this.city}&appid=${this.apiKey}&units=metric`
    );

    const responseData = await response.json();
    return responseData;
  }
  //Change weather location
  changeLocation(city) {
    this.city = city;
    //this.state = state;
  }
}
