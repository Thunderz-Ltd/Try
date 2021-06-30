<template>
  <div id="app">
      <Nav />
    <div class="auth-wrapper">
      
      <router-view />
    </div>
    <Footer />
  </div>
</template>

<script>
import Nav from './components/Nav.vue'
import VisitorNav from './components/VisitorNav.vue'
import Footer from './components/Footer.vue'

export default {
    name: 'App',
    components:{
        Nav, 
        VisitorNav,
        Footer
    }
  
}
</script>

<style>
  #app{
    position: relative;
	  min-height: 100vh;
  }
  
  body{

    background: url("./assets/Buildings.jpg")0 -350px; 
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
    background-size: cover;

    background-color: white;



  }

  /* h3{
    text-align: center;
  } */

  .navbar{
    background-color:#175B5B;
    
  }

  *
		{
			padding: 0;
			margin: 0;
			box-sizing: border-box;
		}


	.row
		{
			background: white;
			box-shadow: 12px 12px 22px grey;
		}
		
	.btn
		{
			border: none;
			outline: none;
			height : 50px;
			width: 100%;
			background-color:#175B5B;
			color: white;
			border-radius: 4px;
			font-weight : bold;
		}
		
	.btn:hover
		{
			background-color: white;
			border: 1px solid;
			color: black;
		}
		
	a
		{
			color: #175B5B;
		}

  .auth-wrapper{
    display: flex;
    justify-content: center;
    flex-direction: column;
    text-align: left;
    

  }

/* .social-media{
  
  text-align: center;
}

.social-media ul{
  list-style: none;
}

.social-media ul li{
  display: inline-block;
  cursor: pointer;
  margin: 5px 5px;
}
  .social-media img
  {
  width: 100px;
  height: 50px;
  } */

</style>