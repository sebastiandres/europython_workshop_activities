# Quarto Slides Template

## Installation

Install quarto using the instructions on the [official documentation](https://quarto.org/docs/get-started/).

Install the pyodide extension:

```bash
quarto add coatless-quarto/pyodide
```

## Official documentation
The official documentation is:
* [https://quarto.org/docs/presentations/revealjs/ ](Reveal basics)
* [https://quarto.org/docs/presentations/revealjs/presenting.html ](Presenting slides)
* [https://quarto.org/docs/presentations/revealjs/advanced.html ](Advanced reveal)
* [https://quarto.org/docs/presentations/revealjs/themes.html ](Reveal themes)

## Personalizations

### Updating the theme and transition
For the transitions, choose from: none, fade, slide, convex, concave, zoom

For the theme, choose from: simple, black, beige, blood, dark, default, league, moon, night, serif, simple, sky, solarized

Personally, I think that fade and simple are the best combination.


## html and pdf Outputs

Executing the makefile should produce the html. Make sure to read the terminal output, the errors tend to be descriptive enough to fix or google them.

$ make render

To create the pdf, open the html file and press the "E" key. Then, print the page using the regular print screen and export as a pdf.

The html presentation can be displayed directly from github, if you set the repo as a github page. You will need to set embed-resourses to true so the html page for the slides is self-contained and does not break any weird local dependency.

Additional advice: As a presenter, I prefer to deactivate the options toc, controls, menu and slide number (value false) to avoid visual distractions. While sharing the presentation slides, I prefer to set them as true to facilitate the exploration of the slides (as the speaker won't be able to explain).  

## Presenting
Press "S" key to show speaker notes. They should be a new, separate tab on your browser.

## Other
* Use &#32; as the blank/empty space on html, when you need to "fill" a property without showing a character.
* Use <br> to do linebreaks on html
* You can always wrap your markdown with ::: to define a div, to which you can apply any property. This is very powerfull (but sometimes hard to debug, so don't overuse it).