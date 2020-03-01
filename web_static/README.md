#0x01. AirBnB clone - Web static

This is a Holberton School project to Static Web (HTML and CSS).
Concepts explored:

##What is HTML
##How to create an HTML page
##What is a markup language
##What is the DOM
##What is an element / tag
##What is an attribute
##How does the browser load a webpage
##What is CSS
##How to add style to an element
##What is a class
##What is a selector
##How to compute CSS Specificity Value
##What are Box properties in CSS##What is localhost/127.0.0.1

##Content:
0-index.html: Write an HTML page that displays a header and a footer. Using Inline styling
- Body: no margin, no padding
- Header: color #FF0000 (red), height: 70px, width: 100%.
- Footer: color #00FF00 (green), height: 60px, width: 100%
- text Holberton School center vertically and horizontally, always at the bottom at the page
1-index.html: Write an HTML page that displays a header and a footer same format as 0-index.html, by using the style tag in the head tag.
2-index.html, styles/2-common.css, styles/2-header.css, styles/2-footer.cssCSS files: Write an HTML page that displays a header and a footer by using CSS files (same as 1-index.html)
3-3-index.html, styles/3-common.css, styles/3-header.css, styles/3-footer.css, images/: page that displays a header and footer by using CSS files (same as 2-index.html)
Layout: Common (no margin, no padding, font color: #484848, font size: 14px, font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif; icon in the browser tab
Header: (color: white, height: 70px, width: 100%, border bottom 1px #CCCCCC, logo align on left and center vertically (20px space at the left))
Footer: (color white, height: 60px, width: 100%, border top 1px #CCCCCC, text Holberton School center vertically and horizontally, always at the bottom at the page
4-4-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/4-filters.css, images/: Write an HTML page that displays a header, footer and a filters box with a search button.
Layout: (based on 3-index.html)
Container:(between header and footer tags, add a div, classname: container, max width 1000px, margin top and bottom 30px - it should be 30px under the bottom of the header (screenshot)
center horizontally)
Filter section: (tag section, classname filters, inside the .container, color white, height: 70px, width: 100% of the container, border 1px #DDDDDD with radius 4px)
Button search: (tag button, text Search, font size: 18px, inside the section filters, background color #FF5A5F, text color #FFFFFF, height: 48px, width: 20% of the section filters
no borders, border radius: 4px, center vertically and at 30px of the right border, change opacity to 90% when the mouse is on the buttonSearch)
5-5-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/5-filters.css, images/: (Write an HTML page that displays a header, footer and a filters box.
Layout: (based on 4-index.html)
Locations and Amenities filters: (tag: div, classname: locations for location tag and amenities for the other, inside the section filters (same level as the button Search)
height: 100% of the section filters, width: 25% of the section filters, border right #DDDDDD 1px only for the first left filter)
contains a title: (tag: h3, font weight: 600, text States or Amenities)
contains a subtitle: (tag: h4, font weight: 400, font size: 14px, text with fake contents)
6- 6-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, images/: Write an HTML page that displays a header, footer and a filters box with dropdown.
Layout: (based on 5-index.html)
Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter div: (tag ul, classname popover, text should be fake now
inside each div, not displayed by default, color #FAFAFA, width same as the div filter, border #DDDDDD 1px with border radius 4px, no list display
Location filter has 2 levels of ul/li: state -> cities)
7-7-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/7-places.css, images/: (Write an HTML page that displays a header, footer, a filters box with dropdown and results, Layout: (based on 6-index.html), Add Places section, tag section, classname: places, contains a title (tag: h1), text: Places, font size: 30px, contains multiple “Places” as listing (horizontal or vertical) describe by: 
tag: article
width: 390px
padding and margin 20px
border #FF5A5F 1px with radius 4px
contains the place name: 
tag: h2
font size: 30px
center horizontally)
8-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/8-places.css, images/:(Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.
Layout: (based on 7-index.html)
Add more information to a Place article:
Price by night: 
tag: div
classname: price_by_night
same level as the place name
font color: #FF5A5F
border: #FF5A5F 4px rounded
min width: 60px
height: 60px
font size: 30px
align: the top right (with space)
Information section: 
tag: div
classname: information
height: 80px
border: top and bottom #DDDDDD 1px
contains (align vertically): 
Number of guests: 
tag: div
classname: max_guest
width: 100px
fake text
icon
Number of bedrooms: 
tag: div
classname: number_rooms
width: 100px
fake text
icon
Number of bathrooms: 
tag: div
classname: number_bathrooms
width: 100px
fake text
icon
User section: 
tag: div
classname: user
text Owner: <fake text>
Owner text should be in bold
Description section: 
tag: div
classname: description)

# Usage
Educational purposes
