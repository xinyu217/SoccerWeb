var w = 1050, h = 680, r = 120;
var middleX = 525, middleY = 340;

var isXChecked = true,
isYChecked = true;

var width = 300,
height = 200,
dragbarw = 20;

// this specifies the svg container
// is this the canvas?
var svg = d3.select("body").append("svg")
.attr("width", w)
.attr("height", h)



//maybe plot the court here? Just the outline first?
// outline of the court
var outlineCourt = svg.append("rect").attr("x", 0).attr("y", 0).attr("width", 1050).attr("height", 680).attr("fill-opacity", 0).attr("stroke-width", 8).attr("stroke", "black");

// halfcourt line
var line1 = svg.append("line").attr("x1", 525).attr("y1", 0).attr("x2", 525).attr("y2", 680).attr("stroke-width", 4).attr("stroke", "black");

// 18 yard box
var line18yard11 = svg.append("line").attr("x1", 0).attr("y1",middleY-200.15).attr("x2",165).attr("y2",middleY-200.15).attr("stroke-width", 4).attr("stroke", "black");
var line18yard12 = svg.append("line").attr("x1", 0).attr("y1",middleY+200.15).attr("x2",165).attr("y2",middleY+200.15).attr("stroke-width", 4).attr("stroke", "black");
var line18yard13 = svg.append("line").attr("x1", 165).attr("y1",middleY-200.15).attr("x2",165).attr("y2",middleY+200.15).attr("stroke-width", 4).attr("stroke", "black");

var line18yard21 = svg.append("line").attr("x1", w).attr("y1",middleY-200.15).attr("x2",w-165).attr("y2",middleY-200.15).attr("stroke-width", 4).attr("stroke", "black");
var line18yard22 = svg.append("line").attr("x1", w).attr("y1",middleY+200.15).attr("x2",w-165).attr("y2",middleY+200.15).attr("stroke-width", 4).attr("stroke", "black");
var line18yard23 = svg.append("line").attr("x1", w-165).attr("y1",middleY-200.15).attr("x2",w-165).attr("y2",middleY+200.15).attr("stroke-width", 4).attr("stroke", "black");


// 6 yard box
var line6yard11 = svg.append("line").attr("x1", 0).attr("y1",middleY-128.2).attr("x2",55).attr("y2",middleY-128.2).attr("stroke-width", 4).attr("stroke", "black");
var line6yard12 = svg.append("line").attr("x1", 0).attr("y1",middleY+128.2).attr("x2",55).attr("y2",middleY+128.2).attr("stroke-width", 4).attr("stroke", "black");
var line6yard13 = svg.append("line").attr("x1", 55).attr("y1",middleY-128.2).attr("x2",55).attr("y2",middleY+128.2).attr("stroke-width", 4).attr("stroke", "black");

var line6yard11 = svg.append("line").attr("x1", w).attr("y1",middleY-128.2).attr("x2",w-55).attr("y2",middleY-128.2).attr("stroke-width", 4).attr("stroke", "black");
var line6yard12 = svg.append("line").attr("x1", w).attr("y1",middleY+128.2).attr("x2",w-55).attr("y2",middleY+128.2).attr("stroke-width", 4).attr("stroke", "black");
var line6yard13 = svg.append("line").attr("x1", w-55).attr("y1",middleY-128.2).attr("x2",w-55).attr("y2",middleY+128.2).attr("stroke-width", 4).attr("stroke", "black");

// penalty spots
var penCircle1 = svg.append("circle").attr("cx", 115).attr("cy", 340).attr("r",2).attr("stroke-width", 4).attr("stroke", "black").attr("fill","none");
var penCircle2 = svg.append("circle").attr("cx", w-115).attr("cy", 340).attr("r",2).attr("stroke-width", 4).attr("stroke", "black").attr("fill","none");

// circle -> on box
var arc = d3.svg.arc().innerRadius(91.5).outerRadius(95.5).startAngle(0.55).endAngle(2.6) //just radians
var arc1 = svg.append("path").attr("d", arc).attr("transform", "translate(115,340)")
var arc2 = d3.svg.arc().innerRadius(91.5).outerRadius(95.5).startAngle(-0.55).endAngle(-2.6) //just radians
var arc3 = svg.append("path").attr("d", arc2).attr("transform", "translate(935,340)")


// center circle
var centerCircle1 = svg.append("circle").attr("cx", 525).attr("cy", 340).attr("r",91.5).attr("stroke-width", 4).attr("stroke", "black").attr("fill","none");
var centerCircle2 = svg.append("circle").attr("cx", 525).attr("cy", 340).attr("r",2).attr("stroke-width", 4).attr("stroke", "black").attr("fill","none");

// put in the STATS logo
var g = svg.append("g");

var img = g.append("svg:image")
.attr("xlink:href", "/static/statslogo.png")
.attr("width", 100)
.attr("height", 100)
.attr("x", 300)
.attr("y",-20);

var img = g.append("svg:image")
.attr("xlink:href", "/static/statslogo.png")
.attr("width", 100)
.attr("height", 100)
.attr("x", 640)
.attr("y",580);


//var drag = d3.behavior.drag()
//.on('dragstart', function() { circle.style('fill', 'yellow'); })
//.on('drag', function() { circle.attr('cx', d3.event.x)
//    .attr('cy', d3.event.y); })
//.on('dragend', function() { circle.style('fill', 'red'); });

var drag = d3.behavior.drag()
.origin(function(d) { return d; })
.on("dragstart", dragstarted)
.on("drag", dragged)
.on("dragend", dragended);


