<template>
    <div class="purchase">
        <Header></Header>
        <div class="purchase-title-container">
            <div class="content-title">
                What a gift!
            </div>
            <div class="content-text">
                Wow, nice! You’ve just been gifted an entire years worth of tech support. Complete the fields below to complete registeration.
            </div>
            <div class="no-charge-text">
                You will not be charged - it’s already been paid!
            </div>
        </div>

        <div class="purchase-form-container">
            <div class="form-container">
                <form>
                    <div class="input-element">
                        <label for="first-name">First name</label>
                        <input v-model="first_name" type="text" id="first-name" placeholder="First name" required>
                    </div>

                    <div class="input-element">
                        <label for="last-name">Last name</label>
                        <input v-model="last_name" type="text" id="last-name" placeholder="Last name" required>
                    </div>

                    <div class="input-element">
                        <label for="email">Email address</label>
                        <input v-model="email" type="email" id="email" placeholder="grumpyteacher@school.com" required>
                    </div>

                    <div class="input-element">
                        <label for="mobile-number">Mobile number</label>
                        <input v-model="mobile_number" type="tel" id="mobile-number" placeholder="Enter phone number" required>
                    </div>

                    <div class="tos">
                        <input type="checkbox" id="tos-checkbox" v-model="tos_checked">
                        <label for="tos-checkbox">By selecting this, you agree to our <span>Terms</span> & <span>Privacy Policy</span> </label>
                    </div>

                    <div>
                        <button @click="complete_registration" class="purchase-button" :disabled="registration_form_disabled">Complete registration</button>
                    </div>
                </form>
            </div>
        </div>

        <div class="dorks-container">
            <img :src="require('@/assets/img/dorks-couple.svg')" class="dorks dorks-couple" alt="">
            <img :src="require('@/assets/img/dorks-single.svg')" class="dorks dorks-single" alt="">
        </div>

        <Footer></Footer>
    </div>
</template>

<script>

import Header from '@/components/Header';
import Footer from '@/components/Footer';
import intlTelInput from 'intl-tel-input';

export default {
    name: "Purchase",
    components: {
        Header,
        Footer
    },
    data() {
        return {
            first_name: '',
            last_name: '',
            email: '',
            mobile_number: '',
            tos_checked: false
        }
    },
    computed: {
        form_active: function() {
            return this.$store.getters.get_form_active;
        },
        registration_form_disabled: function() {
            return !this.first_name.length > 0 || !this.last_name.length > 0 || !this.email.length > 0 || !this.mobile_number.length > 0 || !this.tos_checked;
        },
    },
    methods: {
        complete_registration: function() {
            this.$router.push('/purchase/myself');
        }
    },
    mounted() {
        const input = document.querySelector("#mobile-number");
        intlTelInput(input, {
        });
    }
}

</script>