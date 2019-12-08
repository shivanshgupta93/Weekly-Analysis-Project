'use strict';

var colors = ["#000000", "#FFFF00", "#1CE6FF", "#FF34FF", "#FF4A46", "#008941", "#006FA6", "#A30059",
"#FFDBE5", "#7A4900", "#0000A6", "#63FFAC", "#B79762", "#004D43", "#8FB0FF", "#997D87",
"#5A0007", "#809693",  "#1B4400", "#4FC601", "#3B5DFF", "#4A3B53", "#FF2F80",
"#61615A", "#BA0900", "#6B7900", "#00C2A0", "#FFAA92", "#FF90C9", "#B903AA", "#D16100",
"#DDEFFF", "#000035", "#7B4F4B", "#A1C299", "#300018", "#0AA6D8", "#013349", "#00846F",
"#372101", "#FFB500", "#C2FFED", "#A079BF", "#CC0744", "#C0B9B2", "#C2FF99", "#001E09",
"#00489C", "#6F0062", "#0CBD66", "#EEC3FF", "#456D75", "#B77B68", "#7A87A1", "#788D66",
"#885578", "#FAD09F", "#FF8A9A", "#D157A0", "#BEC459", "#456648", "#0086ED", "#886F4C",
"#34362D", "#B4A8BD", "#00A6AA", "#452C2C", "#636375", "#A3C8C9", "#FF913F", "#938A81",
"#575329", "#00FECF", "#B05B6F", "#8CD0FF", "#3B9700", "#04F757", "#C8A1A1", "#1E6E00",
"#7900D7", "#A77500", "#6367A9", "#A05837", "#6B002C", "#772600", "#D790FF", "#9B9700",
"#549E79", "#FFF69F", "#201625", "#72418F", "#BC23FF", "#99ADC0", "#3A2465", "#922329",
"#5B4534", "#FDE8DC", "#404E55", "#0089A3", "#CB7E98", "#A4E804", "#324E72", "#6A3A4C"];
var first_tag;
$(document).ready(() => {
        $.get("/api/tags", (tags, err) => {
            if (err !== "success") console.error(err);
            if (tags && Array.isArray(tags.data)) {
                var tags_array = [...new Set(tags.data.map(tags => tags.tag))]
                var dropdown = document.getElementById('selectGenre');
                for (var i = 0; i<tags_array.length; i++){
                    var opt = document.createElement('option');
                    opt.value = tags_array[i];
                    opt.innerHTML = tags_array[i];
                    dropdown.appendChild(opt);
                }
                
            }
            first_tag = tags_array[0];
        }),
        artists(first_tag);
    });
