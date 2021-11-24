import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Purchase from '../views/Purchase';
import PurchaseResult from '../views/PurchaseResult';
import PurchaseRedirect from "../views/PurchaseRedirect";
import RegistrationGifted from "../views/RegistrationGifted";
import StripeCheckout from '../views/StripeCheckout';
import PurchaseEmail from '../views/PurchaseEmail';
import PaymentDetails from '../views/PaymentDetails'
import Checkout from '../views/Checkout'


Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/purchase',
        name: 'Purchase',
        component: Purchase
    },
    {
        path: '/checkout/stripe',
        name: 'StripeCheckout',
        component: StripeCheckout
    },
    {
        path: '/registration/gifted',
        name: 'RegistrationGifted',
        component: RegistrationGifted
    },
    {
        path: '/purchase/redirect',
        name: 'PurchaseRedirect',
        component: PurchaseRedirect
    },
    {
        path: '/purchase/result/:who',
        name: 'PurchaseResult',
        component: PurchaseResult
    },
    {
        path: '/purchase_email',
        name: 'PurchaseEmail',
        component: PurchaseEmail
    },
    {
        path: '/paymentdetails',
        name: 'PaymentDetails',
        component: PaymentDetails
    },
    {
        path: '/checkout',
        name: 'Checkout',
        component: Checkout
    }
];

// mode: 'hash' or 'history'.
const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

// vue middleware to run before each page switch
router.beforeEach((to, from, next) => {
    console.log(`Navigating from ${from.fullPath} to ${to.fullPath}`);
    next();
});

export default router