// homeTeam
var homeTeamA01 = svg.selectAll('.draggableCircleHomeA01')
.data([{ x: 120, y: 300, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleHomeA01')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'yellow').style("opacity", 1);

var homeTeamA02 = svg.selectAll('.draggableCircleHomeA02')
.data([{ x: 250, y: 100, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleHomeA02')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'red').style("opacity", 1);

var homeTeamA03 = svg.selectAll('.draggableCircleHomeA03')
.data([{ x: 250, y: 250, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleHomeA03')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'red').style("opacity", 1);

var homeTeamA04 = svg.selectAll('.draggableCircleHomeA04')
.data([{ x: 250, y: 350, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleHomeA04')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'red').style("opacity", 1);

var homeTeamA05 = svg.selectAll('.draggableCircleHomeA05')
.data([{ x: 250, y: 500, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleHomeA05')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'red').style("opacity", 1);

var homeTeamA06 = svg.selectAll('.draggableCircleHomeA06')
.data([{ x: 350, y: 300, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleHomeA06')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'red').style("opacity", 1);

var homeTeamA07 = svg.selectAll('.draggableCircleHomeA07')
.data([{ x: 350, y: 400, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleHomeA07')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'red').style("opacity", 1);

var homeTeamA08 = svg.selectAll('.draggableCircleHomeA08')
.data([{ x: 400, y: 340, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleHomeA08')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'red').style("opacity", 1);

var homeTeamA09 = svg.selectAll('.draggableCircleHomeA09')
.data([{ x: 500, y: 100, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleHomeA09')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'red').style("opacity", 1);

var homeTeamA10 = svg.selectAll('.draggableCircleHomeA10')
.data([{ x: 500, y: 400, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleHomeA10')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'red').style("opacity", 1);

var homeTeamA11 = svg.selectAll('.draggableCircleHomeA11')
.data([{ x: 500, y: 600, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleHomeA11')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'red').style("opacity", 1);


// awayTeam
var awayTeamB01 = svg.selectAll('.draggableCircleAwayB01')
.data([{ x: 900, y: 300, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleAwayB01')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'cyan').style("opacity", 1);

var awayTeamB02 = svg.selectAll('.draggableCircleAwayB02')
.data([{ x: 800, y: 600, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleAwayB02')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'blue').style("opacity", 1);

var awayTeamB03 = svg.selectAll('.draggableCircleAwayB03')
.data([{ x: 800, y: 450, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleAwayB03')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'blue').style("opacity", 1);

var awayTeamB04 = svg.selectAll('.draggableCircleAwayB04')
.data([{ x: 800, y: 250, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleAwayB04')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'blue').style("opacity", 1);

var awayTeamB05 = svg.selectAll('.draggableCircleAwayB05')
.data([{ x: 800, y: 100, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleAwayB05')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'blue').style("opacity", 1);

var awayTeamB06 = svg.selectAll('.draggableCircleAwayB06')
.data([{ x: 700, y: 400, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleAwayB06')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'blue').style("opacity", 1);

var awayTeamB07 = svg.selectAll('.draggableCircleAwayB07')
.data([{ x: 700, y: 300, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleAwayB07')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'blue').style("opacity", 1);

var awayTeamB08 = svg.selectAll('.draggableCircleAwayB08')
.data([{ x: 650, y: 340, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleAwayB08')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'blue').style("opacity", 1);

var awayTeamB09 = svg.selectAll('.draggableCircleAwayB09')
.data([{ x: 550, y: 500, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleAwayB09')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'blue').style("opacity", 1);

var awayTeamB10 = svg.selectAll('.draggableCircleAwayB10')
.data([{ x: 550, y: 300, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleAwayB10')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'blue').style("opacity", 1);

var awayTeamB11 = svg.selectAll('.draggableCircleAwayB11')
.data([{ x: 550, y: 100, r: 10}]).enter().append('svg:circle')
.attr('class', 'draggableCircleAwayB11')
.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
.call(drag).style('fill', 'blue').style("opacity", 1);




// awayTeam
//var awayTeamPG = svg.selectAll('.draggableCircleAwayPG')
//.data([{ x: 650, y: 150, r: 15}]).enter().append('svg:circle')
//.attr('class', 'draggableCircleAwayPG')
//.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
//.call(drag).style('fill', 'blue');
//
//var awayTeamSG = svg.selectAll('.draggableCircleAwaySG')
//.data([{ x: 650, y: 350, r: 15}]).enter().append('svg:circle')
//.attr('class', 'draggableCircleAwaySG')
//.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
//.call(drag).style('fill', 'blue');
//
//var awayTeamC = svg.selectAll('.draggableCircleAwayC')
//.data([{ x: 800, y: 250, r: 15}]).enter().append('svg:circle')
//.attr('class', 'draggableCircleAwayC')
//.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
//.call(drag).style('fill', 'blue');
//
//var awayTeamSF = svg.selectAll('.draggableCircleAwaySF')
//.data([{ x: 800, y: 150, r: 15}]).enter().append('svg:circle')
//.attr('class', 'draggableCircleAwaySF')
//.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
//.call(drag).style('fill', 'blue');
//
//var awayTeamPF = svg.selectAll('.draggableCircleAwayPF')
//.data([{ x: 800, y: 350, r: 15}]).enter().append('svg:circle')
//.attr('class', 'draggableCircleAwayPF')
//.attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; })
//.call(drag).style('fill', 'blue');


var ballObj = svg.selectAll('.draggableCircleBall')
.data([{ x: 600, y: 240, r: 10}])
.enter()
.append('svg:circle')
.attr('class', 'draggableCircleBall')
.attr('cx', function(d) { return d.x; })
.attr('cy', function(d) { return d.y; })
.attr('r', function(d) { return d.r; })
.call(drag)
.style('fill', 'orange');


// make a global variable here - specify the intial position here...
trajVec = [];
trajVecHomeA01 = [homeTeamA01.attr("cx"), homeTeamA01.attr("cy") ];
trajVecHomeA02 = [homeTeamA02.attr("cx"), homeTeamA02.attr("cy") ];
trajVecHomeA03 = [homeTeamA03.attr("cx"), homeTeamA03.attr("cy") ];
trajVecHomeA04 = [homeTeamA04.attr("cx"), homeTeamA04.attr("cy") ];
trajVecHomeA05 = [homeTeamA05.attr("cx"), homeTeamA05.attr("cy") ];

trajVecAwayB01 = [awayTeamB01.attr("cx"), awayTeamB01.attr("cy") ];
trajVecAwayB02 = [awayTeamB02.attr("cx"), awayTeamB02.attr("cy") ];
trajVecAwayB03 = [awayTeamB03.attr("cx"), awayTeamB03.attr("cy") ];
trajVecAwayB04 = [awayTeamB04.attr("cx"), awayTeamB04.attr("cy") ];
trajVecAwayB05 = [awayTeamB05.attr("cx"), awayTeamB05.attr("cy") ];

trajVecBall = [ballObj.attr("cx"), ballObj.attr("cy") ];

//This is the accessor function for all players
var lineFunctionHomeA01 = d3.svg.line().x(function(d) { return d.x; }).y(function(d) { return d.y; }).interpolate("linear");
var lineFunctionHomeA02 = d3.svg.line().x(function(d) { return d.x; }).y(function(d) { return d.y; }).interpolate("linear");
var lineFunctionHomeA03 = d3.svg.line().x(function(d) { return d.x; }).y(function(d) { return d.y; }).interpolate("linear");
var lineFunctionHomeA04 = d3.svg.line().x(function(d) { return d.x; }).y(function(d) { return d.y; }).interpolate("linear");
var lineFunctionHomeA05 = d3.svg.line().x(function(d) { return d.x; }).y(function(d) { return d.y; }).interpolate("linear");

var lineFunctionAwayB01 = d3.svg.line().x(function(d) { return d.x; }).y(function(d) { return d.y; }).interpolate("linear");
var lineFunctionAwayB02 = d3.svg.line().x(function(d) { return d.x; }).y(function(d) { return d.y; }).interpolate("linear");
var lineFunctionAwayB03 = d3.svg.line().x(function(d) { return d.x; }).y(function(d) { return d.y; }).interpolate("linear");
var lineFunctionAwayB04 = d3.svg.line().x(function(d) { return d.x; }).y(function(d) { return d.y; }).interpolate("linear");
var lineFunctionAwayB05 = d3.svg.line().x(function(d) { return d.x; }).y(function(d) { return d.y; }).interpolate("linear");

var lineFunctionBall = d3.svg.line().x(function(d) { return d.x; }).y(function(d) { return d.y; }).interpolate("linear");


function dragstarted(d) {
    d3.event.sourceEvent.stopPropagation();
    d3.select(this).classed("dragging", true);
    trajVec = [];
    trajVec.push(d.x, d.y);
}

function dragged(d) {
    d3.select(this).attr("cx", d.x = d3.event.x).attr("cy", d.y = d3.event.y);
    // we can save the array here?
    trajVec.push(d.x, d.y);
}

function dragended(d) {
    d3.select(this).classed("dragging", false);
    // we can plot the line here?
    trajVec.push(d.x, d.y)
    // go through each point...
    // assign this to the player selected
    var someDom = d3.select(this)[0][0];

    // can we plot the trajectory here
    console.log(trajVec.length)
    // set the lines, so when we redraw, we update the line instead of keeping it there
    var lineData = [], lineDataBall = [];
    var lineDataHomeA01 = [], lineDataHomeA02 = [], lineDataHomeA03 = [], lineDataHomeA04 = [], lineDataHomeA05 = [];
    var lineDataAwayB01 = [], lineDataAwayB02 = [], lineDataAwayB03 = [], lineDataAwayB04 = [], lineDataAwayB05 = [];
    
    //This is the accessor function
    //var lineFunction = d3.svg.line()
    //.x(function(d) { return d.x; })
    //.y(function(d) { return d.y; })
    //.interpolate("linear");
    

    for (i = 0; i < trajVec.length; i+=2) {
        lineData.push({"x":trajVec[i], "y":trajVec[i+1]});
    }
    
    console.log(d3.select(this).attr("class"))
    
    // homeTeamVec
    if (d3.select(this).attr("class") == "draggableCircleHomeA01"){
        d3.select("svg").selectAll("#homeTrajA01").remove();
        trajVecHomeA01 = trajVec;
        lineDataHomeA01 = lineData;
        //The line SVG Path we draw
        var lineGraphHomePG = svg.append("path").attr("d", lineFunctionHomePG(lineDataHomePG)).attr("stroke", "red").attr("stroke-width", 2).attr("fill", "none").attr("id", "homeTrajA01");
    }
    
    if (d3.select(this).attr("class") == "draggableCircleHomeA02"){
        d3.select("svg").selectAll("#homeTrajA02").remove();
        trajVecHomeA02 = trajVec;
        lineDataHomeA02 = lineData;
        //
        console.log("WHY BLUE");
        //The line SVG Path we draw
        var lineGraphHomeSG = svg.append("path").attr("d", lineFunctionHomeSG(lineDataHomeSG)).attr("stroke", "red").attr("stroke-width", 2).attr("fill", "none").attr("id", "homeTrajA02");
    }
    
    if (d3.select(this).attr("class") == "draggableCircleHomeA03"){
        d3.select("svg").selectAll("#homeTrajA03").remove();
        trajVecHomeA03 = trajVec;
        lineDataHomeA03 = lineData;
        var lineGraphHomeA03 = svg.append("path").attr("d", lineFunctionHomeA03(lineDataHomeA03)).attr("stroke", "red").attr("stroke-width", 2).attr("fill", "none").attr("id", "homeTrajA03");
    }
    
    if (d3.select(this).attr("class") == "draggableCircleHomeA04"){
        d3.select("svg").selectAll("#homeTrajA04").remove();
        trajVecHomeA04 = trajVec;
        lineDataHomeA04 = lineData;
        //The line SVG Path we draw
        var lineGraphHomeA04 = svg.append("path").attr("d", lineFunctionHomeA04(lineDataHomeA04)).attr("stroke", "red").attr("stroke-width", 2).attr("fill", "none").attr("id", "homeTrajA04");
    }
    
    if (d3.select(this).attr("class") == "draggableCircleHomeA05"){
        d3.select("svg").selectAll("#homeTrajA05").remove();
        trajVecHomeA05 = trajVec;
        lineDataHomeA05 = lineData;
        //The line SVG Path we draw
        var lineGraphHomeA05 = svg.append("path").attr("d", lineFunctionHomeA05(lineDataHomeA05)).attr("stroke", "red").attr("stroke-width", 2).attr("fill", "none").attr("id", "homeTrajA05");
    }
    
    // awayTeamVec
    if (d3.select(this).attr("class") == "draggableCircleAwayB01"){
        d3.select("svg").selectAll("#awayTrajB01").remove();
        trajVecAwayB01 = trajVec;
        lineDataAwayB01 = lineData;
        //The line SVG Path we draw
        var lineGraphAwayB01 = svg.append("path").attr("d", lineFunctionAwayB01(lineDataAwayB01)).attr("stroke", "blue").attr("stroke-width", 2).attr("fill", "none").attr("id", "awayTrajB01");
    }
    
    if (d3.select(this).attr("class") == "draggableCircleAwayB02"){
        d3.select("svg").selectAll("#awayTrajB02").remove();
        trajVecAwayB02 = trajVec;
        lineDataAwayB02 = lineData;
        //The line SVG Path we draw
        var lineGraphAwayB02 = svg.append("path").attr("d", lineFunctionAwayB02(lineDataAwayB02)).attr("stroke", "blue").attr("stroke-width", 2).attr("fill", "none").attr("id", "awayTrajB02");
    }
    
    if (d3.select(this).attr("class") == "draggableCircleAwayB03"){
        d3.select("svg").selectAll("#awayTrajB03").remove();
        trajVecAwayB03 = trajVec;
        lineDataAwayB03 = lineData;
        //The line SVG Path we draw
        var lineGraphAwayB03 = svg.append("path").attr("d", lineFunctionAwayB03(lineDataAwayB03)).attr("stroke", "blue").attr("stroke-width", 2).attr("fill", "none").attr("id", "awayTrajB03");
    }
    
    if (d3.select(this).attr("class") == "draggableCircleAwayB04"){
        d3.select("svg").selectAll("#awayTrajB04").remove();
        trajVecAwayB04 = trajVec;
        lineDataAwayB04 = lineData;
        //The line SVG Path we draw
        var lineGraphAwayB04 = svg.append("path").attr("d", lineFunctionAwayB04(lineDataAwayB04)).attr("stroke", "blue").attr("stroke-width", 2).attr("fill", "none").attr("id", "awayTrajB04")
    };
    
    if (d3.select(this).attr("class") == "draggableCircleAwayB05"){
        d3.select("svg").selectAll("#awayTrajB05").remove();
        trajVecAwayB05 = trajVec;
        lineDataAwayB05 = lineData;
        //The line SVG Path we draw
        var lineGraphAwayB05 = svg.append("path").attr("d", lineFunctionAwayB05(lineDataAwayB05)).attr("stroke", "blue").attr("stroke-width", 2).attr("fill", "none").attr("id", "awayTrajB05");
    }
    
    if (d3.select(this).attr("class") == "draggableCircleBall"){
        d3.select("svg").selectAll("#ballTraj").remove();
        trajVecBall = trajVec;
        lineDataBall = lineData;
        //The line SVG Path we draw
        var lineGraphBall = svg.append("path").attr("d", lineFunctionBall(lineDataBall)).attr("stroke", "orange").attr("stroke-width", 2).attr("fill", "none").attr("id", "ballTraj");
    }
    
    
}


function plotRetrievedPlays(data) {

    // ---------- A01 -----------
    var homeA01 = (data.homeA01);
    // now let's plot
    lineData = [];
    console.log(homeA01)
    for (i = 0; i < homeA01.length; i++) {
        // need to add 525 to x and 340 to y
        lineData.push({"x":homeA01[i][0]+525, "y":homeA01[i][1]+340});
    }
    endPoint = lineData[lineData.length-1];
    
    lineGraph = svg.append("path").attr("d", lineFunctionHomeA01(lineData)).attr("stroke", "red").attr("stroke-width", 2).attr("fill", "none").attr("id", "homeTrajA01");
    // plot the circle
    var homeTeamA01 = svg.selectAll('.draggableCircleHomeA01').data([{ x: endPoint["x"], y: endPoint["y"], r: 15}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA01').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');

    // ---------- A02 -----------
    var homeA02 = (data.homeA02);
    // now let's plot
    lineData = [];
    for (i = 0; i < homeA02.length; i++) {
        lineData.push({"x":homeA02[i][0]+525, "y":homeA02[i][1]+340});
        
    }
    endPoint = lineData[lineData.length-1];

    lineGraph = svg.append("path").attr("d", lineFunctionHomeA02(lineData)).attr("stroke", "red").attr("stroke-width", 2).attr("fill", "none").attr("id", "homeTrajA02");
    // plot the circle
    var homeTeamA02 = svg.selectAll('.draggableCircleHomeA02').data([{ x: endPoint["x"], y: endPoint["y"], r: 15}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA02').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');
    
    
    // ---------- A03 -----------
    var homeA03 = (data.homeA03);
    // now let's plot
    lineData = [];
    for (i = 0; i < homeA03.length; i++) {
        lineData.push({"x":homeA03[i][0]+525, "y":homeA03[i][1]+340});
        
    }
    
    endPoint = lineData[lineData.length-1];
    
    lineGraph = svg.append("path").attr("d", lineFunctionHomeC(lineData)).attr("stroke", "red").attr("stroke-width", 2).attr("fill", "none").attr("id", "homeTrajA03");
    // plot the circle
    var homeTeamA03 = svg.selectAll('.draggableCircleHomeA03').data([{ x: endPoint["x"], y: endPoint["y"], r: 15}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA03').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');

    
    
    // ---------- A04 -----------
    var homeA04 = (data.homeA04);
    // now let's plot
    lineData = [];
    for (i = 0; i < homeA04.length; i++) {
        lineData.push({"x":homeA04[i][0]+525, "y":homeA04[i][1]+340});
        
    }
    endPoint = lineData[lineData.length-1];
    
    lineGraph = svg.append("path").attr("d", lineFunctionHomeA04(lineData)).attr("stroke", "red").attr("stroke-width", 2).attr("fill", "none").attr("id", "homeTrajA04");
    // plot the circle
    var homeTeamA04 = svg.selectAll('.draggableCircleHomeA04').data([{ x: endPoint["x"], y: endPoint["y"], r: 15}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA04').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');
    
    
    // ---------- A05 -----------
    var homeA05 = (data.homeA05);
    // now let's plot
    lineData = [];
    for (i = 0; i < homeA05.length; i++) {
        lineData.push({"x":homeA05[i][0]+525, "y":homeA05[i][1]+340});
        
    }
    
    endPoint = lineData[lineData.length-1];
    
    lineGraph = svg.append("path").attr("d", lineFunctionHomePF(lineData)).attr("stroke", "red").attr("stroke-width", 2).attr("fill", "none").attr("id", "homeTrajA05");
    // plot the circle
    var homeTeamA05 = svg.selectAll('.draggableCircleHomeA05').data([{ x: endPoint["x"], y: endPoint["y"], r: 15}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA05').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');
    
//    // AWAY TEAM
//    // ---------- PG -----------
//    var awayPG = (data.awayPG);
//    // now let's plot
//    lineData = [];
//    for (i = 0; i < awayPG.length; i++) {
//        lineData.push({"x":awayPG[i][0]*10, "y":awayPG[i][1]*10});
//        
//    }
//    
//    endPoint = lineData[lineData.length-1];
//    
//    lineGraph = svg.append("path").attr("d", lineFunctionAwayPG(lineData)).attr("stroke", "blue").attr("stroke-width", 2).attr("fill", "none").attr("id", "awayTrajPG");
//    // plot the circle
//    var awayTeamPG = svg.selectAll('.draggableCircleAwayPG').data([{ x: endPoint["x"], y: endPoint["y"], r: 15}]).enter().append('svg:circle').attr('class', 'draggableCircleAwayPG').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    // ---------- SG -----------
//    var awaySG = (data.awaySG);
//    // now let's plot
//    lineData = [];
//    for (i = 0; i < awaySG.length; i++) {
//        lineData.push({"x":awaySG[i][0]*10, "y":awaySG[i][1]*10});
//        
//    }
//    
//    endPoint = lineData[lineData.length-1];
//    
//    lineGraph = svg.append("path").attr("d", lineFunctionAwaySG(lineData)).attr("stroke", "blue").attr("stroke-width", 2).attr("fill", "none").attr("id", "awayTrajSG");
//    // plot the circle
//    var awayTeamSG = svg.selectAll('.draggableCircleAwaySG').data([{ x: endPoint["x"], y: endPoint["y"], r: 15}]).enter().append('svg:circle').attr('class', 'draggableCircleAwaySG').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    
//    // ---------- C -----------
//    var awayC = (data.awayC);
//    // now let's plot
//    lineData = [];
//    for (i = 0; i < awayC.length; i++) {
//        lineData.push({"x":awayC[i][0]*10, "y":awayC[i][1]*10});
//        
//    }
//    
//    endPoint = lineData[lineData.length-1];
//    
//    lineGraph = svg.append("path").attr("d", lineFunctionAwayC(lineData)).attr("stroke", "blue").attr("stroke-width", 2).attr("fill", "none").attr("id", "awayTrajC");
//    // plot the circle
//    var awayTeamC = svg.selectAll('.draggableCircleAwayC').data([{ x: endPoint["x"], y: endPoint["y"], r: 15}]).enter().append('svg:circle').attr('class', 'draggableCircleAwayC').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    
//    
//    // ---------- SF -----------
//    var awaySF = (data.awaySF);
//    // now let's plot
//    lineData = [];
//    for (i = 0; i < awaySF.length; i++) {
//        lineData.push({"x":awaySF[i][0]*10, "y":awaySF[i][1]*10});
//        
//    }
//    
//    endPoint = lineData[lineData.length-1];
//    
//    lineGraph = svg.append("path").attr("d", lineFunctionHomeSF(lineData)).attr("stroke", "blue").attr("stroke-width", 2).attr("fill", "none").attr("id", "awayTrajSF");
//    // plot the circle
//    var awayTeamC = svg.selectAll('.draggableCircleAwaySF').data([{ x: endPoint["x"], y: endPoint["y"], r: 15}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeSF').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    
//    // ---------- PF -----------
//    var awayPF = (data.awayPF);
//    // now let's plot
//    lineData = [];
//    for (i = 0; i < awayPF.length; i++) {
//        lineData.push({"x":awayPF[i][0]*10, "y":awayPF[i][1]*10});
//        
//    }
//    
//    endPoint = lineData[lineData.length-1];
//    
//    lineGraph = svg.append("path").attr("d", lineFunctionHomePF(lineData)).attr("stroke", "blue").attr("stroke-width", 2).attr("fill", "none").attr("id", "awayTrajPF");
//    // plot the circle
//    var awayTeamPF = svg.selectAll('.draggableCircleAwayPF').data([{ x: endPoint["x"], y: endPoint["y"], r: 15}]).enter().append('svg:circle').attr('class', 'draggableCircleHomePF').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    
//    // ---------- Ball -----------
//    var ballInfo = (data.ballInfo);
//    // now let's plot
//    lineData = [];
//    for (i = 0; i < ballInfo.length; i++) {
//        lineData.push({"x":ballInfo[i][0]*10, "y":ballInfo[i][1]*10});
//        
//    }
//    
//    endPoint = lineData[lineData.length-1];
//    
//    lineGraph = svg.append("path").attr("d", lineFunctionBall(lineData)).attr("stroke", "orange").attr("stroke-width", 2).attr("fill", "none").attr("id", "ballTraj");
//    // plot the circle
//    ballTraj = svg.selectAll('.draggableCircleBall').data([{ x: endPoint["x"], y: endPoint["y"], r: 15}]).enter().append('svg:circle').attr('class', 'draggableCircleBall').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'orange');
    

}


function plotPlayerPos(data,role_flag) {
    

    
    
//    var text = svg.selectAll("text")
//    .data([{ x: (data['A01_X']*10)+525, y: (data['A01_Y']*10)+340, r: 10}])
//    .enter()
//    .append("text");
//    
//    var textLabels = text
//                    .attr("cx", function(d) { return d.cx; })
//                    .attr("cy", function(d) { return d.cy; })
//                    .text( function (d) { return "( " + d.cx + ", " + d.cy +" )"; })
//                    .attr("font-family", "sans-serif")
//                    .attr("font-size", "20px")
//                    .attr("fill", "red");
    

    

    
    // ---------- A01 -----------
    // plot the circle
//    var homeTeamA01 = svg.selectAll('.draggableCircleHomeA01').data([{ x: (data['A01_X']*10)+525, y: (data['A01_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA01').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');
//    
//     var homeTeamA02 = svg.selectAll('.draggableCircleHomeA02').data([{ x: (data['A02_X']*10)+525, y: (data['A02_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA02').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');
//    
//    var homeTeamA03 = svg.selectAll('.draggableCircleHomeA03').data([{ x: (data['A03_X']*10)+525, y: (data['A03_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA03').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');
//    
//    var homeTeamA04 = svg.selectAll('.draggableCircleHomeA04').data([{ x: (data['A04_X']*10)+525, y: (data['A04_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA04').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');
//    
//    var homeTeamA05 = svg.selectAll('.draggableCircleHomeA05').data([{ x: (data['A05_X']*10)+525, y: (data['A05_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA05').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');
//    
//    var homeTeamA06 = svg.selectAll('.draggableCircleHomeA06').data([{ x: (data['A06_X']*10)+525, y: (data['A06_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA06').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');
//    
//    var homeTeamA07 = svg.selectAll('.draggableCircleHomeA01').data([{ x: (data['A07_X']*10)+525, y: (data['A07_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA07').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');
//    
//    var homeTeamA08 = svg.selectAll('.draggableCircleHomeA08').data([{ x: (data['A08_X']*10)+525, y: (data['A08_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA08').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');
//    
//    var homeTeamA09 = svg.selectAll('.draggableCircleHomeA09').data([{ x: (data['A09_X']*10)+525, y: (data['A09_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA09').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');
//    
//    var homeTeamA10 = svg.selectAll('.draggableCircleHomeA10').data([{ x: (data['A10_X']*10)+525, y: (data['A10_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA10').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');
//    
//    var homeTeamA11 = svg.selectAll('.draggableCircleHomeA11').data([{ x: (data['A11_X']*10)+525, y: (data['A11_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeA11').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'red');
//    
//    var awayTeamB01 = svg.selectAll('.draggableCircleAwayB01').data([{ x: (data['B01_X']*10)+525, y: (data['B01_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleHomeB01').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    var awayTeamB02 = svg.selectAll('.draggableCircleAwayB02').data([{ x: (data['B02_X']*10)+525, y: (data['B02_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleAwayB02').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    var awayTeamB03 = svg.selectAll('.draggableCircleAwayB03').data([{ x: (data['B03_X']*10)+525, y: (data['B03_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleAwayB03').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    var awayTeamB04 = svg.selectAll('.draggableCircleAwayB04').data([{ x: (data['B04_X']*10)+525, y: (data['B04_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleAwayB04').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    var awayTeamB05 = svg.selectAll('.draggableCircleAwayB05').data([{ x: (data['B05_X']*10)+525, y: (data['B05_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleAwayB05').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    var awayTeamB06 = svg.selectAll('.draggableCircleAwayB06').data([{ x: (data['B06_X']*10)+525, y: (data['B06_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleAwayB06').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    var awayTeamB07 = svg.selectAll('.draggableCircleAwayB07').data([{ x: (data['B07_X']*10)+525, y: (data['B07_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleAwayB07').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    var awayTeamB08 = svg.selectAll('.draggableCircleAwayB08').data([{ x: (data['B08_X']*10)+525, y: (data['B08_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleAwayB08').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    var awayTeamB09 = svg.selectAll('.draggableCircleAwayB09').data([{ x: (data['B09_X']*10)+525, y: (data['B09_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleAwayB09').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    var awayTeamB10 = svg.selectAll('.draggableCircleAwayB10').data([{ x: (data['B10_X']*10)+525, y: (data['B10_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleAwayB10').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');
//    
//    var awayTeamB11 = svg.selectAll('.draggableCircleAwayB11').data([{ x: (data['B11_X']*10)+525, y: (data['B11_Y']*10)+340, r: 10}]).enter().append('svg:circle').attr('class', 'draggableCircleAwayB11').attr('cx', function(d) { return d.x; }).attr('cy', function(d) { return d.y; }).attr('r', function(d) { return d.r; }).call(drag).style('fill', 'blue');

    
    
    
    var p = svg.selectAll("circle")
        .data([{ "cx": (data['A01_X']*10)+525, "cy": (data['A01_Y']*10)+340, "radius": 10, "color": 'blue'},
               { "cx": (data['A02_X']*10)+525, "cy": (data['A02_Y']*10)+340, "radius": 10, "color": 'blue'},
               { "cx": (data['A03_X']*10)+525, "cy": (data['A03_Y']*10)+340, "radius": 10, "color": 'blue'},
               { "cx": (data['A04_X']*10)+525, "cy": (data['A04_Y']*10)+340, "radius": 10, "color": 'blue'},
               { "cx": (data['A05_X']*10)+525, "cy": (data['A05_Y']*10)+340, "radius": 10, "color": 'blue'},
               { "cx": (data['A06_X']*10)+525, "cy": (data['A06_Y']*10)+340, "radius": 10, "color": 'blue'},
               { "cx": (data['A07_X']*10)+525, "cy": (data['A07_Y']*10)+340, "radius": 10, "color": 'blue'},
               { "cx": (data['A08_X']*10)+525, "cy": (data['A08_Y']*10)+340, "radius": 10, "color": 'blue'},
               { "cx": (data['A09_X']*10)+525, "cy": (data['A09_Y']*10)+340, "radius": 10, "color": 'blue'},
               { "cx": (data['A10_X']*10)+525, "cy": (data['A10_Y']*10)+340, "radius": 10, "color": 'blue'},
               { "cx": (data['A11_X']*10)+525, "cy": (data['A11_Y']*10)+340, "radius": 10, "color": 'blue'},
               { "cx": (data['B01_X']*10)+525, "cy": (data['B01_Y']*10)+340, "radius": 10, "color": 'red'},
               { "cx": (data['B02_X']*10)+525, "cy": (data['B02_Y']*10)+340, "radius": 10, "color": 'red'},
               { "cx": (data['B03_X']*10)+525, "cy": (data['B03_Y']*10)+340, "radius": 10, "color": 'red'},
               { "cx": (data['B04_X']*10)+525, "cy": (data['B04_Y']*10)+340, "radius": 10, "color": 'red'},
               { "cx": (data['B05_X']*10)+525, "cy": (data['B05_Y']*10)+340, "radius": 10, "color": 'red'},
               { "cx": (data['B06_X']*10)+525, "cy": (data['B06_Y']*10)+340, "radius": 10, "color": 'red'},
               { "cx": (data['B07_X']*10)+525, "cy": (data['B07_Y']*10)+340, "radius": 10, "color": 'red'},
               { "cx": (data['B08_X']*10)+525, "cy": (data['B08_Y']*10)+340, "radius": 10, "color": 'red'},
               { "cx": (data['B09_X']*10)+525, "cy": (data['B09_Y']*10)+340, "radius": 10, "color": 'red'},
               { "cx": (data['B10_X']*10)+525, "cy": (data['B10_Y']*10)+340, "radius": 10, "color": 'red'},
               { "cx": (data['B11_X']*10)+525, "cy": (data['B11_Y']*10)+340, "radius": 10, "color": 'red'}
           ])
        .enter()
        .append("circle");
    
    var circleAttributes = p
        .attr("cx", function (d) { return d.cx; })
        .attr("cy", function (d) { return d.cy; })
        .attr("r", function (d) { return d.radius; })
        .style("fill", function (d) { return d.color; });
    
    
   
    // display players name
    //-----------------------------------------------------------------------------------//
    var str1 = "Frame: ";
    var str2 = Math.round(data['time']*10)/10;
    var f = str1.concat(str2);
    
    if (role_flag==false){
        var text = svg.selectAll("text")
        .data([{ "cx": (data['A01_X']*10)+480, "cy": (data['A01_Y']*10)+310, "radius": 10, "name": data['A01_Name']},
               { "cx": (data['A02_X']*10)+480, "cy": (data['A02_Y']*10)+310, "radius": 10, "name": data['A02_Name']},
               { "cx": (data['A03_X']*10)+480, "cy": (data['A03_Y']*10)+310, "radius": 10, "name": data['A03_Name']},
               { "cx": (data['A04_X']*10)+480, "cy": (data['A04_Y']*10)+310, "radius": 10, "name": data['A04_Name']},
               { "cx": (data['A05_X']*10)+480, "cy": (data['A05_Y']*10)+310, "radius": 10, "name": data['A05_Name']},
               { "cx": (data['A06_X']*10)+480, "cy": (data['A06_Y']*10)+310, "radius": 10, "name": data['A06_Name']},
               { "cx": (data['A07_X']*10)+480, "cy": (data['A07_Y']*10)+310, "radius": 10, "name": data['A07_Name']},
               { "cx": (data['A08_X']*10)+480, "cy": (data['A08_Y']*10)+310, "radius": 10, "name": data['A08_Name']},
               { "cx": (data['A09_X']*10)+480, "cy": (data['A09_Y']*10)+310, "radius": 10, "name": data['A09_Name']},
               { "cx": (data['A10_X']*10)+480, "cy": (data['A10_Y']*10)+310, "radius": 10, "name": data['A10_Name']},
               { "cx": (data['A11_X']*10)+480, "cy": (data['A11_Y']*10)+310, "radius": 10, "name": data['A11_Name']},
               { "cx": (data['B01_X']*10)+480, "cy": (data['B01_Y']*10)+310, "radius": 10, "name": data['B01_Name']},
               { "cx": (data['B02_X']*10)+480, "cy": (data['B02_Y']*10)+310, "radius": 10, "name": data['B02_Name']},
               { "cx": (data['B03_X']*10)+480, "cy": (data['B03_Y']*10)+310, "radius": 10, "name": data['B03_Name']},
               { "cx": (data['B04_X']*10)+480, "cy": (data['B04_Y']*10)+310, "radius": 10, "name": data['B04_Name']},
               { "cx": (data['B05_X']*10)+480, "cy": (data['B05_Y']*10)+310, "radius": 10, "name": data['B05_Name']},
               { "cx": (data['B06_X']*10)+480, "cy": (data['B06_Y']*10)+310, "radius": 10, "name": data['B06_Name']},
               { "cx": (data['B07_X']*10)+480, "cy": (data['B07_Y']*10)+310, "radius": 10, "name": data['B07_Name']},
               { "cx": (data['B08_X']*10)+480, "cy": (data['B08_Y']*10)+310, "radius": 10, "name": data['B08_Name']},
               { "cx": (data['B09_X']*10)+480, "cy": (data['B09_Y']*10)+310, "radius": 10, "name": data['B09_Name']},
               { "cx": (data['B10_X']*10)+480, "cy": (data['B10_Y']*10)+310, "radius": 10, "name": data['B10_Name']},
               { "cx": (data['B11_X']*10)+480, "cy": (data['B11_Y']*10)+310, "radius": 10, "name": data['B11_Name']},
               { "cx": 40, "cy": 40, "radius":10, "name": f}
               ])
        .enter()
        .append("text");
    }else{
        var text = svg.selectAll("text")
        .data([{ "cx": (data['A01_X']*10)+510, "cy": (data['A01_Y']*10)+310, "radius": 10, "name": data['A01_Role']},
               { "cx": (data['A02_X']*10)+510, "cy": (data['A02_Y']*10)+310, "radius": 10, "name": data['A02_Role']},
               { "cx": (data['A03_X']*10)+510, "cy": (data['A03_Y']*10)+310, "radius": 10, "name": data['A03_Role']},
               { "cx": (data['A04_X']*10)+510, "cy": (data['A04_Y']*10)+310, "radius": 10, "name": data['A04_Role']},
               { "cx": (data['A05_X']*10)+510, "cy": (data['A05_Y']*10)+310, "radius": 10, "name": data['A05_Role']},
               { "cx": (data['A06_X']*10)+510, "cy": (data['A06_Y']*10)+310, "radius": 10, "name": data['A06_Role']},
               { "cx": (data['A07_X']*10)+510, "cy": (data['A07_Y']*10)+310, "radius": 10, "name": data['A07_Role']},
               { "cx": (data['A08_X']*10)+510, "cy": (data['A08_Y']*10)+310, "radius": 10, "name": data['A08_Role']},
               { "cx": (data['A09_X']*10)+510, "cy": (data['A09_Y']*10)+310, "radius": 10, "name": data['A09_Role']},
               { "cx": (data['A10_X']*10)+510, "cy": (data['A10_Y']*10)+310, "radius": 10, "name": data['A10_Role']},
               { "cx": (data['A11_X']*10)+510, "cy": (data['A11_Y']*10)+310, "radius": 10, "name": data['A11_Role']},
               { "cx": (data['B01_X']*10)+510, "cy": (data['B01_Y']*10)+310, "radius": 10, "name": data['B01_Role']},
               { "cx": (data['B02_X']*10)+510, "cy": (data['B02_Y']*10)+310, "radius": 10, "name": data['B02_Role']},
               { "cx": (data['B03_X']*10)+510, "cy": (data['B03_Y']*10)+310, "radius": 10, "name": data['B03_Role']},
               { "cx": (data['B04_X']*10)+510, "cy": (data['B04_Y']*10)+310, "radius": 10, "name": data['B04_Role']},
               { "cx": (data['B05_X']*10)+510, "cy": (data['B05_Y']*10)+310, "radius": 10, "name": data['B05_Role']},
               { "cx": (data['B06_X']*10)+510, "cy": (data['B06_Y']*10)+310, "radius": 10, "name": data['B06_Role']},
               { "cx": (data['B07_X']*10)+510, "cy": (data['B07_Y']*10)+310, "radius": 10, "name": data['B07_Role']},
               { "cx": (data['B08_X']*10)+510, "cy": (data['B08_Y']*10)+310, "radius": 10, "name": data['B08_Role']},
               { "cx": (data['B09_X']*10)+510, "cy": (data['B09_Y']*10)+310, "radius": 10, "name": data['B09_Role']},
               { "cx": (data['B10_X']*10)+510, "cy": (data['B10_Y']*10)+310, "radius": 10, "name": data['B10_Role']},
               { "cx": (data['B11_X']*10)+510, "cy": (data['B11_Y']*10)+310, "radius": 10, "name": data['B11_Role']},
               { "cx": 40, "cy": 40, "radius":10, "name": f}
               ])
        .enter()
        .append("text");
    }

    
    //Add SVG Text Element Attributes
    var PlayerName = text
    .attr("x", function(d) { return d.cx; })
    .attr("y", function(d) { return d.cy; })
    .text(function (d) { return d.name; })
    .attr("font-family", "sans-serif")
    .attr("font-size", "25px")
    .attr("fill", "black");
    //-----------------------------------------------------------------------------------//
    

}


function plotRolePos(data) {
    console.log("test");


    var c = ['red','green','blue','black','yellow','violet','tomato','slateblue','Sienna','seagreen','salmon'];
    var temp = [];

    
    
    for (i = 0; i < data.Frame.length; i++) {
        ux = data.Frame[i]['ux'];
        uy = data.Frame[i]['uy'];
        obj = { "cx": ((data.Frame[i]['A01_X']-ux)*10)+525, "cy": ((data.Frame[i]['A01_Y']-uy)*10)+340, "radius": 5, "color": c[data.Frame[i]['A01_Role']]}
        temp.push(obj)
        obj = { "cx": ((data.Frame[i]['A02_X']-ux)*10)+525, "cy": ((data.Frame[i]['A02_Y']-uy)*10)+340, "radius": 5, "color": c[data.Frame[i]['A02_Role']]}
        temp.push(obj)
        obj = { "cx": ((data.Frame[i]['A03_X']-ux)*10)+525, "cy": ((data.Frame[i]['A03_Y']-uy)*10)+340, "radius": 5, "color": c[data.Frame[i]['A03_Role']]}
        temp.push(obj)
        obj = { "cx": ((data.Frame[i]['A04_X']-ux)*10)+525, "cy": ((data.Frame[i]['A04_Y']-uy)*10)+340, "radius": 5, "color": c[data.Frame[i]['A04_Role']]}
        temp.push(obj)
        obj = { "cx": ((data.Frame[i]['A05_X']-ux)*10)+525, "cy": ((data.Frame[i]['A05_Y']-uy)*10)+340, "radius": 5, "color": c[data.Frame[i]['A05_Role']]}
        temp.push(obj)
        obj = { "cx": ((data.Frame[i]['A06_X']-ux)*10)+525, "cy": ((data.Frame[i]['A06_Y']-uy)*10)+340, "radius": 5, "color": c[data.Frame[i]['A06_Role']]}
        temp.push(obj)
        obj = { "cx": ((data.Frame[i]['A07_X']-ux)*10)+525, "cy": ((data.Frame[i]['A07_Y']-uy)*10)+340, "radius": 5, "color": c[data.Frame[i]['A07_Role']]}
        temp.push(obj)
        obj = { "cx": ((data.Frame[i]['A08_X']-ux)*10)+525, "cy": ((data.Frame[i]['A08_Y']-uy)*10)+340, "radius": 5, "color": c[data.Frame[i]['A08_Role']]}
        temp.push(obj)
        obj = { "cx": ((data.Frame[i]['A09_X']-ux)*10)+525, "cy": ((data.Frame[i]['A09_Y']-uy)*10)+340, "radius": 5, "color": c[data.Frame[i]['A09_Role']]}
        temp.push(obj)
        obj = { "cx": ((data.Frame[i]['A10_X']-ux)*10)+525, "cy": ((data.Frame[i]['A10_Y']-uy)*10)+340, "radius": 5, "color": c[data.Frame[i]['A10_Role']]}
        temp.push(obj)
        obj = { "cx": ((data.Frame[i]['A11_X']-ux)*10)+525, "cy": ((data.Frame[i]['A11_Y']-uy)*10)+340, "radius": 5, "color": c[data.Frame[i]['A11_Role']]}
        temp.push(obj)
        
    }

    
    var p = svg.selectAll("circle")
    .data(temp)
    .enter()
    .append("circle");
    
    var circleAttributes = p
    .attr("cx", function (d) { return d.cx; })
    .attr("cy", function (d) { return d.cy; })
    .attr("r", function (d) { return d.radius; })
    .style("fill", function (d) { return d.color; });

}





