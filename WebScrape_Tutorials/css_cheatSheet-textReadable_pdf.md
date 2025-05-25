
"C:\Users\Ben\OneDrive\Documents\Gaba_Docs\development\Python\Python_Ben\gitProject\WebScrape_Tutorials\css_cheatSheet-textReadable.pdf"

class                   bin                         Selects all elements with class="btn
#id                     #myButton                   Selects the element with id="myButton
*                       *                           Selects all elements
element                 h1                          Selects all <h1> elements
element,element         div, p                      Selects all <div> elements and all <p> elements
element element         div p                       Selects all <p> elements inside <div> elements
elemen > element        div>p                       Selects all <p> elements where the parent is a <div> element
elemer\i+element
element1~element2
div+p
p~uI
Selects all <p> elements that are placed directly after <div> elements
Selects every <ul> element that is preceded by a <p> element
[attribute]
[attribute=value]
Selects all elements with [data-toggle] a data-toggle attribute
[data-toggle=dropdown] Selects all elements with data-toggle="dropdown"
[attribute~=value] [ti'tle~=cheatsheet] Seieds all elements with a title attribute containing the word "cheatsheet"
[attribute=value]
[attribute"=value]
[Iangl=en]
a[href"="htlps"]
Selects all elements with a lang attribute value starting with "en"
Selects every <a> element whose href attribute value begins with "https"
[attribu1e$=value]
[attribute*=value]
a[href$=".ly"]
a[href*="welcm"]
Selects every <a> element whose href attribute value ends with ".ly"
Selects every <a> element whose href attribute value contains the substring "welcm"
:active a:active Selects the active link
::after p::after Insert something after the content of each <p> element
::before
:checked
p::before
input:checked
Insert something before the content of each <p> element
Selects every checked <inpu1> element
:default input:defauI1 Selects the default <input> element
:disabled buttorudisabled Selects every disabled <button> element
:empty p:empty Selects every <p> element that has no children (including text nodes)
:enabled
:first-child
Er\put:enabled
p:first-child
Selects every enabled <input> element
Selects every <p> element that is the first child of its parent
::first-letter p::first-letter Selects the first letter of every <p> element
::first-line p::first-line Selects the first line of every <p> element
:first-of-type
:focus
p:first-of-type
input:focus
Selects every <p> element that is the first <p> element of its parent
Selects the input element that has focus
i
:hover a:hover Selects links on mouse over
:in-range input:in-range Selects input elements with a value within a specified range
:indeterminate input:indeterminate Selects input elements that are in an indeterminate state
:invalid
:lang(Ianguage)
input:invalid
p:Iang(en)
Selects all input elements with an invalid value
Selects every <p> element with a lang attribute equal to "en" (English)
:last-child
:last-of-type
p:Iast-child
p:last-of-type
Selects every <p> element that is the last child of its parent
Selects every <p> element that is the last <p> element of its parent
:link a:link Selects all unvisited links
:not(selector) :not(h1) Selects every element that is not an <h1> element
:nth-child(n)
:nth-last-child(n)
:nth-last-of-type(n)
:r\'lh-of-typ€(n)
p:nth-child(3)
p:nth-last-child(3)
p:nth-last-of-type(3)
p:nth-of-type(3)
Selects every <p> element that is the third child of its parent
Selects every <p> element that is the third child of its parent, counting from the last
child
Selects every <p> element that is the third <p> element of its parent, counting from
the last child
Selects every <p> element that is the third <p> element of its parent
:only-of-type
:only-child
p:only-of-type
p:only-child
Selects every <p> element that is the only <p> element of its parent
Selects every <p> element that is the only child of its parent
:optional input:optionaI Selects input elements with no "required" attribute
:out-of-range input:out-of-range Selects input elements with a value outside a specified range
::placeholder
:read-only
ir\put::placeholder
inputread-only
Selects input elements with placeholder text
Selects input elements that have the "readonly" attribute specified
:read-write input:read-write Selects input elements that do not have the "readonly" attribute specified
:required
:root
ir\put:required
:root
Selects input elements with the "required" attribute specified
Selects the root element of the document
::selection
:target
:valid
:visited
::selection
#cheatsheettargei
input:valid
a:visited
Selects the portion of an element that is selected by a user
Selects the current active #cheatsheet element (clicked on a URL containing that
anchor name)
Selects all input elements with a valid value
Selects all visited links