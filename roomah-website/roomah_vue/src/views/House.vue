<template>
    <div class="page-product">
        <div>
            <div>
                <figure>
                    <img v-bind:src="product.get_image">
                </figure>

                <h1 class="title">{{ product.name }}</h1>

                <p>{{ product.description }}</p>
            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
// import { toast } from 'bulma-toast'
export default {
    name: 'House',
    data() {
        return {
            product: {},
            // quantity: 1
        }
    },
    mounted() {
        this.getProduct() 
    },
    methods: {
        getProduct() {
            // this.$store.commit('setIsLoading', true)
            // const category_slug = this.$route.params.category_slug
            const house_slug = this.$route.params.house_slug
            axios
                .get(`/djangohouse/${house_slug}`) //from django REST API       ${variable} -> insert variable inside a string
                .then(response => {
                    this.product = response.data
                    document.title = 'Roomah | ' + this.product.name
                })
                .catch(error => {
                    console.log(error)
                })
            
        },
    }
}
</script>