<template>
  <div>
    <h1>Enter screen names:</h1>

    <div class="Search">
      <input class="InputBox" v-model="message" placeholder="" >
      <img  class=AddButton src="../assets/addB.png" height="36px" width="36px" v-on:click="counter += 1">
    </div>

    <br>

    <button class="SearchButton" v-on:click="counter += 1">Search</button>

  </div>
</template>

<script>
export default {
  name: 'Main',
  props: {
    msg: String
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
