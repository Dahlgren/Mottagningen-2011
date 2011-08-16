var mainChart;
var groupChart;

var mainOptions;
var groupOptions;

var groupsDict = {};
var groupShowing;

var mainScores = [];

function requestMain() { 
    $.getJSON('/score/day/', function(series) {
        var groups = series['score'];
        var days = series['days'];
        
        $.each(days, function(index, name) {
            mainOptions.xAxis.categories.push(name);
        });
        
        $.each(groups, function(id, group) {
            $.each(group, function(name, scores) {
                groupsDict[name] = id;
                mainScores.push({
                    name: name,
                    data: scores
                });
            });  
        });
        
        mainChart = new Highcharts.Chart(mainOptions);
        $.each(mainScores, function(index, mainScore) {
            mainChart.addSeries(mainScore, true);
        });
    });
}

function requestGroup(id) {
    $.getJSON('/score/group/'+id, function(series) {
        var authors = series['score'];
        var colors = series['color'];
        $.each(authors, function(author, score) {
            groupChart.addSeries({
                name: author,
                data: score,
                color: colors[author]
            },true);
        });
    });
}

mainOptions = {
	chart: {
		renderTo: '{{ graph_div }}',
		defaultSeriesType: 'line'
	},
	credits: {
		enabled: false
	},
	title: {
		text: 'Kongliga Spelen'
	},
	xAxis: {
		categories: []
	},
	yAxis: {
		title: {
			text: 'Poäng'
		}
	},
    tooltip: {
        formatter: function() {
            return '<b>'+ this.series.name +'</b><br/>'+
            this.x +': '+ this.y;
        }
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -10,
        y: 100,
        borderWidth: 0
    },
	plotOptions: {
		series: {
			point: {
				events: {
					click: function() {
                        
					}
				}
			},
			events: {
			    // legendItemClick: function(event) {
			    //                   if(groupShowing != this.name) {
			    //                       groupShowing = this.name
			    //                       groupOptions.xAxis.categories = []
			    //                       groupOptions.xAxis.categories.push(this.name);
			    //                       groupChart = new Highcharts.Chart(groupOptions);
			    //                       requestGroup(groupsDict[this.name]);
			    //                   } else {
			    //                       groupShowing = ""
			    //                       $('#' + {{ group }}).html("");
			    //                   }
			    //                   return false;
			    //               }
			}
		}
	},
};

groupOptions = {
	chart: {
		renderTo: '{{ group_div }}',
		defaultSeriesType: 'bar',
	},
	credits: {
		enabled: false
	},
	title: {
		text: ''
	},
	xAxis: {
		categories: []
	},
	yAxis: {
		title: {
			text: 'Poäng'
		}
	},
    tooltip: {
        formatter: function() {
            return '<b>'+ this.series.name +'</b><br/>'+
            this.x +': '+ this.y;
        }
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -10,
        y: 100,
        borderWidth: 0
    },
	plotOptions: {
		series: {
			point: {
				events: {
					click: function() {
                        
					}
				}
			},
			events: {
			    legendItemClick: function(event) {
        			return false
			    }
			}
		}
	},
};

$(document).ready(function() {
    requestMain();	
});