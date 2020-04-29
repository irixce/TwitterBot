<template>
  <div>
    <h1>Enter screen names:</h1>

    <div class="Search">
      <input class="InputBox" v-model="screen_name" placeholder="" >
      <img  class=AddButton src="../assets/addB.png" height="36px" width="36px" v-on:click="addUserName(screen_name)">
    </div>

    <br>

    <div>
      <tr v-for="(sn,  index) in screen_names" :key="index">
      <td>{{sn}}</td>
      </tr>
    </div>

    <button class="SearchButton" v-on:click="counter += 1">Search</button>

  </div>
</template>

<script>
  import axios from 'axios';

export default {
  name: 'Main',
  data() {
    return {
      screen_name: '',
      screen_names: [],
      isProtected: false,
    }
  },
  methods: {
    getUserNames() {
      const path = 'http://localhost:5000/usernamesLink';
      axios.get(path)
              .then((res) => {
                this.screen_names = res.data.screenNames;
                console.log(this.screen_names);
              })
              .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
              });
    },
    addUserName(sn) {
      const path = 'http://localhost:5000/usernamesLink';
      const sn_obj = {sn};
       axios.post(path, sn_obj)
              .then(() => {
                this.getUserNames();
              })
              .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
                this.getUserNames();
              });

    }
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

  .AddButton:hover{
    cursor:pointer;
  }


</style>
