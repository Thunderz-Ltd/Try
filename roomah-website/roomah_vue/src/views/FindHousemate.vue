<template>
  <div class="home" style="margin-top: 10%;">
    <h3 class="header">You are looking for a housemate</h3>
        <form action="">
            <div class="center-block">
                <input type="text" v-model="search"  class="search">
                <button type="button" class="my-button" @click="showModal">Filter</button>
                <ProfileModal v-show="isModalVisible" @close="closeModal"
                />
            </div>
        </form>

        <div class ="postgroup">
          <template v-if="filterSearch==''">
            <div class="NoResult">
              <h3 style="margin-left:2%;">No Results</h3>
            </div>
          </template>
          <template v-else>
            <h3 style="margin-left:2%;">Results for '{{this.search}}'</h3>
          </template>

          <div class="group">
            
            <div class="posts" v-for="housemate in filteredPosts" :key="housemate.id">
              <router-link :to="housemate.get_absolute_url" style="text-decoration:none;">
                <figure class="polaroid">
                  <template v-if="housemate.get_profilethumbnail==''">
                    <img src="../assets/defaultprofilepicture.png" class="profilephoto">
                  </template>
                  <template v-else>
                    <img :src="housemate.get_profilethumbnail" class="profilephoto">
                  </template>
                    <div class="container">
                      <div style="height:80px">
                        <h3 class="title">{{ housemate.fullname }}, {{ housemate.age }}</h3>
                      </div>
                      
                      <b class="profilepostcontent" style="color:#175B5B">{{ housemate.HasRoom }}</b><br><br>
                      <!-- <p class="profilepostcontent">Budget: RM{{ profile.preferredmaxrent }}/month</p> -->
                      <p class="profilepostcontent" style="font-style:italic">{{ housemate.occupation }}</p>
                      <!-- <p class="profilepostcontent">{{ profile.gender }}</p> -->
                      <div style="height:60px">
                        <p class="profilepostcontent" style="font-size: 14px;font-style:italic">{{ housemate.bio }}</p>
                      </div>
                    </div>
                </figure>
              </router-link>
            </div>
          </div>

          
        </div>
        <!-- <Footer /> -->
        
  </div>
</template>

<script>
import ProfileModal from '../components/ProfileModal.vue';
import Footer from '../components/Footer.vue'
import axios from 'axios'
export default {
  name: 'FindHousemate',
  components: {
      ProfileModal,
      Footer,
    },
  data(){
    return{
      isModalVisible: false,
      search:'',
      Housemates:[],

      HousemateType:'',
      Age:1000,
      MinAge:0,
      Gender:'',
      Religion:'',
      Occupation:'',
      Pet:'',
      
      

      filterhousematetype:'',
      filterage:'',
      filtergender:'',
      filterreligion:'',
      filteroccupation:'',
      filterpet:'',
      filterSearch:''
    }
  },
  mounted(){
    this.getHouses()
    document.title = 'Roomah | Find Housemate' //Title of the page
  },
  methods:{
    getHouses(){
      axios  
         .get('/djangoprofiles/') //to get data that is converted by Django REST with the help of Axios
        .then(response => {
          this.Housemates = response.data
        })
        .catch(error => {
          console.log(error)
        })

      },
      showModal() {
          this.isModalVisible = true;
      },
      closeModal(housematetype, age, minage, gender, religion, occupation, pet) {
        this.isModalVisible = false;
        this.HousemateType = housematetype;
        this.Age = age;
        this.MinAge = minage;
        this.Gender = gender;
        this.Religion = religion;
        this.Occupation = occupation;
        this.Pet = pet;

        // console.log(this.MinAge);
      },
      
    
  },
  computed:{
    filteredPosts(){
        
      //Filter Results (Housemate Type)                             //Data from database                   //Data from Modal
      this.filterhousematetype = this.Housemates.filter(housemate => housemate.HasRoom.toLowerCase().includes(this.HousemateType.toLowerCase()))

      //Filter Results (Age) 
      this.filterage = this.filterhousematetype.filter(housemate => (housemate.age <= this.Age) && (housemate.age >= this.MinAge))

      //Filter Results (Gender)
      this.filtergender = this.filterage.filter(housemate => housemate.gender.includes(this.Gender))

      //Filter Results (Religion)
      this.filterreligion = this.filtergender.filter(housemate => housemate.religion.toLowerCase().includes(this.Religion.toLowerCase()))

      //Filter Results (Occupation)
      this.filteroccupation = this.filterreligion.filter(housemate => housemate.occupation.toLowerCase().includes(this.Occupation.toLowerCase()))

      //Filter Results (Pet)
      this.filterpet = this.filteroccupation.filter(housemate => housemate.pet.toLowerCase().includes(this.Pet.toLowerCase()))


      
      // Filter Results (Search)
      this.filterSearch = this.filterpet.filter(housemate => housemate.fullname.toLowerCase().includes(this.search.toLowerCase()) 
      || housemate.phonenumber.toLowerCase().includes(this.search.toLowerCase())
      || housemate.occupation.toLowerCase().includes(this.search.toLowerCase())
      )

      //Return Final Results
      
      return this.filterSearch
    }
  }
}
</script>

<style>
    
    .profilephoto{
      width:100%;
      border-top-left-radius: 25px;
      border-top-right-radius: 25px;
      height:200px;
    }

    figure.polaroid {
      width: 100%;
      height: 100%;
      background-color: white;
      box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
      margin-bottom: 25px;
      border-radius: 25px;
    }

    div.container {
      text-align: center;
      padding: 10px 20px;
    }
    .center-block{
      display: flex;
      margin: auto;
      max-width: 900px;
      flex-wrap: wrap;
      justify-content: space-evenly;
    }

    .posts{
        margin-top: 1%;
        width: 300px;
        height: 450px;
        margin: 2%;
        
    }

    .postgroup{
        margin-top: 3%;
        padding-top: 3%;
        background-color: white;
        height: 100%;
        position: relative;
        min-height: 100vh;
        
    }

    .group{
        padding-top: 10px;
        padding-bottom: 3%;
        display: flex;
        width: 85%;
        flex-wrap: wrap;
        margin: auto;
        justify-content: space-evenly;
    }

    .header{
        color: white;
        margin-bottom:3%;
        font-weight: bold;
        text-align: center;
    }

    .search
		{
      margin-top: 10px;
			display: inline-block;
      padding: 8px;
			width :90%;
      height:50px;
      border: 1px solid #ccc;
      border-radius: 10px;
      box-sizing: border-box;
		}
		
		
		.my-button
		{
			margin-top: 10px;
      background-color:#fbd864;
      margin-left:2px;
      width :80px;
      height: 50px;
      border: 1px solid #ccc;
      border-radius: 10px;
      box-sizing: border-box;
		}

    .profilepostcontent{
        text-align: center;
    }

    .title{
        color: black;
    }
</style>
