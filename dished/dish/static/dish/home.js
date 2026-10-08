$(document).ready(function () {
    console.log("hello")
    const recipe_cards = document.getElementsByClassName('recipe_card')
    const link_cards = document.getElementsByClassName('link_large')
    const links = document.getElementsByClassName('link_small')
    for (const card of recipe_cards) {
        card.style.fontSize = getFontSize(card.textContent.trim().length)
        // console.log(card.textContent.trim())
        // console.log(card.style.fontSize)
        // console.log(getFontSize(card.textContent.length))
    }
    for (const card of link_cards) {
        card.style.fontSize = getFontSize(card.textContent.trim().length)
        // console.log(card.textContent.trim())
        // console.log(card.style.fontSize)
        // console.log(getFontSize(card.textContent.length))
    }
    for (const card of links) {
        card.style.fontSize = getFontSize2(card.textContent.trim().length)
    }

});

// code adapted from https://codepen.io/jsstrn/pen/mMMmZB
const getFontSize = (textLength) => {
    console.log(textLength)
    let fontSize;
    if (textLength > 40) {
        fontSize = 1.25
    }
    else if (textLength > 20) {
        // textLength = baseSize - 2
        // fontSize = textLength - baseSize
        fontSize = 1.5
    }
    else {
        // console.log(textLength)
        fontSize = 2
    }
    console.log(fontSize)
    return `${fontSize}em`
}

const getFontSize2 = (textLength) => {
    // console.log(textLength)
    const baseSize = 20
    let fontSize;
    if (textLength >= baseSize) {
        // textLength = baseSize - 2
        // fontSize = textLength - baseSize
        fontSize = 1
    }
    else {
        // console.log(textLength)
        fontSize = 1.25
    }
    // console.log(fontSize)
    return `${fontSize}em`
}
