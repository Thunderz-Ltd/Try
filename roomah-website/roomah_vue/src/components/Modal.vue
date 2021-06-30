<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div class="modal"
        role="dialog" aria-labelledby="modalTitle" aria-describedby="modalDescription">
        <header class="modal-header" id="modalTitle">
          <h2>Filter</h2>

        </header>
        <h3 class="modalsection">House Preferences</h3>
        <section class="modal-body" id="modalDescription">
          
          <div class="filter">
            <h5>Property Type: </h5>
            <input type="radio" value="Entire Place" v-model="property" id="entire"/>
            <label style="margin-left:1%" for="entire">Entire Place</label><br>

            <input type="radio" value="Private Room" v-model="property"  id="privateroom"/>
            <label style="margin-left:1%" for="privateroom">Private Room</label><br>

            <input type="radio" value="Shared Room" v-model="property" id="sharedroom"/>
            <label style="margin-left:1%" for="sharedroom">Shared Room</label>
          </div>
          
          <div class="filter">
            <h5>Room : </h5>
            <input type="radio" value="Master Room" v-model="room"  id="masterroom"/>
            <label style="margin-left:1%" for="masterroom">Master Room</label><br>

            <input type="radio" value="Middle Room" v-model="room"  id="middleroom"/>
            <label style="margin-left:1%" for="middleroom">Middle Room</label><br>

            <input type="radio" value="Kitchen Room" v-model="room" id="kitchenroom"/>
            <label style="margin-left:1%" for="kitchenroom">Kitchen Room</label>
          </div>
          
          <div class="filter">
            <h5>Amenities : </h5>
            <input type="checkbox" value="Wifi" v-model="amenities" id="wifi"/>
            <label style="margin-left:1%" for="wifi">Wifi</label><br>

            <input type="checkbox" value="Car Park" v-model="amenities" id="carpark"/>
            <label style="margin-left:1%" for="carpark">Car Park</label><br>

            <input type="checkbox" value="Gym" v-model="amenities" id="gym"/>
            <label style="margin-left:1%" for="gym">Gym</label>
          </div>
          
        </section>
        <h3 class="modalsection">Housemate Preferences</h3>
        <section class="modal-body" id="modalDescription">
          <div class="filter">
            <h5>Gender : </h5>
            <input type="radio" value="Male" v-model="gender" id="male"/>
            <label style="margin-left:1%" for="male">Male</label><br>

            <input type="radio" value="Female" v-model="gender"  id="female"/>
            <label style="margin-left:1%" for="female">Female</label><br>

            <input type="radio" value="" v-model="gender"  id="gnope"/>
            <label style="margin-left:1%" for="gnope">I don't mind</label>
          </div>

          <div class="filter">
            <h5>Age : </h5>
            <input type="radio" value="25" v-model="age"  id="25yo"/>
            <label style="margin-left:1%" for="masterroom">Less than 25 years old</label><br>

            <input type="radio" value="35" v-model="age"  id="35yo"/>
            <label style="margin-left:1%" for="middleroom">Less than 35 years old</label><br>

            <input type="radio" value="45" v-model="age"  id="45yo"/>
            <label style="margin-left:1%" for="kitchenroom">Less than 45 years old</label><br>

            <input type="radio" value="" v-model="age"  id="anope"/>
            <label style="margin-left:1%" for="kitchenroom">I don't mind</label>
          </div>

          <div class="filter">
            <h5>Pets : </h5>
            <input type="radio" value="Have pets" v-model="pets" id="yespet"/>
            <label style="margin-left:1%" for="yespet">Yes</label><br>

            <input type="radio" value="No pets" v-model="pets"  id="nopet"/>
            <label style="margin-left:1%" for="nopet">No</label><br>

            <input type="radio" value="" v-model="pets" id="pnope"/>
            <label style="margin-left:1%" for="kitchenroom">I don't mind</label>
          </div>
        </section>
        <!-- <h5>Filter : {{amenities}}</h5> -->
        <div class="filterbtns">
          <button type="button" class="filter-btn" @click="$emit('close',property, room, amenities)" aria-label="Close modal">
              Apply Filters
          </button>
          <button type="button" style="background-color:red;color:white;" class="filter-btn" @click="reset"  aria-label="Close modal">
              Clear Filters
          </button>
        </div>
        
      </div>
    </div>
  </transition>
</template>

<script>
  export default {
    name: 'Modal',
    data(){
      return{
        property:'',
        room:'',
        amenities:[],
        gender:'',
        age:'',
        pets:'',
        amenitiesnoarray: '',
      }
    },
    methods: {
      reset() {
        this.property = '';
        this.room = '';
        this.amenities = [];
        this.gender = '';
        this.age = '';
        this.pets = '';
      },
    },
  };
</script>

<style>

  .modalsection{
    text-align: center;
  }
  
  .filterbtns{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    background: #FFFFFF;
    max-width: 60%;
    min-width: 250px;
    height: 80%;
    margin-left:20%;
    margin-top: 5%;
    box-shadow: 2px 2px 20px 1px;
    border-radius: 15px;
    /* overflow-x: auto; */
    display: flex;
    flex-direction: column;
    overflow-y: auto;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    position: relative;
    border-bottom: 1px solid #eeeeee;
    color: #175B5B;
    justify-content: space-between;
  }

  .modal-body {
      padding-top: 10px;
      padding-bottom: 3%;
      display: flex;
      width: 90%;
      flex-wrap: wrap;
      margin: auto;
      justify-content: space-evenly;
  }

  .filter{
    margin-top: 1%;
    width: 200px;
    max-height: 500px;
    margin: 2%;
  }

  .filter-btn {
    margin-top: 10px;
    background-color:#fbd864;
    height: 50px;
    width: 100px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-sizing: border-box;
    padding: 5px;
    margin: 2%;
  }

  .modal-fade-enter,
  .modal-fade-leave-to {
    opacity: 0;
  }

  .modal-fade-enter-active,
  .modal-fade-leave-active {
    transition: opacity .5s ease;
  }
</style>