#!/usr/bin/node
// Scrip that display the status code of get request
const request = require('request');
const url = process.argv.slice(2)[0];
if (url){
	request.get(url, (e, res) => {
		if (!err){
		consol.log('code: ' + res && res.statuscode);
		}
	});
}
