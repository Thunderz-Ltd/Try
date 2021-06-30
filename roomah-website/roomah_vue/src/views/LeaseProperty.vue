<template>
    <div class="wholepage">
        <div>
            
        </div>
        
        <div class="paymentsection">
            
            <h3 style="text-align:center">Lease Property Plans</h3><br><br>
            
            <input type="radio" value=30 v-model="total" id="3months"/>
            <label style="margin-left:1%" for="3months">RM 30 for 3 Months (Basic Plan)</label><br>

            <input type="radio" value=60 v-model="total"  id="6months"/>
            <label style="margin-left:1%" for="6months">RM 60 for 6 Months (Silver Plan)</label><br>

            <input type="radio" value=100 v-model="total" id="12months"/>
            <label style="margin-left:1%" for="12months"> RM 100 for 12 Months (Gold Plan)</label><br><br>


            <!-- <span>MYR</span> -->
            <!-- <input class="profileinput" type="text" v-model="total" placeholder="0.99" required><br><br> -->
            <button class="filter-btn" @click="payment">Pay</button>
        </div>
    
    </div>
</template>

<script>
import Footer from '../components/Footer.vue'
export default {
    name:'LeaseProperty',
    components: {
      Footer
    },
    data(){
      return{
        total : 100,
        packages:'',
      }
    },methods:{
        payment(){
            this.$router.push({path: '/leasepayment', query: {total: this.total }})
        }
    }
}
</script>

<style>

    .wholepage{
        position: relative;
	    min-height: 100vh;
        background-color: white;
        
    }
    .paymentsection{
        display: block;
        margin: 0 auto;
        max-width: 350px;
        margin-top: 2%;
    }
</style>