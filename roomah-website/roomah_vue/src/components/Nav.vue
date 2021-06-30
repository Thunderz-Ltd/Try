<template>
    <nav class="navbar navbar-expand-md navbar-light">
        <a class="navbar-brand" href="#">
            
            <router-link to="/" style="color:white;margin-left:10px;text-decoration:none;" class="navbar-item">
            <img src="../assets/RoomahLogo.png" width="30" height="30"  class="d-inline-block align-top" alt="">
            ROOMAH
            </router-link>
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar" aria-controls="navbar" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div id="navbar" class="collapse navbar-collapse" :class="{'is-active': showMobileMenu}">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <!-- <router-link to="/" style="color:white;margin-left:10px" class="nav-link">Home</router-link> -->
                    <!-- <a class="nav-link" style="color:white;" href="#">Home <span class="sr-only"></span></a> -->
                </li>
                
            </ul>
            
            <ul class="navbar-nav ml-auto">
                <li class="nav-item dropdown">
                    <ul class="listing navbar-nav ml-auto" style="margin-top:3px;">
                      <li class="nav-item">
                        <!-- <a href="#" class="nav-link" style="color:white;">Create a Listing</a> -->
                        <router-link to="/leaseproperty" style="color:white;margin-left:10px" class="nav-link">Create a Listing</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/messages" style="color:white;margin-left:10px" class="nav-link">Messages</router-link>
                        <!-- <a href="#" class="nav-link" style="color:white;">Messages</a> -->
                      </li>
                      <li class="nav-item">
                        <router-link to="/notifications" style="color:white;margin-left:10px" class="nav-link">Notifications</router-link>
                        <!-- <a href="" class="nav-link" style="color:white;">Notifications</a> -->
                      </li>
                          <li class="nav-item dropdown" style="margin-left:10px">
                              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <span style="color:white">Account</span>
                              </a>
                              <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">
                                  <a class="dropdown-item" href="">Account Settings</a>
                                  <a class="dropdown-item" href="">Logout</a>
                              </div>
                          </li>
                    </ul>
                </li>
            </ul>
          
        </div>
    </nav>
</template>

<script>
export default {
    name:'Nav',
    data(){
      return{
        profile:'https://www.coachcarson.com/wp-content/uploads/2018/09/Chad-Profile-pic-circle.png',
        showMobileMenu:false,
      }
    }
}
</script>
<style>
  
</style>