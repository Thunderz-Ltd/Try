<template>
    <div style="background-color:white">
        <div class="Form">
            <h1 style="text-align:center;">Edit Profile</h1>
            <form @submit.prevent="submitForm" enctype="multipart/form-data" class="formcontent">

                <h3 style="text-align:center">About Me</h3><br>
                <img class="photosetup" :src="profilephoto"  alt="">
                <input type="file" style="margin-top:5%" class="inputfile" @change="fileChange" required/>
                <!-- <label for="file">Choose a file</label> -->
                <br><br>
                
                <label for="">Name</label><br>
                <input class="profileinput" type="text" v-model="fullname" required><br><br>
                <label for="">Phone Number</label><br>
                <input class="profileinput" type="text" v-model="phonenumber" placeholder="012-3456789" pattern="[0][1][0-9]{1}-[0-9]{7}" required><br><br>
                <label for="">Date of Birth</label><br>
                <input class="profileinput" type="date" v-model="dateofbirth" required><br><br>
                <label for="">Gender</label><br>
                <select class="profileinput" v-model="gender" required>
                    <option disabled value="">Please select one</option>
                    <option>Male</option>
                    <option>Female</option>
                </select><br><br>
                <label for="">Orientation</label><br>
                <select class="profileinput" v-model="orientation" required>
                    <option disabled value="">Please select one</option>
                    <option>Straight</option>
                    <option>Gay</option>
                    <option>Lesbian</option>
                    <option>Bisexual</option>
                </select><br><br>
                <label for="">Religion</label><br>
                <select class="profileinput" v-model="religion" required>
                    <option disabled value="">Please select one</option>
                    <option>Muslim</option>
                    <option>Buddha</option>
                    <option>Hindu</option>
                    <option>Christian</option>
                    <option>Others</option>
                </select><br><br>
                <label for="">Occupation</label><br>
                <select class="profileinput" v-model="occupation" required>
                    <option disabled value="">Please select one</option>
                    <option>Student</option>
                    <option>Working</option>
                    <option>Not Working</option>
                </select><br><br>
                <label for="">Do you have pet?</label><br>
                <select class="profileinput" v-model="pet" required>
                    <option disabled value="">Please select one</option>
                    <option>Yes</option>
                    <option>No</option>
                </select><br><br>
                <label for="">Bio</label><br>
                <input class="profileinput" style="height:100px" type="text" v-model="bio" required><br><br>


                <br><h3>Housemate Preferences</h3><br>
                <label for="">Preferred Gender</label><br>
                <select class="profileinput" v-model="preferredgender" required>
                    <option disabled value="">Please select one</option>
                    <option>Male</option>
                    <option>Female</option>
                    <option>I don't mind</option>
                </select><br><br>
                <label for="">Preferred Orientation</label><br>
                <select class="profileinput" v-model="preferredorientation" required>
                    <option disabled value="">Please select one</option>
                    <option>Straight</option>
                    <option>Gay</option>
                    <option>Lesbian</option>
                    <option>Bisexual</option>
                    <option>I don't mind</option>
                </select><br><br>
                <label for="">Preferred Age</label><br>
                <select class="profileinput" v-model="preferredage" required>
                    <option disabled value="">Please select one</option>
                    <option>18 - 25</option>
                    <option>26 - 35</option>
                    <option>> 35</option>
                    <option>I don't mind</option>
                </select><br><br>
                <label for="">Preferred Religion</label><br>
                <select class="profileinput" v-model="preferredreligion" required>
                    <option disabled value="">Please select one</option>
                    <option>Muslim</option>
                    <option>Buddha</option>
                    <option>Hindu</option>
                    <option>Christian</option>
                    <option>I don't mind</option>
                </select><br><br>
                <label for="">Preferred Occupation</label><br>
                <select class="profileinput" v-model="preferredoccupation" required>
                    <option disabled value="">Please select one</option>
                    <option>Student</option>
                    <option>Working</option>
                    <option>Not Working</option>
                    <option>I don't mind</option>
                </select><br><br>
                

                <br><h3>Property Preferences</h3><br>
                <label for="">Preferred Location</label><br>
                <input class="profileinput" type="text" v-model="preferredlocation" placeholder="Kuala Lumpur, Malaysia" required><br><br>
                <label for="">Preferred Rent Budget</label><br>
                <label for="">RM <input type="number" v-model="preferredmaxrent"> /month</label><br>
                <input class="profileinput" type="range" v-model="preferredmaxrent" min="0" max="10000" step="1" required><br><br>
                <label for="">Preferred Accomodation Type</label><br>
                <select class="profileinput" v-model="preferredaccommodationtype" required>
                    <option disabled value="">Please select one</option>
                    <option>Entire House</option>
                    <option>Private Room</option>
                    <option>Shared Room</option>
                    <option>I don't mind</option>
                </select><br><br>
                
                <button class="submitprofilebtn">Submit</button>
            </form>
        </div>
        <!-- <Footer /> -->
    </div>
