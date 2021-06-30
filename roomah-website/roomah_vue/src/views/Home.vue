<template>
  <div class="homepage">
    <h1>This is Home</h1>
    <router-link to="/findhouse" style="color:black;" class="nav-link"><button>Find House</button></router-link>
    <router-link to="/findhousemate" style="color:black;" class="nav-link"><button>Find Housemate</button></router-link>
    <router-link to="/profilesetup" style="color:black;" class="nav-link"><button>Profile Setup</button></router-link>
    <router-link to="/leaseproperty" style="color:black;" class="nav-link"><button>Least Property Payment</button></router-link>
    <!-- <Footer /> -->
  </div>
</template>
<script>
  import Modal from '../components/Modal.vue';
  import Footer from '../components/Footer.vue'
  export default {
    name: 'Home',
    components: {
      Modal,
      Footer
    },
    data() {
      return {
        isModalVisible: false,
      };
    },
    mounted(){
      document.title = 'Roomah | Home' //Title of the page
    },
    methods: {
      showModal() {
        this.isModalVisible = true;
      },
      closeModal() {
        this.isModalVisible = false;
      }
    }
  };
</script>
<style>
  .homepage{
    margin-top: 20%;
    background-color:white;
    position: relative;
    min-height: 60vh;
    
  }
</style>