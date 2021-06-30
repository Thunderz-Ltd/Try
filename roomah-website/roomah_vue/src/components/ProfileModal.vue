<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div class="modal"
        role="dialog" aria-labelledby="modalTitle" aria-describedby="modalDescription">
        <header class="modal-header" id="modalTitle">
          <h2>Filter</h2>

        </header>
        <section class="modal-body" id="modalDescription">
          
          <div class="filter">
            <h5>Housemate Type: </h5>
            <input type="radio" value="Needs A Room" v-model="housematetype" id="needsroom"/>
            <label style="margin-left:1%" for="needsroom">Needs A Room</label><br>

            <input type="radio" value="Has A Room" v-model="housematetype"  id="privateroom"/>
            <label style="margin-left:1%" for="privateroom">Has A Room</label><br>

            <input type="radio" value="" v-model="housematetype"  id="hnope"/>
            <label style="margin-left:1%" for="hnope">I don't mind</label>
          </div>
          
          <div class="filter">
            <h5>Age : </h5>
            <input type="radio" value=25 v-model="age" @change="MinAge" id="25yo"/>
            <label style="margin-left:1%" for="25yo">18 - 25</label><br>

            <input type="radio" value=35 v-model="age" @change="MinAge" id="35yo"/>
            <label style="margin-left:1%" for="35yo">26 - 35</label><br>

            <input type="radio" value=500 v-model="age" @change="MinAge" id="45yo"/>
            <label style="margin-left:1%" for="45yo">> 35</label><br>

            <input type="radio" value=1000 v-model="age" @change="MinAge" id="anope"/>
            <label style="margin-left:1%" for="anope">I don't mind</label>
          </div>
          
          <div class="filter">
            <h5>Gender : </h5>
            <input type="radio" value="Male" v-model="gender" id="male"/>
            <label style="margin-left:1%" for="male">Male</label><br>

            <input type="radio" value="Female" v-model="gender"  id="female"/>
            <label style="margin-left:1%" for="female">Female</label><br>

            <input type="radio" value="" v-model="gender"  id="gnope"/>
            <label style="margin-left:1%" for="gnope">I don't mind</label>
          </div>
          
        </section>

        <section class="modal-body" id="modalDescription">
          <div class="filter">
            <h5>Religion : </h5>
            <input type="radio" value="Muslim" v-model="religion" id="muslim"/>
            <label style="margin-left:1%" for="muslim">Muslim</label><br>

            <input type="radio" value="Buddha" v-model="religion"  id="buddha"/>
            <label style="margin-left:1%" for="buddha">Buddha</label><br>

            <input type="radio" value="Hindu" v-model="religion"  id="hindu"/>
            <label style="margin-left:1%" for="hindu">Hindu</label><br>

            <input type="radio" value="Christian" v-model="religion"  id="hindu"/>
            <label style="margin-left:1%" for="hindu">Christian</label><br>

            <input type="radio" value="" v-model="religion"  id="rnope"/>
            <label style="margin-left:1%" for="rnope">I don't mind</label>
          </div>

          <div class="filter">
            <h5>Occupation : </h5>
            <input type="radio" value="Student" v-model="occupation"  id="student"/>
            <label style="margin-left:1%" for="student">Student</label><br>

            <input type="radio" value="Working" v-model="occupation"  id="working"/>
            <label style="margin-left:1%" for="working">Working</label><br>

            <input type="radio" value="Not Working" v-model="occupation"  id="notworking"/>
            <label style="margin-left:1%" for="notworking">Not Working</label><br>

            <input type="radio" value="" v-model="occupation"  id="onope"/>
            <label style="margin-left:1%" for="onope">I don't mind</label>
          </div>

          <div class="filter">
            <h5>Pet : </h5>
            <input type="radio" value="Yes" v-model="pet" id="yespet"/>
            <label style="margin-left:1%" for="yespet">Yes</label><br>

            <input type="radio" value="No" v-model="pet"  id="nopet"/>
            <label style="margin-left:1%" for="nopet">No</label><br>

            <input type="radio" value="" v-model="pet" id="pnope"/>
            <label style="margin-left:1%" for="pnope">I don't mind</label>
          </div>
        </section>
        
        <div class="filterbtns">
          <button type="button" class="filter-btn" @click="$emit('close', housematetype, age, minage, gender, religion, occupation, pet)" aria-label="Close modal">
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
    name: 'ProfileModal',
    data(){
      return{
        housematetype:'',
        age:1000,
        minage:0,
        gender:'',
        religion:'',
        occupation:'',
        pet:'',
        
      }
    },
    methods: {
      reset() {
        this.housematetype = '';
        this.age = 1000;
        this.minage = 0;
        this.gender = '';
        this.religion = '';
        this.occupation = '';
        this.pet = '';
      },
      MinAge(){
        if (this.age == 25){
          this.minage = 18;
        }else if (this.age == 35){
          this.minage = 26;
        }else if (this.age == 500){
          this.minage = 36;
        }else{
          this.minage = 0;
        }
      }
    },
  };
</script>

<style>
  
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