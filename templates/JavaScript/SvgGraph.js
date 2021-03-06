﻿var step = 0;
var todo = [];
var keep_moving = [true,true,true,true,true,true];


function Start(){
	for (var i=1; i<7; i++){
		BuildSvgGraph(i);
	}

	BuildSvgSingles(2);
	BuildSvgSingles(4);
	BuildSvgSingles(6);
	
	Move();
}

function Move()
{
	setTimeout(Move, 120);
	RedrawGraphs();
	step++;
	if (step>40){
		todo[1].g.physics = false;
		todo[3].g.physics = false;
		todo[5].g.physics = false;
	}
};

function StopMoving(id){
	keep_moving[id-1] = !keep_moving[id-1];
	alert(stop_move);
};

function MouseEvent(e){

	id = e.currentTarget.id[3];
	svg_graph=todo[id-1];

	if (svg_graph.g.is3D){return};

	if (e.type == "mousedown" || e.type == "touchstart"){
		svg_graph.g.SetDragged(mouseX(e)-svg_graph.hw, mouseY(e)-svg_graph.hh, 30);
		};
	if (e.type == "mousemove" || e.type == "touchmove"){
		svg_graph.g.MoveDragged	(mouseX(e)-svg_graph.hw, mouseY(e)-svg_graph.hh);
		};
	if (e.type == "mouseup" || e.type == "touchend"){
		svg_graph.g.StopDragging();
		};
	if (e.type == "touchmove"){
		e.preventDefault();
		};
};



function RedrawGraphs()
{
	for (var i = 0; i < todo.length; i++) {		
		if(keep_moving[i]) {
			todo[i].g.Iterate();
			Redraw(todo[i]);
		}
	}
}


function BuildSvgGraph(id)
{
	svg_id = "svg" + String(id);
	
	graph_spec = graph_specs[id-1];
	nodes_labels = graph_nodes_labels[id-1];
	nodes_size = graph_nodes_size[id-1];
	
	svg_element = document.getElementById(svg_id);

	svg_graph = new SvgGraph(svg_element, graph_spec, nodes_labels, nodes_size);

	
	if ( id==2 || id==4 || id==6 ){
		svg_graph.g.is3D = false;
		svg_graph.g.repulsion = 4*RepulsionSym;
		svg_graph.g.attraction = 0.001*AttractionSym;
		svg_graph.g.damping = 0.6;
	} else {
		svg_graph.g.is3D = true;
		svg_graph.g.repulsion = 4*Repulsion;
		svg_graph.g.attraction = 0.001*Attraction;
		svg_graph.g.damping = 0.6;
	};

	RebuildGraph(svg_graph);

	todo.push(svg_graph);	
	n = todo.length;

}

function SvgGraph(svg_element, spec, nodes_labels, nodes_size)
{

	this.spec = spec;
	this.svg = svg_element;
	
	var svg = this.svg;
	svg.addEventListener("mousedown", MouseEvent, false);
	svg.addEventListener("mousemove", MouseEvent, false);
	svg.addEventListener("mouseup", MouseEvent, false);
	
	svg.addEventListener("touchmove", MouseEvent, false);	
	svg.addEventListener("touchstart", MouseEvent, false);
	svg.addEventListener("touchend", MouseEvent, false);
	svg.addEventListener("touchmove", MouseEvent, false);
	
	
	this.c3d = { camz : 900, ang:0, d:0.003 };
	
	this.circs = [];
	this.lines = [];
	this.labls = [];
	this.labels_text = nodes_labels;
	
	this.w = Width-20;
	this.h = Height-20;
	this.hw= this.w/2;
	this.hh= this.h/2;
	this.labels = true;
	this.nodes_size = nodes_size;
	
	this.g = new Grapher2D();
	this.g.stable = false;
	this.g.physics = true;
	this.g.SetBounds(-this.hw,this.hw,-this.hh,this.hh,-this.hw,this.hw);
	
}

ChangeLabels = function(svg_graph) 
{
	svg_graph.labels = !svg_graph.labels;
	for(var i=0; i<svg_graph.labls.length; i++) svg_graph.labls[i].style.visibility = (svg_graph.labels?"visible":"hidden");
}

MinColoring = function(svg_graph) 
{
	svg_graph.g.MinColoring();
	for(var i=0; i<svg_graph.circs.length; i++)
		svg_graph.circs[i].setAttribute("fill", colors[svg_graph.g.vcolors[i]%colors.length]);
}

