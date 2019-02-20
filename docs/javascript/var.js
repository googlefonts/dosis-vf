'use strict';

// init
const container = document.querySelector('.controls');
let variableElement = document.querySelector('.variable');

// Set style value
function setStyles (property, value) {
    return document.documentElement.querySelector(".variable").style.setProperty(property, value);
}

function updateInputElements(e) {
    // setting up the instances
    const rowContainer = e.target.parentNode;
    const slider = rowContainer.querySelector(".slider"); 
    const textbox = rowContainer.querySelector(".textbox");
    const styleType = slider.getAttribute("id");
    const sliderValue = e.target.value;

    // setting values
    slider.value = sliderValue;
    textbox.value = sliderValue;

    // Checks and updates the input field so they don't go over their maximum.
    const slidermax = Number(slider.getAttribute("max"));
    if (textbox.value > slidermax) {
        textbox.value = slidermax;
    }

    // setting the style
    setStyles(`--${styleType}`, sliderValue);
}

window.addEventListener('load', function() {
    // Updates all inputs and their values depending on what the user has changed. 
    container.addEventListener('input', updateInputElements);
});
