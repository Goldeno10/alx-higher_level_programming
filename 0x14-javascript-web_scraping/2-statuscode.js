#!/usr/bin/node
// Scrip that display the status code of get request
const request = require('request');
const url = process.argv[2];
if (url){
	request(url, (e, res) => {
		if (!err){
		consol.log('code: ' + res && res.statuscode);
		}
	});
}
