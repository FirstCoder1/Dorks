<template>
    <div class="purchase-result">
        <Header></Header>
        <div class="purchase-result-wrapper">
            <div v-if="$route.params.who === 'myself'" class="result-container">
                <div class="content-title">You got Dorks!</div>
                <div class="content-text">
                    Your year long tech support is now live. Contact your Dork through our dedicated channels whenever you need it. Congratulations!
                </div>
                <button class="purchase-button">Contact your Dork</button>
            </div>
            <div v-else-if="$route.params.who === 'gift'" class="result-container">
                <div class="content-title">Dorks, gifted!</div>
                <div class="content-text">
                    You’ve successfully gifted someone a Dork for a whole year! They will notified to setup an account with us. Feel free to reach out to them to get them started!
                </div>
            </div>
            <div v-if="is_mobile" class="dorks-container">
                <img :src="require('@/assets/img/dork-girl-hat-mobile.svg')" class="dorks dork-girl-hat" alt="">
                <img :src="require('@/assets/img/dork-guy-hat-mobile.svg')" class="dorks dork-guy-hat" alt="">
            </div>
            <div v-else class="dorks-container">
                <img :src="require('@/assets/img/dork-girl-hat.svg')" class="dorks dork-girl-hat" alt="">
                <img :src="require('@/assets/img/dork-guy-hat.svg')" class="dorks dork-guy-hat" alt="">
            </div>
        </div>
        <Footer></Footer>
    </div>
</template>

<script>

import Header from '@/components/Header';
import Footer from '@/components/Footer';
export default {
    name: "PurchaseResult",
    components: {
        Header,
        Footer
    },
    data() {
        return {
            current_width: window.innerWidth,
            current_height: window.innerHeight
        }
    },
    mounted() {
        window.addEventListener('resize', this.set_dims);
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.set_dims);
        console.log("Resize destroyed");
    },
    computed: {
        is_mobile: function() {
            console.log(this.current_width, this.current_height);
            return this.current_width < 768;
        }
    },
    methods: {
        set_dims: function() {
            this.current_width = window.innerWidth;
            this.current_height = window.innerHeight;
        },
    }
}

</script>
