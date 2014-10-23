function main(){
	var svg2png = require('/home/virtwww/w_rost_8baa4f5f/convert/node_modules/svg2png');
	var async = require('/home/virtwww/w_rost_8baa4f5f/convert/node_modules/async');	
	var fs = require('fs');
	
	var path = 'todo';
	var names = fs.readdirSync(path);
	var current_dir = '';
	var sourceImg = ''
	var destImg = '';
	
	for (var i=0; i<names.length; i++){
		if (fs.statSync('todo/'+names[i]).isDirectory()){
			console.log(names[i]);
			current_dir = 'todo/'+names[i];
			
			var png_names = fs.readdirSync(current_dir + '/png');
			console.log(png_names);
			
			if (png_names.length == 0) {

				var svg_names = fs.readdirSync(current_dir + '/svg');
				async.each(svg_names, function(item, callback) {
					setTimeout(function() {
						console.log('>', item);
						sourceImg = current_dir + '/svg/' + item;
						destImg = current_dir + '/png/' + item + '.png';
						console.log(sourceImg + ', ' + destImg);
						svg2png(sourceImg, destImg, function (err) {console.log(item); if(err){console.log('Convert Error');} else {console.log('Finally done');}});
						callback();
					}, (Math.random())* 50000);
					}, function(err) {
					if(err){
						console.log('> Error');
					} else {
						console.log('> ALL COMPLETE');
					}
				});
				console.log(':)');
			}
			
		};
	};
};

main();