function RebuildGraph(svg_graph)
{

	svg_graph.g.MakeGraph(svg_graph.spec);
	
	var svg = svg_graph.svg;
	
	for(var i=0; i<svg_graph.circs.length; i++) svg.removeChild(this.circs[i]);
	for(var i=0; i<svg_graph.lines.length; i++) svg.removeChild(this.lines[i]);
	for(var i=0; i<svg_graph.labls.length; i++) svg.removeChild(this.labls[i]);
	svg_graph.circs = [];
	svg_graph.lines = [];
	svg_graph.labls = [];
	
	for(i=0; i<svg_graph.g.graph.edgesl.length; i++)
	{
		var l = document.createElementNS("http://www.w3.org/2000/svg", "line");
		l.setAttribute("style", "stroke:#000055;stroke-width:1");
		svg.appendChild(l);
		svg_graph.lines.push(l);
	}
	for(i=0; i<svg_graph.g.graph.n; i++)
	{
		var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
		var title = document.createElementNS("http://www.w3.org/2000/svg", "title");
		title.textContent = getName(svg_graph.labels_text[i]);
		c.appendChild(title);

		if(svg_graph.labels_text[i]=='1'){
			if (svg_graph.g.is3D){
				c.setAttribute("fill", "url(#GradientBoss)");
			} else {
				c.setAttribute("fill", "RGB(255,251,75)");
			};
		}else{
			if (svg_graph.g.is3D){
				c.setAttribute("fill", "url(#GradientAll)");
			} else {
				c.setAttribute("fill", "RGB(215,215,225)");
			};
		};	

		svg.appendChild(c);
		svg_graph.circs.push(c);
		
		var t = document.createElementNS("http://www.w3.org/2000/svg", "text");
		t.setAttribute("fill", "#000000");
		t.setAttribute("font-size", "13");
		t.setAttribute("style",  "pointer-events:none;");
		t.setAttribute("class", "GraphLabel");
		t.textContent = svg_graph.labels_text[i];
		svg.appendChild(t);
		svg_graph.labls.push(t);
	}
	
	Redraw(svg_graph);
};

function Redraw(svg_graph)
{
	//if(g.is3D) g.vertices.sort(sorter);
	
	var c3d = svg_graph.c3d;
	var g = svg_graph.g;

	
	c3d.ang += c3d.d;
	var sn = Math.sin(svg_graph.c3d.ang);
	var cs = Math.cos(svg_graph.c3d.ang);

	var hw = svg_graph.hw, hh = svg_graph.hh;

	for(var i=0; i<g.graph.n; i++)
	{
		var nx, ny, nz;
		var v = g.vertices[i];
		if(g.is3D)
		{
			nx = cs*v.x - sn*v.z;
			nz = sn*v.x + cs*v.z;
			ny = v.y;
		}
		else {nx = v.x; ny = v.y; nz = v.z;}
		v.px = c3d.camz*nx/(c3d.camz - nz);
		v.py = c3d.camz*ny/(c3d.camz - nz);
		v.pz = nz;

		// observe the borders
		if(v.px < -hw+15){v.px = -hw + 15};
		if(v.py < -hh+15){v.py = -hh + 15};
		if(v.px > hw-15){v.px = hw - 15};
		if(v.py > hh-15){v.py = hh - 15};
	};
	
	var num_edges = g.graph.edgesl.length;
	
	var N_switch = 120;
	var delta = 20;
	var selected = Math.floor(step/N_switch) % g.graph.n;
	var sel_step = step % N_switch;
	var fraction;
	if (sel_step <= delta){ fraction = sel_step / delta };
	if (sel_step > delta) { fraction = 1 };
	if (sel_step >= N_switch - delta){ fraction = (N_switch-sel_step)/delta };
	
	for(i=0; i<num_edges; i++)
	{
		var u_num = g.graph.edgesl[i];
		var v_num = g.graph.edgesr[i];
		var u = g.vertices[u_num];
		var v = g.vertices[v_num];
		
		if(g.is3D){

			if (u_num == selected || v_num==selected){
				brgh1 = String(57 + Math.round((255-57)*fraction));
				brgh2 = String(101 + Math.round((255-101)*fraction));
				line_color = "RGB(77," + brgh1 + "," + brgh2 + ")";
				stroke_width = "1.3";
			} else {
				line_color = "RGB(77,111,111)";		
				stroke_width = "1";
			};
		} else {
			line_color = "RGB(0,0,0)";		
			stroke_width = "1";
		};
		
		svg_graph.lines[i].setAttribute("style", "stroke:" + line_color + ";stroke-width:" + stroke_width);
		
		svg_graph.lines[i].setAttribute("x1", u.px + hw);
		svg_graph.lines[i].setAttribute("y1", u.py + hh);
		svg_graph.lines[i].setAttribute("x2", v.px + hw);
		svg_graph.lines[i].setAttribute("y2", v.py + hh);
	};
	
	var dr, circle_style;
	for(var i=0; i<g.graph.n; i++)
	{
		var v = g.vertices[i];
		
		if(g.is3D){
			if (i==selected){
				circle_color = "RGB(77,255,255)";
				stroke_width = String(1.1 + fraction*0.2);
			} else {
				circle_color = "RGB(121,121,121)";	
				for(edge=0; edge<num_edges; edge++)
				{
					var u_num = g.graph.edgesl[edge];
					var v_num = g.graph.edgesr[edge];
					if( ((u_num == selected && v_num == i) || (v_num == selected && u_num == i)) 
						&& (sel_step < N_switch - delta) && (sel_step > delta) ){
						circle_color = "RGB(210,255,255)";	
					}
				};
				stroke_width = "1";
			};
			circle_style ="stroke:" + circle_color + ";stroke-width:" + stroke_width;
		} else {
			circle_color = "RGB(0,0,0)";		
			stroke_width = "1";
			circle_style ="stroke:" + circle_color + ";stroke-width:" + stroke_width + ";cursor:move;";
		};

		svg_graph.circs[i].setAttribute("style", circle_style);
		
		svg_graph.circs[i].setAttribute("cx", hw+v.px);
		svg_graph.circs[i].setAttribute("cy", hh+v.py);
		svg_graph.circs[i].setAttribute("r", svg_graph.nodes_size[i]);
		
		dr = 4 + (svg_graph.labels_text[i].length - 1)*3;
		svg_graph.labls[i].setAttribute("x", hw+v.px-dr);
		svg_graph.labls[i].setAttribute("y", hh+v.py+5);
	}
};


