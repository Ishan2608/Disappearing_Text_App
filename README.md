# Python Desktop Application - Disappearing Text Application
If you don't type anything for 5 seconds, text will disappear. Thus, when you are done typing, save your text.

<div>
  <img src="./disappearing_text.gif" alt="Code Output">
</div>

<hr>

<h1> Program Flowchart </h1>
<div>
  <img src="./Disappearing Text Flowchart.png" alt="Program Flowchart">
</div>

<hr>

<h1> Guide to Build this Project </h1>

<h2> Step 1: UI Setup </h2>
<p>
  First decide on the widgets to show to user in program window. First comes the heading, then instructions, a typing area and then tow buttons, one to reset app and one to save our text into a text document.
</p>

<h2> Step 2: Tracking User's Typed Text </h2>
<p>
  Bind the typing area to <em> <b> KepPress </b> </em> so that whenever, user starts typing, we can track it. The moment first character is entered, we start a timer.
  We will reset app after 5 seconds. When another key is pressed, before 5 seconds elapse, we cancel the timer, if it exists. However, if 5 seconds have elapsed, everything that user has typed, will be deleted.
</p>


<h2> Step 3: Reset App Button </h2>
<p>
  We link our reset app button with the same function that we call using timer to reset app, so that the user can do it himself, if he wants to.
</p>

<h2> Step 4: Save Button </h2>
<p>
  When user clicks on save button, first we check if he has written something, if not nothing happens. If he has written something, we see if a text file already exists, where his wrtieups are stored, if not we create one. We append the user text to this file.
</p>
