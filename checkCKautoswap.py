const exec = require('child_process').exec;

if(text.indexOf("cookie已失效")! =-1){
	exec('task raw_master_de.py', function(error, stdout, stderr){
		console.log(error, stdout, stderr)
	})
}