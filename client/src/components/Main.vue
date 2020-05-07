<template>
  <div>
    <h1>Enter screen names:</h1>

    <img class=RefreshButton src="../assets/refresh.png" height="60px" width="60px" v-on:click="Refresh">

    <div class="Search">
      <input class="InputBox" v-model="screen_name" placeholder="" >
      <img  class=AddButton src="../assets/addB.png" height="36px" width="36px" v-on:click="addUserName(screen_name)">
    </div>

    <br>

    <span v-for="(sn,  index) in screen_names" :key="index">
        <ScreenName v-bind:sn="sn"></ScreenName>
    </span>
    <br>
    <br>

    <span v-show="isValid">
         <button class="SearchButton" v-on:click="Search">Search</button>
    </span>
    <br>
    <br>
    <span v-for="(follower,  index) in common_followers" :key="index">
      <p class="Follower"> {{follower}} </p>
    </span>

    <span v-show="noCommonFollowers">
         <p> Sorry, no common followers for these users. </p>
    </span>
  </div>
</template>

<script>
  import axios from 'axios';
  import ScreenName from "./ScreenName";
  import { EventBus } from '../event-bus.js';


  export default {
  name: 'Main',
  data() {
    return {
      screen_name: '',
      screen_names: [],
      isValid: false,
      isProtected: true,
      common_followers: [],
      noCommonFollowers: false,
    }
  },
  methods: {
    getUserNames() {
      const path = 'http://localhost:5000/usernamesLink';
      axios.get(path)
              .then((res) => {
                this.screen_names = res.data.screenNames;
                this.checkValid(this.screen_names);
                console.log(this.screen_names);
              })
              .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
              });
    },
    Search() {
      const path = 'http://localhost:5000/followers';
      axios.get(path)
              .then((res) => {
                this.common_followers = res.data.common_followers_list;
                if (this.common_followers.length  == 0) {
                  this.noCommonFollowers = true;
                }
              })
              .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
              });
    },
    addUserName(sn) {
      const path = 'http://localhost:5000/usernamesLink';
      const sn_obj = {"exitCue": false, sn};
       axios.post(path, sn_obj)
              .then(() => {
                this.checkProtected();
                //this.getUserNames();

              })
              .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
                this.checkProtected();
                //this.getUserNames();
              });

    },
    Refresh() {
      const path = 'http://localhost:5000/usernamesLink';
      const sn_obj = {"exitCue": true};
       axios.post(path, sn_obj)
              .then(() => {
                this.getUserNames();
              })
              .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
                this.getUserNames();
              });

    },
    checkProtected() {

      alert("SN from main got clicked");

      const path = 'http://localhost:5000/database';

        axios.get(path)
              .then((res) => {
                this.isProtected = res.data.db[this.screen_name.toString()]['protected'];
                //alert box to check if data is being passed correctly

                if (this.isProtected) {
                  alert("Cannot run search on" + this.screen_name.toString() +
                          ". It is a protected account. Please add a valid screen name." );
                  EventBus.$emit('delete-sn', this.screen_name);
                } else {
                  this.getUserNames();
                }

              })
              .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
              });
    },
    checkValid(screenNames) {
      if (screenNames.length >= 2) {
        this.isValid  = true;
      } else {
        this.isValid = false;
      }
    },
  },
  components: {
    ScreenName
  },
  created() {
    EventBus.$on('delete-sn', sn  => {
        const path = 'http://localhost:5000/usernamesLink';
        const sn_obj = {"exitCue": "snDel", "deleteSn": sn};

        axios.post(path, sn_obj)
              .then(() => {
                this.getUserNames();
              })
              .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
                this.getUserNames()
              });
  });

  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

   .Search {
    display: inline-block;
    vertical-align: middle;
     padding-bottom: 50px;
}
  .InputBox  {
    border-radius: 0px;
    border-color: #11557C;
    border-top: none;
    border-left: none;
    border-right: none;
    border-bottom-width: thick;
    font-size: 25px;
    padding-right: 20px;
    padding-left: 20px;
    font-family: Monaco;
    vertical-align: top;
  }


  .SearchButton   {
    border-radius: 10px;
    background: black;
    font-size: 25px;
    color: white;
    padding-right: 20px;
    padding-left: 20px;
    font-family: Arial;
  }

  .SearchButton:hover{
    cursor:pointer;
  }

  .RefreshButton:hover{
    cursor:pointer;
  }


  .AddButton:hover{
    cursor:pointer;
  }

  .ScreenNameListing {
    border-radius: 10px;
    background: blue;
    font-size: 25px;
    color: white;
    padding-right: 20px;
    padding-left: 20px;
    font-family: Arial;
  }

  .Follower {
    padding: 4px;
    background: purple;
    border-radius: 5px;
    border-radius: 10px;
    font-family: "Courier New";
    color:white;
    margin-left: auto;
    margin-right: auto;
    align-content: center;
    display: block;
    font-size: 35px;
    width: 260px;
  }


</style>
