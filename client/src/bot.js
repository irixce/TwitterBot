var Twitter = require("twitter-lite");
var auth_keys = require("./auth"); //contains Twitter API authentication keys

const client = new Twitter(auth_keys, {
  subdomain: "api", // "api" is the default (change for other subdomains)
  version: "1.1", // version "1.1" is the default (change for other subdomains)
   });

client.get("users/lookup",
    {screen_name: "whatsupshqipe" })
    .then(results => {
        console.log("results", results[0]["protected"]);
    }).catch(console.error);