</template>

<script>
import axios from 'axios'
import Footer from '../components/Footer.vue'
import ProfilePhoto from '../assets/ProfilePhoto.png'

export default {
    name:'ProfileSetup',
    data(){
        return{
            profilephoto: ProfilePhoto,
            file: null,
            fullname:'',
            phonenumber:'',
            dateofbirth:'',
            gender:'',
            orientation:'',
            religion:'',
            occupation:'',
            pet:'',
            bio:'',
            preferredgender:'',
            preferredorientation:'',
            preferredage:'',
            preferredreligion:'',
            preferredoccupation:'',
            preferredlocation:'',
            preferredmaxrent:0,
            preferredaccommodationtype:'',
        }
    },
    components:{
        Footer, 
        
    },
    mounted(){
        document.title = 'Roomah | Profile Setup' //Title of the page
    },
    methods:{
        fileChange(e){
        this.file = e.target.files[0]
        this.profilephoto = URL.createObjectURL(this.file)
        // console.log(this.profilephoto)
        console.log(this.file)
        },

        submitForm(){

            const formData = {
                    profilephoto: this.file,
                    fullname: this.fullname,
                    phonenumber: this.phonenumber,
                    dateofbirth: this.dateofbirth,
                    gender: this.gender,
                    orientation: this.orientation,
                    religion: this.religion,
                    occupation:this.occupation,
                    pet: this.pet,
                    bio: this.bio,
                    preferredgender: this.preferredgender,
                    preferredorientation: this.preferredorientation,
                    preferredage: this.preferredage,
                    preferredreligion:this.preferredreligion,
                    preferredoccupation:this.preferredoccupation,
                    preferredlocation: this.preferredlocation,
                    preferredmaxrent: this.preferredmaxrent,
                    preferredaccommodationtype:this.preferredaccommodationtype,
                }

            // const fd = new FormData();
            // fd.append('profilephoto', this.file)

            axios
                .post("/djangoprofiles/", formData)
                .then(response =>{
                    alert("Your Profile is submitted!");
                    this.profilephoto='https://static.thenounproject.com/png/556457-200.png',
                    this.file= null,
                    this.fullname='',
                    this.phonenumber='',
                    this.dateofbirth='',
                    this.gender='',
                    this.orientation='',
                    this.religion='',
                    this.occupation='',
                    this.pet='',
                    this.bio='',
                    this.preferredgender='',
                    this.preferredorientation='',
                    this.preferredage='',
                    this.preferredreligion='',
                    this.preferredoccupation='',
                    this.preferredlocation='',
                    this.preferredmaxrent=0,
                    this.preferredaccommodationtype=''
                })
                // this.$router.push('/')
        }
    }
}
</script>

<style>
    .inputfile{
        display: block;
        margin:0 auto;
        width: 100px;
    }
    
    .photosetup{
        width:200px;
        height:200px;
        display:block;
        margin:0 auto;
    }

    .Form{
        margin: 0 auto;
        width: 50%;
        margin-top: 5%;
        padding-bottom:5%;
    }

    .formcontent{
        margin: 0 auto;
        margin-top: 10%;
    }

    .profileinput{
        width: 100%;
        padding: 1%;
    }

    .submitprofilebtn{
        margin-top: 10%;
        
        background-color:#175B5B;
        color: white;
        height: 50px;
        width: 120px;
        border: 1px solid #ccc;
        border-radius: 9px;
        box-sizing: border-box;
        padding: 5px;
        margin: 0 auto;
        display: block;
    }
    

</style>