function getEl(s)
{
	return document.getElementById(s);
}


function getName(id)
{
	names_list_table = getEl("NamesList");
	row_index = parseInt(id)+1;
	res = names_list_table.rows[row_index].cells[1].textContent; 
	return res;
}


function mouseX(e)
{

	id = e.currentTarget.id[3];
	svg_graph=todo[id-1];

	var cx;
	if(e.type == "touchstart" || e.type == "touchmove") {
		cx = e.touches.item(0).clientX;
	} else {
		cx = e.clientX;
	};

	rect = svg_graph.svg.getBoundingClientRect();
	return (cx-rect.left);
}

function mouseY(e)
{	
	id = e.currentTarget.id[3];
	svg_graph=todo[id-1];

	var cy;
	if(e.type == "touchstart" || e.type == "touchmove")	{
		cy = e.touches.item(0).clientY;
	} else {
		cy = e.clientY;
	};

	rect = svg_graph.svg.getBoundingClientRect();
	return (cy-rect.top); 
}


function BuildSvgSingles(id)
{

	svg = getEl("svg"+String(id)+"a");
	total = graph_nodes_labels[0].length;
	used_labels = graph_nodes_labels[id-1];

	labels = [];
	for (i=1; i <= total; i++){
		used = false;
		for (j=0; j<used_labels.length; j++){
			used = used || (used_labels[j] == String(i));
		};
		if (!used){ labels.push(i); };
	};

	size = labels.length;

	width = 370; radius = 9; 
	x_dist = 30; x_offset = 15; 
	y_dist = 30; y_offset = 15;
	max_in_row = Math.floor((width - x_offset)/x_dist);
	rows = Math.floor((size-1)/ max_in_row) + 1;
	height = y_offset + (rows - 1) * y_dist + radius + 1;
	svg.setAttribute("height", String(height));

	for (i=0; i<size; i++){
		var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
		var title = document.createElementNS("http://www.w3.org/2000/svg", "title");
		title.textContent = getName(labels[i]);
		c.appendChild(title);

		if(labels[i]==1){
				c.setAttribute("fill", "RGB(255,251,75)");
		}else{
				c.setAttribute("fill", "RGB(215,215,225)");
		};	
	
		
		x = (i % max_in_row) * x_dist + x_offset;
		row = Math.floor(i / max_in_row) ;
		y = y_offset + row * y_dist;
		
		
		c.setAttribute("cx", x);
		c.setAttribute("cy", y);
		c.setAttribute("r", radius);
		circle_color = "RGB(0,0,0)";		
		stroke_width = "1";
		circle_style ="stroke:" + circle_color + ";stroke-width:" + stroke_width ;
		c.setAttribute("style", circle_style);
		svg.appendChild(c);

		var t = document.createElementNS("http://www.w3.org/2000/svg", "text");
		var label = String(labels[i]);
		var dr = 0 + label.length*3;
		
		t.setAttribute("fill", "#000000");
		t.setAttribute("font-size", "11");
		t.setAttribute("style",  "pointer-events:none;");
		t.setAttribute("class", "GraphLabel");
		t.setAttribute("x", x-dr);
		t.setAttribute("y", y+4);
		
		t.textContent = label;
		svg.appendChild(t);

	}
}
