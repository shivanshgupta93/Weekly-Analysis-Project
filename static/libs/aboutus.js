'use strict';

$(document).ready(() => {

        var d = new Date();
        var date = d.getDate();
        var year = d.getFullYear();
        var month = d.getMonth();
        var monthArr = ["January", "February","March", "April", "May", "June", "July", "August", "September", "October", "November","December"];
        month = monthArr[month];
        const datediv = document.querySelector(".date")
        datediv.innerText = date+" "+month+", "+year;
    });