document.getElementById("selectGenre").onchange = function(){
        var selIndex = document.getElementById("selectGenre").selectedIndex;
        var selValue = document.getElementById("selectGenre").options[selIndex].innerHTML;
        console.log(selValue);
        artists(selValue);
        topartist(selValue);
        topalbum(selValue);
        toptrack(selValue);
    };

    function topartist(tag_value)
    {
        $.get("/api/artists?rank=1&tag="+tag_value, (top_artists, err) => {
            if (err !== "success") console.error(err);
            if (top_artists && Array.isArray(top_artists.data)) {
                var insert_dates = []
                var artist_name = ""
                const artist_container = document.querySelector(".topartistdata")
                for(var i=0; i<top_artists.data.length; i++)
                    {
                        insert_dates.push(top_artists.data[i]["inserted_date"])
                    }
                    insert_dates.sort();
                
                for(var i=0; i<top_artists.data.length; i++)
                {
                    if((top_artists.data[i]["inserted_date"] == insert_dates[0]))
                        {
                            artist_name = top_artists.data[i]["artist_name"]
                        }
                }

                if((tag_value == "Choose a Genre"))
                {
                    artist_container.innerText = "Select a Genre";
                }
                else
                {
                    artist_container.innerText = artist_name;
                }
            }
        });
    }
    function topalbum(tag_value)
    {
        $.get("/api/albums?rank=1&tag="+tag_value, (top_albums, err) => {
            if (err !== "success") console.error(err);
            if (top_albums && Array.isArray(top_albums.data)) {
                var insert_dates = []
                var album_name = ""
                var artist_name = ""
                const album_container = document.querySelector(".topalbumdata")
                for(var i=0; i<top_albums.data.length; i++)
                    {
                        insert_dates.push(top_albums.data[i]["inserted_date"])
                    }
                    insert_dates.sort();
                
                for(var i=0; i<top_albums.data.length; i++)
                {
                    if((top_albums.data[i]["inserted_date"] == insert_dates[0]))
                        {
                            album_name = top_albums.data[i]["album_name"]
                            artist_name = top_albums.data[i]["artist_name"]
                        }
                }

                if((tag_value == "Choose a Genre"))
                {
                    album_container.innerText = "Select a Genre";
                }
                else
                {
                    album_container.innerText = album_name + " by " + artist_name;
                }
            }
        });
    }
    function toptrack(tag_value)
    {
        $.get("/api/tracks?rank=1&tag="+tag_value, (top_tracks, err) => {
            if (err !== "success") console.error(err);
            if (top_tracks && Array.isArray(top_tracks.data)) {
                var insert_dates = []
                var track_name = ""
                var artist_name = ""
                const track_container = document.querySelector(".toptrackdata")
                for(var i=0; i<top_tracks.data.length; i++)
                    {
                        insert_dates.push(top_tracks.data[i]["inserted_date"])
                    }
                    insert_dates.sort();
                
                for(var i=0; i<top_tracks.data.length; i++)
                {
                    if((top_tracks.data[i]["inserted_date"] == insert_dates[0]))
                        {
                            track_name = top_tracks.data[i]["track_name"]
                            artist_name = top_tracks.data[i]["artist_name"]
                        }
                }

                if((tag_value == "Choose a Genre"))
                {
                    track_container.innerText = "Select a Genre";
                }
                else
                {
                    track_container.innerText = track_name + " by " + artist_name;
                }
            }
        });
    }
    var chart = null;

    function artists(tag_value){
    $.get("/api/artists?tag="+tag_value, (artists, err) => {
        if (err !== "success") console.error(err);
        if (artists && Array.isArray(artists.data)) {
            const insert_dates = [...new Set(artists.data.map(artist => artist.inserted_date))]
            const artists_name = [...new Set(artists.data.map(artist => artist.artist_name))]
            const ctx = document.getElementById('artists').getContext('2d');
            var artists_ranks = []
            var ranks = []
            for (var j=0; j<artists_name.length; j++)
            {
                artists_ranks = {}
                var datasets = []
                for (var i=0; i<artists.data.length; i++)
                {
                    if((artists.data[i]["artist_name"] == artists_name[j]))
                    {
                        datasets.push(artists.data[i]["artist_rank"])
                    }
                }
                var randomcolor = colors[j]
                artists_ranks.label = artists_name[j]
                artists_ranks.data = datasets
                artists_ranks.fill = false
                artists_ranks.lineTension = 0
                artists_ranks.radius = 5
                artists_ranks.backgroundColor = randomcolor
                artists_ranks.borderColor = randomcolor
                artists_ranks.steppedLine = true
                //artists_ranks.borderWidth = "50px"
                ranks.push(artists_ranks)
            }
            line_chart(ctx, insert_dates, ranks)
        }
    });
}

function line_chart(ctx, data_labels, dataset){
    if(chart!=null){
        chart.destroy();
    }
    chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data_labels,
            datasets: dataset
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    },
                    gridLines: {
                       display: true
                    }
                }],

                xAxes: [{
                    gridLines: {
                        display: true
                    }
                }]
            },
            legend:{
                display:true,
                position:"bottom"
            }
        }
    });
}