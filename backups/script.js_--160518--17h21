//JS file
function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    $("#clock").html(h + ":" + m);
    var t = setTimeout(startTime, 500);
    if(m == 00 && s == 00){
        location.reload();
    }
}

function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}

update = function() {
    var current = [];
    var forecast = [];
    var activity = [];
    var monthNames = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"];
    var quotes = [];
    var rand = Math.floor((Math.random() * 10) + 1)
    g = new Date();
    gTime = monthNames[g.getMonth()] + "-" + g.getDate();
    //Gets and sets current conditions
    $.ajax({
        url: "http://api.wunderground.com/api/" + WEATHER_KEY + "/conditions/q/MO/Rolla.json",
        dataType: 'json',
        timeout: 5000,
        success: function(data, status) {
            $.each(data, function(i, item) {
                current = item;
            });
            $("#temp_f").html(Math.round(current.temp_f));
            
            iconDisplay("#icon", String(current.weather))
        },
        error: function() {
            $("#temp_f").html('Error');
        }
    });

    //Gets and sets the forecast
    $.ajax({
        url: "http://api.wunderground.com/api/" + WEATHER_KEY + "/forecast/q/MO/Rolla.json",
        dataType: 'json',
        timeout: 5000,
        success: function(data, status) {
            $.each(data, function(i, thing) {
                forecast = thing;
            });
            /*For each of these lines, the id of a tag is found (e.g. HLOne) 
             *and then a segment of the forecast data is assigned to that tag.
             */
            iconDisplay("#iconOne", String(forecast.simpleforecast.forecastday[0].conditions));
            $("#HLOne").html(forecast.simpleforecast.forecastday[0].high.fahrenheit + "&deg" + "/" +
                    forecast.simpleforecast.forecastday[0].low.fahrenheit + "&deg");
            $("#PWOne").html(forecast.simpleforecast.forecastday[0].pop + "%" + " | " +
                    forecast.simpleforecast.forecastday[0].avewind.mph + "mph");

            iconDisplay("#iconTwo", String(forecast.simpleforecast.forecastday[1].conditions));
            $("#HLTwo").html(forecast.simpleforecast.forecastday[1].high.fahrenheit + "&deg" + "/" +
                    forecast.simpleforecast.forecastday[1].low.fahrenheit + "&deg");
            $("#PWTwo").html(forecast.simpleforecast.forecastday[1].pop + "%" + " | " +
                    forecast.simpleforecast.forecastday[1].avewind.mph + "mph");
            $("#forecastTwo").html(forecast.simpleforecast.forecastday[1].date.weekday);

            iconDisplay("#iconThree", String(forecast.simpleforecast.forecastday[2].conditions));
            $("#HLThree").html(forecast.simpleforecast.forecastday[2].high.fahrenheit + "&deg" + "/" +
                    forecast.simpleforecast.forecastday[2].low.fahrenheit + "&deg");
            $("#PWThree").html(forecast.simpleforecast.forecastday[2].pop + "%" + " | " +
                    forecast.simpleforecast.forecastday[2].avewind.mph + "mph");
            $("#forecastThree").html(forecast.simpleforecast.forecastday[2].date.weekday);

            iconDisplay("#iconFour", String(forecast.simpleforecast.forecastday[3].conditions));
            $("#HLFour").html(forecast.simpleforecast.forecastday[3].high.fahrenheit + "&deg" + "/" +
                    forecast.simpleforecast.forecastday[3].low.fahrenheit + "&deg");
            $("#PWFour").html(forecast.simpleforecast.forecastday[3].pop + "%" + " | " +
                    forecast.simpleforecast.forecastday[3].avewind.mph + "mph");
            $("#forecastFour").html(forecast.simpleforecast.forecastday[3].date.weekday);
        },
        error: function() {
            $("#iconOne").html('Error');
        }
    });

    /* quotes.json is a json file I made that has, in json object notation, 
     * a list of quotes are their authors. This block of code randomly selects
     * one of the quotes to display (using the getJSON function).
     */
    $.getJSON('/static/page/quotes.json', function(data) {
        var q = Math.floor(Math.random() * data.quotes.length);
        $("#quote").html("\"" + data.quotes[q].text + "\"");
        $("#author").html(data.quotes[q].author);
    });

    $.ajax({
        url: "https://www.googleapis.com/calendar/v3/calendars/justin.brown400@gmail.com/events?orderBy=starttime&singleEvents=true&alt=json&maxResults=10&timeMin=2016-" + gTime + "T" + g.getHours()  + "%3A00%3A00-07%3A00&key=" + GOOGLE_KEY + "",
        dataType: 'json',
        timeout: 5000,
        success: function(data, status) {
            $.each(data, function(i, item) {
                cal = item;
            });
            for(i = 0; i < 10; i++){
                if(cal[i].summary === "Internet Bill" || cal[i].summary === "Pay Day" || cal[i].summary === "Run"){
                    continue;
                }
                var tmp = "#event" + i;
                var simpleDate = new Date(Date.parse(cal[i].start.dateTime));
                $(tmp).html(cal[i].start.dateTime.slice(11, 16) + " (" + monthNames[simpleDate.getMonth()] + "/" + simpleDate.getDate() + ") : " + cal[i].summary);
                $("#test").html(gTime);
            }
        },
        error: function() {
            $("#event").html('There was an error loading the data.');
        }
    });
    calendar();
}

