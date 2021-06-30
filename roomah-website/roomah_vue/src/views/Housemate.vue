<template>
    <div class="page-product">
        <div>
            <div>
                <template v-if="housemate.get_profilephoto==''">
                    <img src="../assets/defaultprofilepicture.png">
                </template>
                <template v-else>
                    <img :src="housemate.get_profilephoto">
                </template>
                

                <h1 class="title">{{ housemate.fullname }}</h1>
                <p>{{ housemate.bio }}</p>
            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Housemate',
    data() {
        return {
            housemate: {},
            // quantity: 1
        }
    },
    mounted() {
        this.getHousemate() 
    },
    methods: {
        getHousemate() {
            
            const housemate_slug = this.$route.params.housemate_slug
            axios
                .get(`/djangohousemate/${housemate_slug}`) //from django REST API       ${variable} -> insert variable inside a string
                .then(response => {
                    this.housemate = response.data
                    document.title = 'Roomah | ' + this.housemate.fullname
                })
                .catch(error => {
                    console.log(error)
                })
            
        },
    }
}
</script>