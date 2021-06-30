<template>
  <div class="home" style="margin-top: 10%;">
    <h3 class="header">You are looking for a house</h3>
        <form action="">
            <div class="center-block">
                <input type="text" v-model="search"  class="search">
                <button type="button" class="my-button" @click="showModal">Filter</button>
                <Modal v-show="isModalVisible" @close="closeModal"
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
            
            <div class="posts" v-for="house in filteredPosts" :key="house.id">
              <router-link :to="house.get_absolute_url" style="text-decoration:none;">
                  <figure class="polaroid">
                    <img :src="house.get_thumbnail" style="width:100%;border-top-left-radius: 25px;border-top-right-radius: 25px;max-height:200px;">
                    <div class="container">
                      <div style="height:80px">
                        <h3 class="title">{{ house.name }}</h3>
                      </div>
                      <div>
                        <b class="postcontent" style="color:#175B5B">{{ house.room }}</b><br><br>
                        <p class="postcontent">RM{{ house.price }}/month</p>
                        <p class="postcontent">{{ house.description }}</p>
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
import Modal from '../components/Modal.vue';
import Footer from '../components/Footer.vue'
import axios from 'axios'
export default {
  name: 'FindHouse',
  components: {
      Modal,
      Footer
    },
  data(){
    return{
      isModalVisible: false,
      search:'',
      Houses:[],
      
      Property:'',
      Room:'',
      Amenities:[],
      filterSearch:'',
      filterProperty:'',
      filterRoom:'',
      filterAmenities:'',
    }
  },
  mounted(){
    this.getHouses()
    document.title = 'Roomah | Find House' //Title of the page
  },
  methods:{
    getHouses(){
      axios  
         .get('/djangohouses/') //to get data that is converted by Django REST with the help of Axios
        .then(response => {
          this.Houses = response.data
        })
        .catch(error => {
          console.log(error)
        })
      },
      showModal() {
          this.isModalVisible = true;
      },
      closeModal(property, room, amenities) {
        this.isModalVisible = false;
        this.Room = room;
        this.Amenities = amenities;
        this.Property = property;
      },
    
  },
  computed:{
    filteredPosts(){
      //Filter Results (Accommodation Type)
      this.filterProperty= this.Houses.filter(house => house.accommodationtype.toLowerCase().includes(this.Property.toLowerCase()))
      
      //Filter Results (Room)
      this.filterRoom = this.filterProperty.filter(house => house.room.toLowerCase().includes(this.Room.toLowerCase()))

      //Filter Results (Amenities)
      if(this.Amenities.length>0){
        for(var i=0;i< this.Amenities.length; i++){
          if(i==0){
            this.filterAmenities = this.filterRoom.filter(house => house.description.toLowerCase().includes(this.Amenities[i].toLowerCase()))
          }else{
            this.filterAmenities = this.filterAmenities.filter(house => house.description.toLowerCase().includes(this.Amenities[i].toLowerCase()))
          }
        }
      }else{
        this.filterAmenities = this.filterRoom.filter(house => house.description.toLowerCase().includes(""))
      }
      
      // Filter Results (Search)
      this.filterSearch = this.filterAmenities.filter(house => house.name.toLowerCase().includes(this.search.toLowerCase()) 
      || house.room.toLowerCase().includes(this.search.toLowerCase())
      || house.description.toLowerCase().includes(this.search.toLowerCase())
      )

      //Return Final Results
      return this.filterSearch
    }
  }
}
</script>

<style>

</style>
