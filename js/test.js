$(document).ready(function() {
    addVideoFrame();
    $("p").mouseup(textSelected);
});

/**
 * Full text selection functionality
 */
function textSelected()
{
    var text = getSelectedText();
    if(text)
    {
        $("#video_frame").removeClass("no_display");
        $("#frame_title").text(text);
    }
}
function addVideoFrame()
{
    var style_css = "\
    .no_display { \
        display : none; \
    } \
    \
    .SSvideo { \
        z-index: 1; \
        padding: 5px; \
        background-color: black; \
        position: fixed; \
        top: 0%; \
    }";
    $("head").append("<style>" + style_css + "</style>");

    var frame_html = "<div id = 'video_frame' class = 'SSvideo no_display'> \
        <h3 id = 'frame_title' style = 'color: white; padding: none;'></h3> \
        <iframe src= 'www.cnn.com' width = 350px  height = 350px style ='display: block; margin: auto'> </iframe> \
        </div>";
    $("body").append(frame_html);
}

function getSelectedText()
{
    var text = "";
    if(window.getSelection)
    {
        text = window.getSelection().toString();
    }
    return text;
}
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