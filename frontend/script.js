const ndc_x = 0.3;
const ndc_y = -0.6;

const screen_width = 800;
const screen_height = 600;

const screen_x = (ndc_x + 1) * (screen_width / 2);
const screen_y = (-ndc_y + 1) * (screen_height / 2);

const svg = document.getElementById("cartesian-plane");

const dottedLineX = document.createElementNS("http://www.w3.org/2000/svg", "line");
dottedLineX.setAttribute("x1", 0);
dottedLineX.setAttribute("y1", screen_y);
dottedLineX.setAttribute("x2", screen_x);
dottedLineX.setAttribute("y2", screen_y);
dottedLineX.setAttribute("class", "dotted-line");
svg.appendChild(dottedLineX);

const dottedLineY = document.createElementNS("http://www.w3.org/2000/svg", "line");
dottedLineY.setAttribute("x1", screen_x);
dottedLineY.setAttribute("y1", 0);
dottedLineY.setAttribute("x2", screen_x);
dottedLineY.setAttribute("y2", screen_y);
dottedLineY.setAttribute("class", "dotted-line");
svg.appendChild(dottedLineY);

const point = document.createElementNS("http://www.w3.org/2000/svg", "circle");
point.setAttribute("cx", screen_x);
point.setAttribute("cy", screen_y);
point.setAttribute("r", 5);
point.setAttribute("class", "point");
svg.appendChild(point);
