var Twitter = require("twitter-lite");
var auth_keys = require("./auth"); //contains Twitter API authentication keys
var axios = require('axios');

const client = new Twitter(auth_keys, {
  subdomain: "api", // "api" is the default (change for other subdomains)
  version: "1.1", // version "1.1" is the default (change for other subdomains)
   });


const db_path = 'http://localhost:5000/database';
const sn_path = 'http://localhost:5000/usernamesLink';


axios.get(sn_path)
    .then((res) => {
        var user = res.data.screenNames.slice(-1)[0];
        //user last added is checked ^
        client.get("users/lookup",
                {screen_name: user })
                .then(results => {
                    axios.post(db_path, results)
                        .then((res) => {
                        console.log(user);
                      })
                      .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                      });

              })
              .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
              });

    })
    .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
    });