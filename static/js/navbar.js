'use strict';

var current = window.location.href;

// if (current.includes("dashbaord")) {
//     document.getElementById("dashboard-navbar").classList.add("active");
//     }

if (current.includes("unit1")) {
    document.getElementById("unit1-navbar").classList.add("active");
}

    if (current.includes("concept1.1")) {
        document.getElementById("concept1.1-sidebar").classList.add("active");
    } else if (current.includes("concept1.2")) {
        document.getElementById("concept1.2-sidebar").classList.add("active");
    }