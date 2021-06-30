import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import ProfileSetup from '../views/ProfileSetup.vue'
import About from '../views/About.vue'
import FindHouse from '../views/FindHouse.vue'
import FindHousemate from '../views/FindHousemate.vue'
import House from '../views/House.vue'
import Housemate from '../views/Housemate.vue'
import LeaseProperty from '../views/LeaseProperty.vue'
import LeasePayment from '../views/LeasePropertyPayment.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/profilesetup',
    name: 'ProfileSetup',
    component: ProfileSetup
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    component: About
  },
  {
    path: '/findhouse',
    name: 'FindHouse',
    component: FindHouse
  },
  {
    path: '/findhouse/:house_slug',
    name: 'House',
    component: House
  },

  {
    path: '/findhousemate',
    name: 'FindHousemate',
    component: FindHousemate
  },

  {
    path: '/leaseproperty',
    name: 'LeaseProperty',
    component: LeaseProperty
  },

  {
    path: '/leasepayment',
    name: 'LeasePayment',
    component: LeasePayment
  },

  {
    path: '/findhousemate/:housemate_slug',
    name: 'Housemate',
    component: Housemate
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
