<template>
  <div v-on:mouseover="mouseIn" v-on:click="emitDeleteToMain" class="ScreenName">
    <span> {{sn}} </span>
    <img v-show="active" src="../assets/blue-x.png" height="20px" width="20px">
  </div>

</template>

<script>
import { EventBus } from '../event-bus.js';

export default {
  name: 'ScreenName',
  props: ['sn'],
  data: function () {
  return {
    active: false
  }
},
  methods: {
        mouseIn: function(){
            this.active = !this.active;
        },
        emitDeleteToMain: function() {
          EventBus.$emit('sn-got-clicked', this.sn);
        },
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  color: rebeccapurple;
}

  .ScreenName {
     background: lightskyblue;
     color: darkblue;
     font: bold;
    font-size: 25px;
     border-radius: 5px;
     padding-left: 4px;
     padding-right: 4px;
    display: inline-block; /* change the display type           */
    margin: 10px 10px;

  }

  .ScreenName:hover {
    cursor: pointer;
}

</style>
