'use strict';


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
    };

function artists(tag_value){
    $.get("/api/artists?tag="+tag_value, (artists, err) => {
        if (err !== "success") console.error(err);
        console.log(tag_value);
        if (artists && Array.isArray(artists.data)) {
            const tags = [...new Set(artists.data.map(artist => artist.tag))] // function(artist) {return artist.tag}
            const insert_dates = [...new Set(artists.data.map(artist => artist.inserted_date))]
            const data = insert_dates.map(inserted_date => artists.data.filter(artist => artist.inserted_date == inserted_date).length)
            const ctx = document.getElementById('artists').getContext('2d');
            console.log(data);
            const artists_chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: insert_dates,
                    datasets: [{
                        label: 'Artists based on tags',
                        data: data,
                         backgroundColor: [
                             'rgba(255, 99, 132, 0.2)',
                             'rgba(54, 162, 235, 0.2)',
                             'rgba(255, 206, 86, 0.2)',
                             'rgba(75, 192, 192, 0.2)',
                             'rgba(153, 102, 255, 0.2)',
                             'rgba(255, 159, 64, 0.2)'
                         ],
                         borderColor: [
                             'rgba(255, 99, 132, 1)',
                             'rgba(54, 162, 235, 1)',
                             'rgba(255, 206, 86, 1)',
                             'rgba(75, 192, 192, 1)',
                             'rgba(153, 102, 255, 1)',
                             'rgba(255, 159, 64, 1)'
                         ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            },
                            gridLines: {
                               display: false
                            }
                        }],

                        xAxes: [{
                            gridLines: {
                                display: false
                            }
                        }]
                    }
                }
            });
        }
    });
}