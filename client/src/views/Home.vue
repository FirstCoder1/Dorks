<template>
    <div class="home">
        <TopBanner></TopBanner>
        <Header></Header>
        <div class="homepage-1">
            <div class="home-container-1">
                <div class="content-title">
                    Are you tired of
                    <div>being <span>tech support</span>?</div>
                </div>
                <div class="content-text">
                    Dorks is the support for family that won't leave you alone. <span>We're even there for you when nana's trying to scan her slippers.</span>
                </div>
                <button class="purchase-button" @click="$router.push('purchase')">Purchase Dorks for $199/yr</button>
            </div>
            <div v-if="is_mobile" class="dorks-container">
                <img :src="require('@/assets/img/dorks-couple-mobile.svg')" class="dorks dorks-couple" alt="">
                <img :src="require('@/assets/img/dorks-single-mobile.svg')" class="dorks dorks-single" alt="">
            </div>
            <div v-else class="dorks-container">
                <img :src="require('@/assets/img/dorks-couple.svg')" class="dorks dorks-couple" alt="">
                <img :src="require('@/assets/img/dorks-single.svg')" class="dorks dorks-single" alt="">
            </div>
        </div>
        <div class="divider"></div>
        <div class="homepage-2">
            <div class="special-abilities-title">
                <div class="content-title">Special Abilities</div>
                <div class="content-text">
                    This is where I talk about our awesome skills for a bit, providing a good lead up to below.
                </div>
            </div>
            <b-container fluid class="special-abilities-container" id="sac">
                <b-row v-if="is_mobile">
                    <b-carousel id="carousel-1" v-model="slide" :interval="0" indicators>
                        <b-carousel-slide>
                            <b-col xs="12" md="6" lg="4">
                                <div class="special-abilities-object">
                                    <div class="content-img">
                                        <img :src="require('@/assets/img/wrench.svg')" alt="">
                                    </div>
                                    <div class="content-title">Installation</div>
                                    <div class="content-text">We can help <span>install new software</span>, upgrade equipment, manage
                                        <span>software updates</span>, and <span>app installations</span>.
                                    </div>
                                </div>
                            </b-col>
                            <b-col xs="12" md="6" lg="4">
                                <div class="special-abilities-object">
                                    <div class="content-img">
                                        <img :src="require('@/assets/img/setup.svg')" alt="">
                                    </div>
                                    <div class="content-title">Setup</div>
                                    <div class="content-text">Setting up your <span>Alexa</span>, managing your home technology, <span>parental controls for all devices</span>
                                        and so much more.
                                    </div>
                                </div>
                            </b-col>
                            <b-col xs="12" md="6" lg="4">
                                <div class="special-abilities-object">
                                    <div class="content-img">
                                        <img :src="require('@/assets/img/protect.svg')" alt="">
                                    </div>
                                    <div class="content-title">Protect</div>
                                    <div class="content-text">Carefully managing fraud prevention, <span>password help</span>, anti-virus,
                                        <span>privacy</span> & best practices.
                                    </div>
                                </div>
                            </b-col>
                        </b-carousel-slide>

                        <b-carousel-slide>
                            <b-col xs="12" md="6" lg="4" class="">
                                <div class="special-abilities-object">
                                    <div class="content-img">
                                        <img :src="require('@/assets/img/speed.svg')" alt="">
                                    </div>
                                    <div class="content-title">Speed</div>
                                    <div class="content-text">Let us <span>improve internet speeds</span>, router issues, applications, <span>free up memory</span> and deliver best practices.</div>
                                </div>
                            </b-col>
                            <b-col xs="12" md="6" lg="4" class="">
                                <div class="special-abilities-object">
                                    <div class="content-img">
                                        <img :src="require('@/assets/img/automation.svg')" alt="">
                                    </div>
                                    <div class="content-title">Automation</div>
                                    <div class="content-text">We’ll <span>establish home commands</span>, voice commands, <span>smart appliances</span> and make your life easier.</div>
                                </div>
                            </b-col>
                            <b-col xs="12" md="6" lg="4" class="">
                                <div class="special-abilities-object">
                                    <div class="content-img">
                                        <img :src="require('@/assets/img/backups.svg')" alt="">
                                    </div>
                                    <div class="content-title">Backups</div>
                                    <div class="content-text"><span>Cherish your memories</span> and create more room on your device with the <span>best backup solution</span>.</div>
                                </div>
                            </b-col>
                        </b-carousel-slide>
                    </b-carousel>
                </b-row>
                <b-row v-else>
                    <b-col xs="12" md="6" lg="4">
                        <div class="special-abilities-object">
                            <div class="content-img">
                                <img :src="require('@/assets/img/wrench.svg')" alt="">
                            </div>
                            <div class="content-title">Installation</div>
                            <div class="content-text">We can help <span>install new software</span>, upgrade equipment, manage
                                <span>software updates</span>, and <span>app installations</span>.
                            </div>
                        </div>
                    </b-col>
                    <b-col xs="12" md="6" lg="4">
                        <div class="special-abilities-object">
                            <div class="content-img">
                                <img :src="require('@/assets/img/setup.svg')" alt="">
                            </div>
                            <div class="content-title">Setup</div>
                            <div class="content-text">Setting up your <span>Alexa</span>, managing your home technology, <span>parental controls for all devices</span>
                                and so much more.
                            </div>
                        </div>
                    </b-col>
                    <b-col xs="12" md="6" lg="4">
                        <div class="special-abilities-object">
                            <div class="content-img">
                                <img :src="require('@/assets/img/protect.svg')" alt="">
                            </div>
                            <div class="content-title">Protect</div>
                            <div class="content-text">Carefully managing fraud prevention, <span>password help</span>, anti-virus,
                                <span>privacy</span> & best practices.
                            </div>
                        </div>
                    </b-col>
                    <b-col xs="12" md="6" lg="4" class="d-none d-md-block">
                        <div class="special-abilities-object">
                            <div class="content-img">
                                <img :src="require('@/assets/img/speed.svg')" alt="">
                            </div>
                            <div class="content-title">Speed</div>
                            <div class="content-text">Let us <span>improve internet speeds</span>, router issues, applications, <span>free up memory</span> and deliver best practices.</div>
                        </div>
                    </b-col>
                    <b-col xs="12" md="6" lg="4" class="d-none d-md-block">
                        <div class="special-abilities-object">
                            <div class="content-img">
                                <img :src="require('@/assets/img/automation.svg')" alt="">
                            </div>
                            <div class="content-title">Automation</div>
                            <div class="content-text">We’ll <span>establish home commands</span>, voice commands, <span>smart appliances</span> and make your life easier.</div>
                        </div>
                    </b-col>
                    <b-col xs="12" md="6" lg="4" class="d-none d-md-block">
                        <div class="special-abilities-object">
                            <div class="content-img">
                                <img :src="require('@/assets/img/backups.svg')" alt="">
                            </div>
                            <div class="content-title">Backups</div>
                            <div class="content-text"><span>Cherish your memories</span> and create more room on your device with the <span>best backup solution</span>.</div>
                        </div>
                    </b-col>
                </b-row>
            </b-container>
        </div>
        <div class="divider divider-2"></div>
        <div class="homepage-3">
            <div class="pay-less-title">
                <div class="content-title">
                    Pay less, <span>supported more</span>
                </div>
                <div class="content-text">
                    In under 5 minutes you can have access to our brightest dorks all year.  Sign up, report the issue and get supported with Dorks.
                </div>
                <button class="purchase-button" @click="$router.push('purchase')">Purchase Dorks for $199/yr</button>
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
        <div class="divider"></div>
        <Footer></Footer>

<!--        <b-container fluid class="special-abilities-container" id="sac">-->
<!--            <b-row>-->
<!--                -->
<!--            </b-row>-->
<!--        </b-container>-->
    </div>
</template>

<script>

import TopBanner from '@/components/TopBanner';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import $ from 'jquery';

export default {
    name: "Home",
    data() {
        return {
            mouse_x_start: null,
            mouse_y_start: null,
            slide: 0,
            current_width: window.innerWidth,
            current_height: window.innerHeight
        }
    },
    components: {
        Header,
        TopBanner,
        Footer
    },
    methods: {
        set_dims: function() {
            this.current_width = window.innerWidth;
            this.current_height = window.innerHeight;
        },
    },
    computed: {
        is_mobile: function() {
            console.log(this.current_width, this.current_height);
            return this.current_width < 768;
        }
    },
    mounted() {
        window.addEventListener('resize', this.set_dims);
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.set_dims);
        console.log("Resize destroyed");
    }
}
</script>

