$(document).ready(function() {
    splitWords($("p:first"));
});

/**
 * This function splits the words given into different span elements so that they can each be given a hover handler later
 * @param words - JQuery <p> object of words to split
 */
function splitWords(p)
{
    p.css({"background-color":"red"});
    var words = p.text().split(" ");        //get each individual word

    //now the paragraph text must have a <span> in front of each word

    return spans    //returns the span objects
}

/**
 * Given the split paragraph, adds a hover handler to each span in the paragraph
 * @param words
 */
function addHoverHandlers(spans)
{

}


function applyASLFunctionality(p)
{
    var words =  splitWords(p);
    addHoverHandlers(words)

}

/**
 * Given the span (or object in general), make its CSS background-color yellow
 * @param span - The JQuery span object
 */
function highlight(span)
{
    span.css({"background-color" : "yellow"});
}

/**
 * Given the span, make its CSS background-color transparent. This is used when a word is not hovered on anymore
 * @param span - The JQuery span object
 */
function dehighlight(span)
{
    span.css({"background-color" : "transparent"});
}