// Receives an id and a weather condition and sets the icon
function iconDisplay(icon, item) {
    dir_name = '/static/page/bower_components/animated-climacons/climacons/svg-css/';
    switch(item) {
        case "Clear":
            if(icon === "#icon"){
                t = new Date();
                if(t.getHours() < 19 && t.getHours() > 6)
                    $(icon).attr('src', dir_name + 'sunFill.svg');
                else
                    $(icon).attr('src', dir_name + 'moonFill.svg');
                break;
            }
            $(icon).attr('src', dir_name + 'sunFill.svg');
            break;

        case "Overcast":
            $(icon).attr('src', dir_name + 'cloudFill.svg');
            break;

        case "Rain":
        case "Heavy Rain":
            $(icon).attr('src', dir_name + 'cloudDrizzle.svg');
            break;

        case "Chance of Rain":
        case "Light Rain":
            $(icon).attr('src', dir_name + 'cloudRainAlt.svg');
            break;

        case "Heavy Snow":
            $(icon).attr('src', dir_name + 'cloudSnow.svg');
            break;

        case "Light Snow":
            $(icon).attr('src', dir_name + 'cloudSnowAlt.svg');
            break;

        case "Sunny":
            $(icon).attr('src', dir_name + 'sunFill.svg');
            break;

        case "Mostly Cloudy":
            $(icon).attr('src', dir_name + 'cloudFill.svg');
            break;

        case "Partly Cloudy":
            $(icon).attr('src', dir_name + 'cloudSunFill.svg');
            break;

        case "Chance of a Thunderstorm":
        case "Thunderstorm":
            $(icon).attr('src', dir_name + 'cloudLightning.svg');
            break;

        default:
            $(icon).html('Error/Other');
    }
}


/* Gets and sets all basic calendar information (current day, month, days in a 
 * month, etc.
 */
function calendar(){
    //Array to houes month names since .getMonth() returns a number
    var monthNames = ["January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"];
    //Array to house weekday names since getDay() returns a number
    var weekdayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday"];
    var date = new Date();
    //Get current day, month, year
    currentDay = date.getDay();
    currentMonth = date.getMonth();
    currentYear = date.getFullYear();

    //Apply current month to month tag
    $("#month").html(monthNames[currentMonth]);

    //Get the weekday of the first day of the month
    dateFirstDay = new Date(currentYear, currentMonth, 1);
    //$("#current-day").html(weekdayNames[dateFirstDay.getDay()]);

    //Get the last day of the month
    dateLastDay = new Date(currentYear, currentMonth + 1, 0);
    //Create tags with necessary ids and classes
    for (i = 0; i < 7; i++){
        var row = document.createElement('div');
        row.className = "week-col";
        row.id = weekdayNames[i];
        document.getElementById("weeks").appendChild(row);
        for (j = 0; j < 5; j++){
            var col = document.createElement('div');
            col.className = "week-row";
            col.id = (1 + i) + (j * 7);
            document.getElementById(weekdayNames[i]).appendChild(col);
        }
    }

    //Set current day and fill tags with day numbers
    var start = false;
    var count = 1;
    for (i = 1; i < 36; i++){
        var x = document.getElementById(i);
        parentDiv = x.parentNode;
        if(weekdayNames[dateFirstDay.getDay()] == parentDiv.getAttribute('id')){
            start = true;
        }
        if(start){
            x.innerHTML = count;
            count++;
        }
        if(weekdayNames[dateLastDay.getDay()] == parentDiv.getAttribute('id') && i > 28){
            break;
        }
    }

    //Get current day and set tag
    var d = document.getElementById(date.getDate())
    d.id = "current-day";
}
