<template>
    <div class="paymentpage">
        <h1 style="text-align:center;margin-top:3%;margin-bottom:2%">Checkout</h1>

        <div style="padding:1%">
            <div>
                <div class="left">
                <!-- <h2>Review</h2><br> -->
                <img class="propertyphoto" src="https://a0.muscache.com/pictures/b67251a8-bafa-43f0-938a-298a618a1a22.jpg" style="margin-top:5%">
                <div class="property">
                    <div class="leftdetails">
                        <h3>Property Details</h3><br>
                        <p class="details">Property Name</p>
                        <p>Serene Residency, Cyberjaya</p>

                        <p class="details">Property Type</p>
                        <p>Private Room</p>

                        <p class="details">Property Rental</p>
                        <p>RM 1000/month</p>

                        <p class="details">Property Description</p>
                        <p>TV, Car park, Washing machine, Water heater, Wifi, Gym</p>
                    </div>

                <div class="rightdetails">
                    <h3>Housemate Preferences</h3><br>

                    <p class="details">Preferred Gender</p>
                    <p>Female</p>

                    <p class="details">Preferred Age</p>
                    <p>18 - 25</p>

                    <p class="details">Preferred Religion</p>
                    <p>I don't mind</p>

                    <p class="details">Preferred Occupation</p>
                    <p>Student</p>

                </div>
                </div>
                    
                <div style="width:100%">
                    <button class="editpropertybtn">Edit</button>
                </div>

            </div>
            
                
            </div>  
            <div class="right">
                <h2>Payment</h2><br>
                <div class="paymentdetails">
                    <p>Basic Plan</p>
                    <p>Service Fees</p>
                </div>

                <div class="paymentdetails">
                    <p class="fees">{{(this.total-this.transactionfees).toFixed(2)}}</p>
                    <p class="fees">{{this.transactionfees}}</p>
                </div>
                
                
                <p style="text-align:right;font-weight: bold;">MYR {{(this.total-0).toFixed(2)}}</p>
                <h3></h3>
                <div id="paypal-button-container"></div>
            </div> 
        </div>
        
    </div>
    
</template>

<script>
export default {
    name:'LeastPayment',
    data(){
      return{
        total : 0,
        transactionfees:''
      }
    },
    mounted(){
        this.paypalpayment()
    },
    created() {
    this.total = this.$route.query.total
    this.transactionfees = ((0.049*this.total)+2).toFixed(2) //https://www.paypal.com/my/webapps/mpp/ua/recpymt-full?locale.x=en_MY
    },
    methods:{
        paypalpayment(){
            
            let Total = this.total
            paypal.Buttons({
                
                // Set up the transaction
                createOrder: function(data, actions) {
                    return actions.order.create({
                        purchase_units: [{
                            amount: {
                                value: Total
                            }
                        }]
                    });
                },

                // Finalize the transaction
                onApprove: function(data, actions) {
                    return actions.order.capture().then(function(details) {
                        // Show a success message to the buyer
                        alert('Transaction completed by ' + details.payer.name.given_name + '!');
                    });
                }


        }).render('#paypal-button-container');
        
            }
    }
}
</script>
<style>
    .property{
        margin-top: 3%;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-evenly;
        padding: 7%;
        min-height: 450px;
        
    }
    .fees{
        text-align: right;
    }

    .paymentdetails{
        width: 50%;
        float: left;
        border-bottom: 1px solid black;
        
    }

    .editpropertybtn{
        margin-top: 10px;
        background-color:#fbd864;
        height: 50px;
        width: 100px;
        border: 1px solid #ccc;
        border-radius: 10px;
        box-sizing: border-box;
        padding: 5px;
        display: block;
        margin: 0 auto;
        }
    .details{
        font-weight: bold;
    }

    .leftdetails{
        
        width: 300px;
        float: left;
        height:430px;
    }

    .rightdetails{
        
        width: 300px;
        float: right;
        height:430px;
    }

    .left{
        background-color: white;
        width: 56%;
        float: left;
        margin: 1%;
        padding: 1%;
        box-shadow: 12px 12px 22px grey;
    }

    .right{
        background-color: white;
        width: 40%;
        float: right;
        margin: 1%;
        padding: 3%;
        box-shadow: 12px 12px 22px grey;
    }

    .paymentpage{
        position: relative;
	    min-height: 100vh;
        background-color: #DCDCDC;
        
    }

    .propertyphoto{
        width: 500px;
        height: 300px;
        display: block;
        margin: 0 auto;
        
    }

</style>