function voice() {
    try {
        var SpeechRecognition =
            window.SpeechRecognition || window.webkitSpeechRecognition;
        var recognition = new SpeechRecognition();
    } catch (e) {
        console.error(e);
        $(".no-browser-support").show();
        $(".app").hide();
    }

    var noteTextarea = $("#voice_text");
    console.log(noteTextarea);

    var noteContent = " ";
    recognition.start();
    recognition.continuous = true;

    // This block is called every time the Speech APi captures a line.
    recognition.onresult = function (event) {
        // event is a SpeechRecognitionEvent object.
        // It holds all the lines we have captured so far.
        // We only need the current one.
        var current = event.resultIndex;

        // Get a transcript of what was said.
        var transcript = event.results[current][0].transcript;

        // Add the current transcript to the contents of our Note.
        // There is a weird bug on mobile, where everything is repeated twice.
        // There is no official solution so far so we have to handle an edge case.
        var mobileRepeatBug =
            current == 1 && transcript == event.results[0][0].transcript;

        if (!mobileRepeatBug) {
            noteContent += transcript;
            noteTextarea.val(noteContent);
        }
    };

    noteTextarea.on("input", function () {
        noteContent = $(this).val();
    });
}

function voice1() {
    try {
        var SpeechRecognition =
            window.SpeechRecognition || window.webkitSpeechRecognition;
        var recognition = new SpeechRecognition();
    } catch (e) {
        console.error(e);
        $(".no-browser-support").show();
        $(".app").hide();
    }

    var noteTextarea = $("#title1");
    console.log(noteTextarea);

    var noteContent = " ";
    recognition.start();
    recognition.continuous = true;

    // This block is called every time the Speech APi captures a line.
    recognition.onresult = function (event) {
        // event is a SpeechRecognitionEvent object.
        // It holds all the lines we have captured so far.
        // We only need the current one.
        var current = event.resultIndex;

        // Get a transcript of what was said.
        var transcript = event.results[current][0].transcript;

        // Add the current transcript to the contents of our Note.
        // There is a weird bug on mobile, where everything is repeated twice.
        // There is no official solution so far so we have to handle an edge case.
        var mobileRepeatBug =
            current == 1 && transcript == event.results[0][0].transcript;

        if (!mobileRepeatBug) {
            noteContent += transcript;
            noteTextarea.val(noteContent);
        }
    };

    noteTextarea.on("input", function () {
        noteContent = $(this).val();
    });
}

function voice3() {
    try {
        var SpeechRecognition =
            window.SpeechRecognition || window.webkitSpeechRecognition;
        var recognition = new SpeechRecognition();
    } catch (e) {
        console.error(e);
        $(".no-browser-support").show();
        $(".app").hide();
    }

    var noteTextarea = $("#msg");
    console.log(noteTextarea);

    var noteContent = " ";
    recognition.start();
    recognition.continuous = true;

    // This block is called every time the Speech APi captures a line.
    recognition.onresult = function (event) {
        // event is a SpeechRecognitionEvent object.
        // It holds all the lines we have captured so far.
        // We only need the current one.
        var current = event.resultIndex;

        // Get a transcript of what was said.
        var transcript = event.results[current][0].transcript;

        // Add the current transcript to the contents of our Note.
        // There is a weird bug on mobile, where everything is repeated twice.
        // There is no official solution so far so we have to handle an edge case.
        var mobileRepeatBug =
            current == 1 && transcript == event.results[0][0].transcript;

        if (!mobileRepeatBug) {
            noteContent += transcript;
            noteTextarea.val(noteContent);
        }
    };

    noteTextarea.on("input", function () {
        noteContent = $(this).val();
    });
}



function voice2() {
    try {
        var SpeechRecognition =
            window.SpeechRecognition || window.webkitSpeechRecognition;
        var recognition = new SpeechRecognition();
    } catch (e) {
        console.error(e);
        $(".no-browser-support").show();
        $(".app").hide();
    }

    var noteTextarea = $("#text2");
    console.log(noteTextarea);

    var noteContent = " ";
    recognition.start();
    recognition.continuous = true;

    // This block is called every time the Speech APi captures a line.
    recognition.onresult = function (event) {
        // event is a SpeechRecognitionEvent object.
        // It holds all the lines we have captured so far.
        // We only need the current one.
        var current = event.resultIndex;

        // Get a transcript of what was said.
        var transcript = event.results[current][0].transcript;

        // Add the current transcript to the contents of our Note.
        // There is a weird bug on mobile, where everything is repeated twice.
        // There is no official solution so far so we have to handle an edge case.
        var mobileRepeatBug =
            current == 1 && transcript == event.results[0][0].transcript;

        if (!mobileRepeatBug) {
            noteContent += transcript;
            noteTextarea.val(noteContent);
        }
    };

    noteTextarea.on("input", function () {
        noteContent = $(this).val();